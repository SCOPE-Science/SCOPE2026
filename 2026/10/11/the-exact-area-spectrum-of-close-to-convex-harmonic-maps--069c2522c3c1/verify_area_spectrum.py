"""Finite coefficient checks for a sharp harmonic area-spectrum theorem.

The all-order theorem follows from its analytic proof. These checks validate
normalizations, exact finite sums, and the extremal-family area formulas.
"""
from fractions import Fraction as Q
from math import log


def polynomial_area_over_pi(h, g, r):
    """Exact normalized Jacobian area from polynomial coefficient sequences."""
    nmax = max(len(h), len(g))
    return sum(
        n * ((h[n] if n < len(h) else Q(0)) ** 2
             - (g[n] if n < len(g) else Q(0)) ** 2) * r ** (2 * n)
        for n in range(1, nmax)
    )


def truncated_analytic_area(alpha, r, s, terms=90):
    c = 1 - alpha
    h = [Q(0), Q(1)] + [2 * c * s ** (n - 1) / n for n in range(2, terms + 2)]
    return polynomial_area_over_pi(h, [], r)


def analytic_area_formula(alpha, r, s):
    c = 1.0 - float(alpha)
    rr = float(r)
    ss = float(s)
    if ss == 0:
        return rr * rr
    x = (ss * rr) ** 2
    return rr * rr + 4 * c * c * (-log(1 - x) - x) / (ss * ss)


def verify():
    tests = 0
    for alpha in [Q(0), Q(1, 5), Q(1, 2), Q(4, 5)]:
        c = 1 - alpha
        for r in [Q(1, 4), Q(1, 2), Q(4, 5)]:
            lo = r * r - c * c * r ** 4 / 2
            low_h = [Q(0), Q(1)]
            low_g = [Q(0), Q(0), c / 2]
            assert polynomial_area_over_pi(low_h, low_g, r) == lo
            tests += 1
            for t in [Q(0), Q(1, 4), Q(3, 4), Q(1)]:
                assert polynomial_area_over_pi(low_h, [Q(0), Q(0), t * c / 2], r) == (
                    r * r - t * t * c * c * r ** 4 / 2
                )
                tests += 1
            # A nontrivial admissible harmonic polynomial has equal analytic and coanalytic areas.
            a, b = c / 8, c / 8
            assert 2 * (abs(a) + abs(b)) < c
            assert polynomial_area_over_pi([Q(0), Q(1), a], [Q(0), Q(0), b], r) == r * r
            tests += 1
            for s in [Q(0), Q(1, 2), Q(3, 4), Q(1)]:
                test_value = float(truncated_analytic_area(alpha, r, s))
                formula_value = analytic_area_formula(alpha, r, s)
                assert abs(test_value - formula_value) < 1e-10, (alpha, r, s)
                assert test_value >= float(r * r) - 1e-12
                tests += 1
    print('PASS:', tests, 'exact coefficient and extremal-family comparisons')
    print('NOTE: finite comparisons supplement, not establish, the all-parameter proof.')


if __name__ == '__main__':
    verify()
