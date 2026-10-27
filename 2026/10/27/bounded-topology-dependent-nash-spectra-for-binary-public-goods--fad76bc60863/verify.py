#!/usr/bin/env python3
"""Exact checks of parity-response public-goods equilibria on ladder graphs."""
from itertools import product

PAIR = tuple(product((0, 1), repeat=2))
ZERO = (0, 0)


def next_pair(a, b):
    flip = 1 ^ b[0] ^ b[1]
    return (a[0] ^ flip, a[1] ^ flip)


def swap(z):
    return (z[1], z[0])


def predicted(kind, n):
    r = n % 4
    if kind == 'open':
        return (1, 2, 1, 4)[r]
    if kind == 'cylinder':
        return (16, 2, 4, 2)[r]
    if kind == 'mobius':
        return (4, 2, 8, 2)[r]
    raise ValueError(kind)


def recurrence_count(kind, n):
    total = 0
    for a, b in product(PAIR, repeat=2):
        if kind == 'open' and a != ZERO:
            continue
        p, q = a, b
        for k in range(1, n + 1):
            p, q = q, next_pair(p, q)
        if kind == 'open' and q == ZERO:
            total += 1
        if kind == 'cylinder' and p == a and q == b:
            total += 1
        if kind == 'mobius' and p == swap(a) and q == swap(b):
            total += 1
    return total


def edges(kind, n):
    # vertex 2*i+row, columns 0..n-1, rows 0..1
    es = set()
    def add(v, w):
        assert v != w
        es.add(tuple(sorted((v, w))))
    for i in range(n):
        add(2*i, 2*i+1)
    for i in range(n-1):
        for row in (0, 1):
            add(2*i+row, 2*(i+1)+row)
    if kind == 'cylinder':
        for row in (0, 1):
            add(row, 2*(n-1)+row)
    if kind == 'mobius':
        add(0, 2*(n-1)+1)
        add(1, 2*(n-1))
    if kind in ('cylinder', 'mobius'):
        assert n >= 3 and len(es) == 3*n
    return tuple(es)


def brute_count(kind, n):
    graph = [[] for _ in range(2*n)]
    for v, w in edges(kind, n):
        graph[v].append(w)
        graph[w].append(v)
    count = 0
    for bits in range(1 << (2*n)):
        if all(((bits >> v) & 1) == int((sum((bits >> w)&1 for w in graph[v]) % 2) == 0)
               for v in range(2*n)):
            count += 1
    return count


def main():
    for kind in ('open', 'cylinder', 'mobius'):
        start = 2 if kind == 'open' else 3
        for n in range(start, 101):
            assert recurrence_count(kind, n) == predicted(kind, n), (kind, n)
        for n in range(start, 9):
            observed = brute_count(kind, n)
            assert observed == predicted(kind, n), (kind, n, observed)
    print('Exact mod-two recurrence verified for every n=2..100 (open), n=3..100 (closed).')
    print('Independent strategy-profile brute force passed all ladder types through n=8.')
    for kind in ('open', 'cylinder', 'mobius'):
        print(kind, [(n, predicted(kind, n)) for n in range(3, 9)])


if __name__ == '__main__':
    main()
