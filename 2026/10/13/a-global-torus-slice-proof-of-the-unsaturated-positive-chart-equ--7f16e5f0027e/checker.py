"""Exact small-instance arithmetic for a multigraded toric positive chart.

This checks the pentagon example's integer weights, Euler relations, and
rational torus point; the general theorem follows from the written proof.
Python 3, standard library only. Run: python checker.py.
"""
from fractions import Fraction as Q
from math import prod

M = [
    [1, 0, -1, -1, 0],
    [0, 1, 1, 0, -1],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 1, 1],
]
# Columns encode the weights of the five Cox coordinates in a Picard basis.
W = [
    (1, 0, 0),
    (-1, 0, 1),
    (1, 1, -1),
    (0, -1, 1),
    (0, 1, 0),
]
# Each monomial is an exponent vector; all coefficients are 1.
F = [
    [(0, 0, 1, 1, 0), (1, 0, 0, 0, 0)],
    [(0, 0, 0, 0, 1), (0, 1, 1, 0, 0)],
    [(0, 0, 0, 1, 1), (0, 1, 1, 1, 0), (1, 1, 0, 0, 0)],
]

def det(A):
    A = [row[:] for row in A]
    n = len(A)
    out = 0
    # Only five columns; Leibniz formula is exact and transparent.
    from itertools import permutations
    for p in permutations(range(n)):
        inversions = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        term = (-1) ** inversions
        for i, j in enumerate(p):
            term *= A[i][j]
        out += term
    return out

assert abs(det(M)) == 1
assert [[sum(M[i][j] * W[j][h] for j in range(5)) for h in range(3)]
        for i in range(5)] == [[0, 0, 0], [0, 0, 0], [1, 0, 0],
                              [0, 1, 0], [0, 0, 1]]

def degree(exponents):
    return tuple(sum(exponents[j] * W[j][i] for j in range(5)) for i in range(3))

for i, terms in enumerate(F):
    expected = tuple(int(h == i) for h in range(3))
    for exponents in terms:
        assert degree(exponents) == expected, (i, exponents, degree(exponents))
        # This also checks E_h(monomial) = deg_h(monomial)*monomial.

point = [Q(1, 2), Q(1, 2), Q(2, 3), Q(3, 4), Q(2, 3)]
lam = [Q(2), Q(3), Q(5)]

def evaluate(poly, at):
    return sum((prod(at[j] ** e[j] for j in range(5)) for e in poly), Q(0))

assert all(x != 0 for x in point)
assert [evaluate(poly, point) for poly in F] == [Q(1)] * 3
acted = [point[j] * prod(lam[h] ** W[j][h] for h in range(3))
         for j in range(5)]
assert [evaluate(poly, acted) for poly in F] == lam
restored = [acted[j] * prod(lam[h] ** (-W[j][h]) for h in range(3))
            for j in range(5)]
assert restored == point
print("VERIFY_OK: unimodularity, weight basis, multihomogeneity, exact torus slice")
