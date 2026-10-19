#!/usr/bin/env python3
"""Algebraic and finite-matrix cross-checks for weighted-noise star pinning.

Requires Python 3, sympy, numpy and scipy. Checks complement (not replace) the proof.
"""
import math
import random
import numpy as np
import sympy as sp
from scipy.optimize import minimize_scalar

m, B, x, rho = sp.symbols('m B x rho', positive=True)
y=(B-x)/m
D=sp.factor((m+x)*(1+y)-m)
J=sp.factor(rho*(1+y)/D + m/(1+y) + m/(D*(1+y)))
N = B**3+4*m*B**2+5*m**2*B+2*m**3
expected_d0=sp.factor((m**3*(m-1)*B-rho*N)/(B*m**2*(B+m)**2))
assert sp.simplify(sp.diff(J,x).subs(x,0)-expected_d0)==0
assert sp.simplify(sp.diff(J,x).subs(x,B)-(B+2)/B)==0
z=sp.symbols('z',positive=True)
f=z/((z+1)**2*(z+2))
assert sp.simplify(sp.diff(f,z)-2*(1-z-z*z)/((z+1)**3*(z+2)**2))==0
zstar=(sp.sqrt(5)-1)/2
cstar=(5*sp.sqrt(5)-11)/2
assert sp.simplify(f.subs(z,zstar)-cstar)==0
assert sp.factor((N.subs(B,m*z)/m**3) - (z+1)**2*(z+2))==0
poly=sp.together((rho*N-m**3*(m-1)*B).subs({m:2,rho:sp.Rational(1,6)}))*6
assert sp.factor(poly)==(B-2)*(B**2+10*B-8)
count=8

def obj(m,B,rho,x):
    y=(B-x)/m
    D=m*y+x*(1+y)
    return rho*(1+y)/D +m/(1+y)+m/(D*(1+y))

def matrix_obj(m,B,rho,x):
    y=(B-x)/m
    A=np.zeros((m+1,m+1))
    A[0,0]=m+x
    A[0,1:]=-1
    A[1:,0]=-1
    A[1:,1:]=np.eye(m)*(1+y)
    Q=np.diag([rho]+[1]*m)
    return np.trace(Q@np.linalg.inv(A))

rng=random.Random(314159)
for m0 in range(2,12):
  for rho0 in [0.06, 0.17, 0.5, 1, 3, 8]:
    for B0 in [0.15, 0.5, 1.,2.,3., 9., 40., 150.]:
      bc=(m0*(m0-1)*(B0/m0))/((1+B0/m0)**2*(2+B0/m0))
      res=minimize_scalar(lambda xx: obj(m0,B0,rho0,xx),bounds=(0,B0),method='bounded',options={'xatol':1e-12})
      assert res.success
      if rho0<bc-1e-7:
          assert res.x<1e-5*max(1,B0), (m0,rho0,B0,res.x,bc)
      if rho0>bc+1e-7:
          assert res.x>1e-7*max(1,B0), (m0,rho0,B0,res.x,bc)
      for xx in [0,B0*0.23,B0*.79,B0]:
          assert abs(obj(m0,B0,rho0,xx)-matrix_obj(m0,B0,rho0,xx))<1e-6*max(1,obj(m0,B0,rho0,xx))
          count+=1
      # independent nonsymmetric feasible designs: convexity ensures no better than optimum
      for j in range(3):
          g=np.array([rng.random() for _ in range(m0+1)])
          g=g*(B0/sum(g))
          A=np.zeros((m0+1,m0+1))
          A[0,0]=m0+g[0];A[0,1:]=-1;A[1:,0]=-1
          A[1:,1:]=np.eye(m0)+np.diag(g[1:])
          Q=np.diag([rho0]+[1.]*m0)
          value=float(np.trace(Q@np.linalg.inv(A)))
          assert value+1e-7>=res.fun, (m0,B0,rho0,value,res.fun)
          count+=1
for B0 in [0.2,1.,3.]:
  m0=2;rho0=1/6
  bc=m0*(m0-1)*(B0/m0)/((1+B0/m0)**2*(2+B0/m0))
  res=minimize_scalar(lambda xx: obj(m0,B0,rho0,xx), bounds=(0,B0),method='bounded')
  assert (res.x<1e-4)==(rho0<bc)
  count+=1
print('PASS: %d symbolic, exact-rational, direct-matrix and optimization assertions.'%count)
