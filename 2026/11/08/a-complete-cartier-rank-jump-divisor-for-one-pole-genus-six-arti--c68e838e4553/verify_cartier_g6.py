#!/usr/bin/env python3
"""Exact finite-field checks of the Cartier filtration on one-pole genus-six AS curves.

Over F_3 the Cartier operator is linear. The general characteristic-three
proof requires the symbolic Cartier calculation given in RESULT.md.
"""
from itertools import product
from math import comb

P = 3
BASIS = [(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (1, 1)]


def cartier_monomial(i):
    """C(x^i dx) in F_3(x), as a sparse polynomial in x."""
    return {(i - 2) // 3: 1} if i >= 2 and i % 3 == 2 else {}


def matrix(a, b, c, d):
    f = {7: 1, 5: a, 4: b, 2: c, 1: d}
    out = [[0] * 6 for _ in range(6)]
    for col, (i, j) in enumerate(BASIS):
        terms = {}
        if j == 0:
            terms = {(n, 0): coef for n, coef in cartier_monomial(i).items()}
        else:
            # Since y^3 = y + f, write x^i y dx = x^i y^3 dx - x^i f dx.
            for n, coef in cartier_monomial(i).items():
                terms[(n, 1)] = (terms.get((n, 1), 0) + coef) % P
            for power, coef in f.items():
                for n, one in cartier_monomial(i + power).items():
                    terms[(n, 0)] = (terms.get((n, 0), 0) - coef * one) % P
        for term, coef in terms.items():
            if coef % P:
                assert term in BASIS, ('nonholomorphic image', term)
                out[BASIS.index(term)][col] = coef % P
    return out


def rank(A):
    m = [row[:] for row in A]
    r = 0
    for j in range(len(m[0])):
        pivot = next((i for i in range(r, len(m)) if m[i][j] % P), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        scale = pow(m[r][j], -1, P)
        m[r] = [(x * scale) % P for x in m[r]]
        for i in range(len(m)):
            if i == r:
                continue
            scale = m[i][j]
            m[i] = [(x - scale * y) % P for x, y in zip(m[i], m[r])]
        r += 1
        if r == len(m):
            break
    return r


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(6)) % P for j in range(6)] for i in range(6)]


assert matrix(0, 0, 0, 0) == [
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

counts = {2: 0, 3: 0}
for a, b, c, d in product(range(P), repeat=4):
    A = matrix(a, b, c, d)
    A2, A3 = mm(A, A), mm(mm(A, A), A)
    assert rank(A) == (3 if a else 2), (a, b, c, d, A)
    assert rank(A2) == 1, (a, b, c, d, A2)
    assert rank(A3) == 0, (a, b, c, d, A3)
    counts[rank(A)] += 1
assert counts == {2: 27, 3: 54}

# In characteristic 3 the x^5 coefficient in (x+h)^7 is zero.
assert comb(7, 2) % 3 == 0
# The Artin-Schreier change y -> y + u x^2 changes only x^6 and x^2.
print('cartier_basis_dim=6; genus=6; p_rank=0 (one wild branch point)')
print('rank3_coefficients=54; rank2_coefficients=27 over F_3')
print('rank_cartier_squared=1; rank_cartier_cubed=0 for all 81 parameter tuples')
print('translation_x5_coefficient_invariant=true')
print('ALL_CHECKS_PASSED')
