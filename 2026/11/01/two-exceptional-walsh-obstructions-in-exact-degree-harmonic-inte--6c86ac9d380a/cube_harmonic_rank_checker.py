#!/usr/bin/env python3
"""Exact-rational small-dimensional checks for hypercube harmonic evaluation ranks.

The universal classification is proved analytically; finite checks are independent
sanity tests, not a substitute for the general proof.
"""
from fractions import Fraction
from math import comb


def gegenbauer(n, alpha, x):
    if n == 0:
        return Fraction(1)
    prev, current = Fraction(1), 2 * alpha * x
    if n == 1:
        return current
    for degree in range(2, n + 1):
        nxt = (2 * (degree + alpha - 1) * x * current -
               (degree + 2 * alpha - 2) * prev) / degree
        prev, current = current, nxt
    return current


def walsh_eigenvalue(d, ell, k):
    alpha = Fraction(d - 2, 2)
    total = Fraction(0)
    for h in range(d + 1):
        charsum = sum((-1)**j * comb(k, j) * comb(d - k, h - j)
                      for j in range(max(0, h - (d-k)), min(k, h) + 1))
        total += charsum * gegenbauer(ell, alpha, Fraction(d - 2*h, d))
    return total


def expected_positive(d, ell, k):
    return (ell >= k and (ell-k) % 2 == 0 and
            not (ell == 2 and k == 0) and
            not (ell == d+2 and k == d))


def main():
    cases = 0
    for d in range(3, 9):
        for ell in range(0, 19):
            rank = 0
            for k in range(d + 1):
                lam = walsh_eigenvalue(d, ell, k)
                wanted = expected_positive(d, ell, k)
                assert (lam > 0) == wanted, (d, ell, k, lam, wanted)
                if wanted:
                    rank += comb(d, k)
                cases += 1
            predicted = sum(comb(d, k) for k in range(d+1)
                            if k <= ell and (ell-k) % 2 == 0)
            predicted -= int(ell == 2) + int(ell == d + 2)
            assert rank == predicted
    print(f'Exact Gegenbauer/Walsh checks passed: {cases} spectral sectors; '
          'dimensions 3..8 and degrees 0..18.')


if __name__ == '__main__':
    main()
