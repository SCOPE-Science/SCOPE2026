#!/usr/bin/env python3
"""Exact-rational checks for weighted star-order isotonic projection and its variation norm.

Run with Python 3 standard library only: python check_star_isotonic.py.
Checks are finite diagnostics; the general theorem is established analytically in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
from random import Random


def project(y, a):
    """Weighted star-order projection by an exact pooled-threshold computation."""
    m = len(y) - 1
    t = y[0]
    mass = a[0]
    for i in sorted(range(m), key=lambda j: (y[j + 1], j)):
        if y[i + 1] < t:
            t = (mass * t + a[i + 1] * y[i + 1]) / (mass + a[i + 1])
            mass += a[i + 1]
    return [t] + [max(y[i + 1], t) for i in range(m)]


def independent_projection(y, a):
    """Independently enumerate every possible strictly/weakly pooled root face."""
    m = len(y) - 1
    feasible = []
    for mask in product((0, 1), repeat=m):
        members = [i for i in range(m) if mask[i]]
        denom = a[0] + sum((a[i + 1] for i in members), F(0))
        level = (a[0] * y[0] + sum((a[i + 1] * y[i + 1] for i in members), F(0))) / denom
        if all(y[i + 1] <= level for i in members) and all(
            y[i + 1] >= level for i in range(m) if not mask[i]
        ):
            feasible.append([level] + [max(y[i + 1], level) for i in range(m)])
    assert feasible, 'The convex optimization oracle found no active face.'
    assert all(z == feasible[0] for z in feasible)
    return feasible[0]


def tv(x, w):
    return sum((w[i] * abs(x[i + 1] - x[0]) for i in range(len(w))), F(0))


def sharp_constant(a, w):
    total = sum(w, F(0))
    return max([F(1)] + [
        a[i + 1] * (total - w[i]) / (w[i] * (a[0] + a[i + 1]))
        for i in range(len(w))
    ])


def all_face_column_norms(a, w):
    m = len(w)
    results = []
    for mask in product((0, 1), repeat=m):
        s = [i for i in range(m) if mask[i]]
        other_mass = sum((w[i] for i in range(m) if not mask[i]), F(0))
        pool_mass = a[0] + sum((a[i + 1] for i in s), F(0))
        cols = []
        for i in range(m):
            if mask[i]:
                cols.append(a[i + 1] * other_mass / (w[i] * pool_mass))
            else:
                cols.append(F(1))
        results.extend(cols)
    return results


def rational_inputs(rng, m):
    a = [F(rng.randrange(1, 13), rng.randrange(1, 7)) for _ in range(m + 1)]
    w = [F(rng.randrange(1, 13), rng.randrange(1, 7)) for _ in range(m)]
    y = [F(rng.randrange(-16, 17), rng.randrange(1, 6)) for _ in range(m + 1)]
    z = [F(rng.randrange(-16, 17), rng.randrange(1, 6)) for _ in range(m + 1)]
    return a, w, y, z


def run():
    rng = Random(20261025)
    counters = {'oracle': 0, 'face_columns': 0, 'pair_inequality': 0,
                'sharp_witness': 0, 'identity_witness': 0, 'uniform_phase': 0,
                'matched_mass_contraction': 0}
    for m in range(1, 8):
        for _ in range(140):
            a, w, y, z = rational_inputs(rng, m)
            p_y, p_z = project(y, a), project(z, a)
            assert p_y == independent_projection(y, a)
            assert p_z == independent_projection(z, a)
            counters['oracle'] += 2
            bound = sharp_constant(a, w)
            norms = all_face_column_norms(a, w)
            assert max(norms) == bound
            counters['face_columns'] += len(norms)
            d = [y[i] - z[i] for i in range(m + 1)]
            e = [p_y[i] - p_z[i] for i in range(m + 1)]
            assert tv(e, w) <= bound * tv(d, w)
            counters['pair_inequality'] += 1
            # Strictly pooled root and precisely one chosen leaf; perturb that leaf.
            for i in range(m):
                y0 = [F(1)] + [F(3)] * m
                y0[i + 1] = F(0)
                y1 = y0[:]
                y1[i + 1] = F(1, 8)
                r = a[i + 1] * (sum(w, F(0)) - w[i]) / (w[i] * (a[0] + a[i + 1]))
                p0, p1 = project(y0, a), project(y1, a)
                assert tv([p1[k] - p0[k] for k in range(m + 1)], w) == r * w[i] / 8
                counters['sharp_witness'] += 1
            # Strictly feasible data with identity projection.
            y0 = [F(0)] + [F(3)] * m
            y1 = y0[:]
            y1[1] += F(1, 8)
            d = [y1[k] - y0[k] for k in range(m + 1)]
            pd = [project(y1, a)[k] - project(y0, a)[k] for k in range(m + 1)]
            assert tv(pd, w) == tv(d, w)
            counters['identity_witness'] += 1
    for m in range(1, 100):
        a = [F(1)] * (m + 1)
        w = [F(1)] * m
        assert sharp_constant(a, w) == max(F(1), F(m - 1, 2))
        counters['uniform_phase'] += 1
    for m in range(1, 50):
        for _ in range(20):
            a = [F(rng.randrange(1, 17)) for _ in range(m + 1)]
            w = a[1:]
            matched = sum(w) <= a[0] + 2 * min(w)
            assert (sharp_constant(a, w) == F(1)) == matched
            counters['matched_mass_contraction'] += 1
    print('CHECKS_OK')
    for k in sorted(counters):
        print(f'{k}: {counters[k]}')
    print('TOTAL:', sum(counters.values()))


if __name__ == '__main__':
    run()
