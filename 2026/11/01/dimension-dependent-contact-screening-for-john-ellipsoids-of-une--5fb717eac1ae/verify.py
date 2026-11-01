#!/usr/bin/env python3
"""Deterministic numerical checks for the unequal-ball lens John ellipsoid.
Run: python3 verify.py. The theorem itself is established analytically in RESULT.md.
No third-party dependencies are required.
"""
import math


def critical_separation(dim, radius):
    return dim * (1.0 - radius * radius) / (dim - 1.0)


def pole_parameter_separation(dim, radius, h):
    return 1.0 + radius * (h - dim - 1.0) / math.sqrt(h * (dim * dim + h - 1.0))


def latitude_separation(dim, radius, t):
    u = t * t
    numerator = dim * (1.0 - radius * radius) * t * (dim * u + 1.0)
    first = dim * dim * u * (radius * radius * u + 1.0 - radius * radius) - 1.0
    second = dim * dim * u * u - 1.0
    return numerator / math.sqrt(first * second)


def solve(dim, radius, separation):
    assert dim >= 2 and 0 < radius < 1 and 0 <= separation < 1 + radius
    if separation <= 1 - radius:
        return ('contained', separation, radius, radius, None, None)
    critical = critical_separation(dim, radius)
    if radius <= 1.0 / dim or separation <= critical:
        low, high = 1.0, 2.0
        while pole_parameter_separation(dim, radius, high) < separation:
            high *= 2.0
            if high > 1e18:
                raise ArithmeticError('Unresolved one-contact parameter')
        for _ in range(90):
            mid = (low + high) / 2.0
            if pole_parameter_separation(dim, radius, mid) < separation:
                low = mid
            else:
                high = mid
        h = (low + high) / 2.0
        a = dim * radius / math.sqrt(h * (dim * dim + h - 1.0))
        b = a * math.sqrt(h)
        c = 1.0 - a
        tsmall = -1.0 / dim
        return ('apex', c, a, b, 1.0, tsmall)
    low = 1.0 / math.sqrt(dim * radius)
    high = 1.0
    for _ in range(90):
        mid = (low + high) / 2.0
        if latitude_separation(dim, radius, mid) > separation:
            low = mid
        else:
            high = mid
    t = (low + high) / 2.0
    theta = dim * dim * (1.0 - radius * radius) * t * t / (
        dim * dim * radius * radius * t**4 - 1.0
    )
    a = 1.0 / math.sqrt((1.0 + theta) * (1.0 + theta * t * t))
    b = a * math.sqrt(1.0 + theta)
    c = a * theta * t
    return ('two latitudes', c, a, b, t, -1.0 / (dim * t))


def ball_squared_max(c, a, b, center):
    # Analytic maximization of a quadratic, not a finite sample test.
    delta = b * b - a * a
    points = [-1.0, 1.0]
    if delta > 0.0:
        vertex = a * (c - center) / delta
        if -1.0 <= vertex <= 1.0:
            points.append(vertex)
    return max((c + a * t - center) ** 2 + b * b * (1.0 - t * t)
               for t in points)


def check(dim, radius, separation):
    kind, c, a, b, t1, t2 = solve(dim, radius, separation)
    assert a > 0 and b > 0 and a <= b * (1.0 + 1e-10)
    error1 = ball_squared_max(c, a, b, 0.0) - 1.0
    error2 = ball_squared_max(c, a, b, separation) - radius**2
    assert error1 < 2e-10 and error2 < 2e-10, (dim, radius, separation, kind, error1, error2)
    assert a * b**(dim - 1) <= radius**dim * (1 + 1e-10)
    if kind == 'contained':
        assert abs(c - separation) < 1e-12
    else:
        assert b > a
        if kind == 'apex':
            assert abs(c + a - 1.0) < 1e-10
            assert abs((c - separation)/(a * ((b/a)**2 - 1.0)) + 1/dim) < 1e-8
            # John weights on the axial pole and the small-sphere latitude.
            w1, w2 = 1.0/(dim+1), dim/(dim+1)
        else:
            assert abs(t1*t2 + 1.0/dim) < 1e-8
            assert 0 < t1 < 1 and -1 < t2 < 0
            w1, w2 = -t2/(t1-t2), t1/(t1-t2)
            delta = b*b - a*a
            assert abs(a*c/delta - t1) < 5e-9
            assert abs(a*(c-separation)/delta - t2) < 5e-9
        assert abs(w1+w2-1) < 1e-12
        assert abs(w1*t1+w2*t2) < 1e-10
        assert abs(w1*t1*t1+w2*t2*t2-1.0/dim) < 1e-10
        assert abs((w1*(1-t1*t1)+w2*(1-t2*t2))/(dim-1)-1.0/dim) < 1e-10
    return kind


def main():
    total = 0
    regimes = set()
    for dim in (2, 3, 5, 10, 20):
        for radius in (0.025, 0.10, 0.21, 0.3, 0.49, 0.50, 0.6, 0.8, 0.95, 0.99):
            for relative in (0, 0.002, 0.02, 0.1, 0.25, 0.5, 0.75, 0.9, 0.98, 0.998):
                separation = max(0.0, 1.0 - radius + 2.0*radius*relative)
                regimes.add(check(dim, radius, separation))
                total += 1
            if radius > 1.0/dim:
                crit = critical_separation(dim, radius)
                for offset in (-1e-5, -1e-7, 0.0, 1e-7, 1e-5):
                    separation = crit + 2*radius*offset
                    if 1-radius < separation < 1+radius:
                        regimes.add(check(dim, radius, separation))
                        total += 1
    assert regimes == {'contained', 'apex', 'two latitudes'}, regimes
    print('PASS: %d dimension/radius/separation configurations.' % total)
    print('PASS: quadratic containment maxima and isotropic contact moments.')
    print('PASS: all three geometric regimes including both sides of transition.')
    print('Finite diagnostics are not a proof of the all-dimensional theorem.')


if __name__ == '__main__':
    main()
