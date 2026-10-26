#!/usr/bin/env python3
"""Exact finite checks for the rank-decreasing binary cellular automaton."""
from itertools import product
from fractions import Fraction
from collections import defaultdict


def forward(r, u):
    return tuple((u[i] ^ (u[i+1] if i+1<len(u) and r[i] == r[i+1]+1 else 0)) for i in range(len(u)))

def inverse(r, v):
    out=[]
    for i in range(len(r)):
        j=i
        val=v[j]
        while j+1<len(r) and r[j]==r[j+1]+1:
            j+=1
            val ^= v[j]
        out.append(val)
    return tuple(out)

def finite_tail(q,k,K):
    z=(1-q**(K+1))/(1-q)
    weight=lambda r: q**r/z
    tot=Fraction(0)
    for r in product(range(K+1),repeat=k+1):
        if all(r[i]==r[i+1]+1 for i in range(k)):
            a=Fraction(1)
            for v in r:a*=weight(v)
            tot+=a
    closed=sum((q**((k+1)*r-k*(k+1)//2) for r in range(k,K+1)),Fraction(0))/z**(k+1)
    assert tot==closed,(q,k,K,tot,closed)
    return tot

def bayes_error(q,R,K):
    length=K+1
    z=(1-q**(K+1))/(1-q)
    pw=[q**r/z for r in range(K+1)]
    mass=defaultdict(lambda:[Fraction(0),Fraction(0)])
    for r in product(range(K+1),repeat=length):
        prob=Fraction(1,2**length)
        for t in r:prob*=pw[t]
        for v in product((0,1),repeat=length):
            target=inverse(r,v)[0]
            key=(r[:R+1],v[:R+1])
            mass[key][target]+=prob
    err=sum((min(p0,p1) for p0,p1 in mass.values()),Fraction(0))
    expected=finite_tail(q,R+1,K)/2
    assert err==expected,('bayes',q,R,K,err,expected)
    return err

checks=0
for r in product(range(4),repeat=5):
    for u in product((0,1),repeat=5):
        v=forward(r,u)
        assert inverse(r,v)==u,(r,u,v)
        checks+=1
print('INVERSION_EXHAUSTIVE_PASS',checks)
for q in [Fraction(1,3),Fraction(1,2),Fraction(2,3)]:
    for k in range(5):
        p=finite_tail(q,k,6)
        print('FINITE_TAIL_PASS',str(q),k,str(p))
for R in range(3):
    print('SHARP_BAYES_PASS',R,str(bayes_error(Fraction(1,2),R,3)))
print('CHECKS_PASS')
