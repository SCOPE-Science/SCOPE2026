#!/usr/bin/env python3
"""Supplementary finite checks for binomial founding-group mating-capacity identities.

The universal claims are proved analytically in RESULT.md; these are finite
exact-arithmetic checks and numerical asymptotic illustrations only.
"""
from fractions import Fraction
from math import comb, sqrt, log, isclose
from statistics import NormalDist


def breeders(k, n, h):
    return min(k, h * (n-k))


def expected(n, h, p):
    return sum(comb(n, k) * p**k * (1-p)**(n-k) * breeders(k, n, h)
               for k in range(n+1))


def derivative(n, h, p):
    return n * sum(comb(n-1, k) * p**k * (1-p)**(n-1-k) *
                   (breeders(k+1, n, h)-breeders(k, n, h))
                   for k in range(n))


def optimum(n, h):
    lo, hi = 0.0, 1.0
    for _ in range(70):
        m = (lo+hi)/2
        if derivative(n, h, m) > 0:
            lo = m
        else:
            hi = m
    return (lo+hi)/2


def binom_cdf(n, p, cutoff):
    return sum(comb(n,k)*p**k*(1-p)**(n-k) for k in range(cutoff+1))


def verify():
    tested = 0
    for n in range(2, 26):
        for h in range(1, 26):
            g = [breeders(k, n, h) for k in range(n+1)]
            d2 = [g[k+2]-2*g[k+1]+g[k] for k in range(n-1)]
            assert max(d2) <= 0 and min(d2) < 0
            dhalf = derivative(n, h, Fraction(1, 2))
            if n >= 3 and h >= 2:
                assert dhalf > 0, (n, h, dhalf)
            else:
                assert dhalf == 0, (n, h, dhalf)
            if h >= n-1:
                for k in range(n+1):
                    assert g[k] == (k if k < n else 0)
            if n % (h+1) == 0:
                p = optimum(n,h)
                q = h*n//(h+1)
                assert abs(binom_cdf(n-1, p, q-1)-h/(h+1)) < 2e-12
            tested += 1
    assert expected(3,2,Fraction(1,2)) == Fraction(9,8)
    assert isclose(optimum(3,2),1/sqrt(3),rel_tol=0,abs_tol=2e-14)
    assert isclose(expected(3,2,1/sqrt(3)),2/sqrt(3),abs_tol=1e-13)
    assert isclose(3*optimum(3,2)*(1-optimum(3,2)),sqrt(3)-1,abs_tol=1e-13)
    for n in range(3, 81):
        h = n-1
        p = optimum(n,h)
        q = n ** (-1/(n-1))
        assert isclose(p,q,rel_tol=0,abs_tol=2e-13)
        assert isclose(expected(n,h,p),(n-1)*q,rel_tol=0,abs_tol=2e-12)
    for h in (2,3,4):
        p0=h/(h+1)
        c=NormalDist().inv_cdf(p0)*sqrt(h)/(h+1)
        n=200*(h+1)
        p=optimum(n,h)
        assert abs(sqrt(n)*(p0-p)-c)<0.025
    n=5000
    p=n ** (-1/(n-1))
    assert abs(n*(1-p)-log(n))<.03
    print('PASS: %d (n,h) exact discrete-concavity and half-ratio cases;' % tested)
    print('PASS: exact small-case moments, binomial-quantile identities, saturated-capacity formula;')
    print('PASS: bounded numerical CLT illustrations, logarithmic male-reserve illustration.')
    print('Limits: finite tests are not universal proofs, and normal quantiles are numerical.')


if __name__=='__main__':
    verify()
