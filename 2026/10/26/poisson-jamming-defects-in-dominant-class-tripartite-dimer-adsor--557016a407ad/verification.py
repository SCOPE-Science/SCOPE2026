#!/usr/bin/env python3
"""Finite-state checks for minority-minority dimer counts in tripartite sequential adsorption."""
import math
import random
from collections import Counter
from functools import lru_cache
from fractions import Fraction

@lru_cache(None)
def exact_law(a,b,c):
    if b+c==0: return (Fraction(1),)
    z=a*b+a*c+b*c
    if z==0: raise ValueError('non-absorbing minority state')
    entries=[(a*b, (a-1,b-1,c),0), (a*c,(a-1,b,c-1),0), (b*c,(a,b-1,c-1),1)]
    law={}
    for w, nxt, shift in entries:
        if not w: continue
        for j,p in enumerate(exact_law(*nxt)):
            law[j+shift]=law.get(j+shift,Fraction(0))+Fraction(w,z)*p
    return tuple(law.get(j,Fraction(0)) for j in range(max(law)+1))

def sample_law(M,B,C,reps,seed):
    rng=random.Random(seed); out=Counter()
    for _ in range(reps):
        a,b,c=M,B,C
        j=0
        while b+c:
            ab=a*b; ac=a*c; bc=b*c
            r=rng.random()*(ab+ac+bc)
            if r<ab: a-=1;b-=1
            elif r<ab+ac: a-=1;c-=1
            else: b-=1;c-=1;j+=1
        assert a==M-B-C+2*j
        out[j]+=1
    return out

def checks():
    tests=0
    for M in range(2,13):
        for B in range(1,min(M-1,4)+1):
            for C in range(1,min(M-B-1,4)+1):
                p=exact_law(M,B,C)
                assert sum(p)==1
                assert p==exact_law(M,C,B)
                assert len(p)<=min(B,C)+1
                assert all(x>=0 for x in p)
                tests+=1
    for n in (20,40,80,160):
        M=n*n
        reps=7000 if n<=80 else 4000
        law=sample_law(M,n,n,reps,271828+n)
        empirical=sum(j*v for j,v in law.items())/reps
        expected=0.5
        stderr=(expected/reps)**.5
        print('n',n,'reps',reps,'mean',round(empirical,5),'target',expected,'P(J=0)',round(law[0]/reps,5),'Poisson',round(math.exp(-expected),5))
        assert abs(empirical-expected)<max(0.25,8*stderr)
    print('PASS',tests,'exact laws, 4 distribution samples and terminal identities')
if __name__=='__main__': checks()
