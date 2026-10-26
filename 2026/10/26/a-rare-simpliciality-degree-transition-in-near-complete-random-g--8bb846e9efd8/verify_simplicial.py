#!/usr/bin/env python3
"""Independent finite and numerical checks for simplicial-vertex degree conditioning.

Run: python3 verify_simplicial.py
Uses only the standard library; no external data are needed.
"""
import math
from collections import Counter
from fractions import Fraction

checks = 0


def exact_weights_by_graphs(n):
    """Counts configurations by root degree and global number of edges."""
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    bit = {edge: k for k, edge in enumerate(pairs)}
    result = Counter()
    for mask in range(1 << len(pairs)):
        neighbors = [u for u in range(1, n) if mask & (1 << bit[(0, u)])]
        simplicial = all(mask & (1 << bit[(a, b)]) for i, a in enumerate(neighbors)
                         for b in neighbors[i + 1:])
        if simplicial:
            result[(len(neighbors), mask.bit_count())] += 1
    return result, len(pairs)


def exact_event_degree_mass(n, counts, M, p):
    q = 1 - p
    masses = [Fraction(0) for _ in range(n)]
    for (d, e), how_many in counts.items():
        masses[d] += how_many * p**e * q**(M-e)
    return masses


for n in range(2, 7):
    counts, total_edges = exact_weights_by_graphs(n)
    for p in (Fraction(2, 5), Fraction(3, 4)):
        masses = exact_event_degree_mass(n, counts, total_edges, p)
        for d in range(n):
            formula = math.comb(n-1, d) * p**(d*(d+1)//2) * (1-p)**(n-1-d)
            assert masses[d] == formula, (n, p, d, masses[d], formula)
            checks += 1
        assert 0 < sum(masses) < 1 if n >= 3 else sum(masses) == 1
        checks += 1


def logweights(n, c):
    q = c * math.log(n) / n
    assert 0 < q < 1
    p = 1-q
    return [math.lgamma(n)-math.lgamma(d+1)-math.lgamma(n-d)
            + d*(d+1)/2*math.log(p)+(n-1-d)*math.log(q)
            for d in range(n)]


def conditioned_mean_and_logprob(n, c):
    w = logweights(n, c)
    max_w = max(w)
    probs = [math.exp(x-max_w) for x in w]
    total = sum(probs)
    mean = sum(i*probs[i] for i in range(n))/(n*total)
    logprob = (max_w+math.log(total))/(n*math.log(n))
    return mean, logprob


# Convergence is slow near criticality; test monotone approach rather than
# asserting that modest sample sizes already equal limiting values.
for c in (0.5, 1.0, 1.5, 2.0, 4.0):
    ideal = min(1.0, 1.0/c)
    ideal_log = -(c/2 if c <= 1 else 1-1/(2*c))
    observations = [conditioned_mean_and_logprob(n, c)
                    for n in (1000, 10000, 40000)]
    for i in range(2):
        assert abs(observations[i+1][0]-ideal) < abs(observations[i][0]-ideal)
        assert abs(observations[i+1][1]-ideal_log) < abs(observations[i][1]-ideal_log)
        checks += 2
    # The weighted formula has an additional exact symmetry under relabeling
    # non-root vertices; its dependence is only through n and d.

print(f'VERIFY_OK checks={checks}; exhaustive_graphs_n2_to_n6=33866; '
      'numeric_n=1000,10000,40000')
