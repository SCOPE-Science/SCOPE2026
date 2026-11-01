#!/usr/bin/env python3
"""Exact algebraic sanity checks for the cyclic Euler Lotka–Volterra map.

These finite checks complement, but cannot replace, the quantified proof.
Run: python CHECK.py (requires sympy).
"""
from fractions import Fraction
import sympy as sp

x, y, z, R, a = sp.symbols('x y z R a', real=True)
b = 2-a
s = x+y+z
k = R*(1-a)
original = (
    x+R*x*(1-x-a*y-b*z),
    y+R*y*(1-b*x-y-a*z),
    z+R*z*(1-a*x-b*y-z),
)
reduced = (
    x*(1+R*(1-s)+k*(y-z)),
    y*(1+R*(1-s)+k*(z-x)),
    z*(1+R*(1-s)+k*(x-y)),
)
assert all(sp.expand(u-v)==0 for u,v in zip(original,reduced))
assert sp.expand(sum(original)-s-R*s*(1-s))==0
prod = sp.prod(original)
prod_formula = x*y*z*sp.prod((1+R*(1-s)+k*d for d in (y-z,z-x,x-y)))
assert sp.expand(prod-prod_formula)==0
# For alpha=1 and the face relation z=1-x-y, every coordinate is fixed.
assert all(sp.expand(u.subs({a:1,z:1-x-y})-v.subs({z:1-x-y}))==0 for u,v in zip(original,(x,y,z)))

Q=Fraction
cases=0
for r in (Q(1,7),Q(1,2),Q(1,1)):
    for alpha in (Q(1,4),Q(1,2),Q(3,4),Q(5,4),Q(3,2),Q(7,4)):
        kap=r*(1-alpha)
        assert abs(kap)<1
        for X,Y,Z in ((Q(1,9),Q(1,6),Q(1,8)),
                      (Q(1,4),Q(1,6),Q(1,12)),
                      (Q(1,3),Q(1,3),Q(1,3)),
                      (Q(1,5),Q(1,5),Q(2,5))):
            S=X+Y+Z
            after=tuple(v*(1+r*(1-S)+kap*d) for v,d in
                        ((X,Y-Z),(Y,Z-X),(Z,X-Y)))
            assert all(v>0 for v in after)
            assert sum(after)==S+r*S*(1-S)
            assert sum(after)<=1
            before_product=(X*Y*Z)/(S*S*S)
            next_product=(after[0]*after[1]*after[2])/sum(after)**3
            if X==Y==Z:
                assert next_product==before_product
            else:
                assert next_product<before_product
            cases+=1
edge_checks=0
for r in (Q(1,7),Q(1,2),Q(1)):
    for alpha in (Q(1,4),Q(1,2),Q(3,4),Q(5,4),Q(7,4)):
        kap=r*(1-alpha)
        for X in (Q(1,20),Q(1,3),Q(3,4),Q(19,20)):
            next_x=X+kap*X*(1-X)
            assert (next_x-X)*kap>0
            edge_checks+=1
print('PASS: all symbolic map identities, 72 rational product steps,',
      edge_checks, 'edge drift cases, and the neutral-face identity.')
assert cases==72 and edge_checks==60
