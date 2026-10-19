#!/usr/bin/env python3
"""Standalone finite identity checks for the Cantor-driven affine invariant law.

Analytical infinitary estimates are proved in RESULT.md; this is not an
infinite proof oracle or an independent audit.
"""
import math
from collections import Counter
from fractions import Fraction


def main():
    # For each diagonal m=n+k with n>=0 and k>=1, exactly m signs occur.
    pairs = Counter(n + k for n in range(12) for k in range(1, 13 - n))
    assert all(pairs[m] == m for m in range(1, 13))

    # Triple-angle product has the exact worst magnitude 9/16.
    vertex = Fraction(3, 8)
    quad = lambda z: 4 * z * z - 3 * z
    assert quad(vertex) == Fraction(-9, 16)
    assert quad(Fraction(1, 4)) == Fraction(-1, 2)
    assert quad(Fraction(3, 4)) == 0
    assert 16 * 16 > 3 * 9 * 9   # kappa=log_3(16/9)>1/2.

    # The bound A >= (1/2)(1-pi^2/144)>4/9>1/3 uses pi<4.
    assert Fraction(4, 9) > Fraction(1, 3)
    assert Fraction(2, 3) * Fraction(1, 3) < Fraction(1, 3)

    J = 30
    A = math.prod(math.cos(math.pi / 3**j) for j in range(1, J + 1))
    B = math.prod(math.cos(math.pi / 3**j)**j for j in range(1, J + 1))
    assert A > 4 / 9 and B > 0 and 3*A > 1

    # Exact finite product grouping at resonant frequencies (modulo floating error).
    for N in (1, 2, 5, 8, 11):
        t = (math.pi / 2) * 3**(N + 1)
        direct = math.prod(abs(math.cos(2*t / 3**(m+1)))**m
                           for m in range(1, N + J + 1))
        grouped = A**N * B
        assert math.isclose(direct, grouped, rel_tol=3e-12, abs_tol=1e-15)

    # The lower Fourier bands are not isolated point artifacts.
    for N in (3, 6, 9):
        t = math.pi * 3**(N + 1) / 2
        for offset in (-0.1, 0, 0.1):
            val = math.prod(abs(math.cos(2*(t+offset)/3**(m+1)))**m
                            for m in range(1, N + J + 1))
            assert val > 0.95 * A**N * B

    print("VERIFY_OK")
    print("A = %.15f, B = %.15f, 3A = %.15f" % (A,B,3*A))
    print("Fourier upper exponent kappa = %.12f" % (math.log(16/9)/math.log(3)))
    print("Sobolev exclusion threshold s_star = %.12f" % (-math.log(A)/math.log(3)))


if __name__ == "__main__":
    main()
