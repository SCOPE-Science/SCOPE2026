#!/usr/bin/env python3
"""Finite exact combinatorial diagnostics for canonical Fibonacci SFT covers.
Scientific infinite statements are proved separately by the Rauzy-graph argument.
"""
from math import exp, sqrt


def fibonacci_prefix(min_length):
    a, b = '0', '01'
    while len(b) < min_length:
        a, b = b, b + a
    return b


def fibonacci_numbers(limit):
    a, b = 1, 1
    out = [a, b]
    while b <= limit:
        a, b = b, a + b
        out.append(b)
    return out


def graph_checks(n, word, fibs):
    vertices = {word[i:i+n] for i in range(len(word)-n+1)}
    edges = {word[i:i+n+1] for i in range(len(word)-n)}
    assert len(vertices) == n + 1, ('vertex language not saturated', n)
    assert len(edges) == n + 2, ('edge language not saturated', n)
    graph = {v: [] for v in vertices}
    indeg = {v: 0 for v in vertices}
    for edge in edges:
        src, dst = edge[:-1], edge[1:]
        graph[src].append(dst)
        indeg[dst] += 1
    branches = [v for v in vertices if len(graph[v]) == 2]
    assert len(branches) == 1 and sorted(indeg.values())[-1] == 2
    assert sum(x == 2 for x in indeg.values()) == 1
    start = branches[0]
    lengths = []
    for nxt in graph[start]:
        u, steps = nxt, 1
        while u != start:
            assert len(graph[u]) == 1, ('hidden branch', n)
            u = graph[u][0]
            steps += 1
            assert steps < n + 10
        lengths.append(steps)
    m = next(i for i in range(2, len(fibs)-1) if fibs[i]-1 <= n <= fibs[i+1]-2)
    expected = [fibs[m-1], fibs[m]]
    assert sorted(lengths) == sorted(expected), (n, lengths, expected)
    return m


def main():
    maximum = 200
    word = fibonacci_prefix(16000)
    fibs = fibonacci_numbers(maximum * 3)
    last_m = -1
    intervals = []
    for n in range(1, maximum+1):
        m = graph_checks(n, word, fibs)
        if m != last_m:
            intervals.append((n, m, fibs[m-1], fibs[m]))
            last_m = m
    phi = (1+sqrt(5))/2
    lo, hi = 0., 2.
    for _ in range(80):
        c = (lo+hi)/2
        if exp(-c/phi)+exp(-c)>1:lo=c
        else:hi=c
    c = (lo+hi)/2
    assert 0.87 < c < 0.88
    assert 1.41 < phi*c < 1.42
    print('VERIFY_OK: 200 exact finite Fibonacci Rauzy graph language and return-loop checks')
    print('first interval records:', intervals[:8])
    print('cluster envelope numerical diagnostics:', c, phi*c)


if __name__ == '__main__':
    main()
