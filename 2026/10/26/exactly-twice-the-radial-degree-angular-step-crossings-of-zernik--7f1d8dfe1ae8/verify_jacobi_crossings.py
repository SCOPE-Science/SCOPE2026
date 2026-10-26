#!/usr/bin/env python3
"""Exact arithmetic checks for adjacent-parameter Jacobi cumulative energies.

Requires Python 3, SymPy and SciPy. Finite checks supplement, not replace,
the all-parameter algebraic argument and standard Jacobi zero theorem.
"""
import sympy as sp
from scipy.special import roots_jacobi

x=sp.symbols('x')
betas=[sp.Rational(-1,2),sp.Integer(0),sp.Rational(1,3),sp.Integer(1),sp.Rational(5,2)]
# Universal algebraic verification of the differentiated boundary identity.
K,B,Q,R=sp.symbols('K B Q R', real=True)
MU=K+B+1
V=(1-x)*(Q**2-(1-x)*R**2)
Qp=(K*Q+MU*R)/x
Rp=(-K*Q-(MU-(MU+1)*x)*R)/(x*(1-x))
Derivative=(B+1)*V+x*(sp.diff(V,x)+sp.diff(V,Q)*Qp+sp.diff(V,R)*Rp)
Target=(2*K+B+1)*(Q+(1-x)*R)**2-(2*K+B+2)*x*Q**2
assert sp.factor(Derivative-Target)==0
checks=1
for k in range(0,7):
 for beta in betas:
  mu=k+beta+1
  p=sp.expand(sp.jacobi(k,0,beta,2*x-1))
  q=sp.expand(sp.jacobi(k,0,beta+1,2*x-1))
  r=sp.expand(sp.diff(p,x)/mu)
  assert sp.expand(q-p+(1-x)*r)==0
  checks+=1
  if k:
   assert sp.expand(r-sp.jacobi(k-1,1,beta+1,2*x-1))==0
   checks+=1
  def weighted_primitive(polynomial,shift):
   poly=sp.Poly(sp.expand(polynomial**2),x)
   return sp.expand(sum(coef*x**(j+shift)/(beta+j+shift+1)
                        for (j,),coef in poly.terms()))
  primitive=sp.expand((2*k+beta+1)*weighted_primitive(p,0)
                       -(2*k+beta+2)*weighted_primitive(q,1))
  boundary=sp.expand((1-x)*(q*q-(1-x)*r*r))
  assert sp.expand(primitive-boundary)==0
  checks+=1
  if k:
   assert bool(boundary.subs(x,0)>0)
   assert sp.expand(boundary.subs(x,1))==0
   checks+=2
   zeros=[float(z) for z in (roots_jacobi(k,0,float(beta))[0]+1)/2]
   turns=[float(z) for z in (roots_jacobi(k-1,1,float(beta)+1)[0]+1)/2] if k>1 else []
   critical=[0.0]+[z for pair in zip(zeros,turns+[1.0]) for z in pair]
   assert len(critical)==2*k+1
   reduced=sp.expand(q*q-(1-x)*r*r)
   vals=[float(sp.N(reduced.subs(x,z))) for z in critical]
   assert all(vals[j]*vals[j+1]<0 for j in range(len(vals)-1)), (k,beta,critical,vals)
   checks+=1
print('PASS',checks,'exact algebraic, endpoint, and root-bracketing assertions',
      'across',7*len(betas),'parameter-degree combinations')
