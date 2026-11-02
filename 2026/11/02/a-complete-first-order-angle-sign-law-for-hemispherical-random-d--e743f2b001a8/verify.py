#!/usr/bin/env python3
"""Finite diagnostics for signed hemisphere-angle asymptotics (NumPy required).

These calculations test identities and sample data; they are not an infinite proof.
"""
import itertools
import math
import numpy as np


def predicted(signs, d, k):
    edges = list(itertools.combinations(range(k), 2))
    idx = {e: j for j, e in enumerate(edges)}
    edge_sum = sum(signs)
    tri_sum = sum(signs[idx[(i, j)]] * signs[idx[(i, h)]] * signs[idx[(j, h)]]
                  for i, j, h in itertools.combinations(range(k), 3))
    c = (2 / math.pi) ** 1.5
    return 2 ** (-len(edges)) * (1 + c * (edge_sum + tri_sum) / math.sqrt(d))


def wick_expectation(indices):
    # Exact even Gaussian moments via recursive Isserlis pairings.
    if not indices:
        return 1
    first = indices[0]
    return sum(wick_expectation(indices[1:j] + indices[j + 1:])
               for j in range(1, len(indices)) if indices[j] == first)


def gram_third_moments():
    vertices = range(5)
    edges = list(itertools.combinations(vertices, 2))
    for a, b in itertools.combinations_with_replacement(edges, 2):
        # Covariances are 1 on the diagonal, zero between distinct edges.
        m = wick_expectation((*a, *b))
        assert m == int(a == b)
    triples = 0
    for ee in itertools.combinations(edges, 3):
        mult = wick_expectation(tuple(v for edge in ee for v in edge))
        degrees = {v: sum(v in e for e in ee) for v in vertices}
        is_triangle = sum(deg == 2 for deg in degrees.values()) == 3
        assert mult == int(is_triangle), (ee, mult)
        triples += 1
    print('WICK_CHECK_OK', len(edges), triples)


def sample_patterns(k=3, d=300, rep=400_000, seed=260):
    rng = np.random.default_rng(seed)
    edges = list(itertools.combinations(range(k), 2))
    counts = np.zeros(2 ** len(edges), dtype=int)
    chunk = 5000
    for _ in range(0, rep, chunk):
        batch = min(chunk, rep - _)
        z = rng.standard_normal((batch, k, d))
        z[:, :, 0] = np.abs(z[:, :, 0])
        codes = np.zeros(batch, dtype=np.int32)
        for j, (a, b) in enumerate(edges):
            codes += ((z[:, a, :] * z[:, b, :]).sum(axis=1) > 0).astype(np.int32) << j
        counts += np.bincount(codes, minlength=len(counts))
    for c in range(len(counts)):
        s = [1 if (c >> j) & 1 else -1 for j in range(len(edges))]
        p = predicted(s, d, k)
        empirical = counts[c] / rep
        # The unknown second-order constant is bounded *empirically*, not certified.
        assert abs(empirical - p) < 0.008
        print('pattern', ''.join('+' if x > 0 else '-' for x in s),
              'empirical', round(empirical, 6), 'first_order', round(p, 6))


def main():
    for k in (3, 4, 5):
        m = k * (k - 1) // 2
        total_correction = 0
        for s in itertools.product((-1, 1), repeat=m):
            total_correction += predicted(s, 1000, k) - 2 ** (-m)
        assert abs(total_correction) < 1e-12
    print('NORMALIZATION_OK')
    gram_third_moments()
    sample_patterns()
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
