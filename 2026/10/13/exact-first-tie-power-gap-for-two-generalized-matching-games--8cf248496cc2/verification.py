#!/usr/bin/env python3
"""Exact-arithmetic checks for a two-game matching-test likelihood ordering.

Run: python3 verification_matching.py

The continuum inequalities and Neyman--Pearson argument are proved in RESULT.md;
finite arithmetic checks are diagnostics, not a substitute for those proofs.
"""
from fractions import Fraction
from math import comb, factorial


def classical(n, k):
    if not 0 <= k <= n:
        return Fraction(0)
    return sum((Fraction(-1 if j % 2 else 1, factorial(j))
                for j in range(n - k + 1)), Fraction(0)) / factorial(k)


def matching(n, k, theta):
    return sum((Fraction(comb(n, ell)) * theta ** ell *
                (1 - theta) ** (n - ell) * classical(n - ell, k - ell)
                for ell in range(k + 1)), Fraction(0))


def qpoly(n, k, r):
    return sum((Fraction(comb(k, ell)) *
                Fraction(factorial(n), factorial(n - ell)) * r ** ell
                for ell in range(k + 1)), Fraction(0))


def tests(n, theta):
    a, b, c = (classical(n, k) for k in (0, 1, 2))
    assert min(a, b, c) > 0
    r = theta / (1 - theta)
    q0, q1, q2, q3 = (qpoly(n, k, r) for k in (0, 1, 2, 3))
    assert q1 * q1 - q0 * q2 == n * r * r
    assert q3 - q1 * q1 == (n*r + n*(2*n-3)*r*r +
                                n*(n-1)*(n-2)*r**3)
    assert q1 > q0 and q2 > q1 and q3 > q2
    for k in range(n + 1):
        mass = classical(n, k)
        if mass:
            assert matching(n, k, theta) / mass == (1-theta)**n * qpoly(n, k, r)
    p0, p1, p2 = (matching(n, k, theta) for k in (0, 1, 2))
    size = 1 - a*a - 2*a*b - 2*a*c
    gamma = b*b/(b*b+2*a*c)
    assert 0 < size < 1 and 0 < gamma < 1
    pow_balanced = 1 - p0*p0 - 2*p0*p1 - 2*p0*p2
    pow_total = 1 - p0*p0 - 2*p0*p1 - (1-gamma)*(p1*p1+2*p0*p2)
    # The total-based test retains the same T>=3 part and randomizes at T=2.
    gap = pow_balanced - pow_total
    exact_gap = (2*a*c*b*b/(b*b+2*a*c) * n * theta**2 *
                 (1-theta)**(2*n-2))
    assert gap == exact_gap and gap > 0
    assert p1*p1 - (p0*p2) * (b*b/(a*c)) == (b*b) * n * theta**2 * (1-theta)**(2*n-2)
    # Complete natural significance band: arbitrary sizes and both NP boundary branches.
    A = b*b
    B = 2*a*c
    beta = 1 - a*a - 2*a*b - A - B
    for t in (Fraction(0), Fraction(1, 4), Fraction(1, 2),
              Fraction(3, 4), Fraction(1)):
        for alpha, np_gain_factor in ((beta + t*A, t),
                                      (beta + A + t*B, 1-t)):
            total_random = (alpha-beta)/(A+B)
            if alpha <= beta+A:
                np_power_at_t = (1 - p0*p0 - 2*p0*p1 - p1*p1 - 2*p0*p2
                                 + ((alpha-beta)/A)*p1*p1)
            else:
                np_power_at_t = (1 - p0*p0 - 2*p0*p1 - p1*p1 - 2*p0*p2
                                 + p1*p1 + ((alpha-beta-A)/B)*2*p0*p2)
            total_power_at_t = (1 - p0*p0 - 2*p0*p1 - p1*p1 - 2*p0*p2
                                + total_random*(p1*p1+2*p0*p2))
            assert np_power_at_t - total_power_at_t == exact_gap*np_gain_factor
    # For any sample with T>=3, LR dominates that of (1,1):
    # coordinatewise monotonicity and q3>q1^2 or q1*q2>q1^2.
    assert q0*q3 > q1*q1 and q1*q2 > q1*q1
    return gap


def main():
    cases = 0
    for n in range(4, 12):
        for theta in (Fraction(1, 20), Fraction(1, 5), Fraction(1, 2),
                      Fraction(4, 5)):
            tests(n, theta)
            cases += 1
    print('PASS: exact mass-function, likelihood, ordering and power-gap checks,',
          cases, 'rational parameter pairs')
    for lam in (Fraction(1, 2), Fraction(1), Fraction(2)):
        for n in (10, 20, 40):
            gap = tests(n, lam/n)
            # The displayed coefficient should be approached as n grows.
            assert gap > 0
        print('positive sparse-intensity power gains: intensity', lam)
    print('PASS: symbolic Q-polynomial identities and finite diagnostics')


if __name__ == '__main__':
    main()
