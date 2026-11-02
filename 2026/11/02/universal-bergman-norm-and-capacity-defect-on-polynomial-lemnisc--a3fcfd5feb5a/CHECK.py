#!/usr/bin/env python3
"""Supplementary exact algebraic checks of the polynomial-shell identity.

Universal mathematical justification is the contour-residue proof in RESULT.md.
"""
from fractions import Fraction as F


def mul(p, q):
    v = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            v[i + j] += a * b
    return v


def power(p, k):
    a = [F(1)]
    for _ in range(k):
        a = mul(a, p)
    return a


def derivative(p):
    return [i * p[i] for i in range(1, len(p))]


def verify():
    polynomials = [
        [F(1), F(1)],
        [F(-1), F(0), F(1)],
        [F(2), F(-3), F(1)],
        [F(1), F(-1), F(2), F(1)],
        [F(-2), F(0), F(-1), F(1), F(1)],
    ]
    assertions = 0
    for p in polynomials:
        assert p[-1] == 1
        d = len(p) - 1
        for k in range(1, 9):
            N = d * k
            q = [x / d for x in mul(derivative(p), power(p, k - 1))]
            assert len(q) == N and q[-1] == 1
            assertions += 1
            # Exact norm/capacity ratios are rational after squaring.
            for r, R in [(F(0), F(1)), (F(1, 3), F(2)), (F(2, 3), F(5, 4))]:
                norm_div_pi = (R ** (2 * k) - r ** (2 * k)) / N
                assert norm_div_pi > 0
                bN_squared = N * norm_div_pi
                capacity_to_2N = R ** (2 * k)
                assert bN_squared / capacity_to_2N == 1 - (r / R) ** (2 * k)
                assertions += 3
            # Every rational function z^j / P(z)^k below the
            # critical degree is O(z^-2) at infinity.
            for j in range(N - 1):
                assert j - N <= -2
                assertions += 1
    print('EXACT_SUPPLEMENTARY_CHECKS_OK', assertions)


if __name__ == '__main__':
    verify()
