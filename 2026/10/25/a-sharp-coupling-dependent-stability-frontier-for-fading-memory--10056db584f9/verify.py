#!/usr/bin/env python3
"""Exact and finite checks for the two-coordinate fading-gradient stability theorem."""
from fractions import Fraction as F
from random import Random
from math import sqrt
import numpy as np
import sympy as sp

def direct_cycle(x, y, p, t, c, g):
    # First refresh coordinate one, then coordinate two; preserve only buffer two.
    fresh1 = x + c * y
    x1, y1 = x - t * fresh1, y - t * g * p
    fresh2 = c * x1 + y1
    return (x1 - t * g * fresh1, y1 - t * fresh2, fresh2)

def matrix(t, c, g):
    return [[1-(1+g)*t, -(1+g)*t*c, 0],
            [-t*c*(1-t), 1-t+t*t*c*c, -t*g*(1-t)],
            [c*(1-t), 1-t*c*c, -t*g]]

def cutoff(c,g):
    return 4/(1+g+sqrt((1+g)**2-8*c*c*g*(1-g)))

t,c,g,z=sp.symbols('t c g z')
M=sp.Matrix(matrix(t,c,g))
P=sp.expand(M.charpoly(z).as_expr())
a1=-c*c*t*t+2*(1+g)*t-2
a2=-2*c*c*g*t*t+(1+g)**2*t*t-2*(1+g)*t+1
a3=-c*c*g*g*t*t
assert sp.expand(P-(z**3+a1*z*z+a2*z+a3))==0
assert sp.expand(1+a1+a2+a3-t*t*(1-c*c)*(1+g)**2)==0
assert sp.expand(1-a1+a2-a3-((2-(1+g)*t)**2+c*c*(1-g)**2*t*t))==0
assert sp.expand(1-a2+a1*a3-a3*a3-t*(1+g)*(1+c*c*g*t)*(2-(1+g)*t+c*c*g*(1-g)*t*t))==0
assert sp.expand(M.det()-c*c*g*g*t*t)==0
print('Five symbolic polynomial and determinant identities passed')
rng=Random(42)
for i in range(500):
    tt=F(rng.randint(1,7),rng.randint(2,9))
    cc=F(rng.randint(-9,9),10)
    gg=F(rng.randint(0,10),10)
    xx=F(rng.randint(-7,7),3)
    yy=F(rng.randint(-7,7),3)
    pp=F(rng.randint(-7,7),3)
    lhs=direct_cycle(xx,yy,pp,tt,cc,gg)
    mm=matrix(tt,cc,gg)
    rhs=tuple(sum(mm[j][k]*v for k,v in enumerate((xx,yy,pp))) for j in range(3))
    assert lhs==rhs,(i,lhs,rhs)
print('500 exact-rational direct-iteration versus monodromy checks passed')
for i in range(750):
    gg=rng.random()
    cc=rng.random()*0.999
    critical=cutoff(cc,gg)
    assert 0<critical<3+1e-12
    for fraction,expected in [(0.73,True),(0.995,True),(1.005,False),(1.33,False)]:
        tt=critical*fraction
        rad=max(abs(np.linalg.eigvals(np.asarray(matrix(tt,cc,gg),dtype=float))))
        assert (rad<1)==expected,(gg,cc,tt,critical,rad,expected)
print('3000 eigenvalue stability checks across the exact frontier passed')
for gg in [0, F(1,3), F(1,2), 1]:
  for cc in [0,F(9,10),F(99,100)]:
    h=cutoff(float(cc),float(gg))
    if gg==0:assert abs(h-2)<1e-13
    if gg==1:assert abs(h-1)<1e-13
    if cc==0:assert abs(h-2/(1+float(gg)))<1e-13
assert cutoff(.95,1/3)>2
assert cutoff(.999999,1/3)<3
assert cutoff(.999999,1/3)>2.99
print('Endpoint, strict enlargement, and limiting sup=3 tests passed')
