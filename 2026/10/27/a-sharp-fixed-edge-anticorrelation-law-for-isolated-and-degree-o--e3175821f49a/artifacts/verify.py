#!/usr/bin/env python3
"""Exact reproducibility checks for isolated-vertex/leaf-count covariance in uniform random graphs."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb


def C(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def moments_fixed(n, m):
    N = C(n, 2)
    A = C(n-1, 2)
    B = C(n-2, 2)
    den = C(N, m)
    x0 = Fraction(n*C(A, m), den)
    x1 = Fraction(n*(n-1)*C(A, m-1), den)
    x01 = Fraction(n*(n-1)*(n-2)*C(B, m-1), den)
    return x0, x1, x01


def covariance_fixed(n, m):
    a, b, c = moments_fixed(n, m)
    return c-a*b


def covariance_bernoulli(n, p):
    q = 1-p
    return n*(n-1)*p*q**(2*n-4)*(n*p-2)


def exhaustive():
    count = 0
    for n in range(3,7):
        edges = list(combinations(range(n), 2))
        N = len(edges)
        aggregates = defaultdict(lambda: [0,0,0,0])
        for mask in range(1 << N):
            degrees = [0]*n
            for j,(u,v) in enumerate(edges):
                if mask >> j & 1:
                    degrees[u] += 1
                    degrees[v] += 1
            m = mask.bit_count()
            x0 = degrees.count(0)
            x1 = degrees.count(1)
            aggregate = aggregates[m]
            aggregate[0] += 1
            aggregate[1] += x0
            aggregate[2] += x1
            aggregate[3] += x0*x1
        for m in range(N+1):
            cnt,s0,s1,s01 = aggregates[m]
            assert cnt == C(N,m)
            theory = moments_fixed(n,m)
            actual = tuple(Fraction(x,cnt) for x in (s0,s1,s01))
            assert actual == theory, (n,m,actual,theory)
            assert covariance_fixed(n,m) < 0 if 2<=m<=C(n-1,2) else covariance_fixed(n,m)==0
            count += 5
        for p in (Fraction(1,5),Fraction(1,2),Fraction(4,5)):
            q=1-p
            ex0=ex1=ex01=Fraction(0)
            for m in range(N+1):
                cnt,s0,s1,s01=aggregates[m]
                weight=p**m*q**(N-m)
                ex0 += weight*s0
                ex1 += weight*s1
                ex01 += weight*s01
            assert ex01-ex0*ex1 == covariance_bernoulli(n,p)
            count += 1
    return count


def symbolic_scope():
    count=0
    for n in range(4,85):
        N,A,B=C(n,2),C(n-1,2),C(n-2,2)
        for m in range(N+1):
            value=covariance_fixed(n,m)
            if 2 <= m <= A: assert value < 0,(n,m,value)
            else: assert value == 0,(n,m,value)
            count += 1
        # Adjacent ratios with positive denominators; compare via integer products.
        r1=Fraction((n-2)*N,n*A)
        assert r1 == 1
        for m in range(1,B+1):
            # (R(m+1)/R(m)) strictly below 1.
            assert (B-m+1)*(N-m) < (A-m)*(A-m+1),(n,m)
            assert (n-3)*(n-1)-(A-m) == (A-m)*(A-m+1)-(B-m+1)*(N-m)
            count+=2
        for p in (Fraction(1,9),Fraction(1,3),Fraction(2,3),Fraction(8,9),Fraction(2,n)):
            # Goldstein--Rinott degree-count covariance identity for the independent-edge model.
            q=1-p
            b0=q**(n-1)
            b1=(n-1)*p*q**(n-2)
            joint=(n-2)*p*q**(2*n-4)
            exact=n*((n-1)*joint-n*b0*b1)
            assert exact == covariance_bernoulli(n,p),(n,p)
            count+=1
    return count


if __name__=='__main__':
    a=exhaustive()
    b=symbolic_scope()
    print('CHECKS_OK exhaustive_assertion_units=',a,' additional_exact_checks=',b, 'total=',a+b)
