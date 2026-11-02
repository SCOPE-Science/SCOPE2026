#!/usr/bin/env python3
"""Exact rational checker for 2-point Euclidean distance moments on parallelograms.

No external dependencies. Independent route integrates polynomials in the four
original independent uniform coordinates, without using the triangular law.
"""
from fractions import Fraction as Q
from itertools import product
from collections import defaultdict

ZERO=(0,0,0,0)
ONE={ZERO:Q(1)}

def add(*polynomials):
    z=defaultdict(Q)
    for p in polynomials:
        for k,v in p.items(): z[k]+=v
    return {k:v for k,v in z.items() if v}

def scale(p,a):
    return {k:a*v for k,v in p.items() if a*v}

def mul(p,q):
    z=defaultdict(Q)
    for k,v in p.items():
        for j,w in q.items(): z[tuple(x+y for x,y in zip(k,j))]+=v*w
    return {k:v for k,v in z.items() if v}

def mean(p):
    return sum((v/Q((k[0]+1)*(k[1]+1)*(k[2]+1)*(k[3]+1)) for k,v in p.items()),Q(0))

xx=add({(1,0,0,0):Q(1)},{(0,1,0,0):Q(-1)})
yy=add({(0,0,1,0):Q(1)},{(0,0,0,1):Q(-1)})

def direct_moments(A,B,C):
    P=add(scale(mul(xx,xx),A),scale(mul(yy,yy),B),scale(mul(xx,yy),C))
    w=ONE
    out=[]
    for j in range(1,4):
        w=mul(w,P)
        out.append(mean(w))
    return tuple(out)

def formula_moments(A,B,C):
    s=A+B;p=A*B;q=C*C
    return (s/6,s*s/15-Q(7,90)*p+q/36,s*s*s/28-Q(31,420)*s*p+s*q/30)

def inverse(m1,m2,m3):
    s=6*m1
    U=m2-s*s/15
    V=m3/s-s*s/28
    p=(-2520*U+2100*V)/41
    q=(-5580*U+5880*V)/41
    return s,p,q

def admissible(s,p,q):
    return s>0 and 0<p<=s*s/4 and 0<=q<4*p

checks=0
for A,B,C in product([Q(1,3),Q(2,3),Q(1),Q(3,2),Q(2),Q(3)], [Q(1,2),Q(1),Q(2)], [Q(0),Q(1,3),Q(1),Q(2)]):
    if C*C>=4*A*B: continue
    direct=direct_moments(A,B,C)
    predicted=formula_moments(A,B,C)
    assert direct==predicted,(A,B,C,direct,predicted)
    s,p,q=inverse(*direct)
    assert (s,p,q)==(A+B,A*B,C*C),(A,B,C,s,p,q)
    assert admissible(s,p,q)
    checks+=1

# Two visibly noncongruent parallelograms with identical first two moments.
s=Q(2)
p1,q1=Q(3,4),Q(1)
p2,q2=Q(21,25),Q(313,250)
# A,B pairs (3/2,1/2) and (7/5,3/5); C is sqrt(q).
def via_invariants(s,p,q):
    return (s/6,s*s/15-Q(7,90)*p+q/36,s*s*s/28-Q(31,420)*s*p+s*q/30)
mA=via_invariants(s,p1,q1); mB=via_invariants(s,p2,q2)
assert mA[:2]==mB[:2]==(Q(1,3),Q(17,72))
assert mA[2]!=mB[2]
assert inverse(*mA)==(s,p1,q1)
assert inverse(*mB)==(s,p2,q2)
assert admissible(s,p1,q1) and admissible(s,p2,q2)
assert p1-q1/4 != p2-q2/4
print('PASS: direct 4-variable exact integration, formulas, and inversion for',checks,'valid rational Gram triples')
print('PASS: sharp two-moment counterexample has common (m1,m2)=',mA[:2], 'and distinct third moments',mA[2],mB[2])
print('PASS: both sample moment triples are admissible; squared areas',p1-q1/4,p2-q2/4)
