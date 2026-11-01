#!/usr/bin/env python3
"""Finite checks of the analytic eigenvector and boundary-asymptotic identities."""
import cmath
import math

N_CHECKS = 0

def check(ok, msg):
    global N_CHECKS
    N_CHECKS += 1
    if not ok:
        raise AssertionError(msg)


def coefficients(a, c, theta, r, terms):
    lam = r * (a * cmath.exp(-1j * theta) + c * cmath.exp(1j * theta))
    arr = [1 + 0j]
    prev = 0j
    for n in range(terms - 1):
        nxt = (n + 2) * (lam * arr[-1] - c * prev) / (a * (n + 1))
        prev = arr[-1]
        arr.append(nxt)
    return lam, arr


def c_real_q(q):
    # a=1, theta=0, c=q: exact Gamma expression for real exponents.
    gamma = (2 - q) / (1 - q)
    s = 1 / (1 - q)
    kappa = (1 + q) / (1 - q)
    h0 = (1 - q) ** (-(3 - gamma))
    return math.sqrt(math.gamma(2 * s) / math.gamma(gamma) ** 2 / (2 * kappa) ** (2 * s) * h0**2)


def norm(arr):
    return math.sqrt(sum(abs(v) ** 2 / (j + 1) for j, v in enumerate(arr)))


def run():
    for q in (-0.4, 0, 0.25):
        C = c_real_q(q)
        s = 1 / (1 - q)
        observed = []
        for eps in (0.007, 0.002, 0.0006):
            r = 1 - eps
            _, f = coefficients(1, q, 0, r, int(27 / eps))
            v = norm(f) / (C * eps ** (-s))
            observed.append(v)
            check(math.isfinite(v) and v > 0, 'finite positive asymptotic ratio')
            if q == 0:
                check(abs(norm(f) - 1 / (1 - r*r)) < 1e-8 * norm(f), 'exact monomial norm')
        check(abs(observed[-1] - 1) < abs(observed[0] - 1), 'ratio approaching one')
        check(abs(observed[-1] - 1) < 0.06, 'sharp coefficient close to one')
        print('real q=', q, 'observed norm ratios=', [round(x, 6) for x in observed])
    # An independent ODE residual check with a nonreal perturbation.
    a, c, theta, r = 1, 0.23 + 0.19j, 0.73, 0.72
    lam, f = coefficients(a, c, theta, r, 300)
    for n in range(1, 299):
        residual = a * (n+1) * f[n+1] - (n+2) * lam * f[n] + c * (n+2) * f[n-1]
        check(abs(residual) < 1e-11 * (1 + abs(f[n])), 'ODE coefficient residual')
    # The boundary power exponent must have the predicted extrema and angular mean.
    rho = 0.42 * cmath.exp(0.37j)
    values = [((1 / (1 - rho * cmath.exp(2j * theta))).real) for theta in
              [math.pi * j / 20000 for j in range(40000)]]
    check(abs(sum(values) / len(values) - 1) < 1e-10, 'Poisson mean-one identity')
    check(abs(max(values) - 1 / (1 - abs(rho))) < 1e-8, 'upper exponent endpoint')
    check(abs(min(values) - 1 / (1 + abs(rho))) < 1e-8, 'lower exponent endpoint')
    print('PASS checks:', N_CHECKS)

if __name__ == '__main__':
    run()
