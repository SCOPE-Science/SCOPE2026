#!/usr/bin/env python3
"""Exact certificate for the matching complex of the Herschel graph.

No third-party modules, data files, or network access are required.
Run with: python3 herschel_matching_verifier.py
"""
from collections import Counter, defaultdict, deque
from itertools import combinations

# Vertices 0,1,2 have degree four; 3,4 and 5,...,10 have degree three.
# Bipartition: 0,...,4 versus 5,...,10. Each edge is one vertex
# of the matching complex, numbered by its position in EDGES.
EDGES = (
    (0, 5), (0, 6), (0, 9), (0, 10),
    (1, 5), (1, 6), (1, 7), (1, 8),
    (2, 7), (2, 8), (2, 9), (2, 10),
    (3, 5), (3, 7), (3, 9),
    (4, 6), (4, 8), (4, 10),
)
ROTATIONS = (
    (5, 9, 10, 6), (5, 6, 8, 7), (8, 10, 9, 7),
    (7, 9, 5), (6, 10, 8), (0, 1, 3),
    (1, 0, 4), (2, 3, 1), (4, 2, 1),
    (3, 2, 0), (2, 4, 0),
)
TOGGLE_EDGES = (17, 14, 16, 13, 7, 12, 5, 3, 1, 10)
EXPECTED_STAGE_PAIRS = (159, 94, 40, 28, 16, 10, 8, 6, 4, 2)
EXPECTED_FACE_COUNTS = (18, 111, 280, 270, 72)
EXPECTED_CRITICAL = {
    0: (131072,), 2: (8328, 73730),
    3: (4488, 4680, 6276, 8728, 10369, 33044, 33857,
        37380, 38976, 41473, 43024, 65812, 66625, 69890),
}


def graph_checks():
    assert len(EDGES) == 18 and len(set(EDGES)) == 18
    adj = [set() for _ in range(11)]
    for u, v in EDGES:
        assert 0 <= u < 5 <= v < 11
        adj[u].add(v)
        adj[v].add(u)
    assert sorted(map(len, adj)) == [3] * 8 + [4] * 3
    assert all(set(ROTATIONS[i]) == adj[i] for i in range(11))

    def connected(removed):
        remaining = set(range(11)) - set(removed)
        q = deque([min(remaining)])
        found = {min(remaining)}
        while q:
            for x in adj[q.popleft()] & remaining - found:
                found.add(x)
                q.append(x)
        return found == remaining

    for count in (0, 1, 2):
        assert all(connected(c) for c in combinations(range(11), count))

    # A rotation-system certificate for a sphere embedding: 36 darts
    # form nine facial cycles, so V-E+F=11-18+9=2.
    darts = {(u, v) for u in range(11) for v in adj[u]}
    remaining = set(darts)
    face_lengths = []
    while remaining:
        start = next(iter(remaining))
        dart = start
        length = 0
        while True:
            assert dart in remaining
            remaining.remove(dart)
            length += 1
            u, v = dart
            around = ROTATIONS[v]
            w = around[(around.index(u) + 1) % len(around)]
            dart = (v, w)
            if dart == start:
                break
        face_lengths.append(length)
    assert len(face_lengths) == 9
    assert 11 - len(EDGES) + len(face_lengths) == 2
    return tuple(sorted(face_lengths))


def all_matching_faces():
    faces = set()
    def visit(e, used, mask):
        if e == len(EDGES):
            if mask:
                faces.add(mask)
            return
        visit(e + 1, used, mask)
        u, v = EDGES[e]
        endpoints = (1 << u) | (1 << v)
        if not (used & endpoints):
            visit(e + 1, used | endpoints, mask | (1 << e))
    visit(0, 0, 0)
    assert len(faces) == 751
    dims = Counter(s.bit_count() - 1 for s in faces)
    assert tuple(dims.get(d, 0) for d in range(5)) == EXPECTED_FACE_COUNTS
    assert sum((-1) ** d * dims[d] for d in range(5)) == -11
    return faces


def construct_matching(faces):
    left = set(faces)
    pairs = []
    stages = []
    for e in TOGGLE_EDGES:
        step = []
        for lower in sorted(left):
            upper = lower | (1 << e)
            if not (lower & (1 << e)) and upper in left:
                step.append((lower, upper))
        for low, high in step:
            assert low in left and high in left
            assert high.bit_count() == low.bit_count() + 1
            left.remove(low)
            left.remove(high)
        pairs.extend(step)
        stages.append(len(step))
    assert tuple(stages) == EXPECTED_STAGE_PAIRS
    assert len(pairs) == 367 and len(left) == 17
    groups = defaultdict(list)
    for s in left:
        groups[s.bit_count() - 1].append(s)
    groups = {d: tuple(sorted(v)) for d, v in groups.items()}
    assert groups == EXPECTED_CRITICAL
    return pairs, left


