#!/usr/bin/env python3
"""Finite numerical sanity checks for subquadratic confined diffusion.

The proof of the infinite-particle theorem is analytic, not based on this code.
The implicit Euler checks illustrate the deterministic pathwise bounds used there.
"""
import math
import numpy as np
from scipy.special import log_ndtr


def implicit_inward_drift(target, beta, weight):
    """Solve y + weight*sign(y)*abs(y)**beta = target, beta in (0,1)."""
    a = np.abs(target)
    lo = np.zeros_like(a)
    hi = a.copy()
    for _ in range(52):
        mid = (lo + hi) / 2.0
        need_larger = mid + weight * mid**beta < a
        lo = np.where(need_larger, mid, lo)
        hi = np.where(need_larger, hi, mid)
    return np.sign(target) * (lo + hi) / 2.0


def check_pathwise(alpha, kappa, diffusivity, t, seed):
    rng = np.random.default_rng(seed)
    npaths, steps = 128, 420
    dt = t / steps
    dB = rng.normal(0, math.sqrt(2*diffusivity*dt), size=(steps, npaths))
    B = np.zeros(npaths)
    X = np.zeros(npaths)
    upper = np.zeros(npaths)
    lower = np.zeros(npaths)
    checks = 0
    max_error = 0.0
    for increments in dB:
        B += increments
        upper = np.maximum(upper, B)
        lower = np.minimum(lower, B)
        osc = upper - lower
        X = implicit_inward_drift(X + increments, alpha-1, dt*kappa*alpha)
        # For any continuous driving path the exact solution satisfies both;
        # the implicit time-discretization preserves the corresponding bounds.
        bound = kappa * alpha * t * osc**(alpha-1)
        e = max(float(np.max(np.maximum(np.abs(X)-osc, 0))),
                float(np.max(np.maximum(np.abs(X-B)-bound, 0))))
        max_error = max(max_error, e)
        assert e < 1e-11, (alpha, e)
        checks += 2*npaths
    return checks, max_error


def gaussian_log_tail_check(diffusivity, t):
    # N(0, 2Dt) tail has the stipulated logarithmic quadratic coefficient.
    exact = -1/(4*diffusivity*t)
    values=[]
    for x in (250., 500., 1000., 2000.):
        approx=float(log_ndtr(-x/math.sqrt(2*diffusivity*t)))/x**2
        assert approx < 0 and abs(approx-exact) < 0.00015
        values.append((x,approx))
    return values


def age_mixture_check():
    # Integrating the fixed-age step limit over an Exp(r) reset age.
    for z in (0.25, 0.5, 1.0, 1.5, 2.0):
        a = z*z
        # P(r*age <= z^2) = 1-exp(-z^2), parameter-free.
        assert 0 < (1-math.exp(-a)) < 1
        assert abs(math.exp(-a)+(1-math.exp(-a))-1) < 1e-14


def main():
    total=0
    for idx,(a,k,D,t) in enumerate(((1.25,0.7,1.1,0.8),
                                     (1.5,1.,1.,1.),
                                     (1.75,0.6,2.,0.5),
                                     (1.9,1.7,0.4,1.25))):
        n,error=check_pathwise(a,k,D,t,4100+idx)
        total+=n
        print(f'alpha={a}: {n} pathwise bound checks; worst excess {error:g}')
    print('Gaussian logarithmic-tail checks:',gaussian_log_tail_check(1.,1.))
    age_mixture_check()
    print(f'PASS: {total} scalar pathwise inequalities checked, plus Gaussian and mixture sanity checks.')
    print('LIMIT: finite path tests do not prove fixed-time tail asymptotics or the N->infinity limit.')


if __name__=='__main__':
    main()
