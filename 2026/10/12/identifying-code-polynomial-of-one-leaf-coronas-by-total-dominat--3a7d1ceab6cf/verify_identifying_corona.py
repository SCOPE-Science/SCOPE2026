"""Exact finite tests of the identifying-code enumerator for one-leaf coronas.

Usage: python check_id_corona.py
Every test uses only the Python standard library.
"""
from collections import Counter
from itertools import combinations
import random
import math


def base_neighbors(n, edge_mask):
    adj = [0] * n
    edges = list(combinations(range(n), 2))
    for k, (u, v) in enumerate(edges):
        if (edge_mask >> k) & 1:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    return adj


def is_identifying_direct(adj, selected):
    """Closed-neighborhood signatures of every vertex in the corona."""
    n = len(adj)
    seen = set()
    for v in range(n):
        root = (adj[v] | (1 << v) | (1 << (v+n))) & selected
        leaf = ((1 << v) | (1 << (v+n))) & selected
        if not root or root in seen:
            return False
        seen.add(root)
        if not leaf or leaf in seen:
            return False
        seen.add(leaf)
    return True


def is_identifying_structural(adj, selected):
    n = len(adj)
    R = selected & ((1 << n) - 1)
    for v in range(n):
        root = (R >> v) & 1
        leaf = (selected >> (n+v)) & 1
        if not root and not leaf:
            return False
        if not adj[v] & R:
            return False
    only_root = [v for v in range(n) if ((R >> v) & 1) and not ((selected >> (n+v)) & 1)]
    signatures = [(adj[v] | (1 << v)) & R for v in only_root]
    return len(signatures) == len(set(signatures))


def polynomial_from_theorem(adj):
    n = len(adj)
    coeffs = [0] * (2*n + 1)
    for R in range(1 << n):
        if any(not (adj[v] & R) for v in range(n)):
            continue
        classes = Counter(((adj[v] | (1 << v)) & R) for v in range(n) if R & (1 << v))
        q = [1]
        for k in classes.values():
            p = [0] * (len(q) + 1)
            for j, a in enumerate(q):
                p[j] += k * a
                p[j+1] += a
            q = p
        shift = n + R.bit_count() - len(classes)
        for j, a in enumerate(q):
            coeffs[shift+j] += a
    return coeffs


def trial(n, edge_mask):
    adj = base_neighbors(n, edge_mask)
    coeffs = [0] * (2*n+1)
    for selected in range(1 << (2*n)):
        direct = is_identifying_direct(adj, selected)
        structural = is_identifying_structural(adj, selected)
        if direct != structural:
            raise AssertionError(('classification', n, edge_mask, selected, direct, structural))
        if direct:
            coeffs[selected.bit_count()] += 1
    predicted = polynomial_from_theorem(adj)
    if coeffs != predicted:
        raise AssertionError(('polynomial', n, edge_mask, coeffs, predicted))
    return 1 << (2*n)


def main():
    cases = 0
    subsets = 0
    by_n = {}
    for n in range(1, 6):
        count = 1 << (n*(n-1)//2)
        checked = 0
        for e in range(count):
            checked += trial(n, e)
        cases += count
        subsets += checked
        by_n[n] = dict(graphs=count, subsets=checked)
    rng = random.Random(1729)
    for n, sample_count in ((6, 120), (7, 16)):
        m = n*(n-1)//2
        sampled = [rng.randrange(1 << m) for _ in range(sample_count)]
        sampled += [0, (1 << m)-1]
        checked = 0
        for e in sampled:
            checked += trial(n, e)
        cases += len(sampled)
        subsets += checked
        by_n[n] = dict(graphs=len(sampled), subsets=checked)
    print('PASS exact direct identification / structural criterion / closed polynomial')
    print('graph instances:', cases)
    print('vertex subsets:', subsets)
    for n, details in by_n.items():
        print('n=', n, details)
    # Independent closed-family coefficients, not based on enumeration of codes.
    for m in range(2, 13):
        adj = [((1 << m)-1) ^ (1 << v) for v in range(m)]
        got = polynomial_from_theorem(adj)
        expected = [0] * (2*m+1)
        for j in range(m+1):
            expected[m+j] += math.comb(m, j)
        expected[m] -= 1
        expected[m+1] -= m
        for j in range(m):
            expected[m+j] += m * math.comb(m-1, j)
        expected[m] -= m
        if got != expected:
            raise AssertionError(('complete-family coefficient formula', m, got, expected))
    for m in range(2, 11):
        n = m + 1
        adj = [(1 << (n-1)) - 1 << 1] + [1] * m
        got = polynomial_from_theorem(adj)
        expected = [0] * (2*n+1)
        expected[n+1] += 2*m
        expected[n+2] += m
        for s in range(2, m+1):
            for j in range(s+2):
                expected[n+j] += math.comb(m, s) * math.comb(s+1, j)
        if got != expected:
            raise AssertionError(('star-family coefficient formula', m, got, expected))
    print('PASS all complete graph formulas m=2..12 and star formulas m=2..10')
    print('unbounded theorem not implied by finite enumeration')

if __name__ == '__main__':
    main()
