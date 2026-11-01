#!/usr/bin/env python3
"""Standalone finite numerical checks for a four-point duality-rank witness.

These checks complement, and do not replace, the exact determinant proof.
"""
import math


def determinant(cols):
    a, b, c = cols
    return (a[0] * (b[1] * c[2] - b[2] * c[1])
            - a[1] * (b[0] * c[2] - b[2] * c[0])
            + a[2] * (b[0] * c[1] - b[1] * c[0]))


def subtract(a, b):
    return tuple(x - y for x, y in zip(a, b))


def norm(x, power):
    return sum(abs(z) ** power for z in x) ** (1.0 / power)


def duality(x, power):
    radius = norm(x, power)
    return tuple(math.copysign(abs(z) ** (power - 1), z) /
                 radius ** (power - 1) if z else 0.0 for z in x)


def witness(p, c):
    q = p / (p - 1)
    s = (1 - c ** q) ** (1 / q)
    t = (1 - 2 ** (1 - q) * c ** q) ** (1 / q)
    w = [(c, 0.0, s), (0.0, c, s),
         (c / 2, c / 2, t), (c / 2, c / 2, -t)]
    inv = lambda z: math.copysign(abs(z) ** (q - 1), z) if z else 0.0
    u = [tuple(inv(z) for z in row) for row in w]
    a = c ** (q - 1)
    b = (c / 2) ** (q - 1)
    T = t ** (q - 1)
    exact_det_expression = -2 * a * T * (a - 2 * b)
    numeric_det = determinant([subtract(u[i], u[0]) for i in (1, 2, 3)])
    scale = max(1e-14, abs(exact_det_expression), abs(numeric_det))
    assert abs(numeric_det - exact_det_expression) < 1e-10 * scale
    assert all(abs(norm(row, q) - 1.0) < 3e-13 for row in w)
    assert all(abs(norm(row, p) - 1.0) < 3e-13 for row in u)
    assert all(abs(z[0] + z[1] - c) < 1e-13 for z in w)
    for urow, wrow in zip(u, w):
        assert max(abs(a - b) for a, b in zip(duality(urow, p), wrow)) < 3e-12
    if abs(p - 2) > 1e-6:
        assert abs(exact_det_expression) > 1e-12
    else:
        assert abs(exact_det_expression) < 1e-12
    return numeric_det


def main():
    count = 0
    for p in (1.2, 1.5, 1.8, 1.99, 2.0, 2.01, 2.2, 2.8, 3.5, 6.0, 10.0):
        for c in (0.4, 0.5, 0.7, 0.9):
            witness(p, c)
            count += 1
    d_left = witness(1.8, .5)
    d_right = witness(2.2, .5)
    assert d_left * d_right < 0
    print('PASS: {} parameter pairs; unit spheres, dual images, coplanarity, determinant and phase'.format(count))


if __name__ == '__main__':
    main()
