#!/usr/bin/env python3
"""Exact small-parameter tests for the bivariate induced-forest enumerator.

Usage: python3 verify.py
Standard-library only; compares a closed coefficient formula with a
separate edge-by-edge graph enumeration. Finite tests do not prove the theorem.
"""
from collections import Counter
from math import comb


def formula(p, q, t):
    out = Counter()

    def add(size, components, ways):
        if ways:
            out[size, components] += ways

    for j in range(p + 1):
        add(j, j, comb(p, j))
    for j in range(q + 1):
        add(j, j, comb(q, j))
    add(0, 0, -1)
    for j in range(1, q + 1):
        add(j + 1, 1, t * comb(q - 1, j) + (p - t) * comb(q, j))
        add(j + 1, 2, t * comb(q - 1, j - 1))
    for j in range(1, p + 1):
        add(j + 1, 1, t * comb(p - 1, j) + (q - t) * comb(p, j))
        add(j + 1, 2, t * comb(p - 1, j - 1))
    add(2, 1, -(p * q - t))
    add(2, 2, -t)
    add(4, 1, t * (p - 1) * (q - 1) - t * (t - 1))
    add(4, 2, comb(t, 2))
    add(5, 1, comb(t, 2) * (p + q - 4))
    return +out


def independent_enumeration(p, q, t):
    ans = Counter()
    path4 = path5 = 0
    for mask in range(1 << (p + q)):
        marked = [i for i in range(p + q) if (mask >> i) & 1]
        parent = list(range(p + q))
        degree = [0] * (p + q)

        def root(v):
            while v != parent[v]:
                parent[v] = parent[parent[v]]
                v = parent[v]
            return v

        acyclic = True
        for i in range(p):
            if not (mask >> i) & 1:
                continue
            for j in range(q):
                if not (mask >> (p + j)) & 1 or (i < t and i == j):
                    continue
                degree[i] += 1
                degree[p + j] += 1
                a, b = root(i), root(p + j)
                if a == b:
                    acyclic = False
                    break
                parent[a] = b
            if not acyclic:
                break
        if not acyclic:
            continue
        c = len({root(v) for v in marked})
        size = len(marked)
        ans[size, c] += 1
        if c == 1 and max((degree[v] for v in marked), default=0) <= 2:
            if size == 4:
                path4 += 1
            elif size == 5:
                path5 += 1
    return ans, (path4, path5)


def main():
    triples = masks = 0
    for p in range(2, 8):
        for q in range(2, 8):
            for t in range(min(p, q) + 1):
                measured, (path4, path5) = independent_enumeration(p, q, t)
                wanted = formula(p, q, t)
                assert measured == wanted, (p, q, t, measured - wanted, wanted - measured)
                assert path4 == t * (p - 1) * (q - 1) - t * (t - 1)
                assert path5 == comb(t, 2) * (p + q - 4)
                triples += 1
                masks += 1 << (p + q)
    for n in range(3, 8):
        count4 = n * (n - 1) * (n - 2)
        count5 = comb(n, 2) * (2 * n - 4)
        assert count4 == count5
    print(f"VERIFY_OK parameter_triples={triples} subsets={masks} "
          "path_type_checks=326 crown_balance_tests=5 max_vertices=14")


if __name__ == "__main__":
    main()
