#!/usr/bin/env python3
"""Standard-library consistency checks for Poisson two-coset Gabor bounds.

Numerical samples are not a substitute for the analytic proof in RESULT.md.
"""
import cmath
import math

TAU = 2 * math.pi


def zak_closed(w, x, s):
    q = math.exp(-TAU * w)
    X = cmath.exp(1j * TAU * x)
    return (math.pi / w) * cmath.exp(1j * TAU * x * s) * (
        q**s / (1 - q * X) + q**(1 - s) / (X - q)
    )


def zak_direct(w, x, s, radius=12000):
    # Fourier tail here is absolutely convergent as 1/n^2.
    total = 0j
    for n in range(-radius, radius + 1):
        total += cmath.exp(1j * TAU * n * s) / ((x - n)**2 + w**2)
    return total


def frame_weight(w, d, x, s):
    return abs(zak_closed(w, x, s))**2 + abs(zak_closed(w, x, (s - d) % 1))**2


def bounds(w, d):
    q = math.exp(-TAU * w)
    a = 4 * math.pi**2 * q / (w*w*(1+q)**2) * (math.cosh(TAU*w*min(d,1-d)) - 1)
    b = math.pi**2 / (w*w*(1-q)**2) * ((1+q)**2 + (q**d + q**(1-d))**2)
    return a, b


def close(a, b, rel=1e-9, ab=1e-10):
    assert abs(a-b) <= ab + rel * max(abs(a), abs(b)), (a, b)


def main():
    for w, d in ((0.5, 0.2), (1.0, 0.3), (1.0, 0.5), (2.0, 0.4)):
        for x, s in ((0.0, 0.2), (0.3, 0.4), (0.5, 0.65)):
            close(zak_direct(w, x, s), zak_closed(w, x, s), rel=3e-8, ab=5e-5)
        a, b = bounds(w, d)
        xlo = 0.5
        slo = (1+d)/2 if d<=0.5 else d/2
        close(frame_weight(w, d, xlo, slo), a)
        close(frame_weight(w, d, 0, 0), b)
        for k in range(53):
            x = k/53
            for j in range(57):
                s = j/57
                val = frame_weight(w, d, x, s)
                assert a - 1e-11 <= val <= b + 1e-11, (w, d, x, s, val, a, b)
        a_half, b_half = bounds(w, 0.5)
        assert a <= a_half + 1e-11
        assert b >= b_half - 1e-11
    for w in (0.6, 1.1, 2.0):
        q = math.exp(-TAU*w)
        coef = 8 * math.pi**4*q/(1+q)**2
        for d in (0.004, 0.007):
            a, _ = bounds(w, d)
            assert abs(a/d**2/coef-1) < 0.002
    print('checks passed')


if __name__ == '__main__':
    main()
