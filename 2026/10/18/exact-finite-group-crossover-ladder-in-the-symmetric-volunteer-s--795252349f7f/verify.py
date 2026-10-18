#!/usr/bin/env python3
"""Independent rational and floating-point checks of a finite-group volunteer law.

Uses only the Python standard library.  This file supplies corroboration; the
unbounded assertions are proved analytically in RESULT.md.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, exp, expm1, log


def S(n, lam):
    return sum(expm1(lam * k / (n * (n - 1))) for k in range(1, n))


def E(n, lam):
    return -n * expm1(-lam / (n - 1))


def boundary(n):
    lo, hi = 0., 2.
    for _ in range(80):
        md = (lo + hi) / 2
        if S(n, md) > 1:
            hi = md
        else:
            lo = md
    return (lo + hi) / 2


def rational_checks():
    count = 0
    for n in range(2, 35):
        a = sorted(([Fraction(k, n * (n - 1)) for k in range(1, n)]
                    + [Fraction(0)]), reverse=True)
        b = sorted([Fraction(k, n * (n + 1)) for k in range(1, n + 1)],
                   reverse=True)
        assert sum(a) == sum(b) == Fraction(1, 2)
        for r in range(1, n):
            assert sum(a[:r]) - sum(b[:r]) == Fraction(
                r * (n - r), n * (n * n - 1))
            count += 1
        # Exact rational identity equivalent to the forward difference.
        for z in (Fraction(1, 2), Fraction(2, 3), Fraction(7, 9)):
            direct = 1 - (n + 1) * z ** (n - 1) + n * z ** n
            rhs = (1 - z) * z ** (n - 1) * (
                sum(z ** (-k) - 1 for k in range(1, n)) - 1)
            assert direct == rhs
            count += 1
    return count


def numerical_checks():
    count = 0
    for n in range(2, 101):
        for lam in (0.3, 0.75, 1.3, 1.5, 1.8, 2., 2.4, 3.2):
            f = E(n + 1, lam) - E(n, lam)
            z = exp(-lam / (n * (n - 1)))
            rhs = (1 - z) * z ** (n - 1) * (S(n, lam) - 1)
            assert abs(f - rhs) < 2e-11
            if S(n, lam) < 1 - 1e-8:
                assert f < 1e-9
            if S(n, lam) > 1 + 1e-8:
                assert f > -1e-9
            count += 1
    seq = [boundary(n) for n in range(2, 1001)]
    assert abs(seq[0] - 2 * log(2)) < 2e-14
    assert all(a < b for a, b in zip(seq[:-1], seq[1:]))
    assert all(x < 2 for x in seq)
    for n in (100, 500, 1000):
        assert abs(n * (2 - boundary(n)) - Fraction(4, 3)) < 0.01
    for lam, maximum in ((1.3, 2), (1.5, 3), (1.7, 5)):
        # Check global maximum over a finite range as a numerical smoke test.
        v = [E(n, lam) for n in range(2, 501)]
        assert v.index(max(v)) + 2 == maximum
        count += 1
    # Validate expected count independently from a binomial distribution.
    for n in range(2, 12):
        for lam in (.75, 1.5, 2.5):
            p = -expm1(-lam / (n - 1))
            expected = sum(k * comb(n, k) * p ** k * (1-p) ** (n-k)
                           for k in range(n + 1))
            assert abs(expected - E(n, lam)) < 2e-12
            count += 1
    return count


if __name__ == '__main__':
    rc = rational_checks()
    nc = numerical_checks()
    print(f'PASS: {rc} exact rational identities; {nc} numerical checks')
    print('Thresholds:', [(n, round(boundary(n), 12)) for n in (2, 3, 4, 5, 10, 100, 1000)])
    print('n=2..5 at lambda=1.5:', [round(E(n, 1.5), 12) for n in range(2, 6)])
