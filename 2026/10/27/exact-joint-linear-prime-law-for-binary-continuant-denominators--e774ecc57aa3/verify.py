#!/usr/bin/env python3
"""Exact finite-state and direct polynomial checks for binary continuant roots."""
from itertools import product
from fractions import Fraction

PAIRS = ((1, 0), (0, 1), (1, 1))
STATES = tuple((u, v, x, y) for u, v in PAIRS for x, y in PAIRS)
INDEX = {state: k for k, state in enumerate(STATES)}
N = len(STATES)
assert N == 9
M = [[0] * N for _ in range(N)]
for col, (u, v, x, y) in enumerate(STATES):
    for bit in (0, 1):
        target = (bit * u ^ v, u, (1 - bit) * x ^ y, x)
        M[INDEX[target]][col] += 1


def apply(vec):
    return [sum(M[i][j] * vec[j] for j in range(N)) for i in range(N)]


def joint_formula(d):
    m = d // 2
    if d % 2 == 0:
        return (4 * 4**m + 4 + (-2)**m) // 9
    return 4 * (2 * 4**m - 1 - (-2)**m) // 9


def marginal(d):
    return (2 ** (d + 1) + (-1) ** d) // 3


def word_counts(d):
    bins = {(b0, b1): 0 for b0 in (0, 1) for b1 in (0, 1)}
    for w in product((2, 3), repeat=d):
        a, b = 1, 0
        for f in w:
            # Multiplication in F_2[T], represented by coefficients in binary.
            mul = (a << 1) ^ (a if f == 3 else 0)
            a, b = mul ^ b, a
        bins[(a & 1, a.bit_count() & 1)] += 1
    return bins

start = [0] * N
start[INDEX[(1, 0, 1, 0)]] = 1
v0 = start
v1 = apply(v0)
v2 = apply(v1)
v3 = apply(v2)
v4 = apply(v3)
assert all(v4[i] == v3[i] + 2 * v1[i] + 4 * v0[i] for i in range(N))

v = start
for d in range(100):
    both = sum(v[i] for i, (u, _v, x, _y) in enumerate(STATES) if u == x == 1)
    zero = sum(v[i] for i, (u, _v, x, _y) in enumerate(STATES) if u == 1)
    one = sum(v[i] for i, (u, _v, x, _y) in enumerate(STATES) if x == 1)
    assert both == joint_formula(d) and zero == one == marginal(d), (d, both)
    assert sum(v) == 2**d
    m = d // 2
    covariance = Fraction(both, 2**d) - Fraction(zero * one, 2**(2 * d))
    if d % 2 == 0:
        expected_covariance = (Fraction((-2)**m, 9 * 4**m)
                               - Fraction(1, 9 * 16**m))
    else:
        expected_covariance = (-Fraction(2 * (-2)**m, 9 * 4**m)
                               - Fraction(1, 36 * 16**m))
    assert covariance == expected_covariance, d
    if d <= 14:
        bins = word_counts(d)
        assert bins[(1, 1)] == both
        assert sum(bins[(1, k)] for k in (0, 1)) == zero
        assert sum(bins[(k, 1)] for k in (0, 1)) == one
        assert bins[(0, 0)] == 2**d - 2*marginal(d) + joint_formula(d)
    v = apply(v)
print('VERIFY_OK transfer_dimension=9 annihilator_degree=4 matrix_degrees=100 direct_words_through=14')
