#!/usr/bin/env python3
"""Exact finite-chain checks for the antipodal quotient of VR(Q4;2)."""
from itertools import combinations, product
from collections import Counter

VERTICES = tuple(range(16))


def admissible(simplex):
    return all((u ^ v).bit_count() <= 2 for u, v in combinations(simplex, 2))


faces_by_size = {
    k: [tuple(t) for t in combinations(VERTICES, k) if admissible(t)]
    for k in range(1, 6)
}
assert [len(faces_by_size[k]) for k in range(1, 6)] == [16, 80, 160, 120, 16]
index3 = {face: i for i, face in enumerate(faces_by_size[4])}


def opposite_pairs(subset, opposite_mask):
    subset = set(subset)
    result = sorted((u, u ^ opposite_mask) for u in subset if u < (u ^ opposite_mask))
    assert len(result) == 4
    assert {x for p in result for x in p} == subset
    return result


def sphere_chain(subset, opposite_mask):
    pairs = opposite_pairs(subset, opposite_mask)
    result = {}
    for choice in product((0, 1), repeat=4):
        vertices = [pairs[i][choice[i]] for i in range(4)]
        swaps = sum(vertices[i] > vertices[j] for i in range(4) for j in range(i + 1, 4))
        orientation = (-1) ** (sum(choice) + swaps)
        simplex = tuple(sorted(vertices))
        assert simplex in index3
        assert simplex not in result
        result[simplex] = orientation
    assert len(result) == 16
    return result


def boundary(chain):
    result = Counter()
    for simplex, coef in chain.items():
        for i in range(len(simplex)):
            result[simplex[:i] + simplex[i+1:]] += coef * (-1) ** i
    return {x: a for x, a in result.items() if a}


sphere_cycles = []
for coordinate in range(4):
    for bit in (0, 1):
        sphere = [v for v in VERTICES if (v >> coordinate) & 1 == bit]
        sphere_cycles.append(sphere_chain(sphere, 15 ^ (1 << coordinate)))
parity_sphere = [v for v in VERTICES if v.bit_count() % 2 == 0]
sphere_cycles.append(sphere_chain(parity_sphere, 15))
assert len(sphere_cycles) == 9
assert all(boundary(cycle) == {} for cycle in sphere_cycles)

# Columns are all 16 tetrahedron boundaries followed by nine sphere cycles.
columns = []
for simplex in faces_by_size[5]:
    columns.append(boundary({simplex: 1}))
columns += sphere_cycles
assert len(columns) == 25

# The rows are positions in the lexicographically ordered list of 120 tetrahedra.
rows = [0, 1, 3, 5, 9, 11, 15, 19, 26, 30, 32, 36, 40, 47, 51,
        55, 62, 66, 73, 77, 84, 91, 96, 100, 104]
minor = [[col.get(faces_by_size[4][row], 0) for col in columns] for row in rows]


def bareiss_determinant(matrix):
    A = [list(row) for row in matrix]
    n = len(A)
    assert all(len(row) == n for row in A)
    sign, divisor = 1, 1
    for k in range(n - 1):
        if A[k][k] == 0:
            r = next((r for r in range(k+1, n) if A[r][k] != 0), None)
            if r is None:
                return 0
            A[k], A[r] = A[r], A[k]
            sign = -sign
        pivot = A[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                numerator = pivot*A[i][j] - A[i][k]*A[k][j]
                assert numerator % divisor == 0
                A[i][j] = numerator // divisor
        for i in range(k+1, n):
            A[i][k] = 0
        divisor = pivot
    return sign * A[-1][-1]

assert bareiss_determinant(minor) == -1


def orbit(face):
    opposite = tuple(sorted(v ^ 15 for v in face))
    return min(face, opposite)

orbits = {k: sorted({orbit(face) for face in faces_by_size[k]}) for k in range(1, 6)}
assert [len(orbits[k]) for k in range(1, 6)] == [8, 40, 80, 60, 8]
assert all(tuple(sorted(v ^ 15 for v in face)) != face for k in faces_by_size for face in faces_by_size[k])


def rank_mod_two(columns):
    basis = {}
    for col in columns:
        v = col
        while v:
            k = v.bit_length() - 1
            if k in basis:
                v ^= basis[k]
            else:
                basis[k] = v
                break
    return len(basis)

ranks = []
for k in range(2, 6):
    row_idx = {face: i for i, face in enumerate(orbits[k-1])}
    boundary_columns = []
    for s in orbits[k]:
        column = 0
        for j in range(len(s)):
            f = orbit(s[:j] + s[j+1:])
            column ^= 1 << row_idx[f]
        boundary_columns.append(column)
    ranks.append(rank_mod_two(boundary_columns))
assert ranks == [7, 32, 47, 8], ranks

# The first two checks, together with the published integral homotopy type
# VR(Q4;2) ~ wedge of nine 3-spheres, prove the integral basis assertion.
print('Q4_ANTIPODAL_RP3_WEDGE_FOUR_S3_UNIMODULAR_BASIS_OK')
print('f_vector=(16,80,160,120,16)')
print('quotient_cell_vector=(8,40,80,60,8)')
print('minor_determinant=-1')
print('quotient_mod2_boundary_ranks=(7,32,47,8)')
