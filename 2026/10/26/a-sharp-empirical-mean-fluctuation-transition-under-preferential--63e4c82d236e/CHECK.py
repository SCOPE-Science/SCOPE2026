#!/usr/bin/env python3
"""Reproduce exact empirical-mean variance identities for preferential relocation.
Requires Python 3, NumPy and SciPy. No randomness is needed for the assertions.
"""
import math
import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.special import hyp1f1, exp1, gamma

EULER_GAMMA = 0.5772156649015328606065120900824
assertions = 0

def require(condition, message):
    global assertions
    assert bool(condition), message
    assertions += 1

def mean_integral_variance(mu, r, D, T):
    assert mu > 0 and r > 0 and D > 0 and T > 0
    ell = mu + r
    alpha = 2*r/ell
    z = ell*T
    if abs(alpha-1.0) <= 1.e-12:
        # E_1(z) = integral_z^infinity exp(-u)/u du.
        if z < 1.e-3:
            F = z/2 - z*z/12 + z*z*z/72 - z**4/480
        else:
            F = EULER_GAMMA + math.log(z) + exp1(z) - 1 - math.expm1(-z)/z
        return (2*D/(mu*ell*T))*F
    return (2*D/(mu*ell*(alpha-1)*T))*(hyp1f1(1-alpha, 2, -z)-1)

def independent_moment_ode(mu, r, D, T):
    ell = mu+r
    v = D/mu
    epsilon = 1.e-7
    def rhs(t, y):
        w,c = y
        return [2*c, -ell*c + v + r*w/t]
    sol=solve_ivp(rhs,[epsilon,T],[v*epsilon**2,v*epsilon],method='DOP853',
                  rtol=3.e-11,atol=1.e-12,max_step=.2)
    require(sol.success, 'moment ODE did not integrate')
    return sol.y[0,-1]/T**2

def long_time_leading(mu,r,D,T):
    ell=mu+r
    alpha=2*r/ell
    if r<mu:return 2*D/(mu*(mu-r)*T)
    if r==mu:return D/(mu**2*T)*math.log(2*mu*T)
    return (2*D*ell**(alpha-1)/(mu*(r-mu)*gamma(1+alpha)))*T**(alpha-2)

# Exact formula from the Laplace transform is checked against a separately
# integrated two-moment generator system, at positive parameter values.
for mu,r,D in [(1.,.25,1.3),(1.,.7,2.),(1.,1.,2.),
               (1.,1.5,.7),(1.,3.,1.),(2.,.5,1.),(2.,2.,1.),(2.,5.,1.)]:
    for T in [.1,.3,1.,3.,5.,12.,30.,80.]:
        x=mean_integral_variance(mu,r,D,T)
        y=independent_moment_ode(mu,r,D,T)
        require(math.isfinite(x) and x>0, 'invalid variance')
        require(abs(x-y)/x < 4.e-5, 'hypergeometric/ODE disagreement')

# Direct critical integral independent of special-function evaluation.
for T in [.1,.4,1,2,5,15]:
    mu=r=1.;D=1.7;ell=mu+r;z=ell*T
    direct,_=quad(lambda u: -math.expm1(-z*u)*(1-u)/u if u else z,
                  0,1,epsabs=1.e-12,epsrel=1.e-12)
    formula=mean_integral_variance(mu,r,D,T)*T*mu*ell/(2*D)
    require(abs(formula-direct)<2.e-9,'critical integral disagrees')

# Asymptotic ratios converge; the largest times probe the precise constants.
for mu,r,D in [(1.,.25,1.3),(1.,.7,2.),(1.,1.,2.),
               (1.,1.5,.7),(1.,3.,1.),(2.,.5,1.),(2.,2.,1.),(2.,5.,1.)]:
    ratios=[]
    for T in [1.e4,1.e6,1.e8]:
        ratio=mean_integral_variance(mu,r,D,T)/long_time_leading(mu,r,D,T)
        require(math.isfinite(ratio) and .60<ratio<1.05,'bad asymptotic regime')
        ratios.append(abs(1-ratio))
    require(ratios[-1]<ratios[0], 'asymptotic did not improve')

# The r->0 limit is ordinary stationary OU averaging, independently known.
for T in [.3,2.,10.]:
    mu=1.4;D=.9;r=1.e-7
    exact_ou=(2*D/mu**2)*(T-(1-math.exp(-mu*T))/mu)/T**2
    require(abs(mean_integral_variance(mu,r,D,T)-exact_ou)<4.e-6,
            'OU limit disagreement')

print(f'PASS: {assertions} deterministic assertions; analytic result also needs its written proof.')
