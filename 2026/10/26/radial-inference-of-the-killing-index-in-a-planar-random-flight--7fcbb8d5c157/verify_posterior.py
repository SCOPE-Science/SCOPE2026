#!/usr/bin/env python3
"""Reproduce deterministic numerical checks for killed planar velocity-jump inference.

Requires Python 3, NumPy, SciPy. All checks are finite and do not certify
asymptotic or continuous-parameter theorems; see the accompanying proof.
"""
from math import exp, log, pi, sqrt
from scipy.integrate import quad
from scipy.special import gammaln, k0, kve, logsumexp
import numpy as np

checks = 0

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def log_count_density(n, radius, beta):
    if n < 1 or radius <= 0 or beta <= 0:
        raise ValueError('n positive, radius and beta strictly positive')
    nu = n / 2 - 1
    value = kve(nu, beta * radius)
    return ((n / 2 + 1) * log(beta) - (n / 2) * log(2) - log(pi)
            - gammaln(n / 2) + nu * log(radius)
            + log(value) - beta * radius)

def marked_density_series(z, radius, beta, p, count_max=220):
    q = 1 - p
    logs = [log(p) + (n-1) * log(q) + n*log(z)
            + log_count_density(n, radius, beta)
            for n in range(1, count_max+1)]
    return exp(logsumexp(logs))

def marked_density_decomposition(z, radius, beta, p):
    q = 1-p
    kappa = beta*sqrt(1-q*q*z*z)
    pole = p*q*z*z*beta*beta/pi * k0(kappa*radius)
    def integrand(t):
        u = sqrt(radius*radius + t*t)
        return (exp(-beta*q*z*t-beta*u)*t/(u*u)
                * (1+1/(beta*u)))
    integral, error = quad(integrand, 0, np.inf, epsabs=1.e-13,
                           epsrel=2.e-11, limit=200)
    remainder = p*z*beta*beta/(2*pi)*integral
    return pole+remainder, pole, remainder

def posterior_moments(radius, beta, p, count_max=250):
    q = 1-p
    ln = np.asarray([log(p)+(n-1)*log(q)+log_count_density(n, radius, beta)
                     for n in range(1,count_max+1)])
    mass = np.exp(ln-logsumexp(ln))
    ns = np.arange(1,count_max+1)
    mean = float(np.sum(ns*mass))
    variance = float(np.sum((ns-mean)**2*mass))
    return mean, variance, float(mass.sum())

# Density normalization for fixed killing index via radial integration.
for beta in (0.8, 1.3):
    for n in (1,2,3,5,8):
        mass, error = quad(lambda radius:
                           2*pi*radius*exp(log_count_density(n, radius, beta)),
                           0, 110/beta, epsabs=1e-11, epsrel=1e-10, limit=300)
        check(abs(mass-1) < 2e-9, f'density integrates to one: {n,beta,mass}')

# Compare two independent density formulas: geometric-Gamma/Bessel sum and
# inverse-Fourier pole plus positive relativistic Poisson-kernel remainder.
for p in (0.2, 0.35, 0.7):
    for beta in (0.8, 1.3):
        for radius in (0.4, 1.5, 3.0, 8.0):
            for z in (0.8, 1.0, 1.1):
                series = marked_density_series(z, radius, beta, p)
                full, pole, remainder = marked_density_decomposition(z, radius, beta, p)
                check(full > pole > 0 and remainder > 0,
                      f'positive inverse-Fourier components: {p,beta,radius,z}')
                check(abs(series/full-1) < 5e-10,
                      f'independent density evaluations: {p,beta,radius,z,series,full}')

# Finite witnesses for strict pairwise monotone likelihood ratios.
for beta in (0.8,1.3):
    radii = (0.7,2.5,5.0)
    for lo in range(1,8):
        for hi in range(lo+1,9):
            ratios = [log_count_density(hi,r,beta)-log_count_density(lo,r,beta)
                      for r in radii]
            for u,v in zip(ratios,ratios[1:]):
                check(v > u+1e-8, f'strict likelihood-ratio growth: {lo,hi,beta}')

# Asymptotic conditional moments, including order-one shifts.
p=0.35; beta=1.3; q=1-p; d=1-q*q
a=beta*q*q/sqrt(d)
b=beta*q*q*(2-q*q)/d**1.5
mean_shift=2+q*q/(2*d)
var_shift=q*q/d**2
for radius in (30.0,60.0,120.0):
    mean, variance, total = posterior_moments(radius,beta,p)
    check(abs(total-1)<1e-12, f'posterior probability normalization {radius}')
    check(abs(mean-(a*radius+mean_shift)) < 0.1/radius,
          f'conditional mean asymptotic {radius,mean,a*radius+mean_shift}')
    check(abs(variance-(b*radius+var_shift)) < 0.41/radius,
          f'conditional variance asymptotic {radius,variance,b*radius+var_shift}')

print(f'PASS: {checks} deterministic checks')
print('Model: independent uniform planar directions, geometric killing at rate-lambda events.')
print('Identity: Bessel-Gamma count-mixture sum equals positive pole-plus-kernel inversion.')
print('Finite checks: radial density normalization, strict sampled MLR, asymptotic conditional moments.')
print(f'Example p={p}, lambda/c={beta}: a={a:.12f}, b={b:.12f}, mean_shift={mean_shift:.12f}, var_shift={var_shift:.12f}')
print('LIMIT: finite calculations do not establish global MLR, Fourier inversion, or the limiting Gaussian law.')
