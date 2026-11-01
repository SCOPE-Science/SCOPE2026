#!/usr/bin/env python3
"""Finite numerical consistency tests for a beta-moment Dirichlet Hankel boundary law.
All asymptotic assertions in the accompanying proof are analytic, not certified by these finite tests.
"""
import numpy as np
from scipy.special import jn_zeros, beta, gammaln

checks=0
z=jn_zeros(0,8)
assert np.all(np.diff(z)>0);checks+=1
# Trace identity has exact origin from kernel; finite sum is a lower bound.
for k in (1,3,10,30,90):
 z=jn_zeros(0,k)
 assert 0<np.sum(z**(-2))<0.25;checks+=1
assert 0.245<sum(jn_zeros(0,100)[-100:]**(-2))<0.25;checks+=1
for g in (0.125,0.35,0.75):
 for m in (1,3,7,15,30):
  formula=np.exp(gammaln(m+1)+gammaln(1+g)-gammaln(m+2+g))
  direct=beta(m+1,1+g)
  assert abs(formula/direct-1)<1e-12;checks+=1
  assert direct<1/(m+1);checks+=1
# Nystrom on [0,9]: compare eigenvalues of K = T*T to analytic Bessel ones.
for n in (180,300,420):
 L=10.
 h=L/n
 x=(np.arange(n)+0.5)*h
 K=0.5*np.exp(-2*np.maximum.outer(x,x))*h
 ev=np.linalg.eigvalsh(K)[-4:][::-1]
 target=jn_zeros(0,4)**(-2)
 assert np.max(abs(ev-target))<0.001, (n,ev,target)
 checks+=4
# Numerically sample the rescaled step kernels: away from diagonal and origin,
# K_g(X,Y) = g sqrt(i/j) mu_{i+j}/sqrt(g log(1+1/i)*g log(1+1/j)).
# To avoid huge integers, use robust gamma-log expression.
for g in (0.2,0.1,0.05):
 for X,Y in ((1.0,0.25),(1.0,0.6),(2.0,0.5),(0.5,1.0),(1.5,2.0)):
  i=int(np.exp(X/g)); j=int(np.exp(Y/g))
  mi=i+j
  log_mu=(gammaln(mi+1)+gammaln(g+1)-gammaln(mi+g+2)
           if mi<10**6 else gammaln(1+g)-(1+g)*np.log(mi))
  log_K=(np.log(g)+0.5*(np.log(i)-np.log(j))+log_mu
         -0.5*(np.log(g*np.log1p(1/i))+np.log(g*np.log1p(1/j))))
  got=np.exp(log_K)
  target=np.exp(-X) if X>Y else 0.
  if g==0.05:
   assert abs(got-target)<0.04, (X,Y,g,got,target)
   checks+=1
print('PASS',checks,'finite assertions; first four limiting singular values',list(1/jn_zeros(0,4)))
