#!/usr/bin/env python3
"""Exact, finite sanity checks for the quantitative quartic-isometry proof."""
from fractions import Fraction as F
from itertools import product

def fourth(z):
    a,b=z
    return (a*a+b*b)**2

def add(z,w): return (z[0]+w[0],z[1]+w[1])
def mult_i(z): return (-z[1],z[0])
def neg(z): return (-z[0],-z[1])

checks=0
S=[(F(a),F(b)) for a,b in product(range(-2,3), repeat=2)]
for u in S:
    for v in S:
        phases=[v,mult_i(v),neg(v),neg(mult_i(v))]
        lhs=sum(fourth(add(u,w)) for w in phases)/4
        rhs=fourth(u)+fourth(v)+4*(u[0]*u[0]+u[1]*u[1])*(v[0]*v[0]+v[1]*v[1])
        assert lhs==rhs
        checks+=1
# An exact two-column, three-row overlap and deletion test.
for a,b,c,d,e,f in product(range(-2,3), repeat=6):
    rows=[(a,b),(c,d),(e,f)]
    pair_overlap=sum(F(x*x*y*y) for x,y in rows)
    deleted=sum(F(min(x**4,y**4)) for x,y in rows)
    assert deleted<=pair_overlap
    checks+=1
    if checks>15000:
        break
print('CHECK_OK',checks)
