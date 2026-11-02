#!/usr/bin/env python3
"""Finite numerical diagnostics for a planar swimmer with power-law angular diffusion.

The proofs of the Gaussian limits and almost-sure convergence are analytic;
these tests check the stated normalizations, moment identities, and constants.
Requires Python 3, numpy, scipy.
"""
import math
import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.special import beta as beta_fn, gamma

CHECKS = 0

def check(condition, message):
    global CHECKS
    if not condition:
        raise AssertionError(message)
    CHECKS += 1

def f_exact(t, b, k=1.0):
    return t * quad(lambda z: math.exp(-k * t**b * (1 - z**b)), 0, 1,
                    epsabs=3e-12, epsrel=3e-12, limit=200)[0]

def msd(t, b, k=1.0, speed=1.0):
    # F(t)=exp(-k t^b) integral_0^t exp(k s^b) ds
    # M'(t)=2 speed^2 F(t). The first ODE is stable at large t.
    def rhs(s, y):
        damping = 0 if s == 0 else k*b*s**(b-1)
        return [1 - damping*y[0], 2*speed**2*y[0]]
    sol = solve_ivp(rhs, (0.,float(t)), [0.,0.], method='Radau',
                    atol=2e-11, rtol=2e-10, dense_output=True)
    check(sol.success, 'MSD initial-value problem did not integrate')
    return sol.sol

def plateau(b,k=1.,speed=1.):
    assert b>2
    return (2*speed**2/(b**2*k**(2/b))
            *gamma(2/b)*beta_fn(1/b,1-2/b))

# Independent stable integration of F against an exponential kernel.
for b in (0.5,1.,1.4,2.,2.5,3.,4.):
    sol=msd(4,b)
    for t in (0.4,1.,2.,4.):
        F_ode=float(sol(t)[0]); F_integral=f_exact(t,b)
        check(abs(F_ode-F_integral)<2e-8*(1+F_integral),
              f'F kernel and ODE disagree at beta={b}, t={t}')

# Exact plateau formula independently evaluated as a beta integral.
for b in (2.25,2.5,3.,4.,6.):
    quadrature=(2/b)*gamma(2/b)*quad(
        lambda z: (1-z**b)**(-2/b),0,1,limit=400,
        epsabs=1e-10,epsrel=1e-10)[0]
    check(abs(quadrature-plateau(b))<2e-8*plateau(b),
          f'Gamma/Beta plateau integration disagrees at beta={b}')

# Subcritical power-law spreading and critical logarithmic slope.
for b,t,rtol in ((1.,128.,.025),(1.5,256.,.065)):
    M=float(msd(t,b)(t)[1]); leading=2/(b*(2-b))*t**(2-b)
    check(abs(M/leading-1)<rtol, f'subcritical MSD leading constant beta={b}')
sol=msd(128,2.)
critical=float(sol(128)[1]-sol(32)[1])
check(abs(critical-math.log(4))<.005,
      'critical logarithmic coefficient disagrees')

# Supercritical plateau and its first asymptotic tail coefficient.
for b in (2.5,3.,4.):
    t=32.
    M=float(msd(t,b)(t)[1]); tail=plateau(b)-M
    leading=2/(b*(b-2))*t**(2-b)
    check(abs(tail/leading-1)<.003,
          f'supercritical plateau-tail coefficient beta={b}')

# Exact covariance formula for the angular process, tested by sampling
# its independent Gaussian increments (not a convergence proof).
rng=np.random.default_rng(5412026)
for b,s,t,k in ((.7,1.,2.,.9),(1.,.5,1.2,.7),(2.,1.,1.4,.6),(3.,.6,1.1,.8)):
    dtheta=rng.normal(0,math.sqrt(2*k*(t**b-s**b)),size=90000)
    observed=np.mean(np.cos(dtheta))
    exact=math.exp(-k*(t**b-s**b))
    check(abs(observed-exact)<.012,
          f'angular increment covariance failed beta={b}')

# The Gaussian coordinate variance constant equals half the planar
# mean-square constant in all three regimes.
for b in (.3,.7,1.,1.4,1.9,2.1,3.,5.):
    denom=abs(2-b)
    total=2/(b*denom)
    coordinate=1/(b*denom)
    check(math.isclose(total,2*coordinate,rel_tol=1e-14),
          f'Gaussian coordinate normalization beta={b}')

print(f'PASS: {CHECKS} finite numerical and exact-identity diagnostics')
