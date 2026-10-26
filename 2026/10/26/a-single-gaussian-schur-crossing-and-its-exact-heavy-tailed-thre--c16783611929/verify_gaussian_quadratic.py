#!/usr/bin/env python3
"""Finite reproducibility tests for the Gaussian-quadratic zero-count theorem.

Requires Python 3 only. The mathematical proof is in RESULT.md; these
finite comparisons are checks, not replacements for the proof.
"""
import cmath
import math
import random

def gaussian(rng):
    scale=1.0/math.sqrt(2.0)
    return complex(rng.gauss(0.0,scale),rng.gauss(0.0,scale))

def root_count(a,b,c,s):
    radical=cmath.sqrt((s*b)**2-4*a*c)
    first=(-s*b+radical)/(2*c)
    second=(-s*b-radical)/(2*c)
    return (abs(first)<1.0)+(abs(second)<1.0)

def schur_count(a,b,c,s):
    delta=abs(c)**2-abs(a)**2
    crossed=s*abs(b*c.conjugate()-a*b.conjugate())>abs(delta)
    return 1 if crossed else (2 if delta>0 else 0)

def run():
    rng=random.Random(20261023)
    nsamples=100000
    samples=[(gaussian(rng),gaussian(rng),gaussian(rng)) for _ in range(nsamples)]
    for s in (0.0,0.02,0.2,0.5,1.0,2.0,5.0,12.0):
        counts=[0,0,0]
        for a,b,c in samples:
            n=root_count(a,b,c,s)
            assert n==schur_count(a,b,c,s), (s,a,b,c,n)
            counts[n]+=1
        p=s/math.sqrt(s*s+2.0)
        theoretical=((1-p)/2,p,(1-p)/2)
        empirical=tuple(x/nsamples for x in counts)
        discrepancy=max(abs(x-y) for x,y in zip(empirical,theoretical))
        assert discrepancy<0.014,(s,discrepancy)
        print('s=',s,'empirical=',empirical,'exact=',theoretical,'error=',discrepancy)
    # A single finite coefficient triple has one Schur transition threshold;
    # both the root classification and its direction are checked directly.
    for a,b,c in samples[:5000]:
        d=abs(c)**2-abs(a)**2
        relation=abs(b*c.conjugate()-a*b.conjugate())
        if relation<1e-12:continue
        t=abs(d)/relation
        below=root_count(a,b,c,t*0.5)
        above=root_count(a,b,c,t*2.0)
        assert below==(2 if d>0 else 0)
        assert above==1
    print('All finite classification, transition, and distribution checks passed.')

if __name__=='__main__':run()
