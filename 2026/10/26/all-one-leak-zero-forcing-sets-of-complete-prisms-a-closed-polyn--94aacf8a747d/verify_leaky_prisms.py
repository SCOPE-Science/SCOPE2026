"""Exhaustive independent small-order check of one-leaky zero forcing on two matched cliques.
Run: python verify_leaky_prisms.py
"""
from collections import Counter
from itertools import combinations
from math import comb


def graph(n):
    # Vertices 0,...,n-1 and n,...,2n-1 are two cliques.
    return [tuple(j for j in range(2*n) if j != i and
                  (i//n == j//n or i % n == j % n))
            for i in range(2*n)]


def eventually_blue(adj, initial, leak):
    blue = set(initial)
    while True:
        additions = set()
        for v in tuple(blue):
            if v == leak:
                continue
            white_neighbors = [u for u in adj[v] if u not in blue]
            if len(white_neighbors) == 1:
                additions.add(white_neighbors[0])
        if not additions:
            return len(blue) == len(adj)
        blue.update(additions)


def leaky(adj, chosen):
    return all(eventually_blue(adj, chosen, leak)
               for leak in range(len(adj)))


def predicted(n, mask):
    a = {i for i in range(n) if mask >> i & 1}
    b = {i for i in range(n) if mask >> (n+i) & 1}
    if len(a) == n or len(b) == n:
        return True
    if n == 3:
        return len(a) == len(b) == 2
    return ((len(a) == n-1 and len(b & a) >= 2) or
            (len(b) == n-1 and len(a & b) >= 2))


def expected_poly(n):
    out = Counter()
    for t in range(n+1):
        out[n+t] += 2*comb(n,t)
    out[2*n] -= 1
    if n == 3:
        out[4] += 9
    else:
        out[n+1] += 2*n*comb(n-1,2)
        for t in range(3, n-1):
            out[n-1+t] += 2*n*comb(n,t)
        out[2*n-2] += n*n
    return +out


def expected_minimal(n):
    if n == 3:
        return {3:2, 4:9}
    return {n:2, n+1:2*n*comb(n-1,2)}


def run():
    aggregate = 0
    for n in range(3,8):
        adj = graph(n)
        family = set()
        for mask in range(1 << (2*n)):
            chosen = {i for i in range(2*n) if mask >> i & 1}
            actual = leaky(adj, chosen)
            expected = predicted(n, mask)
            assert actual == expected, ('classification', n, mask, actual, expected)
            if actual:
                family.add(mask)
        all_hist = Counter(x.bit_count() for x in family)
        assert all_hist == expected_poly(n), ('all', n, all_hist, expected_poly(n))
        minimal = [x for x in family if not any((x & (1<<i)) and
                  ((x ^ (1<<i)) in family) for i in range(2*n))]
        min_hist = Counter(x.bit_count() for x in minimal)
        assert min_hist == expected_minimal(n), ('minimal', n, min_hist)
        aggregate += 1 << (2*n)
        print('PASS n=', n, 'all=', dict(sorted(all_hist.items())),
              'minimal=', dict(sorted(min_hist.items())))
    print('ALL_PASS subsets=', aggregate)

if __name__ == '__main__':
    run()
