#!/usr/bin/env python3
"""Finite exact checks for the degree-one random circle-map level-set calculation."""
from fractions import Fraction
from itertools import product
from collections import Counter
from math import exp, log

def lift(s,x):
    assert 0 <= x < 1
    if s == '+':
        return 3*x if x < Fraction(2,3) else 4-3*x
    return -3*x if x < Fraction(1,3) else 3*x-2

def win(s,d):
    return (0,1,1)[d] if s=='+' else (-1,-1,0)[d]

def inv(s,d,u):
    if s=='+':
        return (u/3,(1+u)/3,(3-u)/3)[d]
    return ((1-u)/3,(1+u)/3,(2+u)/3)[d]

counts={'branches':0,'telescopes':0,'polynomials':0,'pressure':0}
for s in '+-':
    for d in range(3):
        for q in range(1,29):
            u=Fraction(q,29)
            x=inv(s,d,u)
            y=lift(s,x)
            assert y==win(s,d)+u, (s,d,u,x,y)
            assert d==int(3*x)
            counts['branches']+=1
for n in range(1,7):
    for ss in product('+-',repeat=n):
        for ds in product(range(3),repeat=n):
            x=Fraction(7,19)
            for s,d in reversed(list(zip(ss,ds))):
                x=inv(s,d,x)
            y=x
            total=0
            for s,d in zip(ss,ds):
                assert int(3*y)==d
                z=lift(s,y)
                total+=win(s,d)
                y=z-win(s,d)
            assert -1<y-x<1
            assert total+ y-x == sum(win(s,d) for s,d in zip(ss,ds))+y-x
            counts['telescopes']+=1
for ss in product('+-',repeat=6):
    poly=Counter({0:1})
    for s in ss:
        nxt=Counter()
        for k,v in poly.items():
            for d in range(3): nxt[k+win(s,d)]+=v
        poly=nxt
    assert sum(poly.values())==3**6
    assert poly==Counter(sum(win(s,d) for s,d in zip(ss,ds)) for ds in product(range(3),repeat=6))
    counts['polynomials']+=1
for p in [0.0,.15,.4,.7,1.0]:
    for t in [-6,-1.4,0,0.9,6]:
        ep=exp(t); em=exp(-t)
        c=p*2*ep/(1+2*ep)-(1-p)*2*em/(1+2*em)
        P=p*log(1+2*ep)+(1-p)*log(1+2*em)
        h=P-t*c
        assert -1e-10<=h<=log(3)+1e-10
        assert p-1-1e-10<=c<=p+1e-10
        if t==0: assert abs(c-(4*p-2)/3)<1e-12
        counts['pressure']+=1
print('FINITE_IDENTITIES_OK',counts)
