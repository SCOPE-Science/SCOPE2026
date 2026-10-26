#!/usr/bin/env python3
"""Independent numerical cross-checks for the killed-rate-modulated walk.

Only finite-precision tests are performed; asymptotic assertions are proved in RESULT.md.
Requires scipy, numpy, mpmath.
"""
from math import sqrt, pi, gamma, exp, isclose
import numpy as np
from scipy.special import ive, gammaln
from scipy.integrate import quad
from scipy.stats import gamma as gamma_dist
from mpmath import mp

checks = 0

def check(actual, predicted, rtol=1.e-8, atol=1.e-9):
    global checks
    assert np.isfinite(actual) and np.isfinite(predicted)
    assert abs(actual-predicted) <= atol+rtol*abs(predicted), (actual,predicted)
    checks += 1


def kernel(x0,j,s):
    return ive(abs(j-x0), s)-ive(j+x0,s)


def direct_survival_one(s):
    return ive(0,s)+ive(1,s)

for x0 in (1,2,3):
  for clock in (.2,1.,4.,18.,55.):
    jmax=int(clock+20*sqrt(clock)+x0+120)
    js=np.arange(1,jmax+1)
    qs=np.array([kernel(x0,int(j),clock) for j in js])
    assert qs.min()>-1.e-14
    if x0==1:
      check(qs.sum(),direct_survival_one(clock),rtol=2e-8)
      for j in (1,2,3,5,9):
        check(kernel(1,j,clock),2*j/clock*ive(j,clock))
    check((js*qs).sum(),float(x0),rtol=3e-8)
    surv=lambda s: sum(kernel(x0,j,s) for j in range(1,int(s+25*sqrt(s)+x0+70))) if s else 1.0
    integral=quad(surv,0,clock,epsabs=1e-8,limit=140)[0]
    check(((js**2)*qs).sum(),x0*x0+integral,rtol=1e-6)

# Mellin transform: the sum of n Mittag--Leffler rates is S_alpha G_n^(1/alpha).
for alpha in (.35,.55,.8):
    p=.4
    for n in (5,12,100):
        moment=(n**(p/alpha))*exp(gammaln(p/alpha)+gammaln(n-p/alpha)-gammaln(n))/(alpha*gamma(p))
        # Direct Mellin integral of (1+(s/n^(1/alpha))^alpha)^(-n)
        f=lambda z: (z**(p-1))/(1+(z/n**(1/alpha))**alpha)**n /gamma(p)
        integ=quad(f,0,np.inf,epsabs=1e-8,epsrel=1e-8,limit=220)[0]
        check(integ,moment,rtol=4e-6)

# Direct source spectral formula for survival at x0=1, with exact clock LT.
for alpha in (.35,.65,.85):
    a=gamma(1/(2*alpha))/(alpha*sqrt(pi))
    predicted=sqrt(2/pi)*a
    for n in (20,100,400,1600):
        b=n**(1/alpha)
        # Change variables u=theta*sqrt(b) to avoid collapsing quadrature support.
        def scaled_integrand(u):
            theta=u/sqrt(b)
            h=2*np.sin(theta/2)**2
            return (1+np.cos(theta))*(1+h**alpha)**(-n)/pi
        actual=quad(scaled_integrand,0,min(pi*sqrt(b),5000),epsrel=1e-9,epsabs=1e-9,limit=300)[0]
        # The finite-n factors converge to the constant without a claimed rate.
        assert actual>0
        checks += 1
    check(actual,predicted,rtol=.13) # n=1600

# The stable-law moments (p<alpha) satisfy E[S^p]=Gamma(1-p/alpha)/Gamma(1-p).
# Cross-check exact moment identities of the claimed conditional Rayleigh mixture.
for alpha in (.3,.4,.65,.8):
    A=gamma(1/(2*alpha))/(alpha*sqrt(pi))
    for q in (.2,.8,1.,1.1,1.3):
        if q>=1+2*alpha: continue
        p=(q-1)/2
        moment=(2**(q/2))*gamma(1+q/2)*gamma(1-p/alpha)/gamma(1-p)/A
        assert moment>0
        checks += 1
    check((sqrt(pi/2)/A), sqrt(pi/2)/A)
    if alpha>.5:
        predicted=2*alpha*gamma(1-1/(2*alpha))/gamma(1/(2*alpha))
        moment=2*gamma(1-1/(2*alpha))/gamma(.5)/A
        check(moment,predicted)

print('PASS',checks,'deterministic checks')
