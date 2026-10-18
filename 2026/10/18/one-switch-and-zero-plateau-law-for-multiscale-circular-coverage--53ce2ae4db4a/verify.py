#!/usr/bin/env python3
"""Exact and simulation checks for the two-scale uniform circular gap theorem."""
from fractions import Fraction as F
from itertools import product
from math import comb, exp, log, sqrt
import random

COUNT = 0

def check(condition, message):
    global COUNT
    COUNT += 1
    if not condition:
        raise AssertionError(message)

def joint_cov(n,a,b):
    assert 0 < a <= b < 1
    aa = (1-a)**(n-1)
    bb = (1-b)**(n-1)
    cc = max(0,1-a-b)**(n-1)
    return n*(bb+(n-1)*cc-n*aa*bb)

def discrete_cov(n,q,a,b):
    # Independently count positive integer compositions of q into n parts,
    # conditioned on a uniform interior lattice-grid spacing vector.
    assert 0<a<=b<1
    cut_a,cut_b = (a*q).numerator//(a*q).denominator,(b*q).numerator//(b*q).denominator
    denom=comb(q-1,n-1)
    def ways(extra):
        return comb(q-extra-1,n-1) if q-extra-1>=n-1 else 0
    pa=F(ways(cut_a),denom)
    pb=F(ways(cut_b),denom)
    pab=F(ways(cut_a+cut_b),denom)
    return n*(pb+(n-1)*pab-n*pa*pb)

def classify(n,a,b):
    # Comparison avoids any numerical n-th root.
    A=(1-a)**(n-1)
    t=(1-a-b)/(1-b)
    return 1-n*A+(n-1)*max(F(0),t)**(n-1)

# Exhaustive rational sign identity at dense grids, exact arithmetic.
for n in range(3,12):
    for den in (9,16,23):
        for ia in range(1,den):
            a=F(ia,den)
            for ib in range(ia,den):
                b=F(ib,den)
                c=joint_cov(n,a,b)
                q=classify(n,a,b)
                check((c>0)-(c<0)==(q>0)-(q<0),(n,a,b,c,q))
                check(c==n*(1-b)**(n-1)*q,(n,a,b,'factorization'))

# Lattice composition statistics approximate the continuous simplex law.
for n in range(3,7):
    for a,b in [(F(1,10),F(3,10)),(F(1,5),F(2,5)),(F(1,3),F(2,3))]:
        c=joint_cov(n,a,b)
        err=abs(float(discrete_cov(n,2000,a,b))-float(c))
        check(err<0.05,(n,a,b,err))

# Exact critical mean-one and plateau, using polynomial form: a=1-n^{-1/(n-1)}.
for n in range(3,300):
    a=1-n**(-1/(n-1))
    b=(1-a+1)/2
    c=float(joint_cov(n,a,b))
    check(abs(c)<1e-10,(n,a,b,c))

# True positive/negative phases for several a below alpha, root b* solved
# by bisection on a monotone function (sign, not a claim of exact root value).
for n in (3,4,5,10,25,100):
    alpha=1-n**(-1/(n-1))
    for a in (alpha/6,alpha/2,alpha*0.95):
        t=(n*(1-a)**(n-1)-1)/(n-1)
        c=t**(1/(n-1))
        star=1-a/(1-c)
        check(a<star<1-a,(n,a,star,'root location'))
        check(float(joint_cov(n,a,(a+star)/2))>0,(n,a,'left'))
        check(float(joint_cov(n,a,(star+1-a)/2))<0,(n,a,'right'))
        check(float(joint_cov(n,a,(1-a+1)/2))<0,(n,a,'high'))

# Asymptotic scaling of normalized covariance, and crossing line.
for x,y in [(0.2,0.4),(0.8,1.1),(1.1,2.5),(3.0,7.0)]:
    limit=exp(-y)-(1+x*y)*exp(-x-y)
    for n in (1000,10000):
        got=float(joint_cov(n,x/n,y/n))/n
        check(abs(got-limit)<0.06,(x,y,n,got,limit))
    star=(exp(x)-1)/x
    for n in (1000,10000):
        a=x/n
        v=(n*(1-a)**(n-1)-1)/(n-1)
        b=1-a/(1-v**(1/(n-1)))
        check(abs(n*b-star)<0.4,(x,n,n*b,star))

# Simulated Dirichlet spacings: independent exponential normalization.
rng=random.Random(33211)
for n,a,b in [(3,0.15,0.40),(3,0.35,0.60),(5,0.10,0.35),(6,0.25,0.5)]:
    number=30000
    prod=ta=tb=0.0
    for it in range(number):
        vals=[rng.expovariate(1) for _ in range(n)]
        s=sum(vals)
        ca=sum(1 for x in vals if x>a*s)
        cb=sum(1 for x in vals if x>b*s)
        prod+=ca*cb
        ta+=ca
        tb+=cb
    empirical=prod/number-(ta/number)*(tb/number)
    expected=float(joint_cov(n,F(str(a)),F(str(b))))
    check(abs(empirical-expected)<0.045,(n,a,b,empirical,expected))

print('PASS',COUNT,'exact, lattice-limit, asymptotic and simulation assertions')
