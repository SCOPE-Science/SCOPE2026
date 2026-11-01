#!/usr/bin/env python3
"""Finite, reproducible diagnostics for the 24-cell Haar directional-width theorem.

Exact assertions test the vertex Gram incidence. Numerical quadrature and a
seeded spherical Monte Carlo independently check the stated probability law.
Neither finite test substitutes for the geometric proof.
"""
import itertools
import math
import random
from collections import Counter
from fractions import Fraction


def vertices():
    vec = []
    for i in range(4):
        for sign in (-1, 1):
            a = [Fraction(0)] * 4
            a[i] = Fraction(sign)
            vec.append(tuple(a))
    vec.extend(tuple(Fraction(sign, 2) for sign in signs)
               for signs in itertools.product((-1, 1), repeat=4))
    return vec


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def single_cap(s):
    if s >= 1.0:
        return 0.0
    return (math.acos(s)-s*math.sqrt(1.0-s*s)) / math.pi


def pair_cap(s):
    s0 = math.sqrt(3.0)/2
    if s >= s0:
        return 0.0
    y = s0*math.sqrt(1.0-s*s)-s/2.0
    return (math.asin(y)-(s/s0)*y)/math.pi


def tail_24(s):
    assert math.sqrt(2.0/3.0) <= s <= 1
    return 24*single_cap(s)-96*pair_cap(s)


def simpson(f, a, b, steps=1000):
    assert steps % 2 == 0
    h=(b-a)/steps
    return h/3.0*(f(a)+f(b)+sum((4 if j%2 else 2)*f(a+h*j) for j in range(1,steps)))


def diagnostics():
    V=vertices()
    assert len(V)==24 and len(set(V))==24
    for v in V:
        assert dot(v, v)==1
        assert tuple(-x for x in v) in V
    pairs=Counter(dot(V[i],V[j]) for i in range(24) for j in range(i+1,24))
    assert pairs=={Fraction(-1):12, Fraction(-1,2):96, Fraction(0):72, Fraction(1,2):96},pairs
    assert all(sum(dot(v,w)==Fraction(1,2) for w in V)==8 for v in V)
    good_triples=0
    for a,b,c in itertools.combinations(V,3):
        sims=(dot(a,b),dot(a,c),dot(b,c))
        if all(q>0 for q in sims):
            assert sims==(Fraction(1,2),)*3
            good_triples+=1
    assert good_triples==96
    s0=math.sqrt(3)/2
    s1=math.sqrt(2/3)
    # A single pair's cap intersection is a Euclidean disk segment because
    # the first two coordinates of a Haar point on S^3 are uniform on B^2.
    for s in [s1, .83, .84, .85, .86, s0-.001]:
        y=s0*math.sqrt(1-s*s)-s/2
        area=2/math.pi*simpson(lambda z: math.sqrt(1-z*z)-(s+z/2)/s0,0,y)
        assert abs(area-pair_cap(s))<5e-13,(s,area,pair_cap(s))
    assert abs(pair_cap(0.0)-1/3)<1e-14
    for ds in [.02,.01,.005,.002,.001]:
        ratio=pair_cap(s0-ds)/ds**2
        assert abs(ratio-4/(math.pi*math.sqrt(3)))<.12,(ds,ratio)
    assert tail_24(s1)>0.93 and tail_24(s1)<0.94
    assert abs(tail_24(1.0))<1e-14
    assert abs(tail_24(s0)-24*single_cap(s0))<1e-14
    # Monte Carlo directly uses all 24 vertex dot products, not cap overlaps.
    rng=random.Random(20261027)
    S=[s1,.82,.83,.84,.85,s0,.9,.94,.97]
    tally=[0]*len(S)
    N=180000
    F=[[float(x) for x in v] for v in V]
    for _ in range(N):
        X=[rng.gauss(0,1) for _ in range(4)]
        X=[x/math.sqrt(sum(z*z for z in X)) for x in X]
        R=max(sum(X[j]*v[j] for j in range(4)) for v in F)
        for j,s in enumerate(S):
            if R>=s:
                tally[j]+=1
    for s,k in zip(S,tally):
        p=tail_24(s)
        obs=k/N
        assert abs(obs-p)<.007,(s,p,obs)
    print('VERIFY_OK 24-cell width: exact Gram profile, two-cap quadrature, first-transition asymptotics, seeded Haar test')
    print('closest-pair count:',pairs[Fraction(1,2)],'positive-pair triples:',good_triples)
    print('exact upper-regime mass at the threshold:',format(tail_24(s1),'.12f'))

if __name__=='__main__':
    diagnostics()
