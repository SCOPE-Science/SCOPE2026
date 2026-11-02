#!/usr/bin/env python3
"""Finite exact checks for leaf-versus-marked-distance laws in uniform Cayley trees.

This script enumerates all Prüfer words through eight vertices. Enumeration
checks finite instances; the accompanying analytic proof covers all n.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb


def prufer_edges(word, n):
    degree = [1] * n
    for v in word:
        degree[v] += 1
    edges = []
    for v in word:
        u = next(i for i, d in enumerate(degree) if d == 1)
        edges.append((u, v))
        degree[u] -= 1
        degree[v] -= 1
    a, b = [i for i, d in enumerate(degree) if d == 1]
    edges.append((a, b))
    return edges


def marked_path(edges, n):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    parent = {0: -1}
    todo = [0]
    for a in todo:
        for b in adj[a]:
            if b not in parent:
                parent[b] = a
                todo.append(b)
    path = [1]
    while path[-1] != 0:
        path.append(parent[path[-1]])
    return tuple(reversed(path)), [len(a) for a in adj]


def ratio(n, s, r, q):
    """Probability that r prescribed off-path vertices and q endpoints are leaves."""
    if q >= s or n - r - q <= 0:
        return Fraction(0)
    # (s-q)/s * ((n-r-q)/n)^(n-s-1)
    return Fraction(s-q, s) * Fraction(n-r-q, n) ** (n-s-1)


def conditional_mean(n, k):
    s = k + 1
    return (Fraction(n-s) + Fraction(2 * (s-1), s)) * Fraction(n-1,n) ** (n-s-1)


def run():
    assertions = 0
    trees = 0
    for n in range(3, 9):
        counts = defaultdict(int)
        leafsums = defaultdict(int)
        events = defaultdict(int)
        for word in product(range(n), repeat=n-2):
            edges = prufer_edges(word, n)
            path, degrees = marked_path(edges, n)
            k = len(path) - 1
            counts[k] += 1
            leafsums[k] += sum(d == 1 for d in degrees)
            trees += 1
            # A canonical ordered path of length k, for independent inclusion checks.
            fixed = (0,) + tuple(range(2, k+1)) + (1,) if k > 1 else (0,1)
            undirected = {frozenset(e) for e in edges}
            if all(frozenset((a,b)) in undirected for a,b in zip(fixed,fixed[1:])):
                events[k,0,0,"denominator"] += 1
                outside = [v for v in range(n) if v not in fixed]
                for r in range(len(outside)+1):
                    chosen = outside[:r]
                    for q in range(3):
                        candidates = chosen + list((0,1)[:q])
                        if all(degrees[v] == 1 for v in candidates):
                            events[k,r,q,"numerator"] += 1
        assert sum(counts.values()) == n ** (n-2)
        assertions += 1
        for k in range(1,n):
            s=k+1
            expected_dist_count = (k+1)
            # Number of ordered intermediate-vertex sequences times completions.
            ways = 1
            for j in range(k-1): ways *= n-2-j
            expected_dist_count *= ways * Fraction(n,1) ** (n-k-2)
            assert counts[k] == expected_dist_count
            assertions += 1
            assert Fraction(leafsums[k], counts[k]) == conditional_mean(n,k), (n,k)
            assertions += 1
            expected_path_count = s * n**(n-s-1) if n-s-1 >=0 else Fraction(s,n**(s+1-n))
            assert events[k,0,0,"denominator"] == expected_path_count
            assertions += 1
            for r in range(n-s+1):
                for q in range(3):
                    num=events[k,r,q,"numerator"]
                    den=events[k,0,0,"denominator"]
                    assert Fraction(num,den)==ratio(n,s,r,q), (n,k,r,q,num,den,ratio(n,s,r,q))
                    assertions += 1
    for n in range(3,150):
        for k in range(1,n-1):
            delta=conditional_mean(n,k+1)-conditional_mean(n,k)
            sign=(delta>0)-(delta<0)
            cubic=2*(n-1)-k*(k+1)**2
            assert sign==(cubic>0)-(cubic<0)
            assertions += 1
    print(f"PASS: {trees:,} trees enumerated; {assertions:,} exact assertions")

if __name__ == '__main__':
    run()
