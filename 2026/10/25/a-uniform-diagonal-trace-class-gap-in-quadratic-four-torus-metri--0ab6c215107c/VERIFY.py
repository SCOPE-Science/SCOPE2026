#!/usr/bin/env python3
"""Finite exact checks of the four-torus energy formula; standard library only."""
import itertools
from fractions import Fraction
u=(1,1,-1,-1)
def f(x):
    h=1
    for z in x[1:]: h*=u[z]
    return (h*u[x[0]],h*u[(x[0]+1)%4])
def dist_sq(a,b): return (abs(a[0]-b[0])+abs(a[1]-b[1]))**2
for n in (2,3,4):
    xs=list(itertools.product(range(4),repeat=n))
    es=list(itertools.product((-1,0,1),repeat=n))
    long=Fraction(sum(dist_sq(f(x),f(tuple((x[i]+(2 if i==j else 0))%4 for i in range(n)))) for x in xs for j in range(n)),len(xs))
    short=Fraction(sum(dist_sq(f(x),f(tuple((x[i]+e[i])%4 for i in range(n)))) for x in xs for e in es),len(xs)*len(es))
    assert long==16*n,(n,long)
    assert short==Fraction(16,3)-Fraction(8,3**n),(n,short)
    assert long/short==Fraction(6*n,1)/(2-Fraction(3,3**n)),(n,long/short)
    betas=(Fraction(1),Fraction(1,3),Fraction(-1,3),Fraction(1,3))
    vals=[]
    for k in xs:
        r=sum(z%2 for z in k)
        v=Fraction(1)
        for z in k: v*=betas[z]
        if v !=1: vals.append(Fraction(2*r,1)/(1-v))
    assert max(vals)==Fraction(2*n,1)/(1-Fraction(1,3**n))
    print('n=',n,'long=',long,'short=',short,'trace quotient=',long/short,'Hilbert=',max(vals))
print('PASS: finite checks supplement the all-dimensional proof')
