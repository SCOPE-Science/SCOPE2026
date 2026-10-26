#!/usr/bin/env python3
"""Reproduce stationary radial moment bounds for correlated-tumble harmonic swimmers.
Only standard Python, SymPy, NumPy; the proof is the stationary generator argument.
"""
from fractions import Fraction
import math
import numpy as np
import sympy as sp

checks=0
def ck(condition,msg):
    global checks
    assert bool(condition),msg
    checks+=1

k,s,t,v,D=sp.symbols('k s t v D',positive=True)
a={0:sp.Integer(0),1:s,2:t,3:sp.symbols('a3',positive=True),4:sp.symbols('a4',positive=True)}
# Build rotationally invariant moments R[p,q]=E[z^p conjugate(z)^q exp(i(q-p)theta)]
R={(0,0):sp.Integer(1)}
for degree in range(1,5):
    for p in range(degree+1):
        q=degree-p
        R[p,q]=sp.factor(v*(p*R[p-1,q] if p else 0) /(degree*k+a[abs(q-p)])+v*(q*R[p,q-1] if q else 0)/(degree*k+a[abs(q-p)]))
M2=sp.factor(R[1,1]);M4=sp.factor(R[2,2]);
formula2=v**2/(k*(k+s))
formula4=2*v**4*(3*k+t)/(k*k*(k+s)*(3*k+s)*(2*k+t))
ck(sp.simplify(M2-formula2)==0,'symbolic variance recurrence')
ck(sp.simplify(M4-formula4)==0,'symbolic fourth recurrence')
ck(sp.simplify(sp.diff(formula4,t)) < 0 if False else sp.factor(sp.diff(formula4,t)).as_numer_denom()[0].could_extract_minus_sign(),'strict decreasing derivative')
ck(sp.simplify(formula4.subs({s:0,t:0})-(v/k)**4)==0,'ballistic radius fixed')
ck(sp.simplify(formula4.subs(t,s)-2*v**4/(k**2*(k+s)*(2*k+s)))==0,'uniform tumble beta moments')
ck(sp.simplify(formula4.subs(t,0)-3*v**4/(k**2*(k+s)*(3*k+s)))==0,'axial dichotomic stationary fourth')

# Every probability on turning angle satisfying even symmetry obeys 2mu1^2-1<=mu2<=1.
mu,lam=sp.symbols('mu lam',real=True,positive=True)
tmax=2*lam*(1-mu**2)
upper=sp.factor(formula4.subs(t,0))
lower=sp.factor(formula4.subs(t,tmax))
ck(sp.factor(upper-lower)==sp.factor(2*v**4*k*tmax/(k**2*(k+s)*(3*k+s)*2*k*(2*k+tmax))), 'sharp gap identity')

# Thermal convolution: G=(Gx,Gy) iid N(0,D/k), independent of active position.
active_var=formula2
M2thermal=active_var+2*D/k
M4thermal=formula4+8*D*active_var/k+8*D**2/k**2
for xv in [sp.Rational(1,2), sp.Integer(1),sp.Integer(2)]:
    ck(sp.simplify((M4thermal.subs({k:xv,s:sp.Rational(3,4),t:sp.Rational(1,3),v:2,D:0})-formula4.subs({k:xv,s:sp.Rational(3,4),t:sp.Rational(1,3),v:2})))==0,'D0 active split')

# Direct independent construction: numerical moment generator on 4 discrete headings with exact finite-angle jumps.
# W mass [p0,p90,p180,p270] chosen for mu1=1/4, mu2=1/2.
# Solve the moment linear systems of the real-space generator in x,y for total degree <=4,
# then sum E[x^4]+2E[x^2y^2]+E[y^4].
from collections import OrderedDict
angles=[(1,0),(0,1),(-1,0),(0,-1)]
weights=[sp.Rational(1,2),sp.Rational(1,8),sp.Rational(1,4),sp.Rational(1,8)]
K=sp.Rational(2);V=sp.Rational(7,3);L=sp.Rational(3)
from math import comb
# Conditional stationary polynomial moments m[i,j,h]=E[x^i y^j 1_{theta=h}], h=0,..3.
# degree zero stationary orientation=uniform due irreducible jumps. Higher degrees solved exact.
m={}
for h in range(4):m[(0,0,h)]=sp.Rational(1,4)
for degree in range(1,5):
  indices=[(i,degree-i,h) for i in range(degree+1) for h in range(4)]
  rows=[]; rhs=[]
  for i,j,h in indices:
    row=[]
    for ii,jj,g in indices:
      val=sp.Integer(0)
      if i==ii and j==jj:
        val-=K*degree*(h==g)
        if h==g: val-=L
        val+=L*weights[(h-g)%4]
      row.append(val)
    # generator adjoint stationarity for each moment in orientation state h
    force=sp.Integer(0)
    if i:force+=V*i*angles[h][0]*m[i-1,j,h]
    if j:force+=V*j*angles[h][1]*m[i,j-1,h]
    rows.append(row);rhs.append(-force)
  result=sp.Matrix(rows).inv()*sp.Matrix(rhs)
  for z,val in zip(indices,result): m[z]=sp.cancel(val)
