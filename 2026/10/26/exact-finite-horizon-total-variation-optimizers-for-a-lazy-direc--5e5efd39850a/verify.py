#!/usr/bin/env python3
"""Independent finite-horizon checks for three-state directed cycle mixing."""
from math import comb, cos, pi, sqrt, tan, atan2, hypot


def exact_distribution(h, p):
    masses = [0.0, 0.0, 0.0]
    for j in range(h + 1):
        masses[j % 3] += comb(h, j) * p**j * (1 - p)**(h-j)
    return masses


def tv(masses):
    return 0.5 * sum(abs(v - 1.0 / 3) for v in masses)


def fourier_tv(h, p):
    re = 1 - 1.5 * p
    im = sqrt(3) * p / 2
    r = hypot(re, im)
    theta = atan2(im, re)
    H = max(abs(cos(h * theta - 2*pi*k/3)) for k in range(3))
    return 2 * r**h * H / 3


def candidate(h):
    a = pi/(6*h)
    p = 0.5 + tan(a)/(2*sqrt(3))
    minimum = sqrt(3) / (3 * 2**h * cos(a)**h)
    return (1-p, p, minimum)


def run():
    tests = 0
    for h in range(1, 19):
        for j in range(101):
            p = j / 100
            d1 = tv(exact_distribution(h, p))
            d2 = fourier_tv(h, p)
            assert abs(d1-d2) < 4e-14, (h, p, d1, d2)
            tests += 1
    for h in range(2, 61):
        low, high, goal = candidate(h)
        assert abs(fourier_tv(h, low) - goal) < 1e-12
        assert abs(fourier_tv(h, high) - goal) < 1e-12
        # On the candidate's zero-nonsmoothness phase, both global minima are checked;
        # the proof, not the following finite mesh, certifies globality.
        for j in range(1001):
            p = j / 1000
            assert fourier_tv(h, p) >= goal - 2e-14, (h, p)
            tests += 1
        assert goal < fourier_tv(h, 0.5)
    for j in range(101):
        p = j/100
        if 1/3 <= p <= 2/3:
            assert abs(tv(exact_distribution(1, p)) - 1/3) < 1e-14
        else:
            assert tv(exact_distribution(1, p)) > 1/3 - 1e-14
        tests += 1
    print(f"PASS: {tests} finite numerical comparisons; proof of all horizons is analytical.")
    for h in (2, 3, 5, 10, 20):
        lo, hi, value = candidate(h)
        print(f"h={h:2d}, optimum p=({lo:.12f}, {hi:.12f}), d={value:.12g}, improvement ratio={value/fourier_tv(h,0.5):.12g}")

if __name__ == '__main__':
    run()
