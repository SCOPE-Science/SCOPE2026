#!/usr/bin/env python3
"""Exact checks for the Roman-domination enumerator of triangular graphs.
Python 3 standard library; no external files or dependencies.
"""
from collections import Counter
from itertools import combinations, product
from math import comb, factorial


def c(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def no_isolates(s, m):
    return sum((-1)**j * comb(s, j) * c(comb(s-j, 2), m)
               for j in range(s+1))


def polynomial_formula(n):
    E = comb(n, 2)
    out = Counter()
    for w in range(n + 1):
        s = n-w
        forced = comb(w, 2)
        for m in range(comb(s, 2)+1):
            g = no_isolates(s, m)
            if not g:
                continue
            ways = comb(n, w)*g
            for j in range(E-m-forced + 1):
                out[2*m+forced+j] += ways*comb(E-m-forced, j)
    return +out


def brute(n):
    edges = list(combinations(range(n), 2))
    N = len(edges)
    neighbors = [tuple(j for j, f in enumerate(edges) if j!=i and set(e)&set(f))
                 for i, e in enumerate(edges)]
    poly = Counter()
    for assignment in product(range(3), repeat=N):
        if all(v != 0 or any(assignment[j] == 2 for j in neighbors[i])
               for i, v in enumerate(assignment)):
            poly[sum(assignment)] += 1
    return +poly


def independent_support_sum(n):
    # A second enumeration: explicitly range over all possible 2-labeled edges,
    # build the forced-1 set, and sum arbitrary 0/1 extensions without
    # inclusion-exclusion or isolated-graph counting.
    edges = list(combinations(range(n), 2))
    N = len(edges)
    out = Counter()
    for mask in range(1 << N):
        m = mask.bit_count()
        seen = set()
        for i, (a,b) in enumerate(edges):
            if mask & (1 << i): seen.add(a); seen.add(b)
        forced = sum(a not in seen and b not in seen for a,b in edges)
        for j in range(N-m-forced+1):
            out[2*m+forced+j] += comb(N-m-forced,j)
    return +out


def odd_double_fact(n):
    t = 1
    for i in range(n,0,-2): t *= i
    return t


if __name__ == '__main__':
    total = 0
    for n in range(3,6):
        p = polynomial_formula(n)
        q = brute(n)
        assert p == q, ('brute',n,p,q)
        total += 3**comb(n,2)
    for n in range(3,7):
        p = polynomial_formula(n)
        q = independent_support_sum(n)
        assert p == q, ('independent-support',n)
    for n in range(3,19):
        p=polynomial_formula(n)
        expected=(n*odd_double_fact(n-2) if n%2 else
                  comb(n,2)*odd_double_fact(n-3))
        assert min(p)==n-1 and p[n-1] == expected, (n,p[n-1],expected)
        assert max(p)==2*comb(n,2) and p[max(p)]==1
        assert sum(p.values()) < 3**comb(n,2)
    print('VERIFY_OK exhaustive_n=3..5 labelings=',total,
          'independent_2supports_n=3..6',
          'exact_minimum_and_multiplicity_n=3..18')
