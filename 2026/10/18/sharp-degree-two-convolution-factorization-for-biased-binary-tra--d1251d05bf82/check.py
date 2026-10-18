#!/usr/bin/env python3
"""Exact-arithmetic finite checks for binary transition-count polynomials.

The universal root-location argument is analytic and is supplied separately;
finite tests are independent diagnostics rather than its proof.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb


def add(a, b):
    c = [Q(0)] * max(len(a), len(b))
    for i, v in enumerate(a): c[i] += v
    for i, v in enumerate(b): c[i] += v
    return c


def mul(a, b):
    c = [Q(0)] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b): c[i + j] += v * w
    return c


def scale(a, c): return [v*c for v in a]


def recurrence(n, p):
    r = p*(1-p)
    if n == 1: return [Q(1)]
    a, b = [Q(1)], [1-2*r, 2*r]
    for _ in range(3, n+1):
        c = add(b, scale(mul([1, Q(0), -1], a), -r))
        a, b = b, c
    return b


def transfer(n, p):
    a, b = [1-p], [p]
    for _ in range(1, n):
        a, b = scale(add(a, mul([Q(0), Q(1)], b)), 1-p), scale(add(mul([Q(0), Q(1)], a), b), p)
    return add(a, b)


def brute(n, p):
    a = [Q(0)] * n
    for bits in product((0, 1), repeat=n):
        pr = (p**sum(bits))*(1-p)**(n-sum(bits))
        changes = sum(bits[i]!=bits[i+1] for i in range(n-1))
        a[changes] += pr
    return a


def determinant(a):
    n = len(a); rows = [row[:] for row in a]; ans=Q(1)
    for j in range(n):
        ind = next((i for i in range(j, n) if rows[i][j] != 0), None)
        if ind is None: return Q(0)
        if ind != j: rows[ind], rows[j] = rows[j], rows[ind]; ans=-ans
        pivot=rows[j][j]; ans*=pivot
        for i in range(j+1,n):
            v=rows[i][j]/pivot
            for k in range(j+1,n):rows[i][k]-=v*rows[j][k]
            rows[i][j]=Q(0)
    return ans


def hurwitz_minors(poly):
    m=len(poly)-1
    a=poly[::-1]
    H=[[a[2*j-i+1] if 0 <= 2*j-i+1 <= m else Q(0)
        for j in range(m)] for i in range(m)]
    return [determinant([row[:k] for row in H[:k]]) for k in range(1,m+1)]


def main():
    coeff_checks=0; root_checks=0; moment_checks=0
    ps=[Q(1,2),Q(1,3),Q(2,5),Q(1,7),Q(9,10),Q(1,17)]
    for n in range(2, 13):
        for p in ps:
            pol=recurrence(n,p)
            assert len(pol)==n
            assert pol==transfer(n,p), (n,p,'transfer')
            coeff_checks += n
            assert sum(pol)==1
            assert all(v>0 for v in pol)
            assert all(x>0 for x in hurwitz_minors(pol)),(n,p,'Hurwitz')
            root_checks += n-1
            r=p*(1-p); mu=2*(n-1)*r
            va=2*(n-1)*r*(1-2*r)+2*(n-2)*r*(1-4*r)
            assert sum(i*pol[i] for i in range(n))==mu
            assert sum(i*i*pol[i] for i in range(n))-mu*mu==va
            moment_checks+=2
            if p==Q(1,2):
                assert pol==[Q(comb(n-1,i),2**(n-1)) for i in range(n)]
            if p!=Q(1,2) and n>=3:
                assert va>mu*(1-mu/(n-1))
        if n<=9:
            for p in [Q(1,2),Q(1,3),Q(1,7)]:
                assert recurrence(n,p)==brute(n,p)
                coeff_checks+=n
    print('PASS',{'coefficient_identities':coeff_checks,
        'positive_Hurwitz_determinants':root_checks,
        'exact_moment_identities':moment_checks,
        'last_tested_sample_size':12})


if __name__=='__main__': main()
