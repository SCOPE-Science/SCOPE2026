#!/usr/bin/env python3
"""Independent finite enumeration of Catalan-monoid power stabilization and bounded Dyck heights.
Only Python's standard library is required. This is finite corroboration, not a proof.
"""
from collections import Counter
from math import comb

LIMIT = 10


def maps(n):
    f = [0] * (n + 1)
    def rec(i, lower):
        if i > n:
            yield tuple(f)
            return
        for x in range(lower, i + 1):
            f[i] = x
            yield from rec(i + 1, x)
    yield from rec(1, 1)


def power_depth(f):
    n = len(f)-1
    d = [0] * (n+1)
    for i in range(1, n+1):
        d[i] = 0 if f[i] == i else 1 + d[f[i]]
    return max(d), d


def forest_dyck(f):
    n = len(f)-1
    roots = [i for i in range(1, n+1) if f[i] == i]
    roots_end = roots[1:] + [n+1]
    out = []
    for a,b in zip(roots, roots_end):
        children = {j:[] for j in range(a,b)}
        for j in range(a+1,b):
            assert a <= f[j] < j
            children[f[j]].append(j)
        # BFS-label reconstruction: original block labels must appear levelwise
        queue = [a]
        for v in queue:
            queue.extend(children[v])
        assert queue == list(range(a,b)), (f, queue)
        def rec(v):
            out.append('(')
            for w in children[v]:rec(w)
            out.append(')')
        rec(a)
    return ''.join(out)


def height(path):
    h=mx=0
    for c in path:
        h += 1 if c == '(' else -1
        assert h>=0
        mx=max(mx,h)
    assert h==0
    return mx


def gf_bounded(k, limit):
    prev = [1] * (limit+1)  # F_0(z) = 1/(1-z)
    for _ in range(k):
        cur = [0]*(limit+1)
        cur[0]=1
        for n in range(1,limit+1):
            cur[n] = sum(prev[j]*cur[n-1-j] for j in range(n))
        prev=cur
    return prev


def expected_fib(n):
    a,b=0,1
    for _ in range(2*n-1):a,b=b,a+b
    return a


def main():
    for n in range(1,LIMIT+1):
        h = Counter()
        for f in maps(n):
            depth, _ = power_depth(f)
            w = forest_dyck(f)
            assert len(w)==2*n
            assert height(w)==depth+1,(n,f,depth,w)
            h[depth]+=1
        assert sum(h.values())==comb(2*n,n)//(n+1)
        for k in range(n):
            pred = gf_bounded(k,n)[n] - (gf_bounded(k-1,n)[n] if k else 0)
            assert h[k]==pred,(n,k,h[k],pred)
        assert sum(v for k,v in h.items() if k<=1) == 2**(n-1)
        if n>=2:
            assert sum(v for k,v in h.items() if k<=2) == expected_fib(n)
        if n>=1:
            assert sum(v for k,v in h.items() if k<=3) == (3**(n-1)+1)//2 if n>=2 else True
        assert h[n-1] == 1
        print('n=',n,'total=',sum(h.values()),'stabilization_counts=',[h[k] for k in range(n)])
    print('VERIFY_OK_CATALAN_POWER_STABILIZATION')

if __name__ == '__main__': main()
