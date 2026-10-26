#!/usr/bin/env python3
"""Small-instance checker for the induced-matching polynomial of rook graphs.
Uses only the Python standard library; the proof in RESULT.md is all-parameter.
"""
from itertools import combinations
from math import factorial


def rook_edges(m, n):
    vertices = [(i, j) for i in range(m) for j in range(n)]
    return [(a, b) for a, b in combinations(vertices, 2)
            if a[0] == b[0] or a[1] == b[1]]


def conflict(e, f):
    return any(a[0] == b[0] or a[1] == b[1] for a in e for b in f)


def brute_coefficients(m, n):
    edges = rook_edges(m, n)
    counts = {0: 1}

    def visit(start, chosen):
        if chosen:
            k = len(chosen)
            counts[k] = counts.get(k, 0) + 1
        for idx in range(start, len(edges)):
            e = edges[idx]
            if all(not conflict(e, f) for f in chosen):
                visit(idx + 1, chosen + [e])

    visit(0, [])
    return counts


def formula_coefficients(m, n):
    counts = {}
    for h in range(m + 1):
        for v in range(n + 1):
            if h + 2 * v <= m and 2 * h + v <= n:
                c = (factorial(m) * factorial(n) //
                     (factorial(h) * factorial(v) * 2 ** (h + v) *
                      factorial(m - h - 2 * v) * factorial(n - v - 2 * h)))
                counts[h + v] = counts.get(h + v, 0) + c
    return counts


def main():
    for m in range(1, 5):
        for n in range(1, 5):
            a = brute_coefficients(m, n)
            b = formula_coefficients(m, n)
            assert a == b, (m, n, a, b)
    print("PASS: all induced-matching polynomial coefficients agree for 1 <= m,n <= 4")


if __name__ == "__main__":
    main()
