#!/usr/bin/env python3
"""Reproduce finite integer Morse certificates for two clique-free complexes.

Standard library only. Run: python3 verify.py
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations

N = 16


def edge_set(kind):
    vertices = [(x, y) for x in range(4) for y in range(4)]
    result = set()
    generators = {(1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)}
    for i, (x, y) in enumerate(vertices):
        for j, (u, v) in enumerate(vertices):
            if j <= i:
                continue
            adjacent = ((u - x) % 4, (v - y) % 4) in generators if kind == 'Shrikhande' else (x == u or y == v)
            if adjacent:
                result.add((i, j))
    return result


def all_faces(kind):
    edges = edge_set(kind)
    forbidden = [sum(1 << x for x in triple)
                 for triple in combinations(range(N), 3)
                 if all((min(i, j), max(i, j)) in edges for i, j in combinations(triple, 2))]
    faces = [x for x in range(1 << N) if not any((x & f) == f for f in forbidden)]
    assert len(edges) == 48 and len(forbidden) == 32
    return faces, forbidden


def toggle_matching(faces):
    remaining = set(faces)
    pairs = []
    for vertex in range(N):
        bit = 1 << vertex
        for low in sorted(remaining):
            high = low | bit
            if low & bit or high not in remaining:
                continue
            remaining.remove(low)
            remaining.remove(high)
            pairs.append((low, high))
    return pairs, remaining


def directed_hasse_acyclic(faces, matching):
    fset = set(faces)
    pairs = set(matching)
    indegree = {f: 0 for f in faces}
    forward = defaultdict(list)
    nedges = 0
    for high in faces:
        for i in range(N):
            if high & (1 << i):
                low = high ^ (1 << i)
                assert low in fset
                source, target = (low, high) if (low, high) in pairs else (high, low)
                forward[source].append(target)
                indegree[target] += 1
                nedges += 1
    queue = deque(f for f in faces if indegree[f] == 0)
    reached = 0
    while queue:
        f = queue.popleft()
        reached += 1
        for next_face in forward[f]:
            indegree[next_face] -= 1
            if indegree[next_face] == 0:
                queue.append(next_face)
    assert reached == len(faces), 'The oriented augmented face poset has a directed cycle'
    return reached, nedges


def simplicial_boundary(face):
    vertices = [i for i in range(N) if face & (1 << i)]
    return [(face ^ (1 << i), (-1) ** position) for position, i in enumerate(vertices)]


def morse_boundary_matrix(pairs, critical):
    counts = Counter(f.bit_count() - 1 for f in critical)
    lower_degree = min(counts)
    assert set(counts) == {lower_degree, lower_degree + 1}
    lower = sorted(f for f in critical if f.bit_count() - 1 == lower_degree)
    upper = sorted(f for f in critical if f.bit_count() - 1 == lower_degree + 1)
    paired_lower = dict(pairs)
    paired_upper = {h for _, h in pairs}
    critical_lower = set(lower)

    @lru_cache(maxsize=None)
    def projection(face):
        if face in critical_lower:
            return {face: 1}
        if face in paired_upper:
            return {}
        assert face in paired_lower
        coface = paired_lower[face]
        signed_boundary = dict(simplicial_boundary(coface))
        pivot_sign = signed_boundary[face]
        output = defaultdict(int)
        for other, coefficient in signed_boundary.items():
            if other != face:
                for survivor, weight in projection(other).items():
                    output[survivor] -= pivot_sign * coefficient * weight
        return {x: y for x, y in output.items() if y}

    columns = []
    for face in upper:
        image = defaultdict(int)
        for subface, coefficient in simplicial_boundary(face):
            for survivor, weight in projection(subface).items():
                image[survivor] += coefficient * weight
        columns.append([image.get(r, 0) for r in lower])
    matrix = [[columns[j][i] for j in range(len(upper))] for i in range(len(lower))]
    return lower_degree, matrix, projection.cache_info().currsize


def integer_determinant(a):
    a = [row[:] for row in a]
    n = len(a)
    assert all(len(row) == n for row in a)
    if n == 0:
        return 1
    sign = 1
    previous = 1
    for j in range(n - 1):
        if a[j][j] == 0:
            pivot = next((i for i in range(j + 1, n) if a[i][j] != 0), None)
            if pivot is None:
                return 0
            a[j], a[pivot] = a[pivot], a[j]
            sign = -sign
        x = a[j][j]
        for i in range(j + 1, n):
            for k in range(j + 1, n):
                numerator = x * a[i][k] - a[i][j] * a[j][k]
                assert numerator % previous == 0
                a[i][k] = numerator // previous
        for i in range(j + 1, n):
            a[i][j] = 0
        previous = x
    return sign * a[n - 1][n - 1]


def raw_mod_two_betti(faces):
    by_degree = defaultdict(list)
    for face in faces:
        by_degree[face.bit_count() - 1].append(face)
    ranks = {}
    for degree in sorted(d for d in by_degree if d >= 0):
        lower_index = {f: i for i, f in enumerate(by_degree[degree - 1])}
        pivots = {}
        for face in by_degree[degree]:
            boundary = 0
            for i in range(N):
                if face & (1 << i):
                    boundary ^= 1 << lower_index[face ^ (1 << i)]
            while boundary:
                pivot = boundary.bit_length() - 1
                if pivot not in pivots:
                    pivots[pivot] = boundary
                    break
                boundary ^= pivots[pivot]
        ranks[degree] = len(pivots)
    return {degree: len(by_degree[degree]) - ranks.get(degree, 0) - ranks.get(degree + 1, 0)
            for degree in by_degree if degree >= 0}


def verify_one(kind):
    faces, triangles = all_faces(kind)
    matching, critical = toggle_matching(faces)
    reached, edges = directed_hasse_acyclic(faces, matching)
    assert len(faces) == 2 * len(matching) + len(critical)
    assert matching[0][0] == 0 or any(low == 0 for low, high in matching)
    degree, matrix, projected = morse_boundary_matrix(matching, critical)
    shape = (len(matrix), len(matrix[0]))
    counts = Counter(face.bit_count() - 1 for face in critical)
    if kind == 'Shrikhande':
        expected_faces, expected_pairs = 8951, 4466
        expected_critical, expected_shape, expected_degree = {5: 5, 6: 14}, (5, 14), 5
        selected = [[row[j] for j in [0, 1, 4, 9, 11]] for row in matrix]
        expected_det, expected_betti = 1, {6: 9}
        expected_f = {-1: 1, 0: 16, 1: 120, 2: 528, 3: 1452, 4: 2496, 5: 2568, 6: 1424, 7: 330, 8: 16}
    else:
        expected_faces, expected_pairs = 7343, 3658
        expected_critical, expected_shape, expected_degree = {5: 21, 6: 6}, (21, 6), 5
        selected = [matrix[i] for i in [0, 2, 4, 7, 9, 11]]
        expected_det, expected_betti = -1, {5: 15}
        expected_f = {-1: 1, 0: 16, 1: 120, 2: 528, 3: 1428, 4: 2304, 5: 2040, 6: 816, 7: 90}
    assert (len(faces), len(matching)) == (expected_faces, expected_pairs)
    assert dict(counts) == expected_critical
    assert shape == expected_shape and degree == expected_degree
    fvec = dict(Counter(face.bit_count() - 1 for face in faces))
    assert fvec == expected_f
    determinant = integer_determinant(selected)
    assert determinant == expected_det, 'No certified unimodular full-rank minor'
    betti = raw_mod_two_betti(faces)
    assert {d: n for d, n in betti.items() if n} == expected_betti
    print(f'{kind}: vertices=16 graph_edges=48 triangles={len(triangles)} ')
    print(f'  augmented_faces={len(faces)} oriented_hasse_edges={edges} reachable_DAG={reached}')
    print(f'  acyclic_matched_pairs={len(matching)} critical_by_degree={dict(counts)}')
    print(f'  integer_Morse_boundary={shape} unimodular_minor_det={determinant} projections={projected}')
    print(f'  independent_full_mod2_Betti={expected_betti}')
    print(f'  f_vector={dict(sorted(fvec.items()))}')
    return matrix


def main():
    sh = verify_one('Shrikhande')
    rook = verify_one('Rook')
    print('VERIFIED: exact integral Morse data and independent raw mod-two homology agree.')


if __name__ == '__main__':
    main()
