#!/usr/bin/env python3
"""Numerical and exact finite checks of a finite-field quadratic chirp theorem.

Pure Python 3, standard library only. Run `python3 verify.py`.
Finite tests corroborate; proofs for all odd primes and ranks are analytic.
"""
import cmath
import itertools
import math
import random

PI = math.pi


def points(p, d):
    return list(itertools.product(range(p), repeat=d))


def q_diag(x, a, p):
    return sum(t * xx * xx for t, xx in zip(a, x)) % p


def c_energy(p, xs, q, theta):
    d = len(xs[0])
    vals = {x: cmath.exp(2j * PI * q(x) / p + 1j * t)
            for x, t in zip(xs, theta)}
    out = 0.0
    for h in xs:
        if not any(h):
            continue
        c = sum(vals[tuple((xx + hh) % p for xx, hh in zip(x, h))] *
                vals[x].conjugate() for x in xs)
        out += abs(c) ** 2
    return out


def eta_hessian(p, xs, q, b, theta):
    n = len(xs)
    ans = 0.0
    for h in xs:
        if not any(h):
            continue
        ft = sum(t * cmath.exp(-2j * PI * b(h, x) / p)
                 for x, t in zip(xs, theta)) / n
        ans += math.sin(2 * PI * q(h) / p) ** 2 * abs(ft) ** 2
    return 8 * n * n * ans


def formula_zero_count(p, d, determinant):
    if d % 2:
        return p ** (d - 1)
    eta = ((-1) ** (d // 2) * determinant) % p
    sign = 1 if pow(eta, (p - 1) // 2, p) == 1 else -1
    return p ** (d - 1) + (p - 1) * p ** (d // 2 - 1) * sign


def check_count(p, a):
    xs = points(p, len(a))
    determinant = math.prod(a) % p
    observed = sum(q_diag(x, a, p) == 0 for x in xs)
    expected = formula_zero_count(p, len(a), determinant)
    assert observed == expected, ('gauss-zero-count', p, a, observed, expected)


def check_hessian(p, a):
    xs = points(p, len(a))
    q = lambda x: q_diag(x, a, p)
    b = lambda h, x: sum(2 * aa * hh * xx
                         for aa, hh, xx in zip(a, h, x)) % p
    random.seed(100 * p + len(a))
    theta = [random.uniform(-1, 1) for _ in xs]
    mean = sum(theta) / len(theta)
    theta = [t - mean for t in theta]
    eps = 2e-5
    zero = [0.] * len(xs)
    e0 = c_energy(p, xs, q, zero)
    ep = c_energy(p, xs, q, [eps * t for t in theta])
    em = c_energy(p, xs, q, [-eps * t for t in theta])
    observed = (ep + em - 2 * e0) / eps ** 2
    predicted = eta_hessian(p, xs, q, b, theta)
    assert abs(observed - predicted) < 1e-3 + 3e-5 * predicted, (
        'hessian', p, a, observed, predicted)
    return abs(observed - predicted) / max(1, predicted)


def check_flat_family(p, d, q, b, s):
    xs = points(p, d)
    assert q(s) == 0 and any(s)
    f = [math.sin(j + .21) + .17 * j * j for j in range(p)]
    theta = [f[b(s, x)] for x in xs]
    err = c_energy(p, xs, q, theta)
    assert err < 1e-17 * len(xs) ** 3, ('flat-family', p, d, err)


def main():
    counts = 0
    for p in (3, 5, 7):
        for d in (1, 2, 3):
            if p == 7 and d == 3:
                continue
            for a in itertools.product(range(1, p), repeat=d):
                check_count(p, a)
                counts += 1
    max_rel = 0.0
    tests = ((3, (1,)), (3, (1, 1)), (3, (1, 1, 1)),
             (5, (1,)), (5, (1, 1)), (5, (1, 2)),
             (5, (1, 1, 1)), (7, (1,)), (7, (1, 1)),
             (7, (1, 3)))
    for p, a in tests:
        max_rel = max(max_rel, check_hessian(p, a))
    for p in (3, 5, 7):
        q = lambda x: x[0] * x[1] % p
        b = lambda h, x: (h[0] * x[1] + h[1] * x[0]) % p
        check_flat_family(p, 2, q, b, (1, 0))
        check_flat_family(p, 2, q, b, (0, 1))
    p = 3
    q = lambda x: (x[0] * x[1] + x[2] * x[2]) % p
    b = lambda h, x: (h[0] * x[1] + h[1] * x[0] + 2 * h[2] * x[2]) % p
    check_flat_family(p, 3, q, b, (1, 0, 0))
    print(f'VERIFY_OK quadratic_zero_counts={counts} hessian_directional={len(tests)} '
          f'flat_families=7 maximum_relative_hessian_error={max_rel:.3e}')


if __name__ == '__main__':
    main()
