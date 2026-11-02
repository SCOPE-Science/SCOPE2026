#!/usr/bin/env python3
"""Exact finite checks for a binary-tree Bernoulli endpoint recursion.
This is finite verification, not a substitute for the infinite analytic proof.
"""
from fractions import Fraction as Q
from itertools import product

checks=0

def check(x):
    global checks
    assert x
    checks+=1

def f(p,y):
    return p*(2*y-y*y)

def atom(p):
    return Q(0) if p<=Q(1,2) else (2*p-1)/p

def f_one(p):
    r=atom(p)
    return p+(1-p)*(2*r-r*r)

def minlaw(law):
    out={}
    for a,pa in law.items():
        for b,pb in law.items():
            v=min(a,b)
            out[v]=out.get(v,Q(0))+pa*pb
    return out

def depth_law(p,h):
    law={Q(0):Q(1)}
    for _ in range(h):
        m=minlaw(law)
        nxt={}
        for x,px in m.items():
            for bit,pb in [(0,1-p),(1,p)]:
                t=1-bit+x/2
                nxt[t]=nxt.get(t,Q(0))+pb*px
        law=nxt
        check(sum(law.values())==1)
        check(all(z>=0 for z in law.values()))
    return law

# Independently enumerate a root-and-two-children tree's 3 Bernoulli labels and compare
# the recursive distribution, without assuming the fixed-point equation.
for p in [Q(1,4),Q(1,2),Q(2,3),Q(3,4)]:
    for h in [1,2,3,4]:
        law=depth_law(p,h)
        check(all(Q(0)<=x<=2-2**(1-h) for x in law))
        check(sum(law.values())==1)
        if h==2:
            brute={}
            for bits in product((0,1),repeat=3):
                b0,b1,b2=bits
                d=1-b0+Q(1,2)*min(1-b1,1-b2)
                prob=p**sum(bits)*(1-p)**(len(bits)-sum(bits))
                brute[d]=brute.get(d,Q(0))+prob
            check(law==brute)
    r=atom(p)
    check(f(p,r)==r)
    check(Q(0)<=r<=p)
    base=f_one(p)
    check(Q(0)<base<=1)
    if p<Q(1,2):check(r==0)
    elif p>Q(1,2):check(r>0)
    for n in range(8):
        check(Q(0)<=base<=1)
        check(base>=r)
        base=f(p,base)
    if p==Q(1,2):
        y=float(f_one(p))
        for n in range(1,1001):
            y=float(p)*(2*y-y*y)
            if n in (500,1000):
                check(abs(float(n*y)-2)<0.1)

# Endpoint linearizations, checked with exact rationals for all tested p.
for p in [Q(1,10),Q(1,4),Q(2,5),Q(3,5),Q(3,4),Q(9,10)]:
    a=2*p
    r=atom(p)
    b=2*(1-p) if p>Q(1,2) else a
    y=f_one(p)
    for n in range(8):
        nxt=f(p,y)
        if p<Q(1,2):
            check(nxt==a*y*(1-y/2))
            check(nxt<=a*y)
        else:
            z=y-r
            check(nxt-r==b*z-p*z*z)
            check(nxt-r<=b*z)
        y=nxt

print('VERIFY_OK',checks)
