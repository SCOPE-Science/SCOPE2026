#!/usr/bin/env python3
"""Reproducibility checks for deterministic first-Hermite two-tone STFT zeros.

Requires Python standard library only. Numerical checks supplement the analytic proof.
"""
import cmath
import math

PI = math.pi
CRITICAL = math.sqrt(2 / PI)


def coeff_a(v, d):
    return (v - d) * math.exp(-PI * (v - d) ** 2)


def coeff_b(v, d):
    return (v + d) * math.exp(-PI * (v + d) ** 2)


def reduced(t, v, gap):
    d = gap / 2
    angle = PI * gap * t
    return (coeff_a(v, d) * cmath.exp(1j * angle)
            + coeff_b(v, d) * cmath.exp(-1j * angle))


def analytic_stft(t, v, gap):
    return -1j * cmath.exp(-2j * PI * v * t) * reduced(t, v, gap)


def direct_stft(t, v, gap):
    # Trapezoidal quadrature in the translated Gaussian integration variable.
    samples = 2600
    step = 12 / samples
    total = 0j
    for j in range(samples + 1):
        u = -6 + j * step
        s = t + u
        f = 2 * math.cos(PI * gap * s)
        integrand = f * u * math.exp(-PI * u * u) * cmath.exp(-2j * PI * v * s)
        total += (0.5 if j in (0, samples) else 1.0) * integrand
    return total * step


def bisect(fn, left, right):
    x = fn(left)
    y = fn(right)
    assert x * y < 0
    for _ in range(90):
        m = (left + right) / 2
        z = fn(m)
        if x * z > 0:
            left, x = m, z
        else:
            right, y = m, z
    return (left + right) / 2


def derivative_gaussian_first(x):
    return (1 - 2 * PI * x * x) * math.exp(-PI * x * x)


def jacobian(t, v, gap):
    d = gap / 2
    ea = cmath.exp(1j * PI * gap * t)
    eb = cmath.exp(-1j * PI * gap * t)
    dt = 1j * PI * gap * (coeff_a(v, d) * ea - coeff_b(v, d) * eb)
    dv = derivative_gaussian_first(v - d) * ea + derivative_gaussian_first(v + d) * eb
    return (dt.conjugate() * dv).imag


def zero_points(gap):
    d = gap / 2
    exterior = bisect(
        lambda v: math.log((v + d) / (v - d)) - 4 * PI * d * v,
        d * (1 + 1e-9), 100 + 100 * d)
    result = [(0.0, 0.0, 1 if gap < CRITICAL else -1),
              (0.5 / gap, exterior, -1),
              (0.5 / gap, -exterior, -1)]
    if gap > CRITICAL + 1e-9:
        alpha = PI * gap * gap / 2
        u = bisect(lambda u: math.atanh(u) / u - alpha, 1e-7, 1 - 1e-12)
        result += [(0, d * u, 1), (0, -d * u, 1)]
    return result


def main():
    count = 0
    gaps = [0.06, 0.2, 0.45, 0.7, 0.9, 1.1, 1.5, 2.0]
    for gap in gaps:
        pts = zero_points(gap)
        assert len(pts) == (3 if gap < CRITICAL else 5)
        for t, v, expected_sign in pts:
            assert abs(analytic_stft(t, v, gap)) < 2e-12, (gap, t, v)
            assert jacobian(t, v, gap) * expected_sign > 0, (gap, t, v)
            count += 1
    for gap in [0.2, 0.7, 1.1, 1.8]:
        for t in [0.0, 0.07 / gap, 0.21 / gap]:
            for v in [-1.1, -0.4, 0.0, 0.3, 0.9]:
                err = abs(analytic_stft(t, v, gap) - direct_stft(t, v, gap))
                assert err < 4e-11, (gap, t, v, err)
                count += 1
    at = CRITICAL
    d = at / 2
    assert abs(2 * PI * d * d - 1) < 1e-14
    for v in [0.02, 0.04]:
        asymp = (4 * PI / 3) * math.exp(-0.5) * v ** 3
        actual = reduced(0, v, at).real
        assert abs(actual / asymp - 1) < 0.008
        count += 1
    print(f'VERIFY_OK: {count} located-zero, Jacobian, integral, and cubic-contact comparisons')


if __name__ == '__main__':
    main()
