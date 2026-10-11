#!/usr/bin/env python3
"""Finite arithmetic checks for the elliptic equal-step covering bounds.
All coordinates in the tests are affine-normalized to the unit disk.
These finite checks supplement, not replace, the analytic arguments.
"""
import math
import random


def central_translations(kappa, delta):
    assert 0 < kappa < 1 and 0 < delta < 1
    c = 1 - kappa*kappa
    q = 1 + kappa/8
    tau = min(kappa/(8*q*q), c/(4*kappa), 1/16)
    eta = 1 - delta*delta
    vectors = [(delta, 0.0), (-delta, 0.0)]
    t0 = math.sqrt(eta)/2
    if t0 < tau/q:
        tj = t0
        while True:
            y = tj/c
            X = math.sqrt(delta*delta-kappa*kappa*y*y)
            for sign_x in (-1, 1):
                for sign_y in (-1, 1):
                    vectors.append((sign_x*X, sign_y*y))
            if q*tj >= tau:
                break
            tj *= q
    return vectors, tau


def covered(point, shifts):
    x, y = point
    return min((x+v[0])**2 + (y+v[1])**2 for v in shifts) <= 1 + 1e-12


def axial_intervals(kappa, delta):
    c = 1-kappa*kappa
    eta = 1-delta*delta
    gamma = (1+kappa)/(1-kappa)
    cutoff = min((1-kappa)/(8*kappa), 1/8)
    shifts = [(delta, 0.0)]
    u0 = math.sqrt(eta)/c
    if u0 >= delta/kappa:
        raise ValueError('Requires smaller eta')
    u = u0
    while True:
        X = math.sqrt(delta*delta-kappa*kappa*u*u)
        shifts.extend([(X, u), (X, -u)])
        if (1+kappa)*u >= cutoff:
            break
        u *= gamma
    return shifts, cutoff


def run():
    rng = random.Random(257891)
    n = 0
    for kappa in (0.15, 0.3, 0.55, 0.8, 0.97):
        for eta in (1e-5, 1e-8):
            delta = math.sqrt(1-eta)
            shifts, tau = central_translations(kappa, delta)
            for j in range(1400):
                x = rng.uniform(-tau, tau)
                y = rng.uniform(-tau, tau)
                if not covered((x, y), shifts):
                    raise AssertionError(('central', kappa, eta, j, x, y))
                n += 1
            axial, cap = axial_intervals(kappa, delta)
            for j in range(1400):
                y = rng.uniform(-cap, cap)
                if not covered((0, y), axial):
                    raise AssertionError(('axis', kappa, eta, j, y))
                n += 1
            for j in range(200):
                x = rng.uniform(-tau,tau)
                y = rng.uniform(-tau,tau)
                # Verify every enumerated displacement has physical length epsilon.
                for vx,vy in rng.sample(shifts,min(5,len(shifts))):
                    if abs(vx*vx+kappa*kappa*vy*vy-delta*delta)>3e-14:
                        raise AssertionError(('length',kappa,eta,vx,vy))
                    n += 1
    print(f'VERIFY_OK: {n} randomized finite checks')

if __name__ == '__main__':
    run()
