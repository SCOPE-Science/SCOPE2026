#!/usr/bin/env python3
"""Standalone, reproducible finite checks for the sparse Mallows matching theorem.

Python standard library only. No external input or random data.
"""
from itertools import permutations
from fractions import Fraction
from math import comb, log, log1p, sqrt


def inversions(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))


def code(p):
    pos = {value: index for index, value in enumerate(p)}
    return tuple(sum(pos[i] > pos[j] for i in range(1, j)) for j in range(1, len(p)+1))


def matching_permutation(p):
    n = len(p)
    for i in range(n):
        if p[i] not in (i, i + 1, i + 2):
            return False
    i = 0
    while i < n:
        if p[i] == i + 1:
            i += 1
        elif i + 1 < n and p[i] == i + 2 and p[i + 1] == i + 1:
            i += 2
        else:
            return False
    return True


def path_matching_poly(n, q):
    return sum(comb(n-k, k)*q**k for k in range(n//2+1))


def normalizer(n, q):
    z = 1
    for j in range(1, n+1):
        z *= sum(q**k for k in range(j))
    return z


def log_probability(n, q):
    # Stable all-n expression via recurrence for the weighted-path partition fn.
    # For q <= 0.5, signs and terms are controlled here for numerical checks.
    w = sqrt(1+4*q)
    rp = (1+w)/2
    rm = (1-w)/2
    log_num = (n+1)*log1p(rp-1) - log(w) + log1p(-(rm/rp)**(n+1))
    log_den = -n*log1p(-q) + sum(log1p(-(q**j)) for j in range(1,n+1))
    return log_num-log_den

checks = 0
for n in range(1, 9):
    pset = list(permutations(range(1,n+1)))
    inv_count = {}
    mallows_codes = set()
    for p in pset:
        c = code(p)
        assert len(c) == n and all(0 <= c[j] <= j for j in range(n))
        mallows_codes.add(c)
        is_match = matching_permutation(p)
        is_code_match = all(x<=1 for x in c) and all(c[j]*c[j+1]==0 for j in range(n-1))
        assert is_match == is_code_match, (n,p,c)
        assert inversions(p) == sum(c)
        inv_count[p] = inversions(p)
        checks += 3
    assert len(mallows_codes) == len(pset)
    for q in (Fraction(1,7),Fraction(1,3),Fraction(2,3)):
        denominator = sum(q**inv_count[p] for p in pset)
        numerator = sum(q**inv_count[p] for p in pset if matching_permutation(p))
        assert numerator == path_matching_poly(n,q), (n,q,numerator)
        assert denominator == normalizer(n,q), (n,q,denominator)
        if n>=2:
            assert abs(log_probability(n,float(q))-log(float(numerator/denominator))) < 1e-9
        checks += 3
for n in (100, 1000, 10000):
    for lam in (0.2, 1., 2.):
        q = lam/sqrt(n)
        if q >= 0.5:
            continue
        val = log_probability(n,q)
        assert abs(val+2*lam*lam) <= 16*(n*q**3 + q*q)
        checks += 1
print('PASS: %s direct structural, exact partition and asymptotic-bound checks'%checks)
