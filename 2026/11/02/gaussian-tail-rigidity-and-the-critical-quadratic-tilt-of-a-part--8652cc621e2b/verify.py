#!/usr/bin/env python3
"""Deterministic and seeded checks for the harmonic partial-reset moment/tail theorem.

Requires Python 3.10+ standard library only. Assertions are bounded checks,
not substitutes for the analytical proof of asymptotic statements.
"""
import math
import random
from fractions import Fraction

CHECKS = 0

def close(x, y, tol):
    global CHECKS
    CHECKS += 1
    if not (math.isfinite(x) and math.isfinite(y) and abs(x-y) <= tol*max(1,abs(y))):
        raise AssertionError((x, y, tol))

def log_p(a,beta, terms=1200):
    return -sum(math.log1p(-beta*a**(2*j)/(j+beta)) for j in range(1,terms+1))

def exact_normalized_nmoment(a,beta,n):
    # Conditional-Gaussian identity, M_{2n}/[(2n-1)!! sigma^{2n}].
    return math.exp(-sum(math.log1p(beta*(1-a**(2*j))/j) for j in range(1,n+1)))

def monte_carlo_variance(a,beta,samples=50000,steps=55):
    rng = random.Random(20261031 + int(100*a)+int(beta*100))
    s1=s2=s3=gap=0.0
    for _ in range(samples):
        v=0.0
        for j in range(steps):
            u=rng.random()**(1/beta)  # e^{-2*kappa*T}
            v=1-u+a*a*u*v
        s1+=v; s2+=v*v; s3+=v*v*v
        gap+=(1-a*a*v)**(-beta)
    return s1/samples,s2/samples,s3/samples,gap/samples

# Exact rational generator recurrence (kappa=D=r=1,a=1/2).
M = Fraction(1)
for n in range(1,13):
    M *= Fraction(2*n*(2*n-1),1)/(Fraction(2*n+1,1)-Fraction(1,4**n))
    # Separate product of n factors checks the stationary recurrence.
    product = Fraction(math.factorial(2*n),1)
    for j in range(1,n+1):
        product /= Fraction(2*j+1,1)-Fraction(1,4**j)
    assert M == product
    CHECKS += 1

for a,beta in [(0.0,0.4),(0.2,0.7),(0.5,0.8),(0.7,1.3),(0.8,3.0)]:
    # Exact Gamma specialization for complete resets.
    for n in (1,2,3,5,10,20):
        if a == 0:
            gamma_value=math.exp(math.lgamma(1+beta)+math.lgamma(n+1)-math.lgamma(n+1+beta))
            close(exact_normalized_nmoment(a,beta,n),gamma_value,1e-12)
    # Algebraic high-moment asymptotics and convergent product.
    for n,tol in ((5000,.0025),(20000,.00065)):
        v=exact_normalized_nmoment(a,beta,n)
        asym=math.exp(math.lgamma(1+beta)+log_p(a,beta)-beta*math.log(n))
        close(v,asym,tol)

# Poisson-backward variance perpetuity: independent numerical construction.
for a,beta in [(0.0,.75),(.25,.7),(.5,.8),(.7,1.4)]:
    mean,m2,m3,ampl=monte_carlo_variance(a,beta,samples=35000,steps=50)
    for n,v in enumerate((mean,m2,m3),start=1):
        close(v,exact_normalized_nmoment(a,beta,n),.02)
    close(ampl,math.exp(log_p(a,beta)),.02)

# For complete resets, integrate the Gaussian mixture density using the
# uniform representation U=T^(1/beta), and compare with tail asymptotics.
for beta in (.7,1.25,2.0):
    for z in (100.0,180.0):
        ns=40000
        S=0.0
        for k in range(ns):
            t=(k+.5)/ns
            u=t**(1/beta)
            S+=(1-u)**(-.5)*math.exp(-z*u/(1-u))
        scaled=S/ns
        asym=math.gamma(beta+1)*z**(-beta)
        close(scaled,asym,.035)

# Endpoint exponential-square moment exists exactly for beta>1/2.
for beta in (.6,.75,1.0,2.0):
    close(beta/(beta-.5),beta*math.gamma(beta-.5)/math.gamma(beta+.5),1e-12)

print('PASS:', CHECKS, 'bounded numerical / rational checks; all asymptotic claims require proof.')
