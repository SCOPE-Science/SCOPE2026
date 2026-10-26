"""Exact rational checks for all-to-all best-response second moments.

This file checks finite identities only; the proof for all populations/times is analytical.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt


def next_error(e, delta, i):
    out = list(e)
    out[i] = -delta * sum((e[j] for j in range(len(e)) if j != i), F(0))
    return tuple(out)


def moment_step(n, d, square_sum, sum_squares):
    return ((1-d)**2 * ((n-2)*square_sum + sum_squares)/n,
            (d*d*(n-2)*square_sum + (n-1+d*d)*sum_squares)/n)


def direct_moments(n, d, e0, horizon):
    out = []
    for t in range(horizon + 1):
        total_u = F(0)
        total_v = F(0)
        for indices in product(range(n), repeat=t):
            e = e0
            for i in indices:
                e = next_error(e, d, i)
            total_u += sum(e, F(0))**2
            total_v += sum((z*z for z in e), F(0))
        denom = n**t
        out.append((total_u/denom, total_v/denom))
    return out


def rho(n, d):
    d = float(d)
    a = (n - 2) * (1-d)**2
    b = (1-d)**2
    c = (n - 2) * d*d
    f = n - 1 + d*d
    return (a+f + sqrt((a-f)**2+4*b*c))/(2*n)


def run():
    configs = [
        (3,F(1,4),5),(3,F(1,2),5),(3,F(3,4),5),
        (4,F(1,5),5),(4,F(2,3),5),
        (5,F(1,3),5),(5,F(3,4),5),
        (6,F(1,3),4),(6,F(2,3),4),
    ]
    tests = 0
    enumerated = 0
    for n, d, horizon in configs:
        q = F(1, 1) / (1 + (n-1)*d)
        e0 = tuple(F((i % 3) - 1, 5000 * (i+1)) for i in range(n))
        assert all(F(0) < q+v < F(1) for v in e0)
        direct = direct_moments(n, d, e0, horizon)
        current = (sum(e0, F(0))**2, sum((v*v for v in e0), F(0)))
        for t, actual in enumerate(direct):
            assert actual == current, (n, d, t, actual, current)
            tests += 2
            if t < horizon: current = moment_step(n, d, *current)
        enumerated += sum(n**t for t in range(horizon+1))
        r = rho(n, d)
        assert 0 < r < 1
        tests += 1
    for n in [3,4,10,30]:
        for d in [F(1,5),F(1,2),F(4,5),F(9,10)]:
            r=rho(n,d)
            assert 0 < r < 1
            # Positive eigenvalue branch equals nonnegative transfer-matrix Perron root.
            a=(n-2)*(1-float(d))**2/n
            b=(1-float(d))**2/n
            c=(n-2)*float(d)**2/n
            f=(n-1+float(d)**2)/n
            assert abs((r-a)*(r-f)-b*c) < 1e-12
            tests+=2
    print(f'EXACT_CHECKS_PASSED {tests}; enumerated_update_strings={enumerated}; configs={len(configs)}')

if __name__ == '__main__': run()
