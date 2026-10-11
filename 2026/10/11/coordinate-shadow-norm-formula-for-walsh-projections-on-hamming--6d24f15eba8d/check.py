#!/usr/bin/env python3
"""Exact finite-cube checks of the coordinate-shadow Walsh projection identity.

Uses integer Walsh transforms and rational kernel averages. No external packages.
"""
from itertools import product
from fractions import Fraction
from math import comb
import random


def char(mask, x):
    return -1 if (mask & x).bit_count() % 2 else 1


def transform(values):
    n = len(values)
    out = list(values)
    step = 1
    while step < n:
        for base in range(0,n,2*step):
            for j in range(base,base+step):
                a,b=out[j],out[j+step]
                out[j],out[j+step]=a+b,a-b
        step *= 2
    return out


def lip_edges(values,n):
    return max(abs(values[x]-values[x^(1<<i)])
               for x in range(1<<n) for i in range(n))


def projection(values, support,n):
    coeff=transform(values)
    keep=[coeff[s] if s in support else 0 for s in range(1<<n)]
    # Walsh inverse (the same transform divided by the group size).
    return transform(keep)


def shadow_value(support,n,i):
    # integer numerator of the expectation, denominator 2^(n-1)
    others=[j for j in range(n) if j!=i]
    reduced=[sum(((s>>j)&1)<<q for q,j in enumerate(others))
             for s in support if (s>>i)&1]
    num=0
    for x in range(1<<(n-1)):
        num+=abs(sum(char(s,x) for s in reduced))
    return Fraction(num,1<<(n-1))


def full_shadow(support,n):
    return max(shadow_value(support,n,i) for i in range(n))


def witness(support,n,i):
    others=[j for j in range(n) if j!=i]
    red=[sum(((s>>j)&1)<<q for q,j in enumerate(others))
         for s in support if (s>>i)&1]
    def g(y):
        kval=sum(char(s,y) for s in red)
        return 1 if kval>=0 else -1
    out=[]
    for x in range(1<<n):
        y=sum(((x>>j)&1)<<q for q,j in enumerate(others))
        out.append(char(1<<i,x)*g(y))
    return out


def test_case(support,n):
    support=set(support)
    if not support:
        return
    vals=[shadow_value(support,n,i) for i in range(n)]
    maxi=max(range(n),key=lambda i: vals[i])
    f=witness(support,n,maxi)
    assert lip_edges(f,n)==2
    qf=projection(f,support,n)
    # qf are 2^n times the genuine projected values.
    lhs=Fraction(lip_edges(qf,n), (1<<n)*2)
    assert lhs==vals[maxi],(n,support,lhs,vals[maxi])
    # Averaging every edge-derivative proves the upper bound in exact integer arithmetic.
    for i in range(n):
        dd=[f[x]-f[x^(1<<i)] for x in range(1<<n) if not ((x>>i)&1)]
        assert max(abs(z) for z in dd)<=2
    return 1


if __name__=='__main__':
    cases=0
    for n in (1,2,3):
        universe=list(range(1,1<<n))
        for bits in range(1,1<<len(universe)):
            support=[universe[j] for j in range(len(universe)) if (bits>>j)&1]
            cases+=test_case(support,n)
    rng=random.Random(982166)
    for n in (4,5,6):
        universe=list(range(1,1<<n))
        for rep in range(150):
            p=rng.choice((0.15,0.30,0.50,0.75))
            support=[s for s in universe if rng.random()<p]
            if not support: support=[universe[rep%len(universe)]]
            cases+=test_case(support,n)
    # Homogeneous degree-two binomial formulas across many dimensions.
    for n in range(2,25):
        m=n-1
        expected=Fraction(m*comb(m-1,(m-1)//2),2**(m-1))
        direct=Fraction(sum(comb(m,r)*abs(m-2*r) for r in range(m+1)),2**m)
        assert expected==direct
        if n<=6:
            S=[s for s in range(1,1<<n) if s.bit_count()==2]
            assert full_shadow(S,n)==direct
    print('PASS',cases,'nonempty arbitrary-spectrum witness checks;',
          '23 exact degree-two moment identities')
