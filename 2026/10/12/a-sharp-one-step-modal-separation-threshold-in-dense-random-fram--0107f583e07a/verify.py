#!/usr/bin/env python3
"""Standalone checks for the color-neighborhood modal depth-one theorem.
Only finite consistency checks are claimed: the probabilistic limit is proved analytically.
"""
import itertools
import math
import random
from collections import defaultdict


def depth_one_signature(n, edges, colors, q):
    nbr = [0] * n
    for v in range(n):
        for u in range(n):
            if edges[v] >> u & 1:
                nbr[v] |= 1 << colors[u]
    return [(colors[v], nbr[v]) for v in range(n)]


def depth_one_boolean_partition(n, edges, colors, q):
    """Enumerate every valuation Boolean union and all its diamonds."""
    signatures = [0] * n
    m = 0
    for pattern in range(1 << q):
        truth = sum(1 << v for v in range(n) if (pattern >> colors[v]) & 1)
        diam = [int(bool(edges[v] & truth)) for v in range(n)]
        for v in range(n):
            signatures[v] |= (int(bool(truth & (1 << v))) << m)
            signatures[v] |= (diam[v] << (m + 1))
        m += 2
    return signatures


count = 0
for n in range(1, 5):
    pairs = list(itertools.combinations(range(n), 2))
    for mask in range(1 << len(pairs)):
        edges = [0] * n
        for k, (v, u) in enumerate(pairs):
            if (mask >> k) & 1:
                edges[v] |= 1 << u
                edges[u] |= 1 << v
        for q in (2, 3):
            for colors in itertools.product(range(q), repeat=n):
                a = depth_one_signature(n, edges, colors, q)
                b = depth_one_boolean_partition(n, edges, colors, q)
                for v in range(n):
                    for u in range(n):
                        assert (a[v] == a[u]) == (b[v] == b[u])
                count += 1
print('EXHAUSTIVE_DEPTH1_OK', count)

# Exact finite-size mean of absent colors: compare the formula against a
# weighted exhaustive sum over every graph and color map for small n.
meanchecks = 0
for n in range(2, 5):
    pairs = list(itertools.combinations(range(n), 2))
    for q in (2, 3):
        total = 0
        reps = 0
        for mask in range(1 << len(pairs)):
            edges = [0] * n
            for k, (v, u) in enumerate(pairs):
                if mask >> k & 1:
                    edges[v] |= 1 << u
                    edges[u] |= 1 << v
            for colors in itertools.product(range(q), repeat=n):
                signatures = depth_one_signature(n, edges, colors, q)
                total += sum(q - signatures[v][1].bit_count() for v in range(n))
                reps += 1
        observed = total / reps
        predicted = n * q * (1 - 0.5 / q) ** (n - 1)
        assert abs(observed - predicted) < 1e-10, (n, q, observed, predicted)
        meanchecks += 1
print('EXACT_MISSING_COLOR_MEANS_OK', meanchecks)

# A seeded non-asymptotic check on three sides of the proposed threshold.
rng = random.Random(134602)
rows = []
for n in (300, 650, 1100):
    for alpha in (0.22, 0.75, 1.55):
        q = max(2, round(alpha * n / math.log(n)))
        colors = [rng.randrange(q) for _ in range(n)]
        neigh = [0] * n
        for v in range(n):
            cv = 1 << colors[v]
            for u in range(v + 1, n):
                if rng.random() < 0.5:
                    neigh[v] |= 1 << colors[u]
                    neigh[u] |= cv
        s = [(colors[v], neigh[v]) for v in range(n)]
        distinct = len(set(s))
        saturated = sum(m.bit_count() == q for m in neigh)
        assert distinct <= n
        assert all(m.bit_length() <= q for m in neigh)
        rows.append((n, alpha, q, distinct, saturated))
print('SEEDED_EXAMPLES', rows)
print('VERIFY_OK')
