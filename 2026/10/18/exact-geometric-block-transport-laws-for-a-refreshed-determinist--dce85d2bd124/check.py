#!/usr/bin/env python3
"""Independent exact-arithmetic and symbolic checks for the arrow-field block law."""
from fractions import Fraction as F
from itertools import product
from math import comb
import sympy as s
q,z=s.symbols('q z', real=True)
r=1-q
p=1-z
a=q*r
b=2*q-1
H=1-z+a*z*z
K=1+z-a*z*z
v=b*p*K/((1+z)*H)
# probability-generating function M(w)=E w^D from two-sided geometric tails
w=s.symbols('w')
A=q*(1-(q*z)**2)/(1+z)
B=r*(1-(r*z)**2)/(1+z)
C=2*a*z/(1+z)
M=C+A*w/(1-q*z*w)+B/w/(1-r*z/w)
assert s.factor(M.subs(w,1)-1)==0
ED=s.factor(s.diff(M,w).subs(w,1))
ED2=s.factor((s.diff(M,w,2)+s.diff(M,w)).subs(w,1))
assert s.factor(ED-v/p)==0
# Geometric time T with P(T=t)=p z^(t-1). For each t, expected D_t is [z^t] of M/p,
# so E(TD)=ED/p + z dED/dz when p is the geometric parameter.
ETD=s.simplify(ED/p+z*s.diff(ED,z))
ET2=(1+z)/p**2
var=s.factor(p*(ED2-2*v*ETD+v*v*ET2))
proposed=4*a*p*(1-a*z**2)**2/((1+z)*H**2)+4*a*b*b*p*z*z*K*(2-a*z**3)/((1+z)**3*H**3)
assert s.factor(var-proposed)==0, s.factor(var-proposed)
assert s.factor(s.diff(v,p) if False else -s.diff(v,z)-2*a*b*z*(2-a*z**3)/((1+z)**2*H**2))==0
balanced=s.factor(proposed.subs(q,s.Rational(1,2)))
balanced_expected=p*(2+z)**2/((2-z)**2*(1+z))
assert s.factor(balanced-balanced_expected)==0
assert s.factor(s.diff(balanced,z))==6*z*z*(z+2)/((z-2)**3*(1+z)**2)
assert s.factor(proposed.subs(z,0)-4*a)==0
assert s.factor(s.diff(proposed,z).subs(z,0))==0
assert s.factor(s.diff(proposed,z,2).subs(z,0)-24*a*b*b)==0
assert s.factor(proposed.subs(z,1))==0
checks=10
# Exhaustive exact distribution for fixed t, using only relevant arrows [-t,t].
for Q in [F(1,2),F(2,3),F(1,4)]:
  R=1-Q
  # Exact distribution D_t obtained by exhaustive independent arrows on [-t,t]
  for t in range(1,7):
    probs={}
    # walker never moves beyond +/-t, only locations -t+1,...,t-1 relevant
    indices=list(range(-t+1,t))
    for directions in product((-1,1),repeat=len(indices)):
      k=sum(d==1 for d in directions)
      weight=Q**k*R**(len(indices)-k)
      arrows=dict(zip(indices,directions))
      x=0
      for j in range(t):
        x+=arrows[x]
      probs[x]=probs.get(x,F(0))+weight
    assert sum(probs.values())==1
    # Compare each finite-time distribution with Taylor coefficients of the closed law.
    for k in range(-t,t+1):
      Qs=s.Rational(Q.numerator,Q.denominator)
      Rs=1-Qs
      if k==0:
        closed=2*Qs*Rs*z/((1+z)*(1-z))
      elif k>0:
        closed=Qs*(1-(Qs*z)**2)*(Qs*z)**(k-1)/((1+z)*(1-z))
      else:
        closed=Rs*(1-(Rs*z)**2)*(Rs*z)**(-k-1)/((1+z)*(1-z))
      predicted=s.expand(s.series(closed,z,0,t).removeO()).coeff(z,t-1)
      actual=s.Rational(probs.get(k,F(0)).numerator,probs.get(k,F(0)).denominator)
      assert s.factor(predicted-actual)==0,(Q,t,k,predicted,actual)
      checks+=1
    checks+=len(probs)+1
# Independent exact enumeration of full mixed law via recurrence t <= 10, including an explicit geometric tail error.
for Q in [F(1,2), F(2,3),F(1,4)]:
  R=1-Q
  Z=F(2,5)
  partial={}
  for t in range(1,9):
    indices=list(range(-t+1,t))
    distribution={}
    for dvec in product((-1,1),repeat=len(indices)):
      weight=Q**sum(d==1 for d in dvec)*R**sum(d==-1 for d in dvec)
      arrows=dict(zip(indices,dvec))
      x=0
      for _ in range(t): x+=arrows[x]
      distribution[x]=distribution.get(x,F(0))+weight
    for x,u in distribution.items():
      partial[x]=partial.get(x,F(0))+(1-Z)*Z**(t-1)*u
  for k in range(-4,5):
    if k==0: exact=2*Q*R*Z/(1+Z)
    elif k>0: exact=Q*(1-(Q*Z)**2)/(1+Z)*(Q*Z)**(k-1)
    else: exact=R*(1-(R*Z)**2)/(1+Z)*(R*Z)**(-k-1)
    assert abs(partial.get(k,F(0))-exact)<=Z**8
    checks+=1
print('SUCCESS',checks,'exact distribution checks, symbolic identities, CLT variance identity')
print('velocity',s.factor(v))
print('variance',s.factor(var))
