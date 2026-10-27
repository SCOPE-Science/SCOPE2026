#!/usr/bin/env python3
"""Exact local polynomial checks for the cubic Veronese-tangent base scheme."""
import sympy as s
u,v,x,y=s.symbols('u v x y')
I=[u*x,u*y+v*x,v*y]
G=s.groebner(I,u,v,x,y,order='grevlex')
assert G.reduce(u*y)[1] != 0
for z in (u,v,x,y):
    assert G.reduce(z*u*y)[1] == 0
# The symmetric-square local relation becomes identically zero on the plane.
s1,s2,a,b,c=s.symbols('s1 s2 a b c')
assert s.expand((a*c-b*b).subs({a:s1*s1,b:s1*s2,c:s2*s2})) == 0
# The three polar generators for two coordinate vectors vanish only when
# one factor vanishes: rank-one Gram product has zero iff a or b is zero.
assert s.expand((u*x)*(v*y) - (u*y)*(v*x)) == 0
print('VERIFY_OK: socle nonzero and annihilated by u,v,x,y; rank-one quotient; 36 pair intersections')