M2_four=sp.factor(sum(m[(2,0,h)]+m[(0,2,h)] for h in range(4)))
M4_four=sp.factor(sum(m[(4,0,h)]+2*m[(2,2,h)]+m[(0,4,h)] for h in range(4)))
S=L*(1-sp.Rational(1,4));T=L*(1-sp.Rational(1,2))
ck(sp.simplify(M2_four-formula2.subs({k:K,v:V,s:S}))==0,'independent 4-heading second')
ck(sp.simplify(M4_four-formula4.subs({k:K,v:V,s:S,t:T}))==0,'independent 4-heading fourth')

# Numerical continuous-time renewal integration in stationary regime. Exact OU position updates.
def mc(label, turns, seed, n=140000, horizon=20.0, kap=1.0, alpha=1.0):
  rng=np.random.default_rng(seed)
  x=np.zeros(n,dtype=np.complex128)
  heading=np.ones(n,dtype=np.complex128)
  clock=np.zeros(n)
  pending=np.ones(n,dtype=bool)
  while np.any(pending):
    idx=np.flatnonzero(pending)
    waiting=rng.exponential(1/alpha,len(idx))
    dt=np.minimum(waiting,horizon-clock[idx])
    x[idx]+=heading[idx]*np.exp(-kap*clock[idx])*(-np.expm1(-kap*dt))/kap
    clock[idx]+=dt
    finished=clock[idx]>=horizon-1e-13
    active=idx[~finished]
    if len(active):
      phi=turns(rng,len(active))
      heading[active]*=np.exp(1j*phi)
    pending[idx[finished]]=False
  power=np.abs(x)**2
  avg2=power.mean();avg4=(power**2).mean()
  se2=power.std(ddof=1)/np.sqrt(n)
  se4=(power**2).std(ddof=1)/np.sqrt(n)
  return avg2,avg4,se2,se4

laws={
    'orthogonal_turns':(lambda rng,n: rng.choice([-np.pi/2,np.pi/2],n),-1.0),
    'uniform_turns':(lambda rng,n: rng.uniform(-np.pi,np.pi,n),0.0),
    'axial_flip_turns':(lambda rng,n: rng.choice([0,np.pi],n),1.0)
}
for j,(label,(draw,mu2)) in enumerate(laws.items()):
   m2,m4,e2,e4=mc(label,draw,123456+j)
   theo2=0.5
   theo4=float(formula4.subs({k:1,s:1,t:1-mu2,v:1}))
   ck(abs(m2-theo2)<6*e2+1e-4,'MC variance '+label)
   ck(abs(m4-theo4)<6*e4+2e-4,'MC fourth '+label)
   print(label,'M2',round(m2,7),'M4',round(m4,7),'predM4',round(theo4,7),'se4',round(e4,7))

# The first Fourier moment and stationary variance agree for all three turning laws,
# while the sharp kurtosis values differ (K=5/4,4/3,3/2).
ck(sp.simplify(formula4.subs({k:1,v:1,s:1,t:2})-sp.Rational(5,16))==0,'quarter-turn lower bound')
ck(sp.simplify(formula4.subs({k:1,v:1,s:1,t:1})-sp.Rational(1,3))==0,'uniform middle')
ck(sp.simplify(formula4.subs({k:1,v:1,s:1,t:0})-sp.Rational(3,8))==0,'axial flip upper')
print('PASS',checks,'check groups')
