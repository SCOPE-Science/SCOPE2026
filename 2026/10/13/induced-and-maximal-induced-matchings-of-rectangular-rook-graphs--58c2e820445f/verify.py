#!/usr/bin/env python3
"""Exact direct enumeration of induced matchings of rectangular rook graphs.

The expected formula is proved separately; this program checks finite instances.
"""
from collections import Counter
from math import factorial


def formula(m, n):
    all_counts = Counter()
    maximal_counts = Counter()
    for a in range(m + 1):
        for b in range(n + 1):
            r, c = m - a - 2 * b, n - 2 * a - b
            if r < 0 or c < 0:
                continue
            count = (factorial(m) * factorial(n) //
                     (factorial(a) * factorial(b) * factorial(r) * factorial(c) * (2 ** (a + b))))
            # Note integer division only after entire denominator.
            assert factorial(m) * factorial(n) % (factorial(a) * factorial(b) * factorial(r) * factorial(c) * (2 ** (a+b))) == 0
            all_counts[a + b] += count
            if not ((r >= 1 and c >= 2) or (r >= 2 and c >= 1)):
                maximal_counts[a + b] += count
    return dict(all_counts), dict(maximal_counts)


def brute(m, n):
    cells = [(i, j) for i in range(m) for j in range(n)]
    edges = [(a, b) for a in range(m*n) for b in range(a + 1, m*n)
             if cells[a][0] == cells[b][0] or cells[a][1] == cells[b][1]]
    e = len(edges)
    conflict = []
    for x, y in edges:
        ex = (cells[x], cells[y])
        mask = 0
        for j, (v, w) in enumerate(edges):
            ey = (cells[v], cells[w])
            if any(p[0] == q[0] or p[1] == q[1] for p in ex for q in ey):
                mask |= 1 << j
        conflict.append(mask)
    total = Counter()
    maximal = Counter()
    # Enumerate in increasing edge-index order; 'allowed' retains all currently
    # addable edges, including indices smaller than the last chosen index.
    def recur(last, allowed, size):
        total[size] += 1
        if not allowed:
            maximal[size] += 1
        t = allowed & ~((1 << (last + 1)) - 1)
        while t:
            bit = t & -t
            j = bit.bit_length() - 1
            recur(j, allowed & ~conflict[j], size + 1)
            t ^= bit
    recur(-1, (1 << e) - 1, 0)
    return dict(total), dict(maximal)


def run():
    boards = 0
    counted = 0
    for m in range(2, 6):
        for n in range(2, 6):
            e, f = formula(m, n)
            t, u = brute(m, n)
            assert e == t, ('all', m, n, e, t)
            assert f == u, ('maximal', m, n, f, u)
            kmax = min(m, n, (m+n)//3)
            kmin = (min(m,n)+1)//2
            assert max(k for k,v in e.items() if v) == kmax
            assert min(k for k,v in f.items() if v) == kmin
            assert max(k for k,v in f.items() if v) == kmax
            boards += 1
            counted += sum(t.values())
    for m in range(2, 19):
        for n in range(2, 19):
            e, f = formula(m, n)
            assert max(k for k,v in e.items() if v) == min(m,n,(m+n)//3)
            assert min(k for k,v in f.items() if v) == (min(m,n)+1)//2
            assert max(k for k,v in f.items() if v) == min(m,n,(m+n)//3)
    print('VERIFY_OK exhaustive_boards=16 dimensions=2..5 total_induced_matchings=%d formula_support_checks=289' % counted)
    print('R_3_3_all=%s R_3_3_maximal=%s' % (formula(3,3)))
    print('R_6_6_all=%s R_6_6_maximal=%s' % (formula(6,6)))


if __name__ == '__main__':
    run()
