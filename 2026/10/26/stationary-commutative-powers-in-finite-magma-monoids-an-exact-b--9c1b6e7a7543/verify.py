#!/usr/bin/env python3
"""Independent exhaustive check of stationary commutative magma-power counts."""
from collections import Counter
from itertools import product
from math import comb


def multiply(a, b, n):
    return tuple(b[a[x*n+y]*n+a[y*n+x]] for x in range(n) for y in range(n))


def commutative(a, n):
    return all(a[x*n+y] == a[y*n+x] for x in range(n) for y in range(n))


def stabilized_rank(a, n):
    # Iterate the defining operation rather than use functional-graph theory.
    p = a
    limit = n + comb(n, 2)
    for _ in range(1, limit+2):
        q = multiply(p, a, n)
        if q == p:
            if not commutative(p, n):
                return None
            return len({p[x*n+x] for x in range(n)})
        p = q
    return None


def graph_rank(a, n):
    # Separate orbit/cycle check, independent of the power multiplication.
    nxt = [a[x*n+y]*n+a[y*n+x] for x in range(n) for y in range(n)]
    roots = set()
    for start in range(n*n):
        seen = set()
        cur = start
        while cur not in seen:
            seen.add(cur)
            cur = nxt[cur]
        if nxt[cur] != cur or cur//n != cur%n:
            return None
        roots.add(cur//n)
    return len(roots)


def expected(n):
    return {r: comb(n, r)*r*n**(n*n-r-2) for r in range(1, n+1)}


def verify():
    for n in (2, 3):
        counts = Counter()
        for a in product(range(n), repeat=n*n):
            r_power = stabilized_rank(a, n)
            r_graph = graph_rank(a, n)
            assert r_power == r_graph, (n, a, r_power, r_graph)
            if r_power is not None:
                counts[r_power] += 1
        assert dict(counts) == expected(n), (n, dict(counts), expected(n))
        print('n =', n, 'verified coefficients =', dict(sorted(counts.items())))
    print('VERIFY_OK')

if __name__ == '__main__':
    verify()
