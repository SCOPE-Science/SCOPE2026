#!/usr/bin/env python3
"""Independent resolvent checks for a local-time/reset-count joint law.

The finite-state birth-death model is a discretization that checks algebra
and conventions; the continuum theorem rests on its separate analytic proof.
"""
import math
import numpy as np
from numpy.linalg import solve


def continuous_parameters(a,D,r):
    z=math.sqrt(r/D)
    success=math.exp(-a*z)
    green=-math.expm1(-2*a*z)/(2*math.sqrt(D*r))
    return success,green


def finite_chain(m,initial,rate_left,rate_right,r,s,z):
    # Transient states 1,...,m; reflect at the upper endpoint m.
    Q=np.zeros((m,m))
    absorb=np.zeros(m)
    for k in range(1,m+1):
        i=k-1
        Q[i,i]-=rate_left
        if k==1:absorb[i]+=rate_left
        else:Q[i,i-1]+=rate_left
        if k<m:
            Q[i,i]-=rate_right
            Q[i,i+1]+=rate_right
    A=-Q+r*np.eye(m)
    e=np.zeros(m);e[initial-1]=1.
    source=np.ones(m)
    p=float(e@solve(A,absorb))
    g=float(e@solve(A,e))
    # Direct counting-propagator backward equation:
    # 0=Qu - r u + r z u(initial) -s 1_{initial}u + absorption.
    direct=float(e@solve(A+s*np.outer(e,e)-r*z*np.outer(source,e),absorb))
    expected=p/(1+s*g-(1-p)*z)
    return direct,expected,p,g


def main():
    # independent direct Markov-chain equations, not invoking renewal proof.
    count=0
    for m in [3,5,7]:
      for initial in [1,2,m]:
        for left,right in [(1.0,1.0),(0.4,2.3),(3.0,0.7)]:
          for r in [0.05,0.5,2.0]:
            for s in [0.0,0.25,1.3]:
              for z in [0.0,0.45,0.96]:
                x,y,p,g=finite_chain(m,initial,left,right,r,s,z)
                assert math.isclose(x,y,rel_tol=6e-12,abs_tol=6e-12),(m,initial,left,right,r,s,z,x,y)
                assert 0<p<1 and g>0
                count+=1
    # closed-form continuum identities, independent numerically of matrix test.
    for a in [0.25,1.,5.]:
      for D in [0.1,1.,4.]:
        for r in [0.02,0.5,3.]:
          p,g=continuous_parameters(a,D,r)
          assert math.isclose(g/p, math.sinh(a*math.sqrt(r/D))/math.sqrt(D*r),rel_tol=1e-10)
          rate=(1-p)/g
          for n in range(5):
            lam=rate*(g/p)
            # Integrating conditional Poisson mass against exponential L.
            # int (p/g)e^{-(p/g+rate)L} (rate L)^n/n! dL
            # =p(1-p)^n.
            integ=(p/g)*rate**n/(p/g+rate)**(n+1)
            assert math.isclose(integ,p*(1-p)**n,rel_tol=1e-9,abs_tol=1e-12)
            count+=1
    print(f'PASS: {count} independent numerical checks')

if __name__=='__main__':main()
