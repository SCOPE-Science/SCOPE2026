#!/usr/bin/env python3
"""Independent exact-rational checks for a symmetric Dirichlet-multinomial occupancy covariance."""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial


def rise(x, n):
    out = F(1)
    for j in range(n):
        out *= x + j
    return out


def compositions(n, k):
    if k == 1:
        yield (n,)
    else:
        for j in range(n + 1):
            for other in compositions(n - j, k - 1):
                yield (j,) + other


def enumerated_cov(k, n, a):
    z = rise(k*a, n)
    mass = F(0)
    mean_zero = F(0)
    mean_two = F(0)
    mean_product = F(0)
    for config in compositions(n, k):
        prob = F(factorial(n), 1)
        for c in config:
            prob *= rise(a, c) / factorial(c)
        prob /= z
        b0 = config.count(0)
        b2 = config.count(2)
        mass += prob
        mean_zero += b0 * prob
        mean_two += b2 * prob
        mean_product += b0 * b2 * prob
    assert mass == 1
    return mean_product - mean_zero * mean_two


def scaled_ratio(k, n, a):
    assert k >= 3 and n >= 2 and a > 0
    r = F(k*a + 1, (k-1)*a + 1)  # R at n = 2
    for j in range(2, n):
        r *= (((k-2)*a+j-2)*(k*a+j)
              / (((k-1)*a+j-2)*((k-1)*a+j)))
    return r


def closed_cov(k, n, a):
    if n < 2:
        return F(0)
    u = rise((k-1)*a, n) / rise(k*a, n)
    v = comb(n, 2) * rise(a, 2) * rise((k-1)*a, n-2) / rise(k*a, n)
    return k*k*u*v*(scaled_ratio(k, n, a)-1)


count_enumeration = 0
for k in range(3, 7):
    for n in range(9 if k <= 5 else 7):
        for a in (F(1,3), F(1,2), F(1), F(3,2), F(2)):
            assert enumerated_cov(k, n, a) == closed_cov(k, n, a), (k, n, a)
            count_enumeration += 1

count_ratio = 0
for k in range(3, 25):
    for a in (F(1,3), F(1,2), F(1), F(3,2), F(2), F(5)):
        r = scaled_ratio(k, 2, a)
        assert r > 1
        first_nonpositive = None
        for n in range(2, 65):
            if first_nonpositive is not None:
                assert r < 1 or (n == first_nonpositive and r == 1)
            elif r <= 1:
                first_nonpositive = n
            rn1 = scaled_ratio(k, n+1, a)
            assert rn1 < r
            assert rn1 / r == 1 - (a*(a+2)) / (((k-1)*a+n-2)*((k-1)*a+n))
            if a == 1:
                assert r - 1 == F(k+2-2*n, k*(k+n-4))
            r = rn1
            count_ratio += 1
        assert first_nonpositive is not None

print('PASS: Dirichlet-multinomial complete-composition enumeration cells',count_enumeration)
print('PASS: exact ratio-step identities, monotonicity, and a=1 zeros',count_ratio)
print('FINITE TESTS DO NOT PROVE THE ALL-PARAMETER OR ASYMPTOTIC CLAIMS.')
