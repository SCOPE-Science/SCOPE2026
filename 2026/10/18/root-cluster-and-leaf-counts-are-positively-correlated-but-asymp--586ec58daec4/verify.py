#!/usr/bin/env python3
"""Exact finite enumeration and analytic recurrence checks for root-cluster–leaf covariance."""
from fractions import Fraction as F
from math import factorial, isclose, gamma
from itertools import product


def exact_enum(n,r):
    den=factorial(n-1)
    av=al=ak=arl=ar2=al2=F(0)
    for parents in product(*[range(v) for v in range(1,n)]):
        children=[0]*n
        for par in parents:children[par]+=1
        leaves={v for v,d in enumerate(children) if d==0}
        l=len(leaves)
        for bits in product((0,1),repeat=n-1):
            weight=r**sum(bits)*(1-r)**(n-1-sum(bits))/den
            root={0}
            for v,par in enumerate(parents,start=1):
                if bits[v-1] and par in root:root.add(v)
            R=len(root)
            K=len(root & leaves)
            av+=weight*R; al+=weight*l; ak+=weight*K
            arl+=weight*R*l; ar2+=weight*R*R; al2+=weight*l*l
    return av,al,ak,arl-av*al,ar2-av*av,al2-al*al


def prodA(n,r):
    out=F(1)
    for j in range(1,n):out*=1+r/F(j)
    return out


def exact_formula(n,r):
    A=prodA(n,r)
    cov=A*r*(1-r)*F(n-2,1)/(2*(1+r)*(n+r-1)) if n>=2 else F(0)
    Rv=2*prodA(n,2*r)-A-A*A
    return A,F(n,2) if n>=2 else F(1),r*A/(1+r) if n>=2 else F(1),cov,Rv,F(n,12) if n>=3 else F(0)

checks=0
for n in range(2,8):
    for r in [F(1,4),F(1,3),F(1,2),F(2,3),F(3,4)]:
        got=exact_enum(n,r)
        want=exact_formula(n,r)
        for i,(g,w) in enumerate(zip(got,want)):
            assert g==w, (n,r,i,g,w)
            checks+=1
        if n>=3:
            assert got[3]>0
            checks+=1
for n in [3,4,5,10,32,128]:
    for r in [F(1,10),F(1,2),F(9,10)]:
        a=exact_formula(n,r)[0]
        c=exact_formula(n,r)[3]
        assert c>=0
        assert c/a== r*(1-r)*(n-2)/(2*(1+r)*(n+r-1))
        checks+=2
for r in [.2,.5,.8]:
    n=100000
    a=gamma(n+r)/(gamma(1+r)*gamma(n)) if False else __import__('math').exp(__import__('math').lgamma(n+r)-__import__('math').lgamma(n)-__import__('math').lgamma(1+r))
    actual=a*r*(1-r)*(n-2)/(2*(1+r)*(n+r-1))
    target=r*(1-r)/(2*(1+r)*gamma(1+r))*n**r
    assert abs(actual/target-1)<0.0001
    checks+=1
print('PASS',checks,'exact/analytic comparisons')
