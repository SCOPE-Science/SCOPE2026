#!/usr/bin/env python3
"""Exact finite verification for dihedral homology of the side-two honeycomb.

Only Python's standard library is required. The mathematical construction
and proof of the acyclic-toggle lemma appear in RESULT.md.
"""
from itertools import combinations
from collections import deque


def inside(p):
    q, t = p
    return max(abs(q), abs(t), abs(q + t)) <= 2


def rotate(p):
    q, t = p
    return (-t, q + t)


def reflect(p):
    q, t = p
    return (t, q)


def move(p, k, reflected):
    if reflected:
        p = reflect(p)
    for _ in range(k):
        p = rotate(p)
    return p


def build():
    triangles = sorted({tuple(sorted(tri))
        for q in range(-3, 3) for t in range(-3, 3)
        for tri in (((q, t), (q + 1, t), (q, t + 1)),
                    ((q + 1, t + 1), (q + 1, t), (q, t + 1)))
        if all(map(inside, tri))})
    assert len(triangles) == 24
    labels = {t: j for j, t in enumerate(triangles)}
    edges = sorted((i, j) for i, j in combinations(range(24), 2)
                   if len(set(triangles[i]) & set(triangles[j])) == 2)
    assert len(edges) == 30
    edge_index = {pair: i for i, pair in enumerate(edges)}
    incident = [[] for _ in triangles]
    for z, (i, j) in enumerate(edges):
        incident[i].append((j, z))
        incident[j].append((i, z))
    matchings = []

    def enumerate_matchings(available, selected):
        if not available:
            matchings.append(tuple(selected))
            return
        i = min(available)
        for j, e in incident[i]:
            if j in available:
                enumerate_matchings(available - {i, j}, selected + [e])

    enumerate_matchings(set(range(24)), [])
    assert len(matchings) == 20 and all(len(m) == 12 for m in matchings)
    faces = set()
    for M in matchings:
        sub = sum(1 << x for x in M)
        f = sub
        while True:
            faces.add(f)
            if f == 0:
                break
            f = (f - 1) & sub
    assert len(faces) == 66370

    def permutation(k, reflected):
        on_triangles = [labels[tuple(sorted(move(p, k, reflected) for p in tri))]
                        for tri in triangles]
        result = [edge_index[tuple(sorted((on_triangles[i], on_triangles[j])))]
                  for i, j in edges]
        assert sorted(result) == list(range(30))
        return tuple(result)

    return faces, permutation


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def orbit_trace(faces, p):
    visited = set()
    orbit_masks = []
    for j in range(len(p)):
        if j in visited:
            continue
        x, member = j, []
        while x not in visited:
            visited.add(x)
            member.append(x)
            x = p[x]
        assert x == j
        orbit_masks.append(sum(1 << i for i in member))
    output = 0
    count = 0
    for mask in faces:
        selected_orbits = 0
        for orbit in orbit_masks:
            intersection = mask & orbit
            if intersection not in (0, orbit):
                break
            if intersection:
                selected_orbits += 1
        else:
            count += 1
            output += (-1) ** selected_orbits
    return (output, count, len(orbit_masks))


def signed_augmented_chain_trace(faces, p):
    """Independent signed simplicial chain calculation for every face."""
    total = 0
    for mask in faces:
        vertices = [j for j in range(30) if (mask >> j) & 1]
        images = [p[j] for j in vertices]
        if sorted(images) != vertices:
            continue
        inversions = sum(1 for i, j in combinations(range(len(images)), 2)
                         if images[i] > images[j])
        total += (-1) ** (len(vertices) - 1 + inversions)
    return total


def acyclic_matching(faces):
    remaining = set(faces)
    matched_pairs = 0
    paired_higher = {}
    for j in range(30):
        bit = 1 << j
        lower = {f for f in remaining if not f & bit and (f | bit) in remaining}
        upper = {f | bit for f in lower}
        assert len(lower) == len(upper)
        assert lower.isdisjoint(upper)
        assert all(f in remaining and f | bit in remaining for f in lower)
        matched_pairs += len(lower)
        paired_higher.update((f, f | bit) for f in lower)
        remaining.difference_update(lower)
        remaining.difference_update(upper)
    assert len(remaining) == 2
    assert all(f.bit_count() == 4 for f in remaining)
    assert 2 * matched_pairs + len(remaining) == len(faces)
    # Check acyclicity directly, without relying solely on the toggle lemma.
    order = sorted(faces)
    rank = {mask: i for i, mask in enumerate(order)}
    adjacency = [[] for _ in order]
    indegree = [0] * len(order)
    for upper in order:
        mask = upper
        while mask:
            b = mask & -mask
            lower = upper ^ b
            if paired_higher.get(lower) == upper:
                a, z = rank[lower], rank[upper]
            else:
                a, z = rank[upper], rank[lower]
            adjacency[a].append(z)
            indegree[z] += 1
            mask -= b
    queue = deque(i for i, deg in enumerate(indegree) if deg == 0)
    seen = 0
    while queue:
        i = queue.popleft()
        seen += 1
        for j in adjacency[i]:
            indegree[j] -= 1
            if indegree[j] == 0:
                queue.append(j)
    assert seen == len(order), ('directed cycle detected', len(order) - seen)
    print('DIRECTED_HASSE_GRAPH_ACYCLIC', seen, 'FACES')
    return matched_pairs, sorted(remaining)


def main():
    faces, perm = build()
    e = tuple(range(30))
    r, s = perm(1, False), perm(0, True)
    assert compose(r, compose(r, compose(r, compose(r, compose(r, r))))) == e
    assert compose(s, s) == e
    assert compose(s, compose(r, s)) == perm(5, False)
    # Sequential face toggles are acyclic by the first-differing-toggle lemma.
    pairs, critical = acyclic_matching(faces)
    print('HONEYCOMB_GRAPH 24 30 PERFECT_MATCHINGS 20 TOTAL_FACES 66370')
    print('ACYCLIC_TOGGLE_MATCHING_PAIRS', pairs, 'CRITICAL_3_CELLS', critical)
    rotation_traces = []
    reflection_traces = []
    for b in (False, True):
        for k in range(6):
            p = perm(k, b)
            trace, invariant_face_count, orbit_count = orbit_trace(faces, p)
            signed = signed_augmented_chain_trace(faces, p)
            assert trace == -signed, (k, b, trace, signed)
            expected = (2 if k % 2 == 0 else 0) if not b else (0 if k % 2 == 0 else -2)
            assert trace == expected, (k, b, trace)
            (reflection_traces if b else rotation_traces).append(trace)
            print('ELEMENT', 'reflection' if b else 'rotation', k,
                  'TRACE', trace, 'INVARIANT_FACES', invariant_face_count,
                  'VERTEX_ORBITS', orbit_count)
    assert rotation_traces == [2, 0, 2, 0, 2, 0]
    assert reflection_traces == [0, -2, 0, -2, 0, -2]
    assert sum(rotation_traces + reflection_traces) == 0
    print('ALL_TWELVE_SIGNED_LEFSCHETZ_IDENTITIES_EXACT')
    print('TWO_ONE_DIMENSIONAL_DIHEDRAL_CHARACTERS_VERIFIED')


if __name__ == '__main__':
    main()
