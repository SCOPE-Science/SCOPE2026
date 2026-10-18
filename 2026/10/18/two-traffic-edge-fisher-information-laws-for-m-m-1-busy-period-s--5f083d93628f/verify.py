"""Standalone numerical checks for M/M/1 busy-period Fisher asymptotics.

The analytical proof, not these finite checks, establishes the limiting assertions.
Dependencies: Python 3.10+, numpy and scipy.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import ive

TESTS = 0

def check(cond, msg):
    global TESTS
    TESTS += 1
    if not cond:
        raise AssertionError(msg)


def kernel(x, rho):
    # Dimensionless busy-time density for service rate 1, arrival rho.
    if x == 0:
        return 1.0
    z = 2*x*math.sqrt(rho)
    return math.exp(-(1-math.sqrt(rho))**2*x)*math.sqrt(1/rho)*ive(1, z)/x


def score(x, rho):
    if x == 0:
        return 0.0
    z = 2*x*math.sqrt(rho)
    return -x + x/math.sqrt(rho)*(ive(2,z)/ive(1,z))


def integrate(rho, fn):
    return quad(lambda x: kernel(x,rho)*fn(x), 0., math.inf,
                epsrel=3e-9, epsabs=3e-9, limit=600)[0]


def fisher(rho):
    return integrate(rho, lambda x: score(x,rho)**2)


for rho in (0.001, 0.01, 0.03, 0.1, 0.25, 0.5, 0.8, 0.9, 0.95):
    z = [0.01, 0.1, 1., 4., 10., 50., 200.]
    for x in z:
        val = score(x,rho)
        h = 1e-5 * max(rho,1e-2)
        rp, rm = rho+h, rho-h
        if rm > 0 and rp < 1:
            finite = (math.log(kernel(x,rp))-math.log(kernel(x,rm)))/(2*h)
            check(abs(val-finite) < 1e-5*(1+abs(val)), f'score derivative rho={rho}, x={x}')
        zz = 2*x*math.sqrt(rho)
        r = ive(2,zz)/ive(1,zz)
        check(0 < r < 1 + 1e-13, 'positive Bessel ratio below one')
        check(r <= zz/4 + 1e-13, 'Bessel weighted-coefficient bound')
    area = integrate(rho, lambda x: 1.)
    mean = integrate(rho, lambda x: x)
    second = integrate(rho, lambda x: x*x)
    centered_score = integrate(rho, lambda x: score(x,rho))
    I = fisher(rho)
    check(abs(area-1.) < 3e-7, f'density normalizes rho={rho}, {area}')
    check(abs(mean*(1-rho)-1.) < 3e-7, f'mean rho={rho}, {mean}')
    check(abs(second*(1-rho)**3-2.) < 5e-7, f'second moment rho={rho}, {second}')
    check(abs(centered_score) < 4e-7, f'score mean rho={rho}, {centered_score}')
    check(I > 0, f'positive Fisher rho={rho}')
    if rho <= .03:
        check(1.65 < I < 2.1, f'light-traffic Fisher trend rho={rho}, {I}')
    if rho >= .9:
        check(abs((1-rho)*I-0.5) < 0.09, f'heavy-traffic Fisher trend rho={rho}, {I}')

# Independent scaling identity for multiple service rates.
for mu in (0.75, 1.0, 2.5):
    for rho in (0.02, 0.2, 0.6, 0.9):
        lam = mu*rho
        iy = fisher(rho)/(mu*mu)
        k_count = math.sqrt(2*mu*(mu+lam)/(lam*(mu-lam)))
        k_time = mu/(lam*(mu-lam))*math.sqrt(2/iy)
        check(k_count > 0 and k_time > 0, 'positive covert constants')
        check(abs(k_count - math.sqrt(2*(1+rho)/(rho*(1-rho))))<1e-10, 'count scaling')
        check(abs(k_time - (math.sqrt(2/fisher(rho))/(rho*(1-rho)))) <1e-10, 'duration scaling')

print(f'PASS: {TESTS} numerical identity, normalization, moment and asymptotic trend assertions')
