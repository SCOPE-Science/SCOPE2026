#!/usr/bin/env python3
"""Separate exact-rational checks of a one-knot linear-spline refinement result."""
from fractions import Fraction as F
from math import isclose
import sympy as sp

T,X=sp.symbols('t x',positive=True,real=True)
U0=(1-T)**2*(T-(1+2*T)*X)
U1=T**2*((3-2*T)*X+T-2)
A=sp.integrate(U0,(X,0,T))+sp.integrate(U1,(X,T,1))
B=sp.integrate(X*U0,(X,0,T))+sp.integrate(X*U1,(X,T,1))
C=sp.factor(sp.integrate(U0**2,(X,0,T))+sp.integrate(U1**2,(X,T,1)))
assert sp.simplify(A)==0 and sp.simplify(B)==0
assert sp.simplify(C-T**3*(1-T)**3/3)==0
assert sp.simplify(sp.integrate(X**2*U0,(X,0,T))+sp.integrate(X**2*U1,(X,T,1)) - T**2*(1-T)**2/12)==0
leftroot=T/(1+2*T)
rightroot=(2-T)/(3-2*T)
L1=sp.factor(2*(sp.integrate(U0,(X,0,leftroot))+sp.integrate(U1,(X,rightroot,1))))
assert sp.simplify(L1-4*T**2*(1-T)**2/((1+2*T)*(3-2*T)))==0

checks=5

def matinv3(t):
    M=sp.Matrix([[t/3,t/6,0],[t/6,sp.Rational(1,3),(1-t)/6],[0,(1-t)/6,(1-t)/3]])
    return M.inv()

def vals_u(t):
    return (t*(1-t)**2, -2*t*t*(1-t)**2, t*t*(1-t))

def hat_nodal(x,t):
    if x==0: return sp.Matrix([[1,0,0]])
    if x==t: return sp.Matrix([[0,1,0]])
    if x==1: return sp.Matrix([[0,0,1]])
    raise ValueError('not a knot')

def kernel(t,x,y,minv):
    return (hat_nodal(x,t)*minv*hat_nodal(y,t).T)[0]-(4-6*x-6*y+12*x*y)

def abs_affine_integral(a,b,length):
    a,b=sp.Rational(a),sp.Rational(b)
    if a==0 or b==0 or (a>0)==(b>0):
        return length*(abs(a)+abs(b))/2
    return length*(a*a+b*b)/(2*(abs(a)+abs(b)))

for den in [3,5,7,11,17,23]:
  for num in range(1,den):
    t=sp.Rational(num,den)
    inv=matinv3(t)
    knot=(sp.Rational(0),t,sp.Rational(1))
    uvals=vals_u(t)
    for i,xx in enumerate(knot):
      for j,yy in enumerate(knot):
        assert sp.simplify(kernel(t,xx,yy,inv)-uvals[i]*uvals[j]/(t**3*(1-t)**3/3))==0
        checks+=1
      rows=[kernel(t,xx,y,inv) for y in knot]
      absint=abs_affine_integral(rows[0],rows[1],t)+abs_affine_integral(rows[1],rows[2],1-t)
      expect=abs(uvals[i])*4*t*t*(1-t)**2/((1+2*t)*(3-2*t))/(t**3*(1-t)**3/3)
      assert sp.simplify(absint-expect)==0
      checks+=1
    true_norm=max([abs(z) for z in uvals])*4*t*t*(1-t)**2/((1+2*t)*(3-2*t))/(t**3*(1-t)**3/3)
    formula=12*max(t,1-t)/((1+2*t)*(3-2*t))
    assert true_norm==formula
    assert formula>=sp.Rational(3,2) and formula<4
    checks+=2
    endpoint_quad=(1-t)/4
    quad_inner=t*t*(1-t)**2/12
    assert sp.simplify(quad_inner/(t**3*(1-t)**3/3)*uvals[0]-endpoint_quad)==0
    checks+=1

print('PASS exact symbolic orthogonality, norms, moments and', checks, 'independent rational assertions')
print('The sharp norm is 12 max(t,1-t)/((1+2t)(3-2t)); minimum 3/2 at t=1/2; supremum 4.')
