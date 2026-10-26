#!/usr/bin/env python3
"""Reproduce the two-frequency reciprocal-wave inversion and depth-conditioning tests.

Standard-library only. The proof of uniqueness is analytic; finite tests are not
an exhaustive mathematical certificate.
"""
import math
import random


def speeds(k, h, shear, surface_tension, gravity=9.81, density=1000.0):
    t = math.tanh(k * h)
    a = (gravity / k + surface_tension * k / density) * t
    delta = shear * t / k
    root = math.sqrt(a + 0.25 * delta * delta)
    return root + delta / 2.0, root - delta / 2.0


def reconstruct(k1, k2, pair1, pair2, density=1000.0):
    """Solve all four unknowns: h, S, g, sigma for known density."""
    if not 0.0 < k1 < k2:
        raise ValueError('Require 0 < k1 < k2')
    u1, d1 = pair1
    u2, d2 = pair2
    if not (u1 > d1 > 0 and u2 > d2 > 0):
        raise ValueError('Require positive speeds and a positive shear orientation')
    delta1, delta2 = u1 - d1, u2 - d2
    ratio = k1 * delta1 / (k2 * delta2)
    if not (k1 / k2 < ratio < 1.0):
        raise ValueError('The depth ratio is outside its open realizability interval')
    def R(h):
        return math.tanh(k1 * h) / math.tanh(k2 * h)
    lo, hi = 0.0, 1.0 / k1
    while R(hi) < ratio:
        hi *= 2.0
        if hi > 1e5 / k1:
            raise ArithmeticError('The ratio is numerically indistinguishable from 1')
    for _ in range(75):
        mid = (lo + hi) * 0.5
        if R(mid) < ratio:
            lo = mid
        else:
            hi = mid
    h = (lo + hi) / 2.0
    t1, t2 = math.tanh(k1 * h), math.tanh(k2 * h)
    shear = k1 * delta1 / t1
    y1, y2 = k1 * u1 * d1 / t1, k2 * u2 * d2 / t2
    if not (y1 < y2 < y1 * (k2 / k1)**2):
        raise ValueError('A positive gravity and capillarity pair is impossible')
    cap = (y2 - y1) / (k2**2-k1**2)
    gravity = y1 - cap * k1**2
    return h, shear, gravity, density * cap, ratio


def ratio_and_derivative(k1, k2, h):
    r = math.tanh(k1 * h) / math.tanh(k2 * h)
    der = r * (2 * k1 / math.sinh(2 * k1 * h)
               - 2 * k2 / math.sinh(2 * k2 * h))
    return r, der


def run():
    rng = random.Random(20261023)
    count = 0
    for _ in range(2000):
        k1 = 10 ** rng.uniform(-0.4, 0.4)
        k2 = k1 * rng.uniform(1.3, 4.0)
        h = rng.uniform(0.08, 3) / k1
        shear = 10 ** rng.uniform(-1.0, 1.0)
        sigma = 10 ** rng.uniform(-2, 3)
        g = 10 ** rng.uniform(-0.4, 1.3)
        rho = 10 ** rng.uniform(0, 3)
        v1 = speeds(k1, h, shear, sigma, g, rho)
        v2 = speeds(k2, h, shear, sigma, g, rho)
        # Independent quadratic identities on each directional pair.
        for k, v in ((k1, v1), (k2, v2)):
            u, d = v
            t = math.tanh(k * h)
            assert abs((u-d) - shear*t/k) < 3e-12 * (1+u+d)
            assert abs(u*d - (g/k+sigma*k/rho)*t) < 4e-12*(1+u*d)
            count += 1
        hh, ss, gg, tt, rr = reconstruct(k1, k2, v1, v2, rho)
        assert abs(hh-h) < 1e-9*(1+h), (hh,h)
        assert abs(ss-shear) < 1e-9*(1+shear)
        assert abs(tt-sigma) < 1e-7*(1+sigma), (tt,sigma)
        assert abs(gg-g) < 1e-9*(1+g), (gg,g)
        count += 4
    # Inadmissible ratio and cross-wavenumber capillarity detect inconsistent data.
    k1, k2, h, s, sig = 0.8, 2.1, 1.4, 0.7, 0.18
    pair1 = speeds(k1, h, s, sig)
    pair2 = speeds(k2, h, s, sig)
    # A nonrealizable depth ratio and two nonphysical restoring-force splits.
    def pair_from_difference_product(delta, product):
        root = math.sqrt(delta * delta + 4 * product)
        return (root + delta) / 2, (root - delta) / 2
    delta2 = pair2[0] - pair2[1]
    product2 = pair2[0] * pair2[1]
    bad_cases = (
        pair_from_difference_product(delta2 * 100, product2),
        pair_from_difference_product(delta2, product2 * 1e-4),
        pair_from_difference_product(delta2, product2 * 1e4),
    )
    for bad in bad_cases:
        try:
            reconstruct(k1,k2,pair1,bad)
        except ValueError:
            pass
        else:
            raise AssertionError('Expected incompatible data rejection')
        count += 1
    for h in (0.01,0.03,0.05,0.1,0.2,0.6,1.5,3.0):
        r, rp = ratio_and_derivative(0.8, 2.1, h)
        assert 0.8/2.1 < r < 1 and rp > 0
        eps = 1e-6
        numerical = (ratio_and_derivative(0.8,2.1,h+eps)[0]
                     - ratio_and_derivative(0.8,2.1,h-eps)[0])/(2*eps)
        assert abs(numerical-rp) < 4e-8*(1+rp)
        count += 2
    # Sharp singular-depth expansions, tested within their validity domains.
    for h in (0.004,0.008,0.015):
        r,rp = ratio_and_derivative(0.8,2.1,h)
        fourth = (0.8/2.1) * (2*0.8**4/15 - 0.8**2*2.1**2/9 - 2.1**4/45)
        pref = (0.8/2.1)*(1+(2.1**2-0.8**2)*h*h/3)+fourth*h**4
        dpre = (2*0.8/(3*2.1))*(2.1**2-0.8**2)*h+4*fourth*h**3
        assert abs(r-pref) < 2*h**6
        assert abs(rp-dpre) < 20*h**5
        count += 2
    for h in (8,9,10):
        _,rp = ratio_and_derivative(0.8,2.1,h)
        assert abs(rp / (4*0.8*math.exp(-2*0.8*h))-1) < 1e-4
        count += 1
    print('PASS; independent dispersion identities, inversions, compatibility, and asymptotic checks:',count)


if __name__ == '__main__':
    run()
