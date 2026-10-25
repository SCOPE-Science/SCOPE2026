#!/usr/bin/env python3
"""Numerical cross-checks for James constants of regular 4k+2-gonal normed planes.

Only finite tests; the accompanying geometric argument proves the all-order result.
"""
import math


def gauge(x, y, n):
    a = math.pi / n
    return max(x * math.cos((2*j + 1)*a) + y * math.sin((2*j + 1)*a)
               for j in range(n)) / math.cos(a)


def formula(n):
    assert n >= 6 and n % 4 == 2
    u = math.pi / (2*n)
    sign = -1 if n % 8 == 2 else 1
    return math.sqrt(2) * (math.cos(u)**3 + sign * math.sin(u)**3) / math.cos(2*u)


def unit(angle, n):
    x, y = math.cos(angle), math.sin(angle)
    radius = gauge(x, y, n)
    return (x/radius, y/radius)


def local_james(angle, n):
    x = unit(angle, n)
    left, right = angle, angle + math.pi
    for _ in range(45):
        mid = (left + right)/2
        y = unit(mid, n)
        plus = gauge(x[0]+y[0], x[1]+y[1], n)
        minus = gauge(x[0]-y[0], x[1]-y[1], n)
        if plus > minus:
            left = mid
        else:
            right = mid
    y = unit((left + right)/2, n)
    return min(gauge(x[0]+y[0], x[1]+y[1], n),
               gauge(x[0]-y[0], x[1]-y[1], n))


def run():
    tested = (6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 50, 62, 74, 98)
    sample_count = 0
    for n in tested:
        c = math.cos(math.pi/n)
        j = formula(n)
        assert abs(gauge(1.0, c, n) - j) < 1e-12
        assert abs(gauge(1.0, -c, n) - j) < 1e-12
        assert abs(gauge(0.0, c, n)-1.0) < 1e-12
        assert abs(local_james(0.0, n)-j) < 5e-11
        for t in range(32):
            angle = (t + 0.271828)*2*math.pi/(32*n)
            assert local_james(angle, n) <= j + 1e-9, (n, t, local_james(angle,n), j)
            sample_count += 1
    assert abs(formula(6)-1.5)<1e-12
    assert abs(formula(10)-(3*math.sqrt(5)-1)/4)<1e-12
    print('CHECK_OK: %s polygon orders, %s sampled local James values; exact special-value checks passed.'
          % (len(tested),sample_count))

if __name__ == '__main__':
    run()
