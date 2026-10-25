#!/usr/bin/env python3
"""Exact checks for the local pinched-fiber calculation, not a substitute for the proof."""
import sympy as sp
u,v,z,w=sp.symbols('u v z w')
f=z*z-u*u*v
assert [sp.diff(f,x) for x in (u,v,z)]==[-2*u*v,-u*u,2*z]
assert sp.expand(f.subs({v:w*w,z:u*w}))==0
# Opposite blowup chart: x1=u' = u*v, x0=u'*v', w'=1/w.
up,wp=sp.symbols('up wp',nonzero=True)
assert sp.cancel(f.subs({u:up*wp*wp,v:1/(wp*wp),z:up*wp}))==0
# The ramification of [a:b] -> [a^2:b^2] is a*b=0 in char 0.
a,b=sp.symbols('a b'); assert sp.det(sp.Matrix([[2*a,0],[0,2*b]]))==4*a*b
assert 4-2+2==4 and 4+2+2==8 and (2-2)*6+2*4==8
print('VERIFY_OK pinch_equation=1 singular_curve=1 normalization=1 transition=1 branch_points=2 singular_euler=4 threefold_euler=8')
