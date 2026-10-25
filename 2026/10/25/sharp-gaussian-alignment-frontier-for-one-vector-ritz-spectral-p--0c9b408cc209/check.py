"""Exact identities and numerical checks for a one-vector spectral preconditioner.
Run: python check.py
"""
from fractions import Fraction
import math
import random
import sympy as s
import numpy as np

k,l,t=s.symbols('k l t', real=True)
lam=1+(k-1)*t
w=s.factor(lam*(k+2-lam)**2/k)
w0=(k+1)**2/k
assert s.simplify(k*(w-w0)-(lam-1)*(lam**2-(2*k+3)*lam+(k+1)**2))==0
assert s.simplify(w.subs(t,s.Rational(1,3))-4*(k+2)**3/(27*k))==0
assert s.simplify(s.diff(w,t).subs(t,s.Rational(1,3)))==0
print('symbolic polynomial, maximizer, and comparison identities: PASS')

N=0
for K in (s.Rational(3,2),s.Rational(2),s.Rational(5),s.Rational(9),s.Rational(100)):
    tc=(2*K+1-s.sqrt(4*K+5))/(2*(K-1))
    for tv in (s.Rational(1,100),s.Rational(1,7),s.Rational(1,3),s.Rational(2,3),s.Rational(99,100)):
        L=1+(K-1)*tv
        W=s.simplify(w.subs({k:K,t:tv}))
        delta=s.sign(s.simplify(W-(K+1)**2/K))
        ref=s.sign(tc-tv)
        assert delta==ref,(K,tv,delta,ref)
        N+=1
print('exact rational condition-number classification:',N,'PASS')

rng=np.random.default_rng(20261023)
num=0
for dimension in (2,3,4,7,16):
 for K in (1.1,1.9,2.0,5.0,25.0,100.0):
  H=np.diag([K]+[1.0]*(dimension-1))
  tc=(2*K+1-math.sqrt(4*K+5))/(2*(K-1))
  for _ in range(200):
   g=rng.normal(size=dimension)
   q=H@g
   q/=np.linalg.norm(q)
   tval=q[0]**2
   L=float(q@H@q)
   P=np.eye(dimension)+(L-1)*np.outer(q,q)
   # Cholesky similarity yields eigenvalues of the preconditioned SPD system.
   C=np.linalg.cholesky(P)
   Ci=np.linalg.inv(C)
   M=Ci@H@Ci.T
   eig=np.linalg.eigvalsh(M)
   cond=float(eig[-1]/eig[0])
   expected=(L*(K+2-L)**2/K)
   W=(cond+1/cond+2)
   assert abs(W-expected)<5e-8*(1+expected),(dimension,K,cond,W,expected)
   assert (cond>K)==(tval<tc) or abs(cond-K)<1e-8*max(1,K)
   if dimension>2:
    assert min(abs(eig-1))<1e-7
   num+=1
print('dense SPD matrix comparisons:',num,'PASS')

# Sample-law test with independent Gaussian sketches: exact Cauchy probability at d=2.
for K,tau in ((2,1),(10,0.1),(100,0.001),(1000,0.0000316227766)):
 tc=(2*K+1-math.sqrt(4*K+5))/(2*(K-1))
 T=K*K*tau*(1-tc)/tc
 target=2/math.pi*math.atan(math.sqrt(T))
 Z=rng.normal(size=(200000,2))
 events=(Z[:,1]**2<T*Z[:,0]**2)
 observed=events.mean()
 assert abs(observed-target)<0.008,(K,tau,target,observed)
 print('Gaussian d=2 K=',K,'tau=',tau,'exact probability=',round(target,6),'MC=',round(observed,6))
print('ALL CHECKS PASSED')
