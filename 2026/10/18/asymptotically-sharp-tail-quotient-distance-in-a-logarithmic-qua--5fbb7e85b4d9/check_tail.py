"""Finite diagnostic checks for logarithmic-defect tail geometry.

Run with Python 3. No dependencies. The general theorem is analytic, not a numerical inference.
"""
import cmath
import math
import random


def ht(z, t):
    return z * math.log(max(abs(z), t)) if z else 0j


def F(x, t):
    return sum(ht(z, t) for z in x) - ht(sum(x), t)


def H_finite(x):
    # Between successive positive magnitude breakpoints, F_t is affine in log t;
    # its modulus is convex on that segment, so its maximum is at an endpoint.
    points = {abs(z) for z in x if z}
    if sum(x):
        points.add(abs(sum(x)))
    return max((abs(F(x, t)) for t in points), default=0.0)


def qnorm_finite(x, theta):
    return sum(abs(z) for z in x) + theta * H_finite(x)


if __name__ == '__main__':
    checks = 0
    for m in (2, 3, 6, 10, 32):
        a = [1.0] * m
        b = a + [-1.0] * m
        assert abs(H_finite(a) - m * math.log(m)) < 1e-9
        assert H_finite(b) < 1e-9
        assert abs(qnorm_finite(b, 0.7) - 2 * m) < 1e-9
        checks += 3
    rng = random.Random(271828)
    for m in (6, 10, 20, 40):
        delta = 0.25
        for _ in range(250):
            w = [complex(rng.uniform(-1, 1), rng.uniform(-1, 1))
                 for _ in range(rng.randrange(2, 26))]
            b = sum(abs(z) for z in w)
            if b:
                w = [z * (0.6 * m / b) for z in w]
            x = [1.0] * m + w
            bound = m * (delta * math.log(m) - 2 * math.log(2 / delta))
            assert abs(F(x, 1.0)) >= bound - 1e-8
            assert H_finite(x) >= abs(F(x, 1.0)) - 1e-8
            checks += 2
    print(f'PASS: {checks} finite diagnostic assertions')
