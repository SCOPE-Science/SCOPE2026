#!/usr/bin/env python3
"""Exact McKay recurrence and direct 600-cell Chebyshev Gram checks.

Optional numerical Gram verification uses NumPy (Python 3, numpy>=1.20).
This is a finite cross-check, not the proof of the all-degree statements.
"""
import itertools
import math

D = (1, 2, 3, 4, 5, 6, 4, 2, 3)
EDGES = ((0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (5, 8))
A = [[0 for _ in range(9)] for _ in range(9)]
for i, j in EDGES:
    A[i][j] = A[j][i] = 1


def multiplicities(bound):
    prior = [0] * 9
    now = [1] + [0] * 8
    result = []
    for degree in range(bound + 1):
        assert all(v >= 0 for v in now)
        assert sum(d * v for d, v in zip(D, now)) == degree + 1
        result.append(tuple(now))
        next_ = [sum(A[i][j] * now[j] for j in range(9)) - prior[i]
                 for i in range(9)]
        prior, now = now, next_
    return result


def rank(multiplicity):
    return sum(d * d for d, c in zip(D, multiplicity) if c > 0)


def vertices():
    phi = (1 + math.sqrt(5)) / 2
    pts = []
    for i in range(4):
        for sign in (-1, 1):
            v = [0.] * 4
            v[i] = float(sign)
            pts.append(v)
    for signs in itertools.product((-1, 1), repeat=4):
        pts.append([s / 2 for s in signs])
    for perm in itertools.permutations(range(4)):
        parity = sum(perm[i] > perm[j]
                     for i in range(4) for j in range(i + 1, 4)) % 2
        if parity:
            continue
        for signs in itertools.product((-1, 1), repeat=3):
            v = (0., signs[0] / 2, signs[1] * phi / 2,
                 signs[2] / (2 * phi))
            pts.append([v[perm[i]] for i in range(4)])
    return pts


def main():
    import numpy as np
    checks = 0
    m = multiplicities(200)
    assert sum(d * d for d in D) == 120
    checks += 1
    examples = {
        6: (0, 0, 0, 0, 0, 0, 1, 0, 1),
        12: (1, 0, 1, 0, 1, 0, 1, 0, 0),
        13: (0, 1, 0, 1, 0, 1, 0, 1, 0),
        27: (0, 0, 0, 2, 0, 3, 0, 1, 0),
        29: (0, 1, 0, 2, 0, 3, 0, 1, 0),
        31: (0, 2, 0, 2, 0, 3, 0, 1, 0),
        33: (0, 1, 0, 3, 0, 3, 0, 1, 0),
        35: (0, 1, 0, 2, 0, 4, 0, 1, 0),
        37: (0, 1, 0, 2, 0, 4, 0, 2, 0),
        39: (0, 1, 0, 3, 0, 4, 0, 1, 0),
        58: (0, 0, 3, 0, 5, 0, 4, 0, 3),
        60: (2, 0, 3, 0, 5, 0, 4, 0, 3),
        62: (1, 0, 4, 0, 5, 0, 4, 0, 3),
        64: (1, 0, 3, 0, 6, 0, 4, 0, 3),
        66: (1, 0, 3, 0, 5, 0, 5, 0, 4),
        68: (1, 0, 3, 0, 6, 0, 5, 0, 3),
        70: (1, 0, 4, 0, 6, 0, 4, 0, 4),
    }
    for degree, wanted in examples.items():
        assert m[degree] == wanted, (degree, m[degree], wanted)
        checks += 1
    assert rank(m[27]) == 56 and rank(m[58]) == 59
    checks += 1
    for degree in range(201):
        assert rank(m[degree]) <= 60
        if degree % 2 and degree >= 29:
            assert rank(m[degree]) == 60
        if degree % 2 == 0 and degree >= 60:
            assert rank(m[degree]) == 60
        if degree + 12 <= 200:
            assert all(x <= y for x, y in zip(m[degree], m[degree + 12]))
        positive = [120 * value / d for d, value in zip(D, m[degree])
                    if value > 0]
        perfectly_tight = (rank(m[degree]) == 60 and
                           max(positive) == min(positive))
        assert perfectly_tight == (degree % 30 == 29)
        if degree + 60 <= 200:
            expected_step = tuple(d if i % 2 == degree % 2 else 0
                                  for i, d in enumerate(D))
            assert tuple(m[degree + 60][i] - m[degree][i]
                         for i in range(9)) == expected_step
        checks += 1

    v = np.array(vertices(), dtype=float)
    assert v.shape == (120, 4)
    assert len({tuple(np.round(p, 12)) for p in v}) == 120
    assert np.max(np.abs(np.sum(v * v, axis=1) - 1)) < 1e-12
    assert {tuple(np.round(p, 12)) for p in v} == {
        tuple(np.round(-p, 12)) for p in v}
    checks += 4
    x = v @ v.T
    u_previous = np.ones((120, 120), dtype=float)
    u_current = 2 * x
    for degree in range(15):
        kernel = u_previous if degree == 0 else u_current
        observed = np.linalg.eigvalsh(kernel)
        predicted = []
        for d, c in zip(D, m[degree]):
            predicted += [120 * c / d] * (d * d)
        predicted.sort()
        error = float(np.max(np.abs(observed - predicted)))
        assert error < 1e-8, (degree, error)
        checks += 1
        if degree >= 1:
            u_previous, u_current = u_current, 2 * x * u_current - u_previous
    # Direct 120-by-120 verification of the nontrivial 60-step kernel identity.
    jmat = np.zeros((120, 120), dtype=float)
    for i in range(120):
        antipode = int(np.argmin(np.sum((v + v[i])**2, axis=1)))
        assert np.sum((v[antipode] + v[i])**2) < 1e-24
        jmat[i, antipode] = 1.
    identity = np.eye(120)
    u_previous = np.ones((120, 120), dtype=float)
    u_current = 2 * x
    initial = {0: u_previous, 1: u_current}
    for degree in range(2, 62):
        u_previous, u_current = u_current, 2 * x * u_current - u_previous
        if degree in (60, 61):
            base = degree - 60
            target = 60 * (identity + (-1)**base * jmat)
            error = float(np.max(np.abs(u_current - initial[base] - target)))
            assert error < 1e-8, (degree, error)
            checks += 1
    print("PASS", checks, "assertion groups; ranks at degrees 27,29,58,60:",
          [rank(m[j]) for j in (27, 29, 58, 60)])


if __name__ == "__main__":
    main()
