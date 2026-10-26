#!/usr/bin/env python3
"""Exact census of pooled and shared species occupancy in two independent surveys."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import isqrt


def direct_cov(m, n):
    h = Counter()
    for seq in product(range(m), repeat=n):
        mask = 0
        for i in seq:
            mask |= 1 << i
        h[mask] += 1
    total = m ** (2*n)
    sum_s = sum_u = sum_su = 0
    for x, cx in h.items():
        for y, cy in h.items():
            weight = cx * cy
            shared = (x & y).bit_count()
            pooled = (x | y).bit_count()
            sum_s += weight * shared
            sum_u += weight * pooled
            sum_su += weight * shared * pooled
    return Fraction(sum_su, total) - Fraction(sum_s * sum_u, total*total)


def closed_cov(m, n):
    a = Fraction(m-1, m)**n
    b = Fraction(m-2, m)**n
    return m*m*a*a*(1-a)**2 - m*(m-1)*(a-b)**2


def sign(v):
    return (v > 0) - (v < 0)


def threshold(m):
    t = Fraction(m-1, m)
    s = Fraction(m-2, m-1)
    n = 1
    while True:
        r = (1-t**n)/(1-s**n)
        if r*r > t:
            return n
        n += 1


def main():
    comparisons = 0
    for m in range(2, 7):
        for n in range(1, 6):
            d = direct_cov(m,n)
            c = closed_cov(m,n)
            assert d == c, (m,n,d,c)
            comparisons += 1
    print('Independent complete two-survey census: %d exact covariance matches (2 <= m <= 6, 1 <= n <= 5).' % comparisons)
    for m in range(2,51):
        t=Fraction(m-1,m)
        s=Fraction(m-2,m-1)
        star=threshold(m)
        assert star >=2
        assert isqrt((m-1)*m)**2 != (m-1)*m
        for n in range(1,star+11):
            c=closed_cov(m,n)
            assert c !=0
            assert sign(c) == (-1 if n < star else 1),(m,n,star,c)
            r=(1-t**n)/(1-s**n)
            assert sign(c) == sign(r*r-t)
        print('m=%02d: exact first positive effort n_*=%d' % (m,star)) if m in (2,3,4,5,6,10,20,30,40,50) else None
    assert closed_cov(2,1) == Fraction(-1,4)
    assert closed_cov(2,2) == Fraction(1,64)
    assert closed_cov(3,3) == Fraction(-710,59049)
    assert closed_cov(3,4) == Fraction(97450,4782969)
    print('Strict unique signs and ratio criterion verified for 2 <= m <= 50 through n_*+10.')
    print('Four exact small-case checks passed. All operations are exact fractions except printed limiting constant.')
    print('alpha ~ 1.2564312086261696770, the positive nonzero solution of exp(alpha)=1+2alpha.')

if __name__ == '__main__':
    main()
