#!/usr/bin/env python3
"""Numerical and finite arithmetic checks for the small-angle inradius theorem.

The universal assertions follow from the written analytical proof. This script
checks concrete instances and the exact integer maximizer rule; it does not
replace a proof or claim exhaustive search across real parameters.
"""
import math


def h_value(a, delta, bound=800):
    return max((a ** j) * (j - delta) for j in range(1, bound + 1))


def h_maximizer(a, delta):
    q = delta + a / (1.0 - a)
    return max(1, math.ceil(q))


def cross(u, v):
    return (u.conjugate() * v).imag


def check(a, theta):
    k = math.floor(math.pi / theta)
    delta = math.pi / theta - k
    p = math.floor(math.pi / (2.0 * theta))
    eigen = lambda n: (a ** n) * complex(math.cos(n * theta), math.sin(n * theta))
    # The maximum search is a finite consistency check, not an infinite proof.
    j = max(range(1, 801), key=lambda t: (a ** t) * math.sin((t - delta) * theta))
    m = (a ** (k + j)) * math.sin((j - delta) * theta)
    assert m > 0.0
    A, u, v = 1.0 + 0j, eigen(p), eigen(k + j)
    assert cross(u - A, -A) > 0
    assert cross(v - u, -u) > 0
    assert cross(A - v, -v) > 0
    distances = [abs(cross(y - x, -x)) / abs(y - x)
                 for x, y in [(A, u), (u, v), (v, A)]]
    tri_radius = min(distances)
    lo = m / (1.0 + a ** k)
    assert tri_radius >= lo * (1.0 - 1e-10), (a, theta, tri_radius, lo)
    assert tri_radius <= m * (1.0 + 1e-10)
    h = h_value(a, delta)
    j0 = h_maximizer(a, delta)
    assert abs(a ** j0 * (j0 - delta) - h) <= 1e-11
    assert abs(m / (theta * a ** k * h) - 1.0) <= 0.05, (a, theta)
    return tri_radius / m


def main():
    for a in (0.5, 0.75, 0.9):
        for delta in (0.0, 0.12, 0.37, 0.5, 0.91, 0.9999):
            h = h_value(a, delta)
            j0 = h_maximizer(a, delta)
            assert abs(h - (a ** j0) * (j0 - delta)) < 1e-11
        assert abs(h_value(a, 1.0) - a * h_value(a, 0.0)) < 1e-11
        for theta in (0.055, 0.04, 0.03):
            ratio = check(a, theta)
            assert ratio > 0.94
    assert abs(h_value(0.5, 0.0) - 0.5) < 1e-12
    assert abs(h_value(0.5, 0.5) - 0.375) < 1e-12
    assert abs((0.5 ** (-0.5)) * 0.375 - 3.0 * math.sqrt(2.0) / 8.0) < 1e-12
    print('SPIRAL_INRADIUS_PHASE_ASYMPTOTIC_CHECKS_OK')


if __name__ == '__main__':
    main()
