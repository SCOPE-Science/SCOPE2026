#!/usr/bin/env python3
"""Exact ray-support feasibility checks plus direct sampled character transforms."""
from itertools import product
from fractions import Fraction
from cmath import exp
from math import pi

def allowed(q):
    n=q+1
    x={(1,0,n)}
    for s in range(1,n+1):
        pos=set(range(n+1)) if s==n else ({s}|set(range(n-s+1,n+1)))
        for r in pos:x.add((1,s,r))
        if s<q:zero=set(range(n-s+1,n+1))
        elif s==q:zero={1}|set(range(3,n+1))
        else:zero=set(range(2,n+1))
        for r in zero:x.add((0,s,r))
    return x

def spectrum_from_weights(q,a,b):
    total=sum(b)
    assert a or total
    return (int(a>0),sum(v>0 for v in b),sum(a-total+q*v != 0 for v in b))

def witnesses(q):
    n=q+1
    yield Fraction(1),[Fraction(0)]*n
    for s in range(1,n+1):
        for r in (set(range(n+1)) if s==n else ({s}|set(range(n-s+1,n+1)))):
            b=[Fraction(0)]*n
            if r==s and s<n:
                b[:s]=[Fraction(1)]*s;a=Fraction(s)
            elif r==0 and s==n:
                b[:s]=[Fraction(1)]*s;a=Fraction(1)
            else:
                m=n-r
                b[:m]=[Fraction(1)]*m;b[m:s]=[Fraction(q+1)]*(s-m)
                a=sum(b)-q
            yield a,b
        if s<q:
            possible=set(range(n-s+1,n+1))
        elif s==q:
            possible={1}|set(range(3,n+1))
        else:
            possible=set(range(2,n+1))
        for r in possible:
            m=n-r;b=[Fraction(0)]*n
            if s<q:
                b[:m]=[Fraction(1)]*m;b[m:s]=[Fraction(q-m,s-m)]*(s-m)
            elif s==q:
                if m==q:b[:q]=[Fraction(1)]*q
                else:
                    k=q-m;d=Fraction(1,2*(k-1))
                    b[:m]=[Fraction(1)]*m
                    b[m:q-1]=[1+d]*(k-1)
                    b[q-1]=1-(k-1)*d
            else:
                b[:m]=[Fraction(1)]*m
                b[m:s]=[Fraction(q-m,n-m)]*(n-m)
            yield Fraction(0),b

def test_direct_prime(q):
    # Projective directions represented by (1,t) and (0,1).
    v=[(1,t) for t in range(q)]+[(0,1)]
    a=2.0;b=[float((i%3)+1) for i in range(q+1)]
    def point_index(x,y):
        if x%q:return (y*pow(x,-1,q))%q
        return q
    vals={(x,y):a if x==y==0 else b[point_index(x,y)] for x in range(q) for y in range(q)}
    S=sum(b)
    for i,(u,vv) in enumerate(v):
        actual=sum(vals[x,y]*exp(-2j*pi*((u*x+vv*y)%q)/q) for x in range(q) for y in range(q))
        annihilator=[j for j,(xx,yy) in enumerate(v) if (u*xx+vv*yy)%q==0]
        assert len(annihilator)==1
        expect=a-S+q*b[annihilator[0]]
        assert abs(actual-expect)<1e-8,(q,i,actual,expect)

for q in (2,3,4,5,7):
    found={spectrum_from_weights(q,a,b) for a,b in witnesses(q)}
    assert found==allowed(q),(q,found^allowed(q))
    assert all(spectrum_from_weights(q,a,b) in allowed(q) for a in range(5) for b in product(range(3),repeat=q+1) if a or any(b)) if q<=4 else True
    if q in (2,3,5,7):test_direct_prime(q)
    print('q',q,'all',len(found),'admissible triples realized and formulas checked')
print('PASS')
