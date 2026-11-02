#!/usr/bin/env python3
"""Independent finite consistency checks for the explicit quadratic norm identity."""
from math import cos, sin, pi
from random import Random


def tau_root():
    lo, hi = 0.0, pi / 2
    for _ in range(100):
        mid = (lo + hi) / 2
        if cos(mid) > mid:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def circle_norm(a, b, c, n=8192):
    s = 0.0
    for j in range(n):
        t = 2*pi*(j+0.5)/n
        z = complex(cos(t), sin(t))
        s += abs(a + b*z + c*z*z)
    return s/n


def main():
    t = tau_root()
    v = sin(t)
    a = 1.0/(2*(1+v))
    b = v/(1+v)
    exact = 2*t/pi
    sampled = circle_norm(a, b, a)
    assert abs(cos(t)-t) < 1e-14
    assert abs(a + b + a - 1) < 1e-14
    assert abs(sampled-exact) < 5e-7, (sampled, exact)
    ratio = 1/(2*exact)
    assert ratio > pi/3
    rng = Random(11504)
    n_random = 256
    for _ in range(n_random):
        alpha = complex(rng.uniform(-1, 1), rng.uniform(-1, 1))
        beta = complex(rng.uniform(-1, 1), rng.uniform(-1, 1))
        gamma = 1-alpha-beta
        assert circle_norm(alpha, beta, gamma, n=2048) > exact - 4e-4
    print('tau:', format(t, '.14f'))
    print('minimum circle L1:', format(exact, '.12f'))
    print('sharp restricted norm:', format(ratio, '.12f'))
    print('midpoint quadrature and', n_random, 'sample checks: PASS')


if __name__ == '__main__':
    main()
