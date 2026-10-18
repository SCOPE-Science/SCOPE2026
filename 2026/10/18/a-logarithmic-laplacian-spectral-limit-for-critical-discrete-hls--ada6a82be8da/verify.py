#!/usr/bin/env python3
"""Reproducible finite checks of the reciprocal-distance cell decomposition.

The script checks finite algebra and illustrative eigenvalues. It does not
verify the continuum limit, which is an analytic theorem.
"""
import cmath
import math
import random

GAMMA = 0.577215664901532860606512090082402431


def c(k):
    assert k >= 1
    return (k + 1) * math.log(k + 1) + ((k - 1) * math.log(k - 1) if k > 1 else 0.0) - 2 * k * math.log(k)


def d(k):
    return c(k) - 1.0 / k


def norm_sq(u):
    return sum(abs(z) ** 2 for z in u)


def overlap(u, k):
    return sum((u[j].conjugate() * u[j + k]).real for j in range(len(u) - k))


def raw_rayleigh(u):
    return 2 * sum(overlap(u, k) / k for k in range(1, len(u)))


def cell_log_form(u):
    n = len(u)
    return (2 * GAMMA - 2 - 2 * math.log(n)) * norm_sq(u) + 2 * sum(c(k) * overlap(u, k) for k in range(1, n))


def remainder(u):
    n = len(u)
    total = 1 - GAMMA
    partial = sum(d(k) for k in range(1, n))
    s = 2 * norm_sq(u) * (total - partial)
    for k in range(1, n):
        shift_energy = 2 * norm_sq(u) - 2 * overlap(u, k)
        s += d(k) * shift_energy
    return s


def power_eigenvalue(n, rounds=270):
    vec = [1.0 / math.sqrt(n)] * n
    for _ in range(rounds):
        mul = [sum(vec[j] / abs(i - j) for j in range(n) if i != j) for i in range(n)]
        z = math.sqrt(sum(t*t for t in mul))
        vec = [t / z for t in mul]
    q = raw_rayleigh(vec)
    return q


def main():
    rng = random.Random(24011)
    checks = 0
    for k in range(1, 300):
        assert d(k) > 0.0
        checks += 1
    for m in [1, 2, 3, 7, 17, 31, 101, 256]:
        lhs = sum(d(k) for k in range(1, m + 1))
        rhs = (m + 1) * math.log(m + 1) - m * math.log(m) - sum(1/k for k in range(1, m + 1))
        assert abs(lhs-rhs) < 2e-10
        checks += 1
    for n in [2, 3, 4, 7, 13, 21, 40, 64]:
        for rep in range(18):
            u = [complex(rng.uniform(-1, 1), rng.uniform(-1, 1)) for _ in range(n)]
            z = math.sqrt(norm_sq(u))
            u = [v / z for v in u]
            lhs = raw_rayleigh(u) - 2 * math.log(n)
            rhs = cell_log_form(u) + remainder(u)
            assert remainder(u) > -1e-11
            assert abs(lhs-rhs) < 2e-10, (n, lhs, rhs)
            checks += 2
        # Exact unweighted-vector Rayleigh identity.
        ones = [1.0 / math.sqrt(n)] * n
        h = sum(1.0/k for k in range(1, n))
        assert abs(raw_rayleigh(ones)-(2*h-2*(n-1)/n)) < 1e-11
        checks += 1
    for n in [16, 32, 64, 96]:
        q = power_eigenvalue(n)
        const = q - 2*math.log(n)
        assert 2*GAMMA-2-1e-9 <= const <= 2*GAMMA+1e-9
        print('N=%3d  top-eigenvalue-2logN = %.9f' % (n, const))
        checks += 1
    print('FINITE_CHECKS_OK', checks)


if __name__ == '__main__':
    main()
