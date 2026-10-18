"""Exact finite-tree bond-percolation source-tail comparison verifier.

Standard-library only. Run: python3 verify.py > certificate.json
"""
from itertools import combinations, product
from fractions import Fraction
from math import comb
import json


def prufer_tree(n, code):
    degrees = [1] * n
    for v in code:
        degrees[v] += 1
    edges = []
    for v in code:
        leaf = next(i for i in range(n) if degrees[i] == 1)
        edges.append((leaf, v))
        degrees[leaf] -= 1
        degrees[v] -= 1
    a, b = (i for i in range(n) if degrees[i] == 1)
    edges.append((a, b))
    return edges


def counts(n, edges):
    """C[v][k][j] counts open-edge subsets of size j with root cluster >=k."""
    assert len(edges) == n - 1
    C = [[[0] * n for _ in range(n + 1)] for _ in range(n)]
    for mask in range(1 << (n - 1)):
        pa = list(range(n))
        sz = [1] * n
        def root(x):
            while pa[x] != x:
                x = pa[x]
            return x
        for t, (a, b) in enumerate(edges):
            if (mask >> t) & 1:
                a, b = root(a), root(b)
                if a != b:
                    pa[b] = a
                    sz[a] += sz[b]
        j = mask.bit_count()
        for v in range(n):
            size = sz[root(v)]
            for k in range(2, size + 1):
                C[v][k][j] += 1
    return C


def coefficientwise_source_order(C, n):
    """Prove a single source orientation for every tail k, all open-edge counts j."""
    tests = nonzero = incomparable = 0
    for a, b in combinations(range(n), 2):
        orientation = 0
        for k in range(2, n + 1):
            for j in range(n):
                delta = C[a][k][j] - C[b][k][j]
                tests += 1
                if delta:
                    nonzero += 1
                    sg = (delta > 0) - (delta < 0)
                    if orientation and sg != orientation:
                        incomparable += 1
                    if not orientation:
                        orientation = sg
    return tests, nonzero, incomparable


def monomial_difference(C, n, a, b, k):
    """Bernstein occupancy expansion to exact integer powers of p."""
    m = n - 1
    out = [0] * (m + 1)
    for j in range(m + 1):
        coefficient = C[a][k][j] - C[b][k][j]
        for h in range(m-j+1):
            out[j+h] += coefficient * comb(m-j, h) * (-1)**h
    return out


def recursive_half_pgf(n, edges, start):
    """Independent rooted subtree recursion using exact rational arithmetic."""
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    def rec(v, parent):
        state = {1: Fraction(1)}
        for w in adj[v]:
            if w == parent:
                continue
            child = rec(w, v)
            factors = {0: Fraction(1, 2)}
            for size, prob in child.items():
                factors[size] = factors.get(size, Fraction(0)) + prob/2
            newer = {}
            for a, pa in state.items():
                for b, pb in factors.items():
                    newer[a+b] = newer.get(a+b, Fraction(0)) + pa*pb
            state = newer
        return state
    result = rec(start, -1)
    return [result.get(k, Fraction(0)) for k in range(n+1)]


def main():
    results = []
    total_trees = total_pairs = total_tests = total_nonzero = 0
    for n in range(2, 7):
        trees = pairs = tests = nonzero = conflicts = 0
        for code in product(range(n), repeat=n-2):
            trees += 1
            C = counts(n, prufer_tree(n, code))
            ct, nz, bad = coefficientwise_source_order(C, n)
            tests += ct
            nonzero += nz
            conflicts += bad
            pairs += comb(n, 2)
        assert trees == n**(n-2)
        assert conflicts == 0
        results.append(dict(vertices=n, labeled_trees=trees, root_pairs=pairs,
                            coefficient_comparisons=tests, nonzero_differences=nonzero,
                            conflicting_signs=conflicts))
        total_trees += trees
        total_pairs += pairs
        total_tests += tests
        total_nonzero += nonzero

    # Three-arm spider with lengths 3,2,1. Center 0, long arm 0-1-2-3,
    # middle arm 0-4-5, short arm 0-6.
    edges = [(0,1),(1,2),(2,3),(0,4),(4,5),(0,6)]
    u, v = 2, 6
    C = counts(7, edges)
    diffs = {str(k): monomial_difference(C,7,u,v,k) for k in range(2,8)}
    assert diffs == {
      '2':[0,1,-1,0,0,0,0], '3':[0]*7,
      '4':[0,0,0,0,-1,1,0],
      '5':[0,0,0,0,1,-2,1],
      '6':[0,0,0,0,0,1,-1], '7':[0]*7
    }
    mean_diff = [sum(diffs[str(k)][t] for k in range(2,8)) for t in range(7)]
    assert mean_diff == [0,1,-1,0,0,0,0]
    exact_half_distributions = {}
    for src in (u,v):
        dynamic = recursive_half_pgf(7, edges, src)
        direct = [C[src][k][0] for k in range(8)]  # unused: tail encoding
        # Reconstruct point probabilities from tail probabilities at p=1/2.
        tails = [2**6] + [sum(C[src][k]) for k in range(2,8)] + [0]
        mass = [0] + [tails[k-1]-tails[k] for k in range(1,8)]
        assert mass == [int(x*2**6) for x in dynamic]
        assert sum(mass) == 64
        exact_half_distributions[str(src)] = mass
    print(json.dumps({
      'claim': 'All rooted epidemic clusters on trees with at most six vertices are totally ordered in first-order stochastic order for every p in (0,1); seven vertices fail for every p.',
      'lower_bound': results, 'total_labeled_trees': total_trees,
      'total_root_pairs': total_pairs, 'total_exact_integer_comparisons': total_tests,
      'total_nonzero_integer_coefficients': total_nonzero,
      'witness_edges': edges, 'witness_sources': [u,v],
      'witness_tail_polynomial_differences_ascending_coefficients': diffs,
      'witness_mean_difference_ascending_coefficients': mean_diff,
      'witness_outbreak_size_counts_at_p_half_denominator_64': exact_half_distributions,
      'witness_independent_rooted_pgf_check': 'passed'
    }, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
