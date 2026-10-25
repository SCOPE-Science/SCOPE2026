#!/usr/bin/env python3
"""Independent standard-library checks of a geometric centroid-capture law.

No external packages. Numerical quadrature and Monte Carlo diagnose only;
the analytic proof is in RESULT.md.
"""
import math
import random

LOG2 = math.log(2.0)
A = 1.0 / 3.0 + 4.0 * LOG2 / 9.0
B = 8.0 * LOG2 / 3.0 - 1.0


def exact_probability(sides):
    perimeter = sum(sides)
    p, q, r = (s / perimeter for s in sides)
    return A * (p * q + q * r + r * p) + B * p * q * r


def midpoint_integral(func, left, right, subdivisions=100000):
    delta = (right - left) / subdivisions
    return delta * sum(func(left + (i + 0.5) * delta) for i in range(subdivisions))


def cross(ax, ay, bx, by):
    return ax * by - ay * bx


def contains(point, triangle):
    px, py = point
    a, b, c = triangle
    signs = [cross(b[0]-a[0], b[1]-a[1], px-a[0], py-a[1]),
             cross(c[0]-b[0], c[1]-b[1], px-b[0], py-b[1]),
             cross(a[0]-c[0], a[1]-c[1], px-c[0], py-c[1])]
    return min(signs) >= -1e-11 or max(signs) <= 1e-11


def sample_boundary(vertices, lengths, rng):
    position = rng.random() * sum(lengths)
    for i, edge_len in enumerate(lengths):
        if position < edge_len:
            t = position / edge_len
            a, b = vertices[i], vertices[(i + 1) % 3]
            return (a[0]*(1-t) + b[0]*t, a[1]*(1-t) + b[1]*t)
        position -= edge_len
    return vertices[0]


def euclidean_triangle(sides):
    a, b, c = sides  # edges AB, BC, CA
    assert a + b > c and b + c > a and c + a > b
    x = (a*a + c*c - b*b)/(2*a)
    y = math.sqrt(max(c*c - x*x, 0.0))
    vertices = [(0.0, 0.0), (a, 0.0), (x, y)]
    return vertices, [(sum((vertices[(i+1)%3][k]-vertices[i][k])**2 for k in (0,1)))**.5 for i in range(3)]


def check():
    integral_a = midpoint_integral(lambda r: 2*r*(2*r-1)/(3*r-1)**2, .5, 1)
    integral_i = midpoint_integral(lambda t: (1-2*t)/(2-3*t), 0, .5)
    integral_j = midpoint_integral(lambda t: (2*t-1)/(3*t-1), .5, 1)
    expected_a = 1/9 + 4*LOG2/27
    expected_i = 1/3 - 2*LOG2/9
    assert abs(integral_a - expected_a) < 2e-9
    assert abs(integral_i - expected_i) < 2e-9
    assert abs(integral_j - expected_i) < 2e-9
    assert abs(1 - 2*integral_i - integral_j - 2*LOG2/3) < 2e-9
    print('Quadrature: all four tests passed')
    assert abs(exact_probability((1,1,1)) - (6+20*LOG2)/81) < 1e-14
    assert abs(exact_probability((1,1,1)) - (2/27+20*LOG2/81)) < 1e-14

    rng = random.Random(20261023)
    triangles = [(1,1,1), (3,4,5), (5,5,1), (5,5,.01), (2,3,4.5)]
    trials = 110000
    for sides in triangles:
        vertices, lengths = euclidean_triangle(sides)
        centroid = tuple(sum(p[k] for p in vertices)/3 for k in (0,1))
        successes = 0
        for _ in range(trials):
            trio = [sample_boundary(vertices, lengths, rng) for _ in range(3)]
            successes += contains(centroid, trio)
        measured = successes/trials
        predicted = exact_probability(sides)
        stderr = math.sqrt(predicted*(1-predicted)/trials)
        z = (measured-predicted)/stderr
        assert abs(z) < 5.0, (sides, z)
        print('sides=%s observed=%.6f predicted=%.6f z=%.3f' %
              (sides, measured, predicted, z))
    print('All numerical diagnostics passed; the analytic proof is independent.')


if __name__ == '__main__':
    check()
