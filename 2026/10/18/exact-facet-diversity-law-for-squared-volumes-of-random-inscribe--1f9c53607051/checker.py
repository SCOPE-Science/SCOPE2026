#!/usr/bin/env python3
"""Reproduce exact squared-volume laws for facet-sampled random simplices."""
from fractions import Fraction
from itertools import permutations
from math import factorial
import numpy as np


def theorem_strat(d):
    m = d + 1
    return Fraction(factorial(m), m ** (m - 1) * d ** m)


def theorem_iid(d, weights):
    weights = [Fraction(w) for w in weights]
    assert sum(weights) == 1 and min(weights) >= 0
    return theorem_strat(d) * (1 - sum(w*w for w in weights))


def exact_moment(d, weights=None):
    """Independent expansion of det^2 by two permutations (no mixed-discriminant identity)."""
    m = d+1
    if weights is None:
        A = []
        for i in range(m):
            A.append([[Fraction((2 if j == k else 1), d*m)
                      if i != j and i != k else Fraction(0)
                      for k in range(m)] for j in range(m)])
    else:
        weights = [Fraction(w) for w in weights]
        C = [[sum(weights[i] * (Fraction(2 if j == k else 1, d*m)
                      if i != j and i != k else 0)
                        for i in range(m)) for k in range(m)] for j in range(m)]
        A = [C] * m
    perms = list(permutations(range(m)))
    signs = []
    for p in perms:
        inv = sum(p[i] > p[j] for i in range(m) for j in range(i+1,m))
        signs.append(-1 if inv % 2 else 1)
    total = Fraction(0)
    for a, p in enumerate(perms):
        for b, q in enumerate(perms):
            v = signs[a]*signs[b]
            for i in range(m):
                v *= A[i][p[i]][q[i]]
                if not v:
                    break
            total += v
    return total


def monte_carlo(d, weights=None, n=200000, seed=4301):
    rng = np.random.default_rng(seed)
    m = d+1
    samples = np.zeros((n, m, m))
    if weights is None:
        labels = np.broadcast_to(np.arange(m), (n,m))
    else:
        labels = rng.choice(m, size=(n,m), p=np.asarray(weights,dtype=float))
    for label in range(m):
        rows, cols = np.nonzero(labels==label)
        if len(rows):
            coords = rng.dirichlet(np.ones(d), size=len(rows))
            face_indices = np.flatnonzero(np.arange(m)!=label)
            samples[rows[:,None], cols[:,None], face_indices[None,:]] = coords
    values = np.linalg.det(samples)**2
    empirical = float(values.mean())
    stderr = float(values.std(ddof=1)/np.sqrt(n))
    expected = float(theorem_strat(d) if weights is None else theorem_iid(d,weights))
    assert abs(empirical-expected) < 6*stderr, (d, weights, empirical, expected, stderr)
    return empirical, expected, stderr


def run():
    cases = 0
    for d in range(1,5):
        expected = theorem_strat(d)
        observed = exact_moment(d)
        assert observed == expected, ('stratified',d,observed,expected)
        print(f'stratified exact d={d}: {observed}')
        cases += 1
        m = d+1
        for weights in [([Fraction(1,m)] * m),
                        ([Fraction(i+1,m*(m+1)//2) for i in range(m)]),
                        ([Fraction(1,2), Fraction(1,2)] + [Fraction(0)]*(m-2))]:
            observed = exact_moment(d, weights)
            expected = theorem_iid(d, weights)
            assert observed == expected, ('iid',d,weights,observed,expected)
            cases += 1
            print(f'iid exact d={d}, pi={weights}: {observed}')
    for d in (2,3,4):
        m=d+1
        for weights in (None, [Fraction(i+1,sum(range(1,m+1))) for i in range(m)]):
            estimate, expected, stderr = monte_carlo(d,weights)
            print(f'Monte Carlo d={d}, pi={weights}: {estimate:.9g}, theory={expected:.9g}, se={stderr:.3g}')
            cases += 1
    print(f'PASS: {cases} exact and numerical comparisons, independent double-permutation expansion')


if __name__=='__main__':
    run()
