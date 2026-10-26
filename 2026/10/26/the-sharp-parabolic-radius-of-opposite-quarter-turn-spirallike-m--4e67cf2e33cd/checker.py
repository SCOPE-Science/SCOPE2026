#!/usr/bin/env python3
"""Exact rational checks for a quarter-angle strong-starlikeness inclusion."""
from fractions import Fraction as Q
# Polynomial coefficients in k=v^2, indexed by degree.
def mul(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c
def add(a,b):
    return [(a[i] if i<len(a) else Q(0))+(b[i] if i<len(b) else Q(0)) for i in range(max(len(a),len(b)))]
def scale(a,s): return [s*x for x in a]
r=Q(3,5)
a=(1+r*r)/(1-r*r); R=2*r/(1-r*r)
assert (a,R,a-R,a+R)==(Q(17,8),Q(15,8),Q(1,4),Q(4))
u=[Q(1,2),Q(1,2)]
k=[Q(0),Q(1)]
u2=mul(u,u)
C=add(add(scale(mul(add(u2,k),add(u2,k)),Q(4)),scale(add(u2,scale(k,Q(-1))),Q(-17))),[Q(4)])
assert C==[Q(0),Q(46,4),Q(21,4),Q(12,4),Q(1,4)],C
assert Q(1,2)**2==a-R
assert (1-r)/(1+r)==Q(1,4)
# q(-r)=sqrt(p(-r))=1/2; q(-s)<1/2 for every s in (3/5,1).
print('VERIFY_OK: exact polynomial, disk, and extremal contact checked')
