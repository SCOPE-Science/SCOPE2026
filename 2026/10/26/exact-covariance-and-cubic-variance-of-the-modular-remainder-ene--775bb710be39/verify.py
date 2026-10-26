#!/usr/bin/env python3
"""Exact arithmetic checks for the modular-remainder variance theorem.

Run with: python3 verify.py
No packages beyond the Python standard library are needed.
"""
from fractions import Fraction
from math import gcd, lcm


def jordan_two(limit):
    # J_2(n) = n^2 * product_{p|n}(1-p^{-2}), integer sieve.
    values = [k*k for k in range(limit + 1)]
    for p in range(2, limit + 1):
        if values[p] == p*p:  # p is prime since no preceding prime changed it
            for j in range(p, limit + 1, p):
                values[j] = values[j] // (p*p) * (p*p - 1)
    return values


def exact_gcd_variance(m):
    return Fraction(sum(gcd(i, j)**2 - 1
                        for i in range(1, m+1)
                        for j in range(1, m+1)), 12)


def exact_jordan_variance(m, j2):
    return Fraction(sum(j2[d]*(m//d)**2 for d in range(1, m+1)) - m*m, 12)


# Independent full-period sampling, not based on the covariance or Jordan formulas.
periods = 0
for m in range(1, 13):
    period = lcm(*range(1, m+1))
    values = [sum(n % k for k in range(1, m+1)) for n in range(period)]
    mean = Fraction(sum(values), period)
    assert mean == Fraction(m*(m-1), 4), (m, 'mean')
    variance = Fraction(sum(v*v for v in values), period) - mean*mean
    assert variance == exact_gcd_variance(m), (m, 'variance')
    periods += 1

# Independent pair-residue sampling over individual joint periods.
pairs = 0
for a in range(1, 31):
    for b in range(1, 31):
        period = lcm(a, b)
        centered_prod = sum((2*(n % a)-(a-1))*(2*(n % b)-(b-1))
                            for n in range(period))
        covariance = Fraction(centered_prod, 4*period)
        assert covariance == Fraction(gcd(a,b)**2-1,12), (a,b)
        pairs += 1

# Jordan's convolution produces the exact second moment independently.
limit = 1200
j2 = jordan_two(limit)
for n in range(1,limit+1):
    assert sum(j2[d] for d in range(1,n+1) if n%d == 0) == n*n, n
for m in list(range(1,121)) + [200, 400, 600, 800, 1000, 1200]:
    assert exact_jordan_variance(m,j2) == exact_gcd_variance(m)

print('VERIFY_OK full_periods=%s pair_covariances=%s jordan_divisor_convolutions=%s'
      ' large_m_checks=6 all_exact_rational=PASS' % (periods,pairs,limit))
