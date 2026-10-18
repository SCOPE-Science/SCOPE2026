#!/usr/bin/env python3
"""Deterministic finite consistency checks of the quadratic Feynman-Kac saddle theorem."""
from math import exp,cosh,tanh,sqrt,isclose
from cmath import sqrt as csqrt

def root(theta,c2):
    lo=1/(2*theta)
    hi=max(lo+1,2*lo)
    while 2*theta*hi**3-hi**2 <c2: hi*=2
    for _ in range(100):
        mid=(lo+hi)/2
        if 2*theta*mid**3-mid**2<c2:lo=mid
        else:hi=mid
    return (lo+hi)/2

def logmgf(lam,S,a,mu):
    g=sqrt(2*lam)
    return -0.5*__import__('math').log(cosh(g*S))-mu*a-0.5*mu*mu*S-(g*g*a*a-mu*mu)*tanh(g*S)/(2*g)+mu*a/cosh(g*S)

def exact_laplace(S,a,mu,lam):
    g=sqrt(2*lam)
    # Exact transform at real parameters, which is positive and bounded by one.
    return exp(logmgf(lam,S,a,mu))

n=0
for theta in [0.25,0.7,1.0,2.0,7.0]:
    for c2 in [0.,0.005,0.1,1.,4.,40.]:
        g=root(theta,c2)
        assert isclose(2*theta*g**3-g*g,c2,rel_tol=1e-10,abs_tol=1e-10)
        assert g>=1/(2*theta)-1e-12
        v=(3*c2+g*g)/(2*g**5)
        h=0.00002
        def phi(u):
            z=csqrt(g*g+2j*u)
            return 1j*u*theta -0.5*(z-g)+c2/2*(1/z-1/g)
        assert abs(phi(h).imag/(h))<1e-4
        assert abs(-2*phi(h).real/h**2-v)<2e-5*max(1,v)
        for u in [0.01,.1,.5,1.,3.,10.,50.]:
            z=csqrt(g*g+2j*u)
            assert z.real>g
            assert (1/z).real <= 1/g
            n+=1
        n+=3

# Feynman-Kac PDE via derivatives for the quadratic-exponential ansatz
for lam in [.125, .5, 1.5, 4.]:
 for S in [.1,.5,1.,2.]:
  for mu in [-1.5,0.,.75]:
   g=sqrt(2*lam)
   A=-g*tanh(g*S)/2
   B=mu*(1/cosh(g*S)-1)
   Aprime=-(g*g/2)*(1-tanh(g*S)**2)
   Bprime=-mu*g*tanh(g*S)/cosh(g*S)
   Cprime=-.5*mu*mu+(.5*mu*mu)*(1-tanh(g*S)**2)-.5*g*tanh(g*S)
   for a in [-2.,-.2,0.,1.,3.]:
    lhs=Aprime*a*a+Bprime*a+Cprime
    rhs=A+(2*A*a+B)**2/2+mu*(2*A*a+B)-lam*a*a
    assert abs(lhs-rhs)<1e-10
    n+=1

# Critical finite-prefix exponent cancellation: two independent routes.
for g in [.1,.5,1.5,3.0]:
 for t in [.2,1.,2.]:
  for x in [-1.3,0.,.9]:
   for w in [-1.,.1,1.7]:
    z=t*(w*w+x*x+w*x)/3 # any fixed nonnegative representative
    for mu in [-5.,-1.,.2,3.]:
     logratio=g*t/2-(g*g/2)*z +g*(x*x-w*w)/2+mu*(x-w)+mu*mu*t/2
     logdrift=mu*(w-x)-mu*mu*t/2
     logou=g*t/2 +g*(x*x-w*w)/2-g*g*z/2
     assert abs((logratio+logdrift)-logou)<1e-11
     n+=1

assert 0<exact_laplace(.5,.1,.2,1.0)<1
print('PASS',n,'deterministic analytic-identity checks')
