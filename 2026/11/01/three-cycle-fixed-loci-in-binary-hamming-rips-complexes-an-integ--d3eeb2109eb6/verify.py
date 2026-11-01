#!/usr/bin/env python3
"""Finite independent checks for a three-coordinate cyclic fixed-space theorem.

Requires only Python 3.9+ from the standard library. Uses original binary
Hamming distances to reconstruct all orbit edges and exact GF(2) boundaries.
"""
from itertools import combinations


def distance(a, b):
    return (a ^ b).bit_count()


def rotate3(v):
    b = v & 7
    return (v & ~7) | ((b << 1) & 7) | (b >> 2)


def swap_first_two(v):
    b0 = v & 1
    b1 = (v >> 1) & 1
    return (v & ~3) | (b0 << 1) | b1


def enumerate_orbits(m):
    seen, orbits = set(), []
    for v in range(1 << (m + 3)):
        if v in seen:
            continue
        orbit = tuple(sorted({v, rotate3(v), rotate3(rotate3(v))}))
        seen.update(orbit)
        if all(distance(x, y) <= 2 for x, y in combinations(orbit, 2)):
            orbits.append(orbit)
    return orbits


def actual_graph(orbits):
    vertices = range(len(orbits))
    edges = set()
    for i, j in combinations(vertices, 2):
        if all(distance(u, v) <= 2 for u in orbits[i] for v in orbits[j]):
            edges.add((i, j))
    return edges


def theoretical_graph(m, orbits):
    labels = {}
    for i, orbit in enumerate(orbits):
        backgrounds = {v >> 3 for v in orbit}
        weights = {(v & 7).bit_count() for v in orbit}
        assert len(backgrounds) == len(weights) == 1
        z, w = next(iter(backgrounds)), next(iter(weights))
        labels[(z, w)] = i
    assert len(labels) == (4 << m)
    edges = set()
    for (z, u), i in labels.items():
        for (y, v), j in labels.items():
            if i >= j:
                continue
            b = distance(z, y)
            connect = ((u == v and u in (0, 3) and b <= 2)
                       or ((u, v) in ((0, 1), (1, 0), (3, 2), (2, 3)) and b <= 1)
                       or ((u, v) in ((0, 2), (2, 0), (3, 1), (1, 3)) and b == 0))
            if connect:
                edges.add((i, j))
    return edges, labels


def faces_of_flag_complex(num_vertices, edges):
    links = [set() for _ in range(num_vertices)]
    for a, b in edges:
        links[a].add(b)
        links[b].add(a)
    by_dim = [[(v,) for v in range(num_vertices)]]
    while True:
        nxt = []
        for f in by_dim[-1]:
            if not links[f[-1]]:
                continue
            for v in sorted(links[f[-1]]):
                if v > f[-1] and all(v in links[u] for u in f):
                    nxt.append(f + (v,))
        if not nxt:
            return by_dim
        by_dim.append(nxt)


def gf2_rank(columns):
    pivots = {}
    for column in columns:
        while column:
            pivot = column.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = column
                break
            column ^= pivots[pivot]
    return len(pivots)


def reduced_betti(by_dim):
    ranks = [1]
    for degree in range(1, len(by_dim)):
        old_index = {f: i for i, f in enumerate(by_dim[degree - 1])}
        boundaries = []
        for f in by_dim[degree]:
            vector = 0
            for i in range(len(f)):
                vector ^= 1 << old_index[f[:i] + f[i+1:]]
            boundaries.append(vector)
        ranks.append(gf2_rank(boundaries))
    ranks.append(0)
    return [len(by_dim[i]) - ranks[i] - ranks[i + 1] for i in range(len(by_dim))]


def cube_sphere_count(m):
    if m < 3:
        return 0
    return sum((j + 1) * ((1 << (m - 2)) - (1 << (i - 1)))
               for i in range(m) for j in range(i))


def expected_retract_faces(m, labels):
    old = set()
    # Two core VR(Q_m;2) flag complexes, plus two paths per background point.
    for w in (0, 3):
        zs = range(1 << m)
        for size in range(1, (1 << m) + 1):
            for zset in combinations(zs, size):
                if all(distance(x, y) <= 2 for x, y in combinations(zset, 2)):
                    old.add(tuple(sorted(labels[(z, w)] for z in zset)))
    for z in range(1 << m):
        for w in (1, 2):
            v = labels[(z, w)]
            a = labels[(z, 0)]
            b = labels[(z, 3)]
            old.update(((v,), tuple(sorted((v, a))), tuple(sorted((v, b)))))
    return old


def check_explicit_collapses(m, faces, labels):
    alive = set(f for dim in faces for f in dim)
    n_pairs = 0
    for z in range(1 << m):
        for w, core_type in ((1, 0), (2, 3)):
            peripheral = labels[(z, w)]
            center = labels[(z, core_type)]
            neigh = [labels[(y, core_type)] for y in range(1 << m)
                     if y != z and distance(z, y) == 1]
            for size in range(len(neigh), 0, -1):
                for subset in combinations(neigh, size):
                    lower = tuple(sorted((peripheral,) + subset))
                    upper = tuple(sorted((peripheral, center) + subset))
                    assert lower in alive and upper in alive, (m, lower, upper)
                    # Check precisely one remaining containing facet, namely upper.
                    containers = [f for f in alive if len(f) == len(lower) + 1
                                  and set(lower).issubset(f)]
                    assert containers == [upper], (m, lower, containers)
                    alive.remove(lower)
                    alive.remove(upper)
                    n_pairs += 1
    assert alive == expected_retract_faces(m, labels), (m, len(alive))
    return n_pairs


def run():
    for m in range(5):
        orbits = enumerate_orbits(m)
        # The full S_3 and its order-three subgroup have identical vertex orbits.
        for orbit in orbits:
            assert all(swap_first_two(v) in orbit for v in orbit)
        actual = actual_graph(orbits)
        expected, labels = theoretical_graph(m, orbits)
        assert actual == expected, (m, actual ^ expected)
        faces = faces_of_flag_complex(len(orbits), actual)
        betti = reduced_betti(faces)
        target = [0] * max(4, len(betti))
        target[1] = (1 << (m + 1)) - 1
        target[3] = 2 * cube_sphere_count(m)
        assert betti + [0] * (len(target) - len(betti)) == target, (m, betti, target)
        pairs = check_explicit_collapses(m, faces, labels)
        print('m=%d orbit_vertices=%d fvector=%s collapse_pairs=%d reduced_F2_Betti=%s' %
              (m, len(orbits), [len(s) for s in faces], pairs, betti))
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
