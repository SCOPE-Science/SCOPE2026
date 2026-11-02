"""Exhaustive test of fence-poset adjacent-transposition geometry.
Scientific definitions are explicit; no external packages are needed.
Run: python3 verify_primary.py
"""
from collections import Counter
from math import comb


def linear_extensions(n):
    predecessors = [0] * n
    for a in range(1, n):
        lo, hi = (a-1, a) if a % 2 else (a, a-1)
        predecessors[hi] |= 1 << lo
    all_mask = (1 << n) - 1

    def rec(mask, word):
        if mask == all_mask:
            yield tuple(word)
            return
        for v in range(n):
            bit = 1 << v
            if mask & bit == 0 and predecessors[v] & mask == predecessors[v]:
                word.append(v)
                yield from rec(mask | bit, word)
                word.pop()
    yield from rec(0, [])


def degree(word):
    return sum(abs(a-b) != 1 for a, b in zip(word, word[1:]))


def endpoints(n):
    p = []
    for a in range(1, n+1, 2):
        p.append(a-1)
        if a >= 3:
            p.append(a-2)
    if n % 2 == 0:
        p.append(n-1)
    q = []
    if n % 2:
        q.append(n-1)
    for a in range((n+1)//2 if n % 2 == 0 else (n-1)//2, 0, -1):
        q += [2*a-2, 2*a-1]
    return tuple(p), tuple(q)


def inversions(a, b):
    idx = {x: i for i, x in enumerate(b)}
    return sum(idx[a[i]] > idx[a[j]] for i in range(len(a)) for j in range(i+1, len(a)))


def test():
    for n in range(3, 12):
        minimum = (n+1)//2 - 1
        count = 0
        optimal = set()
        dist = Counter()
        for a in linear_extensions(n):
            count += 1
            deg = degree(a)
            dist[deg] += 1
            assert deg >= minimum, (n, a, deg)
            if deg == minimum:
                optimal.add(a)
        target = 1 if n % 2 == 0 else 2 ** ((n-1)//2)
        assert len(optimal) == target, (n, len(optimal), target)
        edges = set()
        for a in optimal:
            near = []
            for i in range(n-1):
                b = a[:i] + (a[i+1], a[i]) + a[i+2:]
                if b in optimal:
                    near.append(b)
                    edges.add(tuple(sorted((a, b))))
            assert len(near) == (0 if n%2==0 else 1), (n, a, near)
        assert len(edges) == (0 if n%2==0 else 2 ** ((n-3)//2))
        x, y = endpoints(n)
        assert x in set(linear_extensions(n)) if n <= 8 else degree(x) >= minimum
        assert degree(y) == minimum
        assert n%2==0 or degree(x) == minimum
        assert inversions(x, y) == (n-1)*(n-2)//2
        print('n',n,'total_extensions',count,'min_degree',minimum,'optimal',len(optimal),
              'optimal_edges',len(edges),'diameter',inversions(x,y), 'degree_hist', dict(sorted(dist.items())))
    print('PRIMARY_FENCE_PASS')


if __name__ == '__main__':
    test()
