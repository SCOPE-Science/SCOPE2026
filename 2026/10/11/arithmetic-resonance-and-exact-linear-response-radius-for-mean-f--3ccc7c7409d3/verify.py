#!/usr/bin/env python3
"""Exact rational Fourier tests for a mean-field linear-response identity.
Run: python verify.py (Python 3, standard library only).
Tests are finite diagnostics, not a proof of the infinite-dimensional result.
"""
from fractions import Fraction as Q
from itertools import permutations
from random import Random

rng=Random(840170)
tests=0

def check(cond, message):
    global tests
    tests+=1
    if not cond:
        raise AssertionError(message)

def plus(a,b):
    r=dict(a)
    for n,x in b.items():r[n]=r.get(n,Q(0))+x
    return {n:x for n,x in r.items() if x}

def scale(a,c):return {n:v*c for n,v in a.items() if v*c}

def P(a,d):return {n//d:v for n,v in a.items() if n%d==0}

def L(a,d,k,b):
    # b=pi*epsilon.  Fourier cosine coefficients, not normalized by 1/2.
    x=P(a,d)
    if k%d==0:
        n=k//d
        x=plus(x,{n:-b*n*a.get(1,Q(0))})
    return x

def iterate(fn,a,t):
    v=a
    for _ in range(t):v=fn(v)
    return v

def det(A):
    n=len(A); v=Q(0)
    for p in permutations(range(n)):
        s=1
        for i in range(n):
            for j in range(i+1,n):
                if p[i]>p[j]:s=-s
        prod=Q(s)
        for i,j in enumerate(p):prod*=A[i][j]
        v+=prod
    return v

# Exact Fourier calculus independently assembles the pushforward's
# first variation and checks the rank-one formula for all tested cases.
for d in range(2,7):
    for k in range(1,115):
        for b in (Q(-3,2),Q(0),Q(2,3)):
            a={i:Q(rng.randint(-3,3),rng.randint(1,4)) for i in range(1,110)}
            a={i:v for i,v in a.items() if v}
            explicit=P(a,d)
            if k%d==0:
                n=k//d
                explicit=plus(explicit,{n:-b*n*a.get(1,Q(0))})
            check(L(a,d,k,b)==explicit,('first-variation',d,k,b))
            # Finite-time exact Duhamel formula (independent calculation).
            for t in (1,2,4,6):
                Lt=iterate(lambda v:L(v,d,k,b),a,t)
                rhs=iterate(lambda v:P(v,d),a,t)
                if k%d==0:
                    g={k//d:-b*(k//d)}
                    for s in range(t):
                        v=iterate(lambda z:L(z,d,k,b),a,t-1-s)
                        rhs=plus(rhs,scale(iterate(lambda z:P(z,d),g,s),v.get(1,Q(0))))
                check(Lt==rhs,('duhamel',d,k,b,t))

# Resonance eigenblock: characteristic polynomial is lambda^j + b*d^(j-1).
for d in range(2,7):
    for j in range(1,6):
        k=d**j
        for b in (Q(-5,3),Q(-1,7),Q(0),Q(2,3),Q(3,2)):
            modes=[d**i for i in range(j)]
            A=[[L({m:Q(1)},d,k,b).get(n,Q(0)) for m in modes] for n in modes]
            for z in (-3,-2,-1,0,1,2,3):
                B=[[Q(z)*(i==h)-A[i][h] for h in range(j)] for i in range(j)]
                check(det(B)==Q(z)**j+b*d**(j-1),('resonance block',d,j,b,z))
            # the moment recursion holds exactly on random cos-polynomials.
            v={i:Q(rng.randint(-4,4),rng.randint(1,7)) for i in range(1,100)}
            for t in range(j,2*j+5):
                lhs=iterate(lambda z:L(z,d,k,b),v,t).get(1,Q(0))
                ordinary=iterate(lambda z:P(z,d),v,t).get(1,Q(0))
                lag=iterate(lambda z:L(z,d,k,b),v,t-j).get(1,Q(0))
                check(lhs==ordinary-b*d**(j-1)*lag,('moment recurrence',d,j,b,t))

# Non-resonance: after finite P-powers the injected mode cannot reach cos(2pi x).
for d in range(2,7):
    for k in range(1,400):
        if k%d:continue
        n=k//d
        if n in (d**j for j in range(0,12)):continue
        for i in range(14):
            check(iterate(lambda z:P(z,d),{n:Q(1)},i).get(1,Q(0))==0,('nonresonance',d,k,i))

print('VERIFY_OK exact_assertions='+str(tests))
