#!/usr/bin/env python3
"""Numerical and exact-algebra sanity checks for a compressed eigensolver step."""
import math
import numpy as np
import sympy as sp

s, a, L, gam, q = sp.symbols('s a L gam q', positive=True)
assert sp.expand((a**3+(1-s**2)*a-s).subs(a,s)) == 0
assert sp.expand((L-1)*(L-s**2-q)-s**2-(L*(L-(1+s**2))-(L-1)*q)) == 0
assert sp.simplify(sp.diff(a**4/4+(1-s**2)*a**2/2-s*a,a)-(a**3+(1-s**2)*a-s)) == 0
assert sp.simplify(sp.expand((L-(1+s**2))*L-(L-1)*q) -(L*(L-1-s*s)-(L-1)*q)) == 0

rng=np.random.default_rng(340262)
for m in range(1,16):
  for rep in range(70):
    sv=float(rng.uniform(.08,.93)); gamma=float(rng.uniform(.2,3)); tau=float(rng.uniform(.01,.15))
    v=rng.uniform(-tau/sv,tau/sv,size=m)
    E=rng.normal(size=(m,m)); D=gamma*np.eye(m)+E.T@E/m
    H=np.zeros((m+2,m+2));H[:2,:2]=-np.outer([1,sv],[1,sv]);H[1,2:]=v;H[2:,1]=v;H[2:,2:]=D
    c=np.r_[1.,sv,np.zeros(m)];b0=H[:,0].copy();b=b0+sv*H[:,1];b[2:]=0
    assert np.max(np.abs(4*(b+np.dot(c,c)*c)))<4e-12
    exact=4*(H@c+np.dot(c,c)*c)
    assert np.max(np.abs(exact[2:]-4*sv*v))<4e-12
    vals=np.linalg.eigvalsh(H);low=-vals[0];A=1+sv**2
    if np.linalg.norm(v)>1e-10:
      assert low>A-1e-9
      secular=low*(low-A)-(low-1)*float(v @ np.linalg.solve(D+low*np.eye(m),v))
      assert abs(secular)<3e-9*(1+low**3)
    # exact extremal frontier using scalar bracketing
    from scipy.optimize import brentq
    Phi=lambda z:z*(z-A)*(gamma+z)/(z-1)
    rhs=m*tau*tau/(sv*sv)
    Lstar=brentq(lambda z:Phi(z)-rhs,A,A+rhs+30)
    assert low<=Lstar+2e-9
    ve=np.full(m,tau/sv);He=H.copy();He[1,2:]=ve;He[2:,1]=ve;He[2:,2:]=gamma*np.eye(m)
    assert abs(-np.linalg.eigvalsh(He)[0]-Lstar)<2e-8

for r in [1,2,3,5,12,29]:
  m=r*r;sv=.5;gamma=1.;v=np.full(m,1/r);tau=.5/r
  H=np.zeros((m+2,m+2));H[:2,:2]=-np.outer([1,sv],[1,sv]);H[1,2:]=v;H[2:,1]=v;H[2:,2:]=np.eye(m)
  K=np.array([[-1.,-.5,0],[-.5,-.25,1],[0,1,1]])
  assert abs(np.linalg.eigvalsh(H)[0]-np.linalg.eigvalsh(K)[0])<5e-11
  assert abs(np.linalg.norm(H,2)-np.linalg.norm(K,2))<5e-11
print('PASS: 4 symbolic relations, 1050 randomized exact-step/secular/bound/sharpness families, 6 fixed-norm sequences')
print('K eigenvalues:',np.linalg.eigvalsh(K),'hidden correction:',-np.linalg.eigvalsh(K)[0]-1.25)
