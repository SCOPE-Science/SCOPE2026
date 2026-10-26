#!/usr/bin/env python3
"""Independent standard-library checks of analytic identities in RESULT.md.
Finite checks are consistency tests, not substitutes for the stated proof.
"""
import math


def progeny_pgf(theta, z):
    assert 0 < theta <= 1 and 0 < z <= 1 if theta == 1 else 0 < z < math.exp(theta-1)/theta
    # The minimal nonnegative fixed point, obtained by increasing iteration.
    f = 0.0
    for _ in range(300000):
        v = z * math.exp(theta * (f-1.0))
        if abs(v-f) < 2e-14:
            return v
        f = v
    raise ArithmeticError('iteration not converged')


def borel_mass(theta, k):
    return math.exp(-theta*k + (k-1)*math.log(theta*k) - math.lgamma(k+1))


def check():
    count = 0
    for theta in [0.13, 0.4, 0.7, 0.91]:
        zstar = math.exp(theta-1)/theta
        qstar = 1 - 1/zstar
        assert zstar > 1 and 0 < qstar < 1
        count += 2
        z = 1 + (zstar-1)*0.12
        f = progeny_pgf(theta, z)
        assert 1 < f < 1/theta
        assert abs(f - z * math.exp(theta*(f-1))) < 3e-12
        count += 2
        # Independent finite Borel-series lower bound on PGF, tail must be positive.
        partial = sum(math.exp(-theta*k + (k-1)*math.log(theta*k) - math.lgamma(k+1) + k*math.log(z)) for k in range(1, 12000))
        assert partial > 1 and partial <= f + 1e-10
        assert abs(f-partial) < 3e-7
        count += 3
    for t in [0.1, 0.25, 1.0, 3.0, 20.0, 100.0]:
        z = t/(t+1)
        f = progeny_pgf(1.0, z)
        u = 1-f
        h = math.log1p(1/t)
        assert 0 < u < 1
        assert abs(-math.log1p(-u)-u-h) < 1e-10
        assert u*u <= 2*h + 1e-10
        assert u <= math.sqrt(2/t)+1e-10
        count += 4
    print(f'PASS: {count} independent numerical algebra/series checks')


if __name__ == '__main__':
    check()
