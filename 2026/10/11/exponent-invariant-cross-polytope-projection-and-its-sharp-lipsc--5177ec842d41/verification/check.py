"""Supplementary finite numerical/rational checks for cross-polytope metric projection.

This script is supplementary: all-parameter conclusions are proved analytically.
"""
from fractions import Fraction
import math
import random


def projection(x, radius):
    if sum(map(abs, x)) <= radius:
        return list(x)
    values = sorted((abs(t) for t in x), reverse=True)
    prefix = 0.0
    tau = None
    for k, value in enumerate(values, 1):
        prefix += value
        guess = (prefix - radius) / k
        if guess < value and (k == len(values) or guess >= values[k]):
            tau = guess
            break
    assert tau is not None
    return [math.copysign(max(abs(v) - tau, 0.0), v) for v in x]


def norm(x, p):
    return sum(abs(v)**p for v in x)**(1.0/p)


def center(x):
    avg = sum(x)/len(x)
    return [t-avg for t in x]


def exact_checks():
    for x in [(1, 1, -2), (3, 7, -10), (-5, -2, 7), (5, -3, -2), (0, 3, -3)]:
        f = [Fraction(t) for t in x]
        assert sum(f) == 0
        assert sum(t**4 for t in f) == Fraction(1, 2)*sum(t*t for t in f)**2
    for n in range(2, 9):
        for i in range(n):
            col = [Fraction(-1,n) for _ in range(n)]
            col[i] += 1
            assert sum(col) == 0
    print('rational algebraic identities verified')


def numeric_checks():
    t = 2**(1/3)
    x = [1.0, 1.0, -t]
    theoretical = ((1+t)**3 / 9)**0.25
    observed = norm(center(x), 4)/norm(x, 4)
    assert abs(theoretical - observed) < 2e-13
    assert theoretical > 1.06
    assert abs(theoretical - 1.0641658628581188) < 2e-14

    # A realizable full-support affine cell has Jacobian the centering map.
    tau = 2.0
    radius = 3.0
    base = [tau+radius/3] * 3
    eps = 1e-5
    shifted = [base[i]+eps*x[i] for i in range(3)]
    ratio = norm([a-b for a,b in zip(projection(shifted,radius),projection(base,radius))],4)/norm([eps*v for v in x],4)
    assert abs(ratio - theoretical) < 1e-9

    # Random inputs test the exact threshold constraint and the KKT condition
    # for several ambient exponents, not the global optimization theorem.
    rng = random.Random(1729)
    for n in (2, 3, 4, 7):
        for _ in range(150):
            z = [rng.uniform(-5, 5) for _ in range(n)]
            r = rng.uniform(0.2, 2.0)
            q = projection(z, r)
            assert sum(map(abs,q)) <= r + 2e-12
            if sum(map(abs,z)) > r:
                assert abs(sum(map(abs,q)) - r) <= 2e-12
                active = [i for i in range(n) if q[i] != 0]
                drops = [abs(z[i])-abs(q[i]) for i in active]
                assert max(drops)-min(drops) < 2e-12
                for p in (1.2, 2.0, 4.0, 11.0):
                    derivative = [p*abs(z[i]-q[i])**(p-1) for i in active]
                    assert max(derivative)-min(derivative) < 1e-6
    print('CROSSPOLYTOPE_LP_METRIC_PROJECTION_CHECK_OK')
    print('exact_minimal_dim_3_p4_Lipschitz',repr(theoretical))


if __name__ == '__main__':
    exact_checks()
    numeric_checks()
