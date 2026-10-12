#!/usr/bin/env python3
'''Supplementary finite checks for an analytic fixed-radius CARS example.'''
import math


def objective(x):
    return 0.5*x*x + 0.5*(math.sin(x)-x)


def central_derivative(x, radius):
    return x - 0.5 + 0.5 * (math.sin(radius)/radius) * math.cos(x)


def central_curvature(x, radius):
    return 1 + math.sin(x) * (math.cos(radius)-1)/(radius*radius)


def shifted_root(radius):
    lo, hi = 0.0, radius*radius/6
    assert central_derivative(lo, radius) < 0
    assert central_derivative(hi, radius) >= -1e-14
    for _ in range(100):
        mid = (lo+hi)/2
        if central_derivative(mid, radius) < 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def cars_candidates(x, radius, sign, relative_smoothness):
    plus = objective(x+radius*sign)
    minus = objective(x-radius*sign)
    d = (plus-minus)/(2*radius)
    h = (plus+minus-2*objective(x))/(radius*radius)
    assert h > 0
    candidate = x - (d/(relative_smoothness*h))*sign
    return [x, candidate, x-radius*sign, x+radius*sign]


def main():
    checked = 0
    for radius in (0.05, 0.1, 0.25, 0.5, 1.0):
        root = shifted_root(radius)
        assert 0 < root <= radius*radius/6
        for portion in (0.125, 0.25, 0.5, 0.75, 0.875):
            x = root*portion
            assert central_derivative(x, radius) < 0
            for sign in (-1, 1):
                for smoothness in (3, 10, 100):
                    pool = cars_candidates(x, radius, sign, smoothness)
                    assert all(objective(y) >= objective(x)-1e-14 for y in pool)
                    assert all(objective(y) > objective(x)+1e-15 for y in pool[1:])
                    checked += 1
        ratio = objective(root)/(radius**4)
        print('radius', radius, 'root', root, 'objective_gap_over_radius4', ratio)
    print('finite guarded-candidate checks passed:', checked)
    print('analytic leading coefficient:', 1/288)


if __name__ == '__main__':
    main()
