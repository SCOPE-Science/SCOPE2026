#!/usr/bin/env python3
"""Exact-rational checks for Mersenne-index reciprocal-binomial sums."""
from fractions import Fraction
from math import comb


def v2_integer(n):
    assert n != 0
    n = abs(n)
    return (n & -n).bit_length() - 1


def v2_fraction(x):
    assert x != 0
    return v2_integer(x.numerator) - v2_integer(x.denominator)


def f_direct(n):
    return sum((Fraction(1, comb(n, k)) for k in range(n + 1)), Fraction(0))


def f_harmonic(n):
    N = n + 1
    S = sum((Fraction(2 ** j, j) for j in range(1, N + 1)), Fraction(0))
    return Fraction(N, 2 ** N) * S


def main():
    vals = {}
    for e in range(1, 10):
        n = (1 << e) - 1
        x = f_direct(n)
        assert x == f_harmonic(n)
        val = v2_fraction(x)
        expected = {1: 1, 2: 3, 3: 8}.get(e, 3 * e - 2)
        assert val == expected, (e, val, expected)
        vals[e] = val
    # In the infinite series for L3, all terms after h=96 have valuation
    # greater than 2. Therefore this finite sum has the same valuation.
    L3_approx = sum((Fraction(2 ** h, h ** 3) for h in range(1, 97)), Fraction(0))
    assert v2_fraction(L3_approx) == -2
    print("VERIFY_OK exponents=1..9 valuations=" + repr(vals) + " Li3_prefix_v2=-2")


if __name__ == '__main__':
    main()
