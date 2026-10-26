#!/usr/bin/env python3
"""Reproduce exact finite polynomial identities and noninteger Jacobi checks.
Analytical quantifiers are proved in RESULT.md; finite checks are diagnostics.
"""
import sys
import sympy as sp
import mpmath as mp

x=sp.symbols('x')
N=0
for k in range(1,6):
    for beta in range(0,4):
        A=sp.jacobi(k,0,beta,2*x-1)
        B=sp.jacobi(k-1,0,beta+2,2*x-1)
        Q=sp.jacobi(k-1,1,beta+1,2*x-1)
        assert sp.cancel(A-x*B+sp.Rational(beta+1,k)*(1-x)*Q)==0
        N+=1
        assert sp.cancel(Q-(1-x)*sp.diff(Q,x)-k*B)==0
        N+=1
        F=(2*k+beta+1)*sp.Rational(beta+1,k*k)*x**(beta+1)*(1-x)**2*Q**2
        H=(2*k+beta+1)*x**beta*(A**2-x**2*B**2)
        assert sp.cancel(sp.diff(F,x)-H)==0
        N+=1
        assert sp.cancel(F.subs(x,0))==0 and sp.cancel(F.subs(x,1))==0
        N+=1

from scipy.integrate import quad
from scipy.special import eval_jacobi
for beta in [0.2,0.5,1.3,2.7]:
  for k in [1,3]:
    L=2*k+beta+1
    for t in [0.12,0.68]:
      Aint=quad(lambda u:u**beta*eval_jacobi(k,0,beta,2*u-1)**2,0,t,epsabs=2e-12)[0]
      Bint=quad(lambda u:u**(beta+2)*eval_jacobi(k-1,0,beta+2,2*u-1)**2,0,t,epsabs=2e-12)[0]
      Q=eval_jacobi(k-1,1,beta+1,2*t-1)
      rhs=L*(beta+1)/k**2 * t**(beta+1)*(1-t)**2*Q**2
      assert abs(L*(Aint-Bint)-rhs)<1e-10
      N+=1
print('PASSED',N,'identities and integral comparisons')
