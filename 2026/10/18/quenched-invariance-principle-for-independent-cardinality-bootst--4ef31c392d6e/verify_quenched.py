#!/usr/bin/env python3
"""Finite exact sanity checks for the one-factor cardinality bootstrap identity.

These checks are NOT a proof of the general almost-sure functional limit.
"""
from fractions import Fraction
from itertools import product
from math import comb


def active(n):
    return [k for k in range(n + 1) if comb(n, k) % 2]


def popcount(n):
    return n.bit_count()


def check_lucas():
    for n in range(1025):
        assert len(active(n)) == (1 << popcount(n)), n
        for k in range(n + 1):
            assert (comb(n, k) % 2 == 1) == ((k & n) == k)


def check_dyadic():
    rho = Fraction(3, 5)
    for d in range(11):
        left = sum((rho ** popcount(s) for s in range(1 << d)), Fraction(0))
        assert left == (1 + rho) ** d


def check_heterogeneous_row():
    for n in range(1, 7):
        p = [Fraction(2 * k + 3, 5 * n + 11) for k in range(n + 1)]
        assert all(Fraction(0) < x < Fraction(1) for x in p)
        for s in range(n + 1):
            odd = active(s)
            expected = Fraction(1)
            for k in odd:
                expected *= 1 - 2 * p[k]
            weighted = Fraction(0)
            for beta in product((0, 1), repeat=n + 1):
                prob = Fraction(1)
                for k, bit in enumerate(beta):
                    prob *= p[k] if bit else (1 - p[k])
                sign = (-1) ** sum(comb(s, k) * beta[k] for k in range(s + 1))
                weighted += prob * sign
            assert weighted == expected, (n, s)


def check_increment_covariance():
    # For any predictable sign, one-step covariance is [[1,zeta],[zeta,1]].
    for zeta in (-1, 1):
        increments = [(1, zeta), (-1, -zeta)]
        for i, j, expected in ((0, 0, 1), (1, 1, 1), (0, 1, zeta), (1, 0, zeta)):
            actual = sum((Fraction(u[i] * u[j], 2) for u in increments), Fraction(0))
            assert actual == expected


if __name__ == '__main__':
    check_lucas()
    check_dyadic()
    check_heterogeneous_row()
    check_increment_covariance()
    print('PASS: exact parity, digit sums, coefficient expectations and covariance tests')
