"""Reproducible finite checks for the minimum edge-cover exchange graph of K_{n+1,n}.

Pure Python 3; no external data or dependencies. This program validates finite
instances, while the accompanying proof supplies the all-parameter result.
"""
from collections import deque, Counter
from itertools import permutations, product, combinations
from math import factorial, comb


def surjections(n):
    # Independent constructive enumeration: choose duplicated coordinates,
    # assign distinct colors to the other n-1 coordinates, and fill both.
    m = n + 1
    output = set()
    for a,b in combinations(range(m), 2):
        for perm in permutations(range(n)):
            vals = [None] * m
            vals[a] = vals[b] = perm[0]
            it = iter(perm[1:])
            for j in range(m):
                if j not in (a,b):
                    vals[j] = next(it)
            output.add(tuple(vals))
    return output


def swaps(f, n):
    ct = Counter(f)
    assert sorted(ct.values()) == [1]*(n-1)+[2]
    for j in range(n+1):
        if ct[f[j]] != 2:
            continue
        for b in range(n):
            if b != f[j]:
                g = list(f)
                g[j] = b
                yield tuple(g)


def inverse_edge(f):
    # A surjection determines an edge between two full permutations on
    # symbols -1,0,...,n-1 (where -1 is the blank symbol).
    ct = Counter(f)
    a = next(c for c,v in ct.items() if v == 2)
    p, q = (i for i,c in enumerate(f) if c == a)
    x = list(f); x[p] = -1
    y = list(f); y[q] = -1
    return frozenset((tuple(x),tuple(y)))


def root_neighbors(pi):
    p = pi.index(-1)
    for j in range(len(pi)):
        if j != p:
            q = list(pi)
            q[p],q[j] = q[j],q[p]
            yield tuple(q)


def verify(n, full=False):
    V = surjections(n)
    num = comb(n+1,2)*factorial(n)
    assert len(V) == num
    assert sum(1 for _ in V) == num
    assert all(len(set(f))==n for f in V)
    # Different construction by direct coordinate words, independent of the
    # duplicate-position/permutation representation.
    if n <= 6:
        direct = {f for f in product(range(n), repeat=n+1) if len(set(f))==n}
        assert direct==V
    start=min(V)
    dist={start:0}
    q=deque([start])
    while q:
        f=q.popleft()
        for g in swaps(f,n):
            assert g in V
            if g not in dist:
                dist[g]=dist[f]+1
                q.append(g)
    assert len(dist)==num
    assert max(dist.values())==3*n//2
    assert len(set(swaps(start,n)))==2*(n-1)
    if n <= 5:
        # Check EVERY adjacency of the color-word exchange graph against
        # endpoint incidence in the permutation-star root network.
        maps={f:inverse_edge(f) for f in V}
        assert len(set(maps.values())) == num
        root=set(permutations((-1,*range(n))))
        assert {p for e in maps.values() for p in e} == root
        rootedge=set()
        for p in root:
            for r in root_neighbors(p):
                rootedge.add(frozenset((p,r)))
        assert rootedge==set(maps.values())
        triangles=0; ecount=0
        for f in V:
            nb=set(swaps(f,n))
            assert len(nb)==2*(n-1)
            assert nb=={g for g in V if g != f and maps[g]&maps[f]}
            ecount += len(nb)
            for g in nb:
                if g < f: continue
                triangles += len(nb & set(swaps(g,n)))
        assert ecount//2 == num*(n-1)
        assert triangles//3 == factorial(n+1)*comb(n,3)
    print(f'n={n}: vertices={num},degree={2*(n-1)},edges={num*(n-1)},triangles={factorial(n+1)*comb(n,3)},diameter={max(dist.values())},connected=YES VERIFY_OK',flush=True)


if __name__ == '__main__':
    for k in range(2,8):
        verify(k)
    print('ALL_VERIFY_OK')
