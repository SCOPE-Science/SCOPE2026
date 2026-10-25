#!/usr/bin/env python3
"""Deterministic checks for active-inertial resetting tail calculation."""
import math
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.optimize import brentq

checks=0
def check(p,msg):
    global checks
    assert p,msg
    checks+=1

def lambda_top(k,a,dr,n=55):
    ii=np.arange(-n,n+1,dtype=float)
    return float(eigh_tridiagonal(-dr*ii*ii,
        np.full(2*n,k*a/2.0),
        select="i", select_range=(2*n,2*n),eigvals_only=True)[0])

def kstar(r,a,dr,D,n=55):
    return float(brentq(lambda k:D*k*k+lambda_top(k,a,dr,n)-r,
                       0.,math.sqrt(r/D)+1.,xtol=1e-12))

def g(t,tau):
    return t-2*tau*(-math.expm1(-t/tau))+0.5*tau*(-math.expm1(-2*t/tau))

def passive_Eg(r,tau):
    # Closed form avoids catastrophic cancellation at large r*tau.
    x=r*tau
    return (1./r)*(2./((1.+x)*(2.+x)))

for a in (0.,0.8,2.5):
  for dr in (.6,2.):
    for D in (.4,1.3):
      for r in (.03,0.7,8.,90.):
        k=kstar(r,a,dr,D)
        check(abs(D*k*k+lambda_top(k,a,dr)-r)<3e-8,"root equation")
        check(0<k<=math.sqrt(r/D)*(1+1e-9),"bound")
        check(abs(lambda_top(k,a,dr)-lambda_top(-k,a,dr))<1e-10,"evenness")
        check(abs(lambda_top(k,a,dr)-lambda_top(k,a,dr,70))<1e-8,
              "Fourier cutoff")
        check(lambda_top(k,a,dr)>=-1e-9,"positive eigenvalue")
        check(lambda_top(k,a,dr)<=a*abs(k)+1e-8,"Feynman-Kac bound")
        check(D*(.98*k)**2+lambda_top(.98*k,a,dr)<r,
              "mgf finite side")
        check(D*(1.02*k)**2+lambda_top(1.02*k,a,dr)>r,
              "mgf infinite side")

for tau in (.02,.2,1.,4.):
 for r in (.2,1.,10.,100.):
    from scipy.integrate import quad
    numeric=quad(lambda t:r*math.exp(-r*t)*g(t,tau),0.,np.inf,epsabs=5e-11)[0]
    analytic=passive_Eg(r,tau)
    check(abs(numeric-analytic)<max(2e-9,1e-5*analytic),"Gaussian variance")
    check(0<analytic<=1/r,"variance bound")
    check(0<analytic/(2./(tau*tau*r**3))<=1+1e-8,
         "high-frequency thermal envelope")

for tau in (.1,1.,3.):
 for r in (1e4,1e5,1e6):
    ratio=passive_Eg(r,tau)/(2./(tau*tau*r**3))
    check(abs(ratio-1)<3e-3,"cubic localization")
for a in (0.7,2.1):
  D=1.1;dr=.6
  for r in (1e-5,1e-4):
    k=kstar(r,a,dr,D)
    approx=math.sqrt(r/(D+a*a/(2*dr)))
    check(abs(k/approx-1)<2e-4,"weak resetting")
  for r in (1e4,1e5):
    k=kstar(r,a,dr,D)
    check(abs(k/math.sqrt(r/D)-1)<.015,"strong resetting")
print("PASS:",checks,"deterministic assertions.")
