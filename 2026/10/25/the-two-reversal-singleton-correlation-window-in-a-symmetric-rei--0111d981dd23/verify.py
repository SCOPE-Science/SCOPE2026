#!/usr/bin/env python3
"""Exact enumeration and asymptotic diagnostics for a reinforced occupancy model.

Each weak composition of n into q labeled parts has equal probability.
This verifies formulas independently by counted outcomes, not by symbolic substitution.
"""
from fractions import Fraction
from math import comb, isqrt

def weak_compositions(n,q):
    if q==1:
        yield (n,)
    else:
        for i in range(n+1):
            for tail in weak_compositions(n-i,q-1):
                yield (i,)+tail

def F(q,n):
    return n**3-(q+1)*n*n-(q*q-4*q+2)*n+(q-1)*(q-2)**2

def theoretical(q,n):
    p=Fraction((q-1)*n,(n+q-1)*(n+q-2))
    pp=Fraction((q-1)*(q-2)*n*(n-1),(n+q-1)*(n+q-2)*(n+q-3)*(n+q-4))
    return p,pp,pp-p*p

def cubic_cov(q,n):
    return Fraction(-n*(q-1)*F(q,n),(n+q-4)*(n+q-3)*(n+q-2)**2*(n+q-1)**2)

def check():
    cases=0; outcomes=0
    for q in range(3,12):
        for n in range(2,22):
            total=comb(n+q-1,q-1)
            if total>25000:continue
            aa=ab=0
            seen=0
            for v in weak_compositions(n,q):
                seen+=1
                aa+=v[0]==1
                ab+=(v[0]==1 and v[1]==1)
            assert seen==total
            p,pp,cov=theoretical(q,n)
            assert Fraction(aa,total)==p
            assert Fraction(ab,total)==pp
            assert Fraction(ab,total)-Fraction(aa,total)**2==cov==cubic_cov(q,n)
            assert (cov>0)==(F(q,n)<0)
            cases+=1; outcomes+=seen
    # q≥5 starts with a negative covariance, passes through positive at n=q,
    # and has a later negative example. q=3,4 begin positive.
    for q in range(3,1000):
        assert F(q,0)>0 and F(q,q)<0 and F(q,4*q+10)>0
        assert (F(q,2)>0)==(q>=5)
        assert F(q,2)!=0
    # The exact polynomial form and two asymptotic root locations also give
    # the signed second-order window, checked on representative large q.
    for q in (100,1000,10000,100000):
        for s in (-2,-1,0,1,2):
            n=q+s*isqrt(q)
            if n<2: continue
            scaled=float(cubic_cov(q,n))*q*q
            target=(1-s*s)/32
            assert abs(scaled-target)<3/isqrt(q)+1e-2
    return cases,outcomes

if __name__=='__main__':
    print('OK',check())
