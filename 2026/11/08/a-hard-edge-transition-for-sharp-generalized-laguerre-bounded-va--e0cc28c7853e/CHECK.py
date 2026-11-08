#!/usr/bin/env python3
"""Reproduce finite arithmetic checks for generalized Laguerre primitive extrema.
The infinite theorems are analytic and are NOT certified by these tests.
Dependencies: Python 3 with NumPy and SciPy.
"""
import math
import numpy as np
from scipy.special import eval_genlaguerre, roots_genlaguerre, jv
from scipy.optimize import brentq
from scipy.integrate import quad

checks = 0

def checked(test, description):
    global checks
    assert bool(test), description
    checks += 1


def F(n, alpha, x):
    return x ** (alpha + 1) * math.exp(-x) * eval_genlaguerre(n - 1, alpha + 1, x) / n


def Fprime(n, alpha, x):
    return x ** alpha * math.exp(-x) * eval_genlaguerre(n, alpha, x)


def E(n, alpha, x):
    return F(n, alpha, x) ** 2 + x * Fprime(n, alpha, x) ** 2 / n


def bessel_first_root(alpha):
    left = 1e-7
    right = left
    for _ in range(20000):
        right += 0.01
        if jv(alpha, left) * jv(alpha, right) < 0:
            return brentq(lambda z: jv(alpha, z), left, right, xtol=1e-13)
        left = right
    raise RuntimeError('No first Bessel zero located')


def constant(alpha):
    if alpha <= -0.5:
        j = bessel_first_root(alpha)
        return (j / 2) ** (alpha + 1) * abs(jv(alpha + 1, j))
    x = alpha + 0.5
    return math.exp(-x / 2) * x ** (alpha / 2 + 0.25) / math.sqrt(math.pi)

# Root-based exact maximum, the finite classification, and ODE/Sonin identities.
for alpha in [-0.9, -0.75, -0.5, -0.4, 0, 0.5, 1.5, 3.0]:
    for n in [1, 2, 3, 4, 8, 12, 20, 40]:
        nodes, _ = roots_genlaguerre(n, alpha)
        heights = np.abs([F(n, alpha, float(z)) for z in nodes])
        max_i = int(np.argmax(heights))
        if alpha <= -0.5:
            checked(max_i == 0, f'first-root extremum n={n}, a={alpha}')
            checked(all(heights[j] > heights[j+1]*(1-1e-9)
                        for j in range(n-1)), f'strict order n={n}, a={alpha}')
        else:
            center = alpha + 0.5
            nearest = {int(np.clip(np.searchsorted(nodes, center) - 1, 0, n - 1)),
                       int(np.clip(np.searchsorted(nodes, center), 0, n - 1))}
            checked(max_i in nearest, f'bracketing roots n={n}, a={alpha}')
        for x in [0.15, 0.37, 0.75, 1.33]:
            eps = 1e-5 * x
            d2f = (Fprime(n, alpha, x + eps) - Fprime(n, alpha, x - eps)) / (2 * eps)
            ode = d2f + (1-alpha/x)*Fprime(n,alpha,x)+(n/x)*F(n,alpha,x)
            checked(abs(ode) < 0.00004 * (1 + abs(Fprime(n,alpha,x)) + n*abs(F(n,alpha,x))),
                    f'ODE n={n}, a={alpha}, x={x}: {ode}')
            de = (E(n,alpha,x+eps)-E(n,alpha,x-eps))/(2*eps)
            target = (2*alpha+1-2*x)*Fprime(n,alpha,x)**2/n
            checked(abs(de-target) < 0.00005*(1+abs(target)),
                    f'Envelope n={n}, a={alpha}, x={x}: {de-target}')

# Independent numerical integral checks (not using the polynomial primitive identity).
for alpha in [-0.8, -0.5, 0.3, 2.0]:
    for n in [1, 2, 5, 12]:
        for x in [0.1, 0.75, 2.0]:
            area, err = quad(lambda t: math.exp(-t)*eval_genlaguerre(n,alpha,t),
                            0, x, weight='alg', wvar=(alpha,0), epsabs=1e-10, epsrel=1e-10)
            checked(abs(area-F(n,alpha,x))<1e-7*(1+abs(area)),
                    f'direct integral n={n}, alpha={alpha}, x={x}')

for alpha in [-0.9, -0.75, -0.5, 0.0, 0.7, 2.0]:
    n = 200
    nodes,_ = roots_genlaguerre(n, alpha)
    observed = max(abs(F(n, alpha, float(z))) for z in nodes)
    target = constant(alpha)
    scaled = n*observed if alpha <= -0.5 else n**(0.75-alpha/2)*observed
    checked(abs(scaled-target)/target < 0.07,
            f'asymptotic representative a={alpha}: computed={scaled}, target={target}')

checked(abs(constant(-0.5)-1/math.sqrt(math.pi)) < 1e-11,
        'critical Bessel continuity')
print('GENERALIZED_LAGUERRE_BV_CHECKS_PASSED', checks)
