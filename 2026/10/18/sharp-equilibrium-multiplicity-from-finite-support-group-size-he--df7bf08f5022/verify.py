#!/usr/bin/env python3
"""Exact rational cross-checks for a quorum-two variable-group-size game.

The general sharpness theorem is proved analytically in RESULT.md; this script
certifies the signs of one illustrative two-support example and checks the
inequality margins on finite small instances only.
"""
from fractions import Fraction
from math import exp


def net_pivotality(x):
    """G(x)-c/B for sizes 101 and 10001, equal weights, c/B=1/8."""
    assert isinstance(x, Fraction)
    assert 0 <= x <= 1
    return (100 * x * (1 - x) ** 99
            + 10000 * x * (1 - x) ** 9999) / 2 - Fraction(1, 8)


def sign(x):
    return (x > 0) - (x < 0)


def main():
    points = [Fraction(0), Fraction(1, 10000), Fraction(1, 1000),
              Fraction(1, 100), Fraction(1)]
    signs = [sign(net_pivotality(x)) for x in points]
    assert signs == [-1, 1, -1, 1, -1], signs
    # Distinct exponents: -1/8 + 50(z^99-z^100)
    #                         + 5000(z^9999-z^10000).
    # There are 5 nonzero monomials and hence <=4 positive roots.
    coefficients = {0: Fraction(-1, 8), 99: Fraction(50),
                    100: Fraction(-50), 9999: Fraction(5000),
                    10000: Fraction(-5000)}
    coeff_signs = [sign(coefficients[k]) for k in sorted(coefficients)]
    changes = sum(a != b for a, b in zip(coeff_signs, coeff_signs[1:]))
    assert changes == 4
    # Finite spot-checks of analytic separation inequalities only.
    for m in range(1, 40):
        L = 16 * m
        assert L >= 16
        assert (L - 1 - 2 * __import__('math').log(L)) > 0
        assert exp(1 - L) * L * L < 1
    print('Exact rational signs:', signs)
    print('Descartes sign variation:', changes)
    print('PASS: four distinct interior roots in the two-size example; elementary margins checked')


if __name__ == '__main__':
    main()
