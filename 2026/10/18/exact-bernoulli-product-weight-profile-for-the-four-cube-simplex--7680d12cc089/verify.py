#!/usr/bin/env python3
"""Exact integer certificate for a four-cube simplex-volume identity.

Requires only the Python standard library. All 4368 five-element subsets are
enumerated, and their integer determinants are checked by two distinct methods.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb, prod

VERTICES = tuple(product((0, 1), repeat=4))
PERMS = tuple(permutations(range(4)))
SIGNS = tuple((-1) ** sum(p[i] > p[j] for i in range(4)
                         for j in range(i + 1, 4)) for p in PERMS)


def det4(matrix):
    return sum(s * prod(matrix[i][p[i]] for i in range(4))
               for s, p in zip(SIGNS, PERMS))


def bareiss_det(matrix):
    """Fraction-free Gaussian elimination, including exact row pivoting."""
    a = [list(row) for row in matrix]
    n = len(a)
    sign = 1
    previous = 1
    for k in range(n - 1):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[pivot], a[k] = a[k], a[pivot]
            sign = -sign
        diagonal = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                value = diagonal * a[i][j] - a[i][k] * a[k][j]
                assert value % previous == 0
                a[i][j] = value // previous
            a[i][k] = 0
        previous = diagonal
    return sign * a[n - 1][n - 1]


M = [0] * 21
counts = Counter()
nonzero = []
for indices in combinations(range(16), 5):
    points = [VERTICES[i] for i in indices]
    v0 = points[0]
    differences = [[points[j][i] - v0[i] for j in range(1, 5)]
                   for i in range(4)]
    determinant = abs(det4(differences))
    augmented = [[1, *v] for v in points]
    assert determinant == abs(bareiss_det(augmented))
    counts[determinant] += 1
    M[sum(sum(v) for v in points)] += determinant
    if determinant:
        nonzero.append((indices, determinant))

assert sum(counts.values()) == comb(16, 5) == 4368
assert dict(counts) == {0: 1360, 1: 2672, 2: 320, 3: 16}
EXPECTED = [0, 0, 0, 0, 1, 12, 66, 204, 417, 624, 712, 624, 417,
            204, 66, 12, 1, 0, 0, 0, 0]
assert M == EXPECTED
assert sum(M) == 3360

# Compare coefficients of the exact diagonal polynomials:
#   sum_k M_k z^k (1-z)^(20-k)
#       = q^4 - 16 q^7 + 18 q^8, q=z(1-z).
left = [0] * 21
for k, coefficient in enumerate(M):
    for j in range(21 - k):
        left[k + j] += coefficient * comb(20 - k, j) * (-1) ** j
right = [0] * 21
for degree, multiplier in ((4, 1), (7, -16), (8, 18)):
    for j in range(degree + 1):
        right[degree + j] += multiplier * comb(degree, j) * (-1) ** j
assert left == right

# A separately weighted, exact rational regression. This is a check,
# not a substitute for the multiaffine-symmetry proof.
p = (Fraction(1, 2), Fraction(1, 3), Fraction(1, 4), Fraction(1, 5))
weights = tuple(prod(p[i] if v[i] else (1 - p[i]) for i in range(4))
                for v in VERTICES)
P = sum((d * prod(weights[i] for i in indices)
         for indices, d in nonzero), Fraction(0))
q = tuple(t * (1 - t) for t in p)
e3 = sum(prod(q[j] for j in range(4) if j != i) for i in range(4))
e4 = prod(q)
assert P / e4 == 1 - 4 * e3 + 18 * e4 == Fraction(1613, 1800)
assert Fraction(1, 1) - 16 * Fraction(1, 4) ** 3 + 18 * Fraction(1, 4) ** 4 == Fraction(105, 128)
print('FOUR_CUBE_PRODUCT_WEIGHT_EXACT_CERTIFICATE_OK')
