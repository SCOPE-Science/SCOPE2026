#!/usr/bin/env python3
"""Reproduce the sharp spectral optimization for a one-dimensional box kernel.

No third-party packages are needed. The theorem is proved analytically in RESULT.md;
these evaluations check constants, derivatives, and finite spectral samples.
"""
import math

PI = math.pi


def a(s):
    return 1.0 - math.sin(s) / s if s else 0.0


def q(s, b):
    return a(s) * (b + 1.0 / (s * s)) if s else 1.0 / 6.0


def F(s):
    return s / (6.0 * (s - math.sin(s))) - 1.0 / (s * s)


def N(s):
    return s**3 * (s * math.cos(s) - math.sin(s)) + 12.0 * (s - math.sin(s))**2


def bisect(f, lo, hi, steps=90):
    flo = f(lo)
    fhi = f(hi)
    assert flo * fhi < 0
    for _ in range(steps):
        mid = (lo + hi) / 2.0
        fmid = f(mid)
        if fmid * flo > 0:
            lo, flo = mid, fmid
        else:
            hi, fhi = mid, fmid
    return (lo + hi) / 2.0


def extrema(b, hi=100.0, count=120000):
    mn = min(1.0 / 6.0, b)
    mx = max(1.0 / 6.0, b)
    for j in range(1, count + 1):
        s = hi * j / count
        v = q(s, b)
        mn = min(mn, v)
        mx = max(mx, v)
    return mn, mx


def q_stationary_numerator(s, b):
    return (b * s * s + 3.0) * math.sin(s) - s * (b * s * s + 1.0) * math.cos(s) - 2.0 * s


def main():
    t = bisect(N, 2.5 * PI, 3.0 * PI)
    b = F(t)
    assert 2.5 * PI < t < 3.0 * PI
    assert 1.0 / 6.0 < b < 0.2
    assert abs(q(t, b) - 1.0 / 6.0) < 2e-14
    assert abs(N(t)) < 1e-8
    assert abs(F(t) - 0.17477799238129124) < 1e-12
    assert abs(t - 7.874519450912597) < 1e-11

    # The displayed analytic formula for the derivative of F is verified.
    for j in range(15, 175):
        x = 0.17 * j
        step = 1e-5
        finite_difference = (F(x + step) - F(x - step)) / (2.0 * step)
        analytic = N(x) / (6.0 * x**3 * (x - math.sin(x))**2)
        assert abs(finite_difference - analytic) < 1e-8

    # Find the maximum on the compact first oscillation band by bracketing
    # the derivative's sign changes (not a proof of uniqueness there).
    roots = []
    previous = 0.0001
    for j in range(1, 20001):
        here = 2.0 * PI * j / 20000.0
        if q_stationary_numerator(previous, b) * q_stationary_numerator(here, b) < 0:
            roots.append(bisect(lambda s: q_stationary_numerator(s, b), previous, here))
        previous = here
    assert roots
    peak = max([(q(s, b), s) for s in [0.0, 2.0 * PI] + roots])
    K = 6.0 * peak[0]
    assert abs(K - 1.7002005645618086) < 2e-8
    assert abs(peak[1] - 3.7526393887050244) < 3e-5
    assert K < 1.701

    # Direct finite-frequency samples must respect the proved condition
    # number bound and the exact endpoint minimum.
    mn, mx = extrema(b)
    assert mn >= 1.0 / 6.0 - 3e-12
    assert mx <= peak[0] + 2e-8
    assert mx >= peak[0] - 2e-6

    for other in [0.10, 0.15, 0.17, 0.174, 0.18, 0.20, 0.50]:
        low, high = extrema(other, 30.0, 60000)
        assert high / low > K + 0.001

    # The mass-normalized tuning is provably worse by evaluating one mode.
    mass_lower_bound = 6.0 * q(4.0, 0.5)
    assert mass_lower_bound > 4.0135
    assert mass_lower_bound / K > 2.36

    # Finite Fourier samples for positive horizons, not a continuum proof.
    for delta in [0.01, 0.019, 0.05, 0.125, 0.25]:
        vals = [q(delta * k, b) for k in range(1, 20001)]
        assert max(vals) / min(vals) <= K + 1e-10

    print('root_t=%.15f' % t)
    print('optimal_b=%.15f' % b)
    print('peak_s=%.12f' % peak[1])
    print('optimal_K=%.12f' % K)
    print('mass_beta_one_half_K_lower_bound=%.12f' % mass_lower_bound)
    print('checks: PASS (algebraic derivatives, root, extrema, tuning comparison, finite spectra)')


if __name__ == '__main__':
    main()
