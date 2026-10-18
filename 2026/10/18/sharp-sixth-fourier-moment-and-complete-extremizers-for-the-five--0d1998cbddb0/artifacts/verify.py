#!/usr/bin/env python3
"""Exact coefficient identities and independent finite-grid checks for a five-mode sixth moment.

Run with Python 3 standard library: python artifacts/verify.py
Finite checks complement, but do not replace, the proof in RESULT.md.
"""
from collections import defaultdict
from fractions import Fraction as Fr
from itertools import product
from math import cos, pi, sin, sqrt
from random import Random


def polyvar(i, n):
    e = [0] * n
    e[i] = 1
    return {tuple(e): Fr(1)}


def const(value, n):
    return {tuple([0] * n): Fr(value)} if value else {}


def plus(*seq):
    out = defaultdict(Fr)
    for p in seq:
        for k, v in p.items():
            out[k] += v
    return {k: v for k, v in out.items() if v}


def mul(p, q):
    out = defaultdict(Fr)
    for a, x in p.items():
        for b, y in q.items():
            out[tuple(v + w for v, w in zip(a, b))] += x * y
    return {k: v for k, v in out.items() if v}


def sc(p, r):
    return {k: v * Fr(r) for k, v in p.items() if v * Fr(r)}


def power(p, n):
    res = const(1, len(next(iter(p))))
    for _ in range(n):
        res = mul(res, p)
    return res


def triple_coefficient_polynomial():
    # Coordinates: (centre, +horizontal, -horizontal, +vertical, -vertical).
    vv = [polyvar(i, 5) for i in range(5)]
    freqs = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
    triple = defaultdict(dict)
    for ix in product(range(5), repeat=3):
        key = (sum(freqs[j][0] for j in ix), sum(freqs[j][1] for j in ix))
        val = mul(mul(vv[ix[0]], vv[ix[1]]), vv[ix[2]])
        triple[key] = plus(triple[key], val)
    return plus(*(power(value, 2) for value in triple.values())), len(triple)


def invariant_moment(k, R, T, Z, W):
    # Every coefficient below follows by collecting independent triple-sum fibers.
    return plus(
        power(k, 3),
        mul(power(k, 2), plus(sc(R, 9), sc(T, 9), sc(Z, 12), sc(W, 12))),
        mul(k, plus(
            sc(power(R, 2), 9), sc(power(T, 2), 9), sc(mul(R, T), 36),
            sc(mul(R, Z), 18), sc(mul(T, W), 18),
            sc(mul(R, W), 36), sc(mul(T, Z), 36),
            sc(power(Z, 2), 18), sc(power(W, 2), 18), sc(mul(Z, W), 72))),
        power(R, 3), power(T, 3),
        sc(mul(mul(R, T), plus(R, T)), 9),
        sc(mul(plus(R, sc(T, 3)), power(Z, 2)), 6),
        sc(mul(plus(sc(R, 3), T), power(W, 2)), 6),
        sc(mul(mul(plus(R, T), Z), W), 36))


