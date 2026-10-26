#!/usr/bin/env python3
"""Reproducible numerical checks for Gamma-radial Poisson-restart quantile clocks."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import gamma, gammainc, kv

passes = 0

def check(ok, message):
    global passes
    if not ok:
        raise AssertionError(message)
    passes += 1

def phi(beta, z):
    return z**beta * kv(beta, z)/(2**(beta-1)*gamma(beta))

def zcritical(beta, q):
    return brentq(lambda z: phi(beta, z) - (1-q), 1e-7, 30,
                  xtol=2e-14)

def ffree(beta, a, t):
    return gammainc(beta, a/t)

def stationary(beta, a, r):
    return 1-phi(beta, 2*math.sqrt(a*r))

def excess(beta, a, r, t):
    return a**beta/gamma(beta)*quad(
        lambda u: math.exp(-r*u-a/u)*u**(-beta-1),
        t, math.inf, epsabs=1e-13, epsrel=1e-12)[0]

def log_excess_dimensionless(beta, a, rc, eps, x):
    # Stable at very small critical distances: remove the tiny e^(-x) factor.
    integral = quad(lambda w: math.exp(-(1-eps)*w-a*rc/(x+w))
                    *(1+w/x)**(-beta-1), 0, 150,
                    epsabs=1e-13, epsrel=1e-12)[0]
    return beta*math.log(a*rc)-math.lgamma(beta) - (1-eps)*x \
        - (beta+1)*math.log(x)+math.log(integral)

# Radial density from the Fokker--Planck fundamental solution.
for alpha in [0, 0.2, 0.5, 0.8, 1.0]:
    beta = 1-alpha/2
    for t in [0.2, 1.0, 3.0]:
        a=1/16
        D=1
        R=1
        density = lambda rho: (4*rho**(2-2*alpha) /
            (gamma(beta)*(16*D*t)**beta)) * math.exp(-rho**4/(16*D*t))
        numeric = quad(lambda rho: rho*density(rho), 0, R,
                       epsabs=1e-11, epsrel=1e-11)[0]
        check(abs(numeric-ffree(beta, a, t))<3e-10,
              'radial Gamma normalization')

for beta in [.5, .75, 1.0]:
    z = zcritical(beta, .5)
    rc = z*z/4 # a=1 here
    H=z**(beta-1)/(2**beta*kv(beta-1, z))
    C=z**(beta+1)*kv(beta-1,z)/(2**beta*gamma(beta))
    B=rc**beta/gamma(beta)
    check(abs(B/C-H)<2e-12,'exact intercept identity')
    check(abs(stationary(beta,1,rc)-.5)<1e-12,'critical quantile root')
    for r in [.3*rc, .7*rc, 1.1*rc]:
        # Stationary law independently as the exponential-age mixture.
        mixture = r*quad(lambda t: math.exp(-r*t)*ffree(beta,1,t),
                         0, math.inf, epsabs=1e-11, epsrel=1e-11)[0]
        check(abs(mixture-stationary(beta,1,r))<2e-9,
              'Bessel stationary law vs independent mixture')
        for t in [.3, 1., 3.]:
            direct=math.exp(-r*t)*ffree(beta,1,t)+r*quad(
                lambda u: math.exp(-r*u)*ffree(beta,1,u),0,t,
                epsabs=2e-11,epsrel=2e-11)[0]
            check(abs(direct-stationary(beta,1,r)-excess(beta,1,r,t))<2e-9,
                  'independent reset-renewal quadrature')

    # The normalized sharp-crossing error tends to zero for a sequence
    # approaching criticality; only finite numerical cases are checked.
    errors=[]
    for k in [9,20,40,80]:
        eps = 10.**(-k)
        L = math.log(1/eps)
        approx = L-(beta+1)*math.log(L)+math.log(H)
        # For very small eps use the first derivative C*eps of the
        # stationary deficit; its relative error is O(eps).
        x=brentq(lambda x:log_excess_dimensionless(beta,1,rc,eps,x)
                    -math.log(C*eps),.1,300,xtol=2e-12)
        errors.append(abs(x-approx))
        check(abs(x-approx)<.6,'critical clock finite-error envelope')
    check(all(errors[j+1]<errors[j] for j in range(len(errors)-1)),
          'nested-log convergence trend')

# Strict ordering across stochastic conventions and two distinct quantiles.
for q in [.25,.5,.75]:
    zs=[zcritical(beta,q) for beta in [.5,.75,1]]
    check(zs[0]<zs[1]<zs[2],'critical rate increases with Gamma shape')
print(f'PASS: {passes} independent finite numerical assertions')
