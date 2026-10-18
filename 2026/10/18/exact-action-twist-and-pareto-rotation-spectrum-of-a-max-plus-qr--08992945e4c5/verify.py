#!/usr/bin/env python3
"""Exact algebraic and finite-orbit cross-checks for a piecewise-affine invariant-rotation law.
Requires Python 3 and SymPy. Finite orbit checks are controls, not an infinite proof.
"""
from fractions import Fraction
import math
import sympy as s

def H(x,y):
    return max(1-x-y, 2-x, 2-y, 1+x-y, 1-x+y, x, y)

def F(x,y):
    return y, max(0,y+1)-x

def vertices(c):
    return [(c,c),(c,1),(c-2,-1),(1,2-c),(-1,2-c),(2-c,-1),(2-c,1),(1,c)]

c,r,C=s.symbols('c r C',real=True)
v=vertices(c)
signed=s.expand(sum(v[j][0]*v[(j+1)%8][1]-v[(j+1)%8][0]*v[j][1] for j in range(8))/2)
area=(5*c*c-6*c-3)/2
assert s.simplify(-signed-area)==0
assert s.simplify(area.subs(c,3)-12)==0
rho=(c-1)/(5*c-3)
assert s.simplify(rho-1/(5+2/(c-1)))==0
assert s.simplify(s.diff(rho,c)/(s.diff(area,c)/(2*s.pi))-4*s.pi/(5*c-3)**3)==0
c_of_r=(1-3*r)/(1-5*r)
assert s.simplify(rho.subs(c,c_of_r)-r)==0
assert s.simplify(s.diff(area,c).subs(c,c_of_r)*s.diff(c_of_r,r)-4/(1-5*r)**3)==0
assert s.simplify(s.integrate(4/(1-5*r)**3,(r,s.Rational(1,6),rho.subs(c,C)))-(area.subs(c,C)-12))==0
assert s.simplify((s.Rational(1,5)-rho)-2/(5*(5*c-3)))==0
assert s.simplify(s.limit(area.subs(c, C*s.Rational(2,25)/s.Symbol('w',positive=True))/area.subs(c,C),C,s.oo)-((s.Rational(2,25)/s.Symbol('w',positive=True))**2))==0
# Exact-gridded invariant checks, including branch boundaries.
for i in range(-22,23):
    for j in range(-22,23):
        x,y=Fraction(i,5),Fraction(j,5)
        X,Y=F(x,y)
        assert H(X,Y)==H(x,y), (x,y)
# Exact rational orbit periods and label-height invariance.
for level in (Fraction(4),Fraction(5),Fraction(9,2),Fraction(7,2),Fraction(31,10)):
    initial=(level,level)
    x,y=initial
    orbit=[]
    for k in range(1,3000):
        assert H(x,y)==level
        orbit.append((x,y))
        x,y=F(x,y)
        if (x,y)==initial:
            break
    else:
        raise AssertionError('Orbit failed to close in a finite check')
    h=Fraction(2,1)/(level-1)
    want=5*h.denominator+h.numerator
    assert k==want, (level,k,want)
    # Independently verify clockwise winding: monotone polygonal angular path.
    cx,cy=1,1
    last=math.atan2(float(orbit[0][1]-cy),float(orbit[0][0]-cx))
    winding=0.0
    for pt in orbit[1:]+[orbit[0]]:
        th=math.atan2(float(pt[1]-cy),float(pt[0]-cx))
        d=(th-last+math.pi)%(2*math.pi)-math.pi
        winding+=d
        last=th
    assert abs(-winding/(2*math.pi)-h.denominator)<1e-9
    assert Fraction(h.denominator,k)==Fraction(level-1,5*level-3)
print('VERIFY_OK')
