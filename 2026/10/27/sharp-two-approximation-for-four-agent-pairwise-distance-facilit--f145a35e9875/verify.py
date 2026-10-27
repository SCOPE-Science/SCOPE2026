"""Exact-arithmetic checks for the four-report two-facility theorem.

Runs with the Python 3 standard library: python verify.py
The universal inequality is established in the accompanying proof;
finite checks are supplementary tests, not a substitute for the proof.
"""
from fractions import Fraction
from itertools import combinations, product


def pairwise_cost(a, b, c):
    xs = (0, a, a + b, a + b + c)
    den = 0
    weighted = 0
    for i, j in combinations(range(4), 2):
        weight = xs[j] - xs[i]
        cost = sum(min(abs(t - xs[i]), abs(t - xs[j])) for t in xs)
        den += weight
        weighted += weight * cost
    return Fraction(weighted, den)


def expected_formula(a, b, c):
    numerator = (
        a * (2 * b + c)
        + (a + b) * (min(a, b) + c)
        + (a + b + c) * (min(a, b + c) + min(a + b, c))
        + b * (a + c)
        + (b + c) * (a + min(b, c))
        + c * (a + 2 * b)
    )
    return Fraction(numerator, 3 * a + 4 * b + 3 * c)


def opt_two(a, b, c):
    return min(a + b, a + c, b + c)


def full_report_opt(a, b, c):
    xs = (0, a, a + b, a + b + c)
    return min(
        sum(min(abs(z - xs[i]), abs(z - xs[j])) for z in xs)
        for i, j in combinations(range(4), 2)
    )


def certify():
    checks = 0
    for a, b, c in product(range(1, 21), repeat=3):
        exact = pairwise_cost(a, b, c)
        assert exact == expected_formula(a, b, c)
        checks += 1
        opt = opt_two(a, b, c)
        assert opt == full_report_opt(a, b, c)
        checks += 1
        assert exact < 2 * opt
        checks += 1
        assert exact == pairwise_cost(c, b, a)
        checks += 1
    for t in (10, 100, 1000, 10_000, 100_000):
        r = pairwise_cost(1, 1, t) / opt_two(1, 1, t)
        assert r == Fraction(12 * t + 13, 6 * t + 14)
        checks += 1
        assert r < 2
        checks += 1
        assert 2 - r == Fraction(15, 6 * t + 14)
        checks += 1
    print('PASS:', checks, 'exact-rational assertions')


if __name__ == '__main__':
    certify()
