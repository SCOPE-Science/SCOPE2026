#!/usr/bin/env python3
"""Independent finite checks of a rank-resolved work frontier.

No external libraries are required; run with Python 3.10 or newer.
"""
from collections import defaultdict
from itertools import combinations_with_replacement
from fractions import Fraction


def frontier(n, r):
    return (n * (n - 1) - r * (r - 1)) // 2


def work(f):
    return sum(abs(i - x) for i, x in enumerate(f, 1))


def remainder_certificate(f):
    n = len(f)
    vals = sorted(set(f))
    r = len(vals)
    N = n - r
    if not N:
        return Fraction(0)
    a = [f.count(x) for x in vals]
    u = [x - j for j, x in enumerate(vals, 1)]
    g = [u[0]] + [u[j] - u[j - 1] for j in range(1, r)] + [N - u[-1]]
    assert min(g) >= 0 and sum(g) == N
    d = lambda m, k: m - k - 1 if k < m else k - m
    return Fraction(sum((a[m-1]-1)*g[k]*(r-1-d(m,k))
                       for m in range(1, r+1) for k in range(r+1)), N)


def exhaustive():
    for n in range(1, 10):
        maxima = defaultdict(lambda: -1)
        counts = defaultdict(int)
        witnesses = defaultdict(list)
        inspected = 0
        for f in combinations_with_replacement(range(1, n + 1), n):
            r = len(set(f)); w = work(f); inspected += 1
            assert w <= frontier(n, r), (n, r, f, w)
            assert Fraction(frontier(n,r)-w) >= remainder_certificate(f), (n,r,f)
            if w > maxima[r]:
                maxima[r] = w
                counts[r] = 1
                witnesses[r] = [f]
            elif w == maxima[r]:
                counts[r] += 1
                witnesses[r].append(f)
        for r in range(1, n + 1):
            N = n - r
            low = (1,) * (N + 1) + tuple(range(2, r + 1))
            high = tuple(range(N + 1, n)) + (n,) * (N + 1)
            expected = {low, high}
            assert maxima[r] == frontier(n, r), (n,r)
            assert set(witnesses[r]) == expected, (n,r,witnesses[r],expected)
            assert counts[r] == len(expected), (n,r)
        print('n=',n,'checked=',inspected,'ranks=',n)


def dynamic_programming():
    # Alternative computation: track last image, rank and maximal work,
    # with ties counted. No reliance on the convexity proof.
    for n in range(2, 21):
        states = {(x, 1): (abs(x-1), 1) for x in range(1, n+1)}
        for i in range(2, n+1):
            nxt={}
            for (last, rank),(cost,num) in states.items():
                for x in range(last,n+1):
                    key=(x,rank+(x>last)); newcost=cost+abs(x-i)
                    if key not in nxt or newcost>nxt[key][0]:nxt[key]=(newcost,num)
                    elif newcost==nxt[key][0]:nxt[key]=(newcost,nxt[key][1]+num)
            states=nxt
        for r in range(1,n+1):
            best=max(w for (x,s),(w,c) in states.items() if s==r)
            count=sum(c for (x,s),(w,c) in states.items() if s==r and w==best)
            target=frontier(n,r)
            desired=1 if r==n else 2
            assert (best,count)==(target,desired),(n,r,best,count,target,desired)
        print('dp n=',n,'OK')

if __name__ == '__main__':
    exhaustive()
    dynamic_programming()
    print('VERIFY_OK_RANK_RESOLVED_CHAIN_WORK_FRONTIER')
