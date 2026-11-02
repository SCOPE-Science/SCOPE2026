#!/usr/bin/env python3
"""Geometric smoothness of the characteristic-seven witness by exact Groebner basis."""
from sympy import groebner,symbols
x,y,z=symbols('x y z')
fx=2*x*y+z*z
fy=x*x+4*y*z
fz=2*x*z+2*y*y
for a,b,c in ((1,0,0),(0,1,0),(0,0,1)):
    G=groebner([fx,fy,fz,a*x+b*y+c*z-1],x,y,z, modulus=7)
    print('chart',a,b,c,'basis',[str(t) for t in G.polys])
    assert len(G.polys)==1 and G.polys[0].is_one
print('GEOMETRIC_SMOOTHNESS_OK')
