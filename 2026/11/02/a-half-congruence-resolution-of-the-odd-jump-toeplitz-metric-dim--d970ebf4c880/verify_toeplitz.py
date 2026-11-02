#!/usr/bin/env python3
"""Independent finite checks for odd-jump Toeplitz metric bases.

Usage: python3 verify_toeplitz.py
Uses only the Python standard library. This tests finite cases; the
universal statements require the separately supplied mathematical proof.
"""
from collections import deque


def bfs(n, b, origin):
    dist = [-1] * n
    dist[origin] = 0
    queue = deque([origin])
    while queue:
        v = queue.popleft()
        for step in (1, 2, b):
            for w in (v - step, v + step):
                if 0 <= w < n and dist[w] == -1:
                    dist[w] = dist[v] + 1
                    queue.append(w)
    assert all(d >= 0 for d in dist)
    return dist


def closed_distance(delta, b):
    q, r = divmod(abs(delta), b)
    return q + min((r + 1) // 2, 1 + (b - r + 1) // 2)


def check(n, b):
    assert b % 4 == 1 and b >= 13 and n >= b + 2
    s = (b + 1) // 2
    landmarks = (0, 1, s)
    vectors = [bfs(n, b, v) for v in landmarks]
    signatures = [tuple(row[i] for row in vectors) for i in range(n)]
    assert len(set(signatures)) == n, (b, n, 'failed to resolve')
    pairs = 0
    for i in range(n):
        other = bfs(n, b, i)
        for j in range(n):
            assert other[j] == closed_distance(i - j, b), (b, n, i, j)
            pairs += 1
    return pairs


def symbolic_residue_check(k):
    b = 4 * k + 1
    s = 2 * k + 1
    def f(d):
        return closed_distance(d, b)
    stable = []
    for r in range(b):
        i = 3*b + r
        empirical = (f(i - 1) - f(i), f(i - s) - f(i))
        if r == 0:
            formula = (1, k - 1)
        elif r % 2 == 1 and r <= s:
            j = (r - 1)//2
            formula = (-1, k - 2*j - 1)
        elif r % 2 == 0 and r <= 2*k:
            j = r//2
            formula = (0, k + 1 - 2*j)
        elif r % 2 == 0:
            j = r//2
            formula = (0, 2*j - 3*k - 2)
        else:
            j = (r - 1)//2
            formula = (1, 2*j - 3*k - 1)
        assert formula == empirical, ('table error', k, r, formula, empirical)
        stable.append(formula)
    assert len(set(stable)) == b, ('residue conflict', k)
    for i in range(1, s):
        special = (f(i - 1) - f(i), f(s - i) - f(i))
        assert special == stable[i]
    first = (f(1) - f(0), f(s) - f(0))
    assert first not in stable


def main():
    cases = [(13, 15), (13, 30), (13, 53), (17, 19), (17, 35),
             (17, 64), (21, 23), (21, 44), (25, 27), (25, 53),
             (29, 31), (29, 62), (37, 39)]
    total = 0
    for b, n in cases:
        pairs = check(n, b)
        total += pairs
        print(f'PASS b={b} n={n}: three landmarks resolve; {pairs} BFS distance checks')
    for k in range(3, 301):
        symbolic_residue_check(k)
    print('PASS symbolic residue formulas for k=3,...,300')
    print(f'PASS {len(cases)} graphs; {total} source-target distances; universal proof is in RESULT.md')

if __name__ == '__main__':
    main()
