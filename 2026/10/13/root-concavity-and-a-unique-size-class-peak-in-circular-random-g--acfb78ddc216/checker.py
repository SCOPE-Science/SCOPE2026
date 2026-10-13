#!/usr/bin/env python3
"""Exact arithmetic and numerical checks for circular component-size profiles."""
from fractions import Fraction
from math import comb, exp, log, sqrt
import random

def predicted(n,k,r):
    return sum(Fraction((-1)**j*comb(k-1,j)) * max(Fraction(0), 1 - (j+2)*r)**(n-1) for j in range(k))

def count_components(gaps, r, k):
    n=len(gaps)
    cuts=[i for i,v in enumerate(gaps) if v>r]
    if len(cuts)<2:
        return 0
    return sum(1 for i,j in zip(cuts, cuts[1:]+cuts[:1]) if (j-i)%n==k)

def check():
    # Rational inclusion-exclusion respects all boundary cases.
    exact=0
    for n in range(3,17):
        for k in range(2,n):
            for j in range(1,48):
                r=Fraction(j,100)
                p=predicted(n,k,r)
                assert 0<=p<=1,(n,k,r,p)
                exact+=1
    # Brunn-Minkowski root-power inequality on dense rational grid.
    concavity=0
    for n in range(3,17):
        for k in range(2,n):
            f=[float(predicted(n,k,Fraction(j,60)))**(1/(n-1)) for j in range(31)]
            for j in range(1,30):
                assert f[j]>=.5*(f[j-1]+f[j+1])-1e-11, (n,k,j, f[j]- .5*(f[j-1]+f[j+1]))
                concavity+=1
    # Independent spacings simulation: cyclic lengths of consecutive run segments.
    rng=random.Random(2137007)
    simulation=0
    for n,k,r in [(4,2,.19),(5,3,.27),(7,2,.21),(8,4,.13),(10,3,.15)]:
        target=n*float(predicted(n,k,Fraction(str(r))))
        count=0
        ntrials=160000
        for _ in range(ntrials):
            z=[rng.expovariate(1) for _ in range(n)]
            total=sum(z);gs=[v/total for v in z]
            count+=count_components(gs,r,k)
        observed=count/ntrials
        err=abs(observed-target)
        assert err<.015,(n,k,r, observed, target, err)
        simulation+=1
    # All fixed-k sparse scaling peaks at log((k+1)/2).
    asym=0
    for k in range(2,7):
        c=log((k+1)/2)
        f=lambda x: exp(-2*x)*(1-exp(-x))**(k-1)
        assert f(c)>f(c-.15) and f(c)>f(c+.15)
        n=1200
        got=sum((-1)**j*comb(k-1,j)*max(0,1-(j+2)*c/n)**(n-1) for j in range(k))
        assert abs(got-f(c))<.004, (k,got,f(c))
        asym+=1
    print(f'PASS exact cells={exact} root-concavity tests={concavity} independent simulations={simulation} sparse cases={asym}')
if __name__=='__main__': check()
