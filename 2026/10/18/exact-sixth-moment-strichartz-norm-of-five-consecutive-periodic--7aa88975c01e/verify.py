#!/usr/bin/env python3
"""Self-contained exact checks for the five-mode periodic Schrödinger sixth-moment theorem.

The finite polynomial checks and rational root isolation supplement the analytic proof.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations_with_replacement
from math import comb
import random

TRIPLES = list(combinations_with_replacement(range(5), 3))
groups = defaultdict(list)
for t in TRIPLES:
    groups[(sum(t), sum(x*x for x in t))].append(t)
assert len(TRIPLES) == 35 and len(groups) == 34
assert {k: ts for k, ts in groups.items() if len(ts)>1} == {
    (6,18): [(0,3,3),(1,1,4)]
}

# Independently reconstruct the moment from coefficient collision classes.
seed=random.Random(20261014)
for trial in range(100):
    coef=[complex(seed.randint(-3,3),seed.randint(-3,3)) for _ in range(5)]
    u=[int(z.real*z.real+z.imag*z.imag) for z in coef]
    denom=sum(u)
    if not denom: continue
    byfiber=defaultdict(complex)
    for t in TRIPLES:
        w=1 if t[0]==t[2] else (3 if t[0]==t[1] or t[1]==t[2] else 6)
        z=complex(w,0)
        for i in t:z*=coef[i]
        byfiber[(sum(t),sum(k*k for k in t))]+=z
    exact_direct=sum(int(z.real*z.real+z.imag*z.imag) for z in byfiber.values())
    cross=18*(coef[0]*coef[3]**2*(coef[1].conjugate()**2)*coef[4].conjugate()).real
    direct_identity=6*denom**3-9*denom*sum(x*x for x in u)+4*sum(x**3 for x in u)+cross
    assert exact_direct == direct_identity, (trial,exact_direct,direct_identity)

# Polynomial lists in b, coefficients in ascending degree.
def add(x,y):
    z=[Q(0)]*max(len(x),len(y))
    for i,v in enumerate(x):z[i]+=v
    for i,v in enumerate(y):z[i]+=v
    return z

def mul(x,y):
    z=[Q(0)]*(len(x)+len(y)-1)
    for i,a in enumerate(x):
        for j,b in enumerate(y):z[i+j]+=a*b
    return z

def scale(x,k):return [k*v for v in x]

def ev(p,x):
    s=Q(0)
    for u in p[::-1]:s=s*x+u
    return s

# a=A/D at interior critical point. f(a,b)=12a²+32ab+2a+13b²-4b-2.
A=[Q(1),Q(11),Q(-8)]
D=[Q(10),Q(25)]
q=add(add(scale(mul(A,A),12),scale(mul(mul(A,[0,1]),D),32)),
      add(scale(mul(A,D),2),mul([Q(-2),Q(-4),Q(13)],mul(D,D))))
assert q == scale([Q(-56),Q(-182),Q(1340),Q(2576),Q(831)], Q(3)) , q
# Check linear combination 8*f-12*g = 4[(25b+10)a+(8b²-11b-1)].
# Check derivative values at simple rationals directly (independent of symbolic package).
def F(a,b):
    c=1-2*a-2*b
    return 6-9*(2*a*a+2*b*b+c*c)+4*(2*a*a*a+2*b*b*b+c*c*c)+18*a*b*b

def fa(a,b):return -6*(12*a*a+32*a*b+2*a+13*b*b-4*b-2)
def fb(a,b):return -12*(8*a*a+13*a*b-2*a+6*b*b+b-1)
for a,b in [(Q(0),Q(0)),(Q(1,5),Q(1,5)),(Q(1,4),Q(1,8))]:
    h=Q(1,10**7)
    assert (F(a+h,b)-F(a-h,b))/(2*h)-fa(a,b) == -24*h*h
    assert (F(a,b+h)-F(a,b-h))/(2*h)-fb(a,b) == -24*h*h
assert F(Q(1,5),Q(1,5)) == Q(563,125) > Q(9,2)
assert F(Q(0),Q(1,3)) == Q(31,9)
assert 97**3 < 989**2  # edge maximum (97 sqrt(97)-260)/162 < 9/2.

# Descartes: q(b) has coefficients with exactly one sign change descending.
poly=[-56,-182,1340,2576,831]
assert sum(x*y<0 for x,y in zip(poly,poly[1:])) == 1
low=Q(222193,10**6); high=Q(222194,10**6)
assert ev(poly,low)<0<ev(poly,high)
for j in range(180):
    mid=(low+high)/2
    if ev(poly,mid)<0:low=mid
    else:high=mid
b=(low+high)/2
a=(1+11*b-8*b*b)/(10+25*b)
c=1-2*a-2*b
assert 0<a and 0<b and 0<c
assert Q(196026,10**6)<a<Q(196028,10**6)
assert Q(163558,10**6)<c<Q(163560,10**6)
assert Q(4518619,10**6)<F(a,b)<Q(4518621,10**6)
print('PASS: 35 triple types with one (6,18) collision; exact cubic, elimination and rational root isolation')
print('a=',float(a),'b=',float(b),'c=',float(c))
print('sixth-moment optimum=',float(F(a,b)))
print('norm optimum=',float(F(a,b))**(1/6))
