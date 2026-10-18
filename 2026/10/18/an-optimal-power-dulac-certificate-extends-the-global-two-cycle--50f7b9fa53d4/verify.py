#!/usr/bin/env python3
"""Exact Dulac-certificate and sample-orbit checks for a polynomial three-flow.
Run with Python 3, sympy, numpy and scipy.
"""
import sympy as sp
from scipy.integrate import solve_ivp
import numpy as np
u,z,mu,alpha=sp.symbols('u z mu alpha',real=True)
B=(u-5)*(sp.Rational(20,21)-u)-sp.Rational(400,21)*z*z
P=2*mu*u*B
Q=-z-u/sp.Integer(10)
D=sp.factor(sp.diff(P/u,u)+sp.diff(Q/u,z))
assert sp.simplify(D-(sp.Rational(250,21)*mu-4*mu*u-1/u))==0
assert sp.simplify(B.subs(z,-u/10)+sp.Rational(25,21)*(u-1)*(u-4))==0
critical=sp.Rational(1764,15625)
assert sp.factor(D.subs(mu,critical)) == -(84*u-125)**2/(15625*u)
assert critical>sp.Rational(588,6575)
# A power-family Dulac factor u^(-alpha) has an exact quadratic envelope.
H=sp.expand((1-alpha)*(u-5)*(sp.Rational(20,21)-u)+u*sp.diff(B,u))
maxH=sp.Rational(15625,1764)*(2-alpha)**2/(3-alpha)-sp.Rational(100,21)*(1-alpha)
vertex=sp.Rational(125,42)*(2-alpha)/(3-alpha)
assert sp.simplify(H.subs(u,vertex)-maxH)==0
assert sp.simplify(sp.diff(maxH,alpha) + 25*(17*alpha-76)*(17*alpha-26)/(1764*(alpha-3)**2))==0
assert sp.factor(maxH.subs(alpha,1))==sp.Rational(15625,3528)
assert sp.simplify(1/(2*maxH.subs(alpha,1))-critical)==0
for a,det_sign,trace_sign in ((1,-1,None),(4,1,-1)):
 J=sp.Matrix([P,Q]).jacobian([u,z]).subs({u:a,z:-sp.Rational(a,10)})
 det=sp.factor(J.det());tra=sp.factor(J.trace())
 assert sp.sign(det.subs(mu,sp.Rational(1,20)))==det_sign
 if trace_sign is not None:assert sp.sign(tra.subs(mu,sp.Rational(1,20)))==trace_sign
 assert det != 0
 assert sp.factor(P.subs({u:a,z:-sp.Rational(a,10)}))==0
# Check the original Cartesian radial reconstruction algebraically.
x,y,e=sp.symbols('x y e',real=True)
w=z+(x*x+y*y)/10
R=x*x+y*y
F1=mu*x*B.subs(u,R)-(1+e*w)*y
F2=mu*y*B.subs(u,R)+(1+e*w)*x
assert sp.expand(2*x*F1+2*y*F2-2*mu*R*B.subs(u,R))==0
assert sp.expand((x*F2-y*F1)-(1+e*w)*R)==0
# Representative trajectories in the parameter interval beyond the source's window.
def rhs(t,state,m):
 U,Z,offset=state
 b=(U-5)*(20/21-U)-400*Z*Z/21
 return [2*m*U*b,-Z-U/10,0.1*(Z+U/10)]
for m in (0.09,0.10,0.112):
 for u0,z0,expected in ((0.3,-0.1,0),(3.9,-0.39,4),(5,-0.5,4)):
  sol=solve_ivp(rhs,(0,450),[u0,z0,0],args=(m,),rtol=2e-11,atol=2e-12)
  assert sol.success
  assert abs(sol.y[0,-1]-expected)<1e-6,(m,u0,sol.y[0,-1])
  assert abs(sol.y[1,-1]+expected/10)<1e-6
  assert np.isfinite(sol.y).all()
print('PASS: exact reduction, weighted divergence, equality boundary, optimal power-family cutoff, equilibrium stability, nine sample trajectories')