def check_acyclic(faces, pairs):
    matched = set(pairs)
    nbr = {s: [] for s in faces}
    degree = {s: 0 for s in faces}
    count = 0
    for high in faces:
        for e in range(len(EDGES)):
            if high & (1 << e):
                low = high ^ (1 << e)
                if low == 0:
                    continue
                source, target = (low, high) if (low, high) in matched else (high, low)
                nbr[source].append(target)
                degree[target] += 1
                count += 1
    assert count == 2502
    q = deque([s for s in faces if degree[s] == 0])
    visited = 0
    while q:
        s = q.popleft()
        visited += 1
        for t in nbr[s]:
            degree[t] -= 1
            if degree[t] == 0:
                q.append(t)
    assert visited == len(faces)
    return count


def simplicial_boundary(faces):
    columns = {}
    for high in faces:
        col = {}
        pos = 0
        for e in range(len(EDGES)):
            if high & (1 << e):
                low = high ^ (1 << e)
                if low:
                    col[low] = (-1) ** pos
                pos += 1
        columns[high] = col
    # Full integral verification of boundary composed with boundary.
    for high, col in columns.items():
        double = defaultdict(int)
        for low, coeff in col.items():
            for lower, next_coeff in columns[low].items():
                double[lower] += coeff * next_coeff
        assert all(x == 0 for x in double.values())
    return columns


def reduce_chain_complex(faces, pairs, columns):
    alive = set(faces)
    for low, high in pairs:
        assert low in alive and high in alive
        p = columns[high].get(low, 0)
        assert p in (-1, 1)
        dimension = high.bit_count()
        # Unit integral pivot: exact elementary cancellation of a two-cell
        # acyclic subcomplex, without modular or floating-point arithmetic.
        for z in sorted(alive):
            if z == high or z.bit_count() != dimension:
                continue
            coefficient = columns[z].get(low, 0)
            if not coefficient:
                continue
            factor = coefficient * p
            for x, value in columns[high].items():
                next_value = columns[z].get(x, 0) - factor * value
                if next_value:
                    columns[z][x] = next_value
                else:
                    columns[z].pop(x, None)
        alive.remove(low)
        alive.remove(high)
        for z in alive:
            columns[z].pop(low, None)
            columns[z].pop(high, None)
    assert len(alive) == 17
    for z in alive:
        assert all(x in alive for x in columns[z])
    zero = [z for z in alive if z.bit_count() == 1]
    twos = sorted(z for z in alive if z.bit_count() == 3)
    threes = sorted(z for z in alive if z.bit_count() == 4)
    assert len(zero) == 1 and len(twos) == 2 and len(threes) == 14
    assert all(not columns[z] for z in zero + twos)
    # A unit determinant exhibits a split surjection from the 14 third
    # cells to the two second cells.
    a, b = twos
    x, y = threes[:2]
    minor = (
        columns[x].get(a, 0) * columns[y].get(b, 0)
        - columns[x].get(b, 0) * columns[y].get(a, 0)
    )
    assert abs(minor) == 1
    assert {z: columns[z] for z in threes[:2]} == {
        4488: {8328: 1}, 4680: {73730: 1}
    }
    assert all(set(columns[z]).issubset({a, b}) for z in threes)
    return minor


def rank_mod_two(faces, d):
    bottom = sorted(z for z in faces if z.bit_count() == d)
    top = sorted(z for z in faces if z.bit_count() == d + 1)
    row = {s: i for i, s in enumerate(bottom)}
    basis = {}
    for high in top:
        col = 0
        for e in range(len(EDGES)):
            if high & (1 << e):
                col ^= (1 << row[high ^ (1 << e)])
        while col:
            pivot = col.bit_length() - 1
            if pivot in basis:
                col ^= basis[pivot]
            else:
                basis[pivot] = col
                break
    return len(basis)


def main():
    faces_lengths = graph_checks()
    faces = all_matching_faces()
    pairs, critical = construct_matching(faces)
    directed_incidence_count = check_acyclic(faces, pairs)
    columns = simplicial_boundary(faces)
    signed_minor = reduce_chain_complex(faces, pairs, columns)
    mod_two_ranks = tuple(rank_mod_two(faces, d) for d in range(1, 5))
    assert mod_two_ranks == (17, 94, 186, 72)
    print('GRAPH vertices=11 edges=18 bipartite=true 3-connected=true planar=true')
    print('FACES', (18, 111, 280, 270, 72), 'total=751')
    print('PLANAR_FACE_LENGTHS', faces_lengths)
    print('MATCHED_PAIRS', len(pairs), 'DIRECTED_INCIDENCES', directed_incidence_count, 'DAG=true')
    print('CRITICAL_COUNTS', {0: 1, 2: 2, 3: 14})
    print('MORSE_D3_MINOR', signed_minor, 'INTEGRAL_RANK', 2)
    print('MOD2_BOUNDARY_RANKS', mod_two_ranks)
    print('RESULT: wedge of 12 three-spheres')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