def exact_symbolic_tests():
    c, a, b, d, e = [polyvar(j, 5) for j in range(5)]
    k, R, T, Z, W = power(c, 2), plus(power(a, 2), power(b, 2)), \
                   plus(power(d, 2), power(e, 2)), mul(a, b), mul(d, e)
    direct, fibers = triple_coefficient_polynomial()
    assert fibers == 25, ("unexpected number of triple-sum fibers", fibers)
    predicted = invariant_moment(k, R, T, Z, W)
    assert direct == predicted, "sextic invariant identity disagrees with independent convolution"
    assert len(direct) == 50, len(direct)
    # Verify the second, equally important reduction in symbolic mass variables.
    kk, rr, tt = [polyvar(j, 3) for j in range(3)]
    halfR, halfT = sc(rr, Fr(1, 2)), sc(tt, Fr(1, 2))
    sym = invariant_moment(kk, rr, tt, halfR, halfT)
    U, v = plus(rr, tt), plus(rr, sc(tt, -1))
    claimed = sc(plus(
        sc(power(U, 3), 25), sc(mul(power(U, 2), kk), 135),
        sc(mul(U, power(kk, 2)), 60), sc(power(kk, 3), 4),
        sc(mul(plus(U, sc(kk, 3)), power(v, 2)), -15)), Fr(1, 4))
    assert sym == claimed, 'mass split deficit identity fails'
    # Check cubic x: after the preceding reductions, M=1, k=x, U=1-x.
    x = polyvar(0, 1)
    one = const(1, 1)
    u = plus(one, sc(x, -1))
    one_var = sc(plus(
        sc(power(u, 3), 25), sc(mul(power(u, 2), x), 135),
        sc(mul(u, power(x, 2)), 60), sc(power(x, 3), 4)), Fr(1, 4))
    expect = plus(const(Fr(25, 4), 1), sc(x, 15),
                  sc(power(x, 2), Fr(-135, 4)), sc(power(x, 3), Fr(27, 2)))
    assert one_var == expect, 'one-variable polynomial mismatch'
    return fibers, len(direct)


def triple_moment(v):
    keys = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
    vals = defaultdict(complex)
    for j, k, l in product(range(5), repeat=3):
        key = (keys[j][0] + keys[k][0] + keys[l][0],
               keys[j][1] + keys[k][1] + keys[l][1])
        vals[key] += v[j] * v[k] * v[l]
    return sum(abs(x) ** 2 for x in vals.values())


def grid_moment(v, n):
    keys = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
    s = 0.0
    for i, j in product(range(n), repeat=2):
        z = complex(cos(2 * pi * i / n), sin(2 * pi * i / n))
        w = complex(cos(2 * pi * j / n), sin(2 * pi * j / n))
        f = v[0] + v[1] * z + v[2] / z + v[3] * w + v[4] / w
        s += abs(f) ** 6
    return s / n ** 2


def numeric_tests():
    root = sqrt(105)
    K = Fr(25, 8) + 35 * root / 72
    xstar = Fr(5, 6) - root / 18
    arm = sqrt((1 - xstar) / 4)
    center = sqrt(xstar)
    v = [center, arm, arm, arm, arm]
    assert abs(triple_moment(v) - K) < 1e-10
    rng = Random(20261014)
    grids_checked = 0
    for n in (7, 8, 9, 11):
        assert abs(grid_moment(v, n) - K) < 5e-10
        grids_checked += 1
    for _ in range(120):
        v = [complex(rng.uniform(-2, 2), rng.uniform(-2, 2)) for j in range(5)]
        M = sum(abs(z) ** 2 for z in v)
        continuous = triple_moment(v)
        assert continuous <= K * M ** 3 * (1 + 2e-12)
        n = (7, 9, 11)[_ % 3]
        assert abs(grid_moment(v, n) - continuous) < 2e-8 * M ** 3
        grids_checked += 1
    # Equality phases are the restrictions of arbitrary torus characters.
    for j in range(36):
        alpha = j * .123
        beta = j * .257
        lam = complex(cos(j * .19), sin(j * .19))
        v = [lam * center, lam * arm * complex(cos(alpha), sin(alpha)),
             lam * arm * complex(cos(-alpha), sin(-alpha)),
             lam * arm * complex(cos(beta), sin(beta)),
             lam * arm * complex(cos(-beta), sin(-beta))]
        assert abs(triple_moment(v) - K) < 1e-10
    v = [center, arm, arm, arm, arm]
    assert grid_moment(v, 6) > K + 1e-5, 'order-six aliasing is strict'
    return K, float(xstar), grids_checked


if __name__ == '__main__':
    fiber_count, term_count = exact_symbolic_tests()
    sharp, xstar, grid_count = numeric_tests()
    print('VERIFY_OK', 'triple_fibers=', fiber_count,
          'polynomial_monomials=', term_count,
          'finite_grid_comparisons=', grid_count,
          'sharp_sixth_power=', format(sharp, '.15f'),
          'central_mass_fraction=', format(xstar, '.15f'),
          'order_6_aliasing=STRICT')
