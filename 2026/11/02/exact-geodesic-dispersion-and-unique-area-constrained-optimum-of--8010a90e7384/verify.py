#!/usr/bin/env python3
"""Numerical checks for the exact geodesic pair-distance theorem on a flat Mobius band.

Run with Python 3 and the standard library only: python3 verify.py
Numerical checks corroborate, but do not replace, the exact integral proof.
"""
import math
import random


def moment_formula(L, w):
    assert L > 0 and w > 0
    A = 4 * w * w / (L * L)
    if A <= 1:
        f = 1 / 12 + A / 6 - A * A / 36
    else:
        f = (3 * A * A + 24 * A - 6 * math.log(A) - 11) / (72 * A)
    return L * L * f


def improvement_integral(A, n=16000):
    # Independent quadrature from the density of a product of uniforms.
    # E[correction]/L^2 = 1/2 integral_0^infty t exp(-t) H(A exp(-t)) dt.
    def H(q):
        return (1 / 6 + q * q / 2) if q <= 1 else (q - 1 / 3)
    def func(t):
        z = math.exp(-t)
        return 0.5 * t * z * H(A * z)
    b = 42.0
    delta = b / n
    acc = func(0) + func(b)
    for k in range(1, n):
        acc += (4 if k % 2 else 2) * func(k * delta)
    return acc * delta / 3


def distance_sq_by_images(L, x0, y0, x1, y1):
    return min((x0 - x1 - k * L) ** 2 + (y0 - ((-1) ** k) * y1) ** 2
               for k in range(-5, 6))


def distance_sq_short(L, x0, y0, x1, y1):
    u = abs(x0 - x1)
    return min(u * u + (y0 - y1) ** 2,
               (L - u) ** 2 + (y0 + y1) ** 2)


def h(A):
    return 3 * A * A - 24 * A + 18 * math.log(A) + 21


def optimum():
    low, high = 3.0, 6.0
    assert h(low) < 0 < h(high)
    for _ in range(120):
        mid = (low + high) / 2
        if h(mid) < 0:
            low = mid
        else:
            high = mid
    return (low + high) / 2


def run():
    rng = random.Random(817253)
    A_values = [0.02, 0.25, 0.9, 0.9999, 1.0, 1.0001, 1.8, 4.3768539312, 13.0, 200.0]
    print('QUADRATURE, dimensions L=1, w=sqrt(A)/2:')
    for A in A_values:
        L, w = 1.0, math.sqrt(A) / 2
        truth = moment_formula(L, w)
        independent = (1 + A) / 6 - improvement_integral(A)
        err = abs(independent - truth)
        print(' A={:.10g} formula={:.12f} integral={:.12f} err={:.3g}'.format(
            A, truth, independent, err))
        assert err < 4e-7 * (1 + truth)
    print('IMAGE GEODESIC CHECK:')
    for A in [0.1, 1.0, 2.4, 12.0]:
        L, w = 1, math.sqrt(A) / 2
        for _ in range(25000):
            x0, x1 = rng.random(), rng.random()
            y0, y1 = (2 * rng.random() - 1) * w, (2 * rng.random() - 1) * w
            s = distance_sq_short(L, x0, y0, x1, y1)
            t = distance_sq_by_images(L, x0, y0, x1, y1)
            assert abs(s - t) < 5e-12 * (1 + t)
        print(' A={:.3g}: 25000 pairs, all 11-image minima agree'.format(A))
    print('MONTE CARLO:')
    for A in [0.1, 0.7, 1.0, 2.0, 4.3768539312, 12.0]:
        L, w = 1, math.sqrt(A) / 2
        n = 170000
        total = total_sq = 0.0
        for _ in range(n):
            x0, x1 = rng.random(), rng.random()
            y0, y1 = (2 * rng.random() - 1) * w, (2 * rng.random() - 1) * w
            d2 = distance_sq_short(L, x0, y0, x1, y1)
            total += d2
            total_sq += d2 * d2
        mean = total / n
        se = math.sqrt(max(0, total_sq / n - mean * mean) / n)
        target = moment_formula(L, w)
        err = abs(mean - target)
        print(' A={:.4g} mean={:.9f} formula={:.9f} error={:.4g} SE={:.4g}'.format(
            A, mean, target, err, se))
        assert err < 7 * se + 0.0002
    A = optimum()
    L, w = 1.0, math.sqrt(A) / 2
    norm = moment_formula(L, w) / (2 * w * L)
    print('OPTIMUM: A={:.13f}, w/L={:.13f}, E[D^2]/area={:.13f}'.format(A, w, norm))
    assert abs(A - 4.376853931208964) < 2e-12
    assert abs(norm - 0.21638029384259242) < 2e-12
    # Independent finite checks that the normalized function is lower at the analytic root.
    for B in [0.001, 0.1, 0.5, 0.99, 1, 1.01, 2, 3, 4, 4.37, 4.39, 5, 10, 100, 1000]:
        val = moment_formula(1.0, math.sqrt(B) / 2) / math.sqrt(B)
        assert val >= norm - 2e-13
    print('ALL CHECKS PASSED (numeric corroboration; proof is analytical).')

if __name__ == '__main__':
    run()
