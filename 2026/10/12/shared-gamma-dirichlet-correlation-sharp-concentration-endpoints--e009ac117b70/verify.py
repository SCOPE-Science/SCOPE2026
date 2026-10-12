#!/usr/bin/env python3
"""Reproducible finite diagnostics for the shared-Gamma Dirichlet coupling.

Requires numpy and sympy. The theorem's continuous-parameter and limit
statements are established analytically in RESULT.md, not by this script.
"""
from fractions import Fraction
import math
import numpy as np
import sympy as sp

s,c,e=sp.symbols('s c e', positive=True)
r2=s*(s*c+1)/(c+1)
# The two equivalent forms of the discrepancy from the linear proxy.
assert sp.simplify((c+1)/(s*c+1)*r2-s)==0
assert sp.simplify(s-(c+1)/(s*c+1)*(r2-e/2)-(c+1)/(2*(s*c+1))*e)==0
# Beta second moment, the shared-Dirichlet covariance and the marginal
# covariance give an identical scalar across all composition vectors.
mu=sp.symbols('mu', positive=True)
delta=sp.symbols('delta', real=True)
cov_w=(mu*delta-mu**2)/(s*c+1)
cov_x=(mu*delta-mu**2)/(c+1)
assert sp.simplify((e*cov_w)/cov_x-(c+1)*e/(s*c+1))==0

rng=np.random.default_rng(25012023)
def check(c0, s0, n=300_000):
    # 3 independent gamma totals, not a dependent-gamma approximation.
    t=rng.gamma(s0*c0, 1.0, n)
    u=rng.gamma((1-s0)*c0,1.0,n)
    v=rng.gamma((1-s0)*c0,1.0,n)
    r=t/(t+u); z=t/(t+v)
    rho=(c0+1)/(s0*c0+1)*float(np.mean(r*z))
    # Two independent numerical routes to the same exact identity.
    rho_via_gap=s0-(c0+1)/(2*(s0*c0+1))*float(np.mean((r-z)**2))
    assert abs(rho-rho_via_gap)<0.012, (rho,rho_via_gap)
    assert 0<rho<s0, (rho,s0)
    return rho,rho_via_gap

# The published (equal-margin) check is r about 0.468 for c=6,s=1/2.
a,b=check(6.0,0.5)
assert abs(a-0.468)<0.012, a
# At small and large concentration, the limits have very different forms.
lo,_=check(0.05,0.4)
hi,_=check(200.0,0.4)
assert abs(lo-0.4/(2-0.4))<0.04, lo
assert abs(hi-0.4)<0.015, hi

# Direct independent-gamma vector construction: off-diagonal covariance
# is negative across views and all same-index correlations are identical.
mu=np.array([0.2,0.3,0.5]); c0=3.0; s0=0.4; n=300_000
share=rng.gamma(s0*c0*mu,size=(n,3))
first=rng.gamma((1-s0)*c0*mu,size=(n,3))
second=rng.gamma((1-s0)*c0*mu,size=(n,3))
x=(first+share)/(first+share).sum(axis=1)[:,None]
y=(second+share)/(second+share).sum(axis=1)[:,None]
emp=np.cov(x.T,y.T,bias=True)[:3,3:]
T=share.sum(axis=1); U=first.sum(axis=1); V=second.sum(axis=1)
rs=float(np.mean((T/(T+U))*(T/(T+V))))
rho=(c0+1)/(s0*c0+1)*rs
pred=rho*(np.diag(mu)-np.outer(mu,mu))/(c0+1)
assert np.max(np.abs(emp-pred))<0.004,(emp,pred)
assert np.all(np.diag(emp)>0)
assert np.all(emp[np.triu_indices(3,1)]<0)
print('Finite diagnostics passed; published check ~',round(a,6))
print('rho at small c, limit:',round(lo,6),round(0.4/1.6,6))
print('rho at large c, limit:',round(hi,6),0.4)
print('cross-covariance max discrepancy:',float(np.max(abs(emp-pred))))
print('Analytic proofs (not finite checks) establish the universal limits.')
