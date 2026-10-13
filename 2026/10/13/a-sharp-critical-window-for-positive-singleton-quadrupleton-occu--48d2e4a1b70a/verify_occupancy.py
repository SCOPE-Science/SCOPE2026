"""Exact reproducibility checks for a two-frequency occupancy covariance."""
from fractions import Fraction
from itertools import product
from math import comb, exp, log1p, sqrt


def formula(m, n):
    assert m >= 3 and n >= 4
    a = Fraction(m - 1, m)
    b = Fraction(m - 2, m)
    e1 = n * a ** (n - 1)
    e4 = Fraction(comb(n, 4), m ** 3) * a ** (n - 4)
    mixed = (Fraction((m - 1) * n * comb(n - 1, 4), m ** 4)
             * b ** (n - 5)) if n >= 5 else Fraction(0)
    covariance = mixed - e1 * e4
    if n >= 5:
        ratio = Fraction(n - 4, n) * b ** (n - 5) / a ** (2 * n - 6)
        assert covariance == e1 * e4 * (ratio - 1)
    return e1, e4, mixed, covariance


def exhaustive(m, n):
    k1 = k4 = both = 0
    for labels in product(range(m), repeat=n):
        occupancies = [0] * m
        for label in labels:
            occupancies[label] += 1
        x1 = occupancies.count(1)
        x4 = occupancies.count(4)
        k1 += x1
        k4 += x4
        both += x1 * x4
    d = m ** n
    a, b, c = Fraction(k1, d), Fraction(k4, d), Fraction(both, d)
    return a, b, c, c - a * b


def ratio(m, n):
    assert m >= 3 and n >= 5
    a, b = Fraction(m - 1, m), Fraction(m - 2, m)
    return Fraction(n - 4, n) * b ** (n - 5) / a ** (2 * n - 6)


def log_ratio(m, n):
    return (log1p(-4.0 / n)
            + (n - 5) * log1p(-2.0 / m)
            - (2 * n - 6) * log1p(-1.0 / m))


def tests():
    exhaustive_cases = [(3, 4), (3, 5), (3, 6), (4, 8), (5, 6)]
    for m, n in exhaustive_cases:
        assert exhaustive(m, n) == formula(m, n), (m, n)

    algebraic_checks = 0
    for m in range(3, 41):
        assert ratio(m, 2 * m) > 1
        for n in range(5, 4 * m + 1):
            if n > 5:
                quotient = ratio(m, n) / ratio(m, n - 1)
                positive = ((n) * (n - 5) < 4 * m * (m - 2))
                assert (quotient > 1) == positive, (m, n)
                assert quotient != 1
            if n < 2 * m:
                assert ratio(m, n + 1) > ratio(m, n)
            elif n >= 2 * m:
                assert ratio(m, n + 1) < ratio(m, n)
            algebraic_checks += 1
        positives = [n for n in range(5, 4 * m + 1) if ratio(m, n) > 1]
        assert positives == list(range(min(positives), max(positives) + 1))
        assert 2 * m in positives

    numerical_checks = 0
    target = (4.0 / 3.0) * exp(-4)
    for m in (500, 2000, 10000):
        for z in (-2.0, -1.0, 0.0, 1.0, 2.0):
            n = max(5, int(round(2 * m + z * sqrt(m))))
            e1 = n * (1 - 1 / m) ** (n - 1)
            e4 = (comb(n, 4) / m ** 3) * (1 - 1 / m) ** (n - 4)
            actual = e1 * e4 * (exp(log_ratio(m, n)) - 1)
            expected = target * (1 - z * z / 2)
            assert abs(actual - expected) < 0.012, (m, z, actual, expected)
            numerical_checks += 1
    print('PASS: {} exhaustive allocations, {} exact-rational quotient checks, {} numerical limit checks'.format(
        len(exhaustive_cases), algebraic_checks, numerical_checks))
    for m in (3, 4, 5, 20, 100):
        pos = [n for n in range(5, 4 * m + 1) if ratio(m, n) > 1]
        print('m={}, positive integer ball counts {}..{}'.format(m, min(pos), max(pos)))


if __name__ == '__main__':
    tests()
