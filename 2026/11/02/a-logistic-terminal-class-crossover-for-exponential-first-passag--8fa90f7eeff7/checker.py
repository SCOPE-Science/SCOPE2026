#!/usr/bin/env python3
"""Finite rational checks for terminal-class first-passage percolation on K_{a,b}."""
from fractions import Fraction
from functools import lru_cache
import math
import random


def backward_last_A(a,b):
    @lru_cache(None)
    def rec(i,j):
        if i==a and j==b:
            return Fraction(0)
        if i==a:
            return Fraction(0)
        if j==b:
            return Fraction(1)
        ra=(a-i)*j
        rb=(b-j)*i
        return (ra*rec(i+1,j)+rb*rec(i,j+1))/(ra+rb)
    return rec(1,0)


def forward_last_A(a,b):
    mass={(1,0): Fraction(1)}
    last_A=Fraction(0)
    last_B=Fraction(0)
    for total in range(1,a+b):
        next_mass={}
        for (i,j),p in mass.items():
            ra=(a-i)*j
            rb=(b-j)*i
            rate=ra+rb
            if rate==0:
                raise ValueError('Premature absorbing state')
            for ni,nj,w in ((i+1,j,ra),(i,j+1,rb)):
                if w==0: continue
                q=p*Fraction(w,rate)
                if ni==a and nj==b:
                    if ni>i: last_A+=q
                    else: last_B+=q
                else:
                    next_mass[(ni,nj)]=next_mass.get((ni,nj),Fraction(0))+q
        mass=next_mass
    assert not mass
    assert last_A+last_B==1
    return last_A


def simulate_last_A(a,b,reps,seed):
    rng=random.Random(seed)
    successes=0
    for _ in range(reps):
        i,j=1,0
        last=0
        while i<a or j<b:
            ra=(a-i)*j;rb=(b-j)*i
            if rng.random()*(ra+rb)<ra:
                i+=1;last=1
            else:
                j+=1;last=0
        successes+=last
    return successes/reps


def main():
    assertions=0
    for a in range(2,10):
        for b in range(2,10):
            x=backward_last_A(a,b)
            y=forward_last_A(a,b)
            assert x==y; assertions+=1
            assert 0<x<1; assertions+=1
    for n in range(2,21):
        assert backward_last_A(n,n)==Fraction(1,2)
        assertions+=1
    # Structural checks on the finite-state intensities.
    for a in range(2,11):
        for b in range(2,11):
            for i in range(1,a+1):
                for j in range(0,b+1):
                    if i==a and j==b:continue
                    ra=(a-i)*j; rb=(b-j)*i
                    assert ra+rb>0; assertions+=1
    print('PASS',assertions,'exact rational/transition assertions')
    # Optional reproducible diagnostic, NOT used as a proof of the limit.
    n=200; lam=1.0
    a=n+math.floor(lam*n/math.log(n))
    estimate=simulate_last_A(a,n,2000,seed=271828)
    print('Finite-n stochastic diagnostic:',a,n,'observed',round(estimate,4),
          'limiting target',round(1/(1+math.exp(-lam)),4))

if __name__=='__main__':
    main()
