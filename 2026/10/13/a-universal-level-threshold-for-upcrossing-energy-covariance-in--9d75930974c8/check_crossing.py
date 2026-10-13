#!/usr/bin/env python3
"""Numerical checks of the Gaussian level-upcrossing/energy covariance formula.
Dependencies: numpy, scipy. No external data or network access needed.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import ndtr
from scipy.optimize import brentq
from scipy.stats import norm

def phi(x):
    return math.exp(-x*x/2)/math.sqrt(2*math.pi)

def pair_formula(a,rho):
    s=math.sqrt(1-rho*rho)
    h=a*(1-rho)/s
    return phi(a)*(a*(1+rho*rho)*(2*ndtr(h)-1)-2*rho*s*phi(h))

def full_formula(n,a,rho,sigma=1):
    return sigma*sigma*pair_formula(a,rho)*sum(1-rho**(2*r) for r in range(1,n))/(1-rho*rho)

def pair_integral(a,rho):
    s=math.sqrt(1-rho*rho)
    l=quad(lambda x: (x*x-1)*phi(x)*ndtr((rho*x-a)/s), -np.inf,a,epsabs=1e-12)[0]
    r=quad(lambda y: (y*y-1)*phi(y)*ndtr((a-rho*y)/s),a,np.inf,epsabs=1e-12)[0]
    return l+r

checks=0
for rho in (-.88,-.65,-.2,0,.05,.3,.71,.93):
    for a in (-2.3,-.7,0,.1,.4,1,2.2):
        f=pair_formula(a,rho)
        q=pair_integral(a,rho)
        assert abs(f-q)<2e-10,(rho,a,f,q)
        checks+=1
        assert abs(pair_formula(a,rho)-pair_formula(-a,rho))<1e-13
for rho in np.linspace(.01,.99,41):
    root=brentq(lambda a: pair_formula(a,rho),0,2,xtol=2e-14)
    b=rho*(1+rho)/(1+rho*rho)
    assert 0<root**2<=b+1e-11<1.000001
    for a in (0,root*.45,root*.999,root*1.001,1,1.4,5):
        sign=np.sign(pair_formula(a,rho))
        assert sign==(-1 if a<root else 1),(rho,a,root,sign)
        checks+=1
# Longitudinal Monte Carlo on a generated AR1 sample; tolerances are conservative.
rng=np.random.default_rng(20261008)
M=250000
for n,rho,a,sigma in ((2,.5,0.,1.3),(5,.7,.4,2.1),(8,-.5,.2,1.),(7,0.,1.,1.5),(6,.91,1.4,.8),(9,.22,-.5,1.)):
    z=rng.standard_normal((M,n))
    x=np.empty_like(z)
    x[:,0]=sigma*z[:,0]
    s=math.sqrt(1-rho*rho)
    for k in range(1,n):x[:,k]=rho*x[:,k-1]+s*sigma*z[:,k]
    c=((x[:,:-1]<=a*sigma)&(x[:,1:]>a*sigma)).sum(axis=1)
    q=np.square(x).sum(axis=1)
    cov=np.mean((c-c.mean())*(q-q.mean()))
    expected=full_formula(n,a,rho,sigma)
    se=np.std((c-c.mean())*(q-q.mean()),ddof=1)/math.sqrt(M)
    assert abs(cov-expected)<6.5*se+0.02,(n,rho,a,cov,expected,se)
    print(f'n={n} rho={rho:g} a={a:g}: simulated={cov:.5f}, analytic={expected:.5f}, error={cov-expected:+.5f}, SE={se:.5f}')
    checks+=1
print(f'PASS: {checks} deterministic and randomized checks.')
