#!/usr/bin/env python3
"""Reproducibility checks for intermittent Robin absorption on a unit interval.

Uses independent Robin--Neumann spectral and half-line formulas; checks only
finite instances, not the infinite-horizon theorem.
"""
from math import pi, sin, cos, tan, exp, erfc, sqrt, isfinite

checks = 0

def verify(condition, description):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(description)


def root(j, rate):
    """Root of z*tan(z)=rate in (j*pi,j*pi+pi/2)."""
    low = j*pi
    high = j*pi + pi/2
    for _ in range(90):
        mid = (low + high)/2
        # tan(mid) is nonnegative in the intended half-period
        if mid*tan(mid) < rate:
            low = mid
        else:
            high = mid
    return (low + high)/2


def spectral_removal(duration, rate, modes=120):
    """1 - spatially integrated surviving mass, uniform initial law."""
    survival = 0.0
    for j in range(modes):
        z = root(j, rate)
        norm = 0.5 + sin(2*z)/(4*z)
        weight = (sin(z)/z)**2 / norm
        survival += weight * exp(-z*z*duration)
    return max(0.0, 1.0 - survival)


def scaled_erfc(z):
    if z < 26:
        return exp(z*z)*erfc(z)
    # Asymptotic expansion, adequate to 1e-9 for z>=26
    inv = 1/(z*z)
    return (1 - inv/2 + 3*inv*inv/4 - 15*inv**3/8 + 105*inv**4/16) / (sqrt(pi)*z)


def halfline_removal(duration, rate):
    z = rate*sqrt(duration)
    if z < 1e-7:
        return rate*duration
    return sqrt(duration) * (2/sqrt(pi) - (1-scaled_erfc(z))/z)


def main():
    # Independent Robin boundary equation, normalization and spectral mass.
    for rate in (0.15, 0.5, 1.0, 2.5, 7.0, 25.0):
        for j in (0, 1, 2, 4):
            z = root(j, rate)
            verify(j*pi < z < j*pi+pi/2, 'eigenvalue bracket')
            verify(abs(z*tan(z)-rate) < 1e-7, 'Robin eigenvalue equation')
        for duration in (0.001, 0.01, 0.04, 0.1, 0.25):
            p = spectral_removal(duration, rate)
            verify(0 < p < 1, 'one-pulse reaction probability in (0,1)')
            verify(0.25*min(rate*duration, sqrt(duration)) <= p+1e-10,
                   'rigorous one-pulse lower envelope')
            verify(p <= 4*min(rate*duration, sqrt(duration))+1e-10,
                   'rigorous one-pulse upper envelope')
            h = halfline_removal(duration, rate)
            verify(abs(p-h) <= 0.5*exp(-1/(4*duration))+5e-14,
                   'uniform short-pulse halfline comparison')
            verify(isfinite(p), 'spectral numerical finiteness')
    # Independent check: stronger Robin rates cause more absorption.
    for duration in (0.001, 0.01, 0.04, 0.1, 0.25):
        previous = 0.0
        for rate in (0.15, 0.5, 1.0, 2.5, 7.0, 25.0):
            current = spectral_removal(duration, rate)
            verify(current > previous, 'monotonicity with reactivity')
            previous = current
    # Transition F(z): interpolates reaction-limited z and diffusion-limited constant.
    for z in (0.001, 0.01, 0.1, 1., 5., 20., 50.):
        f = halfline_removal(0.01,z/0.1)/0.1
        verify(0 < f < 2/sqrt(pi), 'crossover range')
        verify(f <= z+1e-8, 'reaction-limited bound')
    for z in (1e-3, 1e-2):
        f = halfline_removal(0.01,z/0.1)/0.1
        verify(abs(f/z-1) < 0.02, 'weak-rate limit')
    for z in (50., 100.):
        f = halfline_removal(0.01,z/0.1)/0.1
        verify(abs(f - 2/sqrt(pi)) < 0.021, 'strong-rate limit')
    # Power law: sample numerical convergence predicates are NOT proofs.
    # Confirm the exponent algebra for all investigated points.
    for p, q, expected in ((4,6,False),(2,1,True),(2,0.9,False),
                           (1,0,True),(1,-0.1,False),(3,8,False),
                           (0.5,-0.5,True),(0.5,-0.6,False)):
        exponent = max(p-q,p/2)  # min(n^(q-p), n^(-p/2)) = n^(-exponent)
        verify((exponent <= 1) == expected, 'power-law classification')
    print(f'PASS: {checks} independent finite numerical and algebraic check groups')

if __name__ == '__main__':
    main()
