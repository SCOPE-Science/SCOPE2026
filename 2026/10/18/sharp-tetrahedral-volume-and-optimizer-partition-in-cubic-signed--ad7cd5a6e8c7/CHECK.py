#!/usr/bin/env python3
"""Exact integer certificate for maximal tetrahedra in a cubic signed-permutahedron family."""
from collections import Counter
from itertools import combinations, permutations, product
from math import comb

# Each coordinate is a pair (constant coefficient, parameter coefficient).
BASE = ((1, 0), (1, 1), (1, 2))
VERTICES = sorted({tuple((sign * a, sign * b) for (a, b), sign in zip(p, signs))
                   for p in permutations(BASE)
                   for signs in product((-1, 1), repeat=3)})
assert len(VERTICES) == 48
INDEX = {v: i for i, v in enumerate(VERTICES)}

def subtract(x, y):
    return x[0] - y[0], x[1] - y[1]

def multiply(x, y):
    return x[0] * y[0], x[0] * y[1] + x[1] * y[0], x[1] * y[1]

def poly_times_linear(p, x):
    assert len(p) == 3
    return (p[0] * x[0], p[1] * x[0] + p[0] * x[1],
            p[2] * x[0] + p[1] * x[1], p[2] * x[1])

def determinant_of_four(ids):
    pts = [VERTICES[k] for k in ids]
    a, b, c = [tuple(subtract(pts[i][j], pts[0][j]) for j in range(3))
               for i in (1, 2, 3)]
    ans = [0] * 4
    for i, j, k, sign in ((0, 1, 2, 1), (1, 2, 0, 1), (2, 0, 1, 1)):
        bc = multiply(b[j], c[k]); cb = multiply(b[k], c[j])
        diff = tuple(bc[l] - cb[l] for l in range(3))
        term = poly_times_linear(diff, a[i])
        for m in range(4):
            ans[m] += sign * term[m]
    return tuple(ans)

BOUNDS = (16, 48, 64, 32)
ANCHOR = 0
unique_at_anchor = []
visited = 0
for others in combinations(range(1, 48), 3):
    coefficients = determinant_of_four((ANCHOR,) + others)
    assert all(abs(coef) <= bound for coef, bound in zip(coefficients, BOUNDS)), (others, coefficients)
    if coefficients == BOUNDS or coefficients == tuple(-b for b in BOUNDS):
        unique_at_anchor.append((ANCHOR,) + others)
    visited += 1
assert visited == comb(47, 3) == 16215
assert unique_at_anchor == [(0, 21, 28, 41)]

# Construct its orbit under the full order-48 signed-coordinate-permutation group.
representative = unique_at_anchor[0]
maximizers = set()
for p in permutations(range(3)):
    for signs in product((-1, 1), repeat=3):
        shifted = tuple(sorted(INDEX[tuple(tuple(signs[j] * coeff for coeff in VERTICES[i][p[j]])
                                          for j in range(3))] for i in representative))
        maximizers.add(shifted)
assert len(maximizers) == 12
usage = Counter(i for tet in maximizers for i in tet)
assert len(usage) == 48 and all(mult == 1 for mult in usage.values())

# Squared edge lengths of the representative as integer polynomials in the parameter.
def squared_edge_poly(i, j):
    ds = [subtract(VERTICES[i][k], VERTICES[j][k]) for k in range(3)]
    return (sum(u*u for u, v in ds), 2*sum(u*v for u, v in ds), sum(v*v for u, v in ds))
edge_profile = Counter(squared_edge_poly(i, j) for i, j in combinations(representative, 2))
assert edge_profile == Counter({(8, 16, 12): 4, (8, 16, 16): 2})

# The convex body is the 9-generator centered zonotope with three axes and
# six short roots; their exact 3-by-3 minors provide its volume polynomial.
AXES = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
ROOTS = []
for i, j in combinations(range(3), 2):
    for sign in (-1, 1):
        v = [0, 0, 0]; v[i] = 1; v[j] = sign
        ROOTS.append(tuple(v))

def det_int(a, b, c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            - a[1]*(b[0]*c[2]-b[2]*c[0])
            + a[2]*(b[0]*c[1]-b[1]*c[0]))

sums = tuple(sum(abs(det_int(*(list(A) + list(B))))
                 for A in combinations(AXES, 3-k)
                 for B in combinations(ROOTS, k)) for k in range(4))
assert sums == (1, 12, 42, 32)
# The centered-zonotope determinant formula gives volume
# 8 * sum_k sums[k] * (q/2)**k = 8+48q+84q^2+32q^3.
print('PASS: 16215 anchored determinant coefficient vectors exhaustively bounded.')
print('PASS: 12 maximizing tetrahedra, one orbit, disjoint partition of 48 vertices.')
print('PASS: edge-length profiles and 9-generator zonotope volume coefficients.')
