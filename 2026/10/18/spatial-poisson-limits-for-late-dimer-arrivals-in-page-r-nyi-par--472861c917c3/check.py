"""Finite, exact checks for edge-acceptance laws in one-dimensional greedy dimer parking.
Run: python3 check.py
"""
from fractions import Fraction as F
from itertools import combinations, permutations
from math import factorial


def poly_edge_accept_probability(n, i):
    return sum((F((-1) ** (k + ell), factorial(k) * factorial(ell) * (k + ell + 1))
                for k in range(i) for ell in range(n - i)), F(0))


def greedy_accepted(edge_order, n):
    used = set()
    kept = set()
    for e in edge_order:
        if e not in used and e + 1 not in used:
            kept.add(e)
            used.add(e)
            used.add(e + 1)
    return kept


def independent_boundary_vacancy(m, u):
    # Independently activate each edge before the observation time,
    # then average over all its possible chronological orders.
    total = F(0)
    edges = range(1, m)
    for size in range(m):
        for active in combinations(edges, size):
            p_subset = u ** size * (1 - u) ** (m - 1 - size)
            for order in permutations(active):
                parked = greedy_accepted(order, m)
                if (m - 1) not in parked:
                    total += p_subset / factorial(size)
    return total


def alternating_exponential_polynomial(m, u):
    return sum((F((-1)**k, factorial(k)) * u**k for k in range(m)), F(0))


def check_all():
    checks = 0
    for m in range(1, 9):
        for u in [F(0), F(1, 3), F(1, 2), F(2, 3), F(1)]:
            observed = independent_boundary_vacancy(m, u)
            expected = alternating_exponential_polynomial(m, u)
            assert observed == expected, ('boundary', m, u, observed, expected)
            checks += 1
    total_orderings = 0
    total_edge_probs = 0
    causal_certificates = 0
    for n in range(2, 10):
        ranks = list(range(1, n))
        counts = [0] * (n - 1)
        for order in permutations(ranks):
            total_orderings += 1
            kept = greedy_accepted(order, n)
            for i in kept:
                counts[i - 1] += 1
            # Edge priorities are their position in the chronological permutation.
            priority = {edge: pos for pos, edge in enumerate(order)}
            for i in range(1, n):
                for L in (1, 2):
                    local_edges = [edge for edge in order if abs(edge - i) <= L]
                    local_kept = greedy_accepted(local_edges, n)
                    if (i in kept) != (i in local_kept):
                        causal = any(
                            (1 <= i + direction * (L + 1) < n) and
                            all(priority[i + direction * k] > priority[i + direction * (k+1)]
                                for k in range(L+1))
                            for direction in (-1, 1)
                        )
                        assert causal, ('causal path', n, i, L, order)
                        causal_certificates += 1
        for i, count in enumerate(counts, start=1):
            observed = F(count, factorial(n-1))
            expected = poly_edge_accept_probability(n, i)
            assert observed == expected, ('edge', n, i, observed, expected)
            total_edge_probs += 1
    assert abs(float(alternating_exponential_polynomial(7, F(1))) - 2.718281828459045**(-1)) < .00025
    print('VERIFY_OK', 'exact_boundary_cases', checks,
          'priority_permutations', total_orderings,
          'exact_edge_probabilities', total_edge_probs,
          'local_causality_witnesses', causal_certificates)

if __name__ == '__main__':
    check_all()
