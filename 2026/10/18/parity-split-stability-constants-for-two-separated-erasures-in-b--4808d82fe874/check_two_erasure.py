#!/usr/bin/env python3
"""Reproducible finite-section and scalar asymptotic consistency checks.
Run with: python3 check_two_erasure.py
These tests do not replace the infinite-dimensional proofs in RESULT.md.
"""
from fractions import Fraction
from math import pi, sin, log

def F(h,t):
    return pi/sin(pi*t) -1/t -((-1)**h)/(t-h) -2*sum(((-1)**j)/(t-j) for j in range(1,h))

def eta_odd(q,n=300):
    # Pair alternating series to improve the convergence rate.
    return sum(1/(2*j-1)**q - 1/(2*j)**q for j in range(1,n+1))

def B(t):
    out=2*log(2)
    for j in range(1,18):
        out+=2*eta_odd(2*j+1)*t**(2*j)
    return out

def I(p):
    # Composite Simpson integration with no external dependencies.
    n=4096
    dt=1/n
    def integrand(x):
        if x==0: return 0.0 if p>1 else 1.0
        return x**(p-1)*(1-x)/(1+x)
    out=integrand(0)+integrand(1)
    for j in range(1,n):
        out+=(4 if j%2 else 2)*integrand(j*dt)
    return out*dt/3

def golden_min(fn,left,right):
    r=(5**0.5-1)/2
    a,b=left,right
    c=b-r*(b-a);d=a+r*(b-a)
    fc,fd=fn(c),fn(d)
    for _ in range(140):
        if fc<fd:
            b,d,fd=d,c,fc
            c=b-r*(b-a);fc=fn(c)
        else:
            a,c,fc=c,d,fd
            d=a+r*(b-a);fd=fn(d)
    t=(a+b)/2
    return t,fn(t)

def min_gap(h):
    return golden_min(lambda t:-F(h,t),-.5,.5)

def lambda_at(N,m,h,t):
    u=m+t; num=0.0;den=0.0; rank=0
    for j in range(N+1):
        if j in (m,m+h):continue
        v=1/(u-j)
        num+=abs(v);den+=(-1 if rank%2 else 1)*v
        rank+=1
    return num/abs(den)

nchecks=0
# All sign reindexings are verified by exact rational arithmetic.
for h in range(2,10):
    for m in range(3,9):
        N=m+h+6
        for t in (Fraction(1,7),Fraction(2,7),Fraction(-2,7)):
            actual=Fraction(0);rank=0
            baseline=Fraction(0);corrections=Fraction(0)
            for j in range(N+1):
                v=1/(Fraction(m)+t-j)
                baseline+=(-1)**j*v
                if j==m or j==m+h:continue
                actual+=(-1)**rank*v;rank+=1
            for j in range(m+1,m+h):
                corrections+=(-2)*(-1)**j/(Fraction(m)+t-j)
            modified=baseline-(-1)**m/(t)-(-1)**(m+h)/(t-h)+corrections
            assert actual==modified
            nchecks+=1

prev={}
for h in range(2,16):
    t,mh=min_gap(h)
    assert abs((-F(h,t))-(B(t)+((-1)**h)*I(h-t)))<8e-5
    assert 0<mh<1.6
    assert t<0 if h%2==0 else t>0
    assert mh>2*log(2) if h%2==0 else mh<2*log(2)
    if h>=4:
        assert mh<prev[h-2] if h%2==0 else mh>prev[h-2]
    prev[h]=mh
    nchecks+=5
    if h<=5:
        for N in (160,640,2560):
            val=lambda_at(N,N//3,h,t)
            assert abs(val-2*log(N)/mh)<3.5
            nchecks+=1

for h in range(12,30):
    t,mh=min_gap(h)
    predicted=1/log(2)-(-1)**h/(4*log(2)**2*h*h)
    assert abs(2/mh-predicted)<4/h**3
    nchecks+=1
print('PASS:',nchecks,'exact-rational and numerical assertions')
for h in range(2,8):
    t,mh=min_gap(h)
    print('h=%d, t=%.9f, C=%.9f'%(h,t,2/mh))
