#!/usr/bin/env python3
"""Finite tests for explicit rotation-sum singular values and trigonometric means.

The proof of infinite asymptotics is analytic; these checks are diagnostic only.
"""
import cmath
import math


def formula(b):
    x = math.pi / (2*b)
    return 2/(b*math.sin(x)) if b % 2 else 2/(b*math.tan(x))


def direct_mean(b):
    return sum(abs(1 + cmath.exp(2j*math.pi*k/b)) for k in range(b))/b


def finite_coefficient(theta, n=2500, cutoff=200000):
    a = [abs(1 + cmath.exp(1j*k*theta))/(k+1) for k in range(cutoff)]
    return n*sorted(a, reverse=True)[n-1]


def main():
    count = 0
    for b in range(1, 101):
        assert abs(formula(b)-direct_mean(b)) < 2e-12, b
        count += 1
    assert abs(formula(1)-2) < 1e-13
    assert abs(formula(2)-1) < 1e-13
    assert abs(formula(3)-4/3) < 1e-13
    count += 3
    for b in range(1, 101):
        if b % 2:
            assert formula(b) > 4/math.pi
        else:
            assert formula(b) < 4/math.pi
        count += 1
    angles = [0.0, math.pi, 2*math.pi/3, math.pi/2,
              2*math.pi/5, 2*math.pi*((math.sqrt(5)-1)/2)]
    targets = [formula(1), formula(2), formula(3), formula(4),
               formula(5), 4/math.pi]
    for angle, target in zip(angles, targets):
        sample = finite_coefficient(angle)
        assert abs(sample-target) < 0.006, (angle, sample, target)
        count += 1
    for theta, phi in [(0.001, 0.002), (0.2, 0.203), (1.31, 1.31002)]:
        for k in range(1000):
            d = abs(cmath.exp(1j*k*theta) - cmath.exp(1j*k*phi))/(k+1)
            assert d <= abs(theta-phi)+1e-13
            count += 1
    print(f"PASS: {count} finite checks (trigonometric means, singular-value samples, norm bounds)")


if __name__ == '__main__':
    main()
