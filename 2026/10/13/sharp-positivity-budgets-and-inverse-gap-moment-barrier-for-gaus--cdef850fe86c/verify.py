#!/usr/bin/env python3
"""Independent checks for a fixed-vector Gaussian sketched Ritz distribution.

Requires numpy >=1.24 and scipy >=1.10. All numerical tests support, not
replace, the exact analytical argument supplied in RESULT.md.
"""
from fractions import Fraction
from math import gamma, sqrt, pi, log
import numpy as np
from scipy.special import betainc
from scipy.stats import t, norm
from scipy.integrate import quad

# A rational two-eigenvalue extremizer: eigenvalues 1 and 9; squared weights 9/10, 1/10.
a, b = Fraction(1), Fraction(9)
w = Fraction(9,10)
mu = w*a + (1-w)*b
variance = w*a*a + (1-w)*b*b - mu*mu
assert mu == Fraction(9,5)
assert variance == Fraction(144,25)
assert mu*mu/variance == Fraction(9,16)
assert Fraction(2,1)*Fraction(3,1)/Fraction(8,1) == Fraction(3,4)
assert (b-a)**2/(4*a*b) == variance/(mu*mu)
checks=5

# Exact Beta relation versus an independently implemented Student-t tail.
for kappa in (1.25, 2., 3., 9., 50.):
    x=((kappa-1)/(kappa+1))**2
    for s in (2,3,4,5,8,12,24,50):
        via_beta=0.5*betainc(s/2,0.5,x)
        via_t=t.sf(2*sqrt(s*kappa)/(kappa-1),s)
        assert abs(via_beta-via_t) < 8e-13 * max(1.,via_t)
        checks+=1
assert abs(.5*betainc(1.,.5,(8/10)**2)-.2)<1e-15
checks+=1

# Exact inverse-mean divergence has a universal local density coefficient.
s=2
mu_f=float(mu)
sig=sqrt(float(variance))
evals=[1.,9.]
def density(z):
    return (gamma((s+1)/2)/(sqrt(pi)*gamma(s/2)) *sig**s
            / ((z-mu_f)**2+sig**2)**((s+1)/2))
for z in (-5.,0.,1.,5.,9.,15.):
    assert abs(density(z)-t.pdf((z-mu_f)*sqrt(s)/sig,s)*sqrt(s)/sig)<1e-14
    checks+=1
coefficient=2*sum(max(abs(lam-x) for x in evals)*density(lam) for lam in evals)
assert coefficient>0

def regularized_condition(z,h):
    gaps=[abs(z-lam) for lam in evals]
    return max(gaps)/max(h,min(gaps))

def expected_condition(h):
    knots=[-np.inf,1-h,1.,1+h,5.,9-h,9.,9+h,np.inf]
    val=0.
    for lo,hi in zip(knots[:-1],knots[1:]):
        v,e=quad(lambda z: regularized_condition(z,h)*density(z),lo,hi,
                 epsabs=2e-10,epsrel=1e-10,limit=250)
        assert e<2e-7
        val+=v
    return val
v1=expected_condition(1e-3)
v2=expected_condition(1e-5)
log_coefficient=(v2-v1)/log(100.)
assert abs(log_coefficient/coefficient-1)<0.005,(log_coefficient,coefficient)
checks+=1

# Fixed-kappa large-s sharp prefactor from endpoint Laplace analysis.
kap=3.
r=(kap-1)/(kap+1)
expected_const=(kap+1)/(2*sqrt(2*pi*kap))
for s in (250,400,600):
    p=.5*betainc(s/2,.5,r*r)
    ratio=sqrt(s)*p/(r**s)
    assert abs(ratio/expected_const-1)<0.03,(s,ratio,expected_const)
    checks+=1

# Sharp high-kappa confidence budget: no closed-form inversion of the beta needed.
def budget(kappa,delta):
    for s in range(2,3000):
        p=.5*betainc(s/2,.5,((kappa-1)/(kappa+1))**2)
        if p<=delta:
            return s
    raise AssertionError('budget exceeded')
critical=norm.isf(.05)**2/4
for kap in (100.,1000.):
    ss=budget(kap,.05)
    assert abs(ss/kap-critical)<.065,(kap,ss,critical)
    checks+=1

# Direct random matrix construction, not a call to the t random variate generator.
rng=np.random.default_rng(20261009)
u=np.array([3.,1.])/sqrt(10)
A=np.diag([1.,9.])
for s in (2,4,8,20):
    n=80000
    # G is independent across trials; theta computed from the two sketched vectors.
    G=rng.standard_normal((n,s,2))/sqrt(s)
    gu=G @ u
    gAu=G @ (A@u)
    theta=np.einsum('ij,ij->i',gu,gAu)/np.einsum('ij,ij->i',gu,gu)
    z=(theta-mu_f)*sqrt(s)/sig
    # Independent Student-t reference: probability at several quantiles.
    for target in (-1.5,0.,1.5):
        empirical=float(np.mean(z<=target))
        theoretical=float(t.cdf(target,s))
        assert abs(empirical-theoretical)<0.012,(s,target,empirical,theoretical)
        checks+=1
    empirical_sign=float(np.mean(theta<=0))
    predicted=float(t.cdf(-mu_f*sqrt(s)/sig,s))
    assert abs(empirical_sign-predicted)<0.012,(s,empirical_sign,predicted)
    checks+=1
print('VERIFY_OK',checks,'independent numerical/algebraic checks',
      'log_coefficient',coefficient, 'observed',log_coefficient)
