#!/usr/bin/env python3
"""Exact dyadic-square geometry check for two diagonal baker-map sensors.

The verification enumerates each n-strip and integrates two intersecting
halfplanes using rational piecewise-affine bounds. It is finite numerical
checking, independent of the theorem's all-n bit-reversal proof.
"""
from fractions import Fraction


def reverse_bits(k, n):
    out = 0
    for _ in range(n):
        out = 2 * out + (k & 1)
        k >>= 1
    return out


def strip_area(n, k, mode):
    """P(sensor initially and n steps later | initial x lies in strip k)."""
    N = 1 << n
    r = reverse_bits(k, n)
    # Coordinates: x=(k+u)/N, y=v, 0<=u,v<=1.
    # Sensor 1 bound: v < A0+A1*u.
    # Sensor after B^n bound: v < C0+C1*u.
    if mode == "sum":
        lines = [(Fraction(N - k, N), Fraction(-1, N)),
                 (Fraction(N-r), Fraction(-N))]
    elif mode == "difference":
        lines = [(Fraction(k, N), Fraction(1, N)),
                 (Fraction(-r), Fraction(N))]
    else:
        raise ValueError(mode)
    endpoints = {Fraction(0), Fraction(1)}
    # The integrand is max(0,min(line1,line2)); partition at zeros,
    # line intersections, and strip endpoints. All steps are rational.
    guides = lines + [(Fraction(0), Fraction(0))]
    for i, (a, b) in enumerate(guides):
        for c, d in guides[i + 1:]:
            if b != d:
                u = (c - a) / (b - d)
                if 0 < u < 1:
                    endpoints.add(u)
    pts = sorted(endpoints)
    area = Fraction(0)
    for u0, u1 in zip(pts, pts[1:]):
        mid = (u0 + u1) / 2
        value, a, b = min((a + b * mid, a, b) for a, b in lines)
        if value <= 0:
            continue
        area += a * (u1 - u0) + b * (u1**2 - u0**2) / 2
    return area


def exact_joint(n, mode):
    N = 1 << n
    return sum((strip_area(n, k, mode) for k in range(N)), Fraction()) / N


def formula(n, mode):
    N = 1 << n
    sign = 1 if mode == "sum" else -1
    return Fraction(1, 4) + Fraction(1, 6 * N) + sign * Fraction(n * N, 8 * (N * N - 1))


def main():
    for n in range(1, 13):
        for mode in ("sum", "difference"):
            joint = exact_joint(n, mode)
            assert joint == formula(n, mode), (n, mode, joint, formula(n, mode))
    assert formula(1, "difference") == Fraction(1, 4)
    assert formula(2, "difference") - Fraction(1, 4) == -Fraction(1, 40)
    assert formula(1, "sum") - Fraction(1, 4) == Fraction(1, 6)
    print("VERIFY_OK: all two-sensor, n=1..12 exact rational polygon integrals")


if __name__ == "__main__":
    main()
