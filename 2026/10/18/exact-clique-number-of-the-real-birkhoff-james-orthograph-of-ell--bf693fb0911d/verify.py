#!/usr/bin/env python3
"""Finite checks of the real sup-norm orthograph clique formula.

Pure Python 3 standard library. Infinite-dimensional quantifiers are handled
by the mathematical proof, not by these finite experiments.
"""
from itertools import combinations, permutations, product
from math import comb


def orthogonal(x, y):
    # Exact real Birkhoff--James criterion for a supremum-norm vector.
    m = max(abs(t) for t in x)
    products = [a*b for a,b in zip(x,y) if abs(a) == m]
    return min(products) <= 0 <= max(products)


def ternary_layer(n, k):
    for indices in combinations(range(n), k):
        for tail in product((-1,1), repeat=k-1):
            v = [0]*n
            for i, s in zip(indices, (1,)+tail):
                v[i] = s
            yield tuple(v)


def active_pattern(x):
    m = max(abs(t) for t in x)
    p = tuple((1 if t > 0 else -1) if abs(t) == m else 0 for t in x)
    first = next(a for a in p if a)
    return tuple(a*first for a in p)


def projectively_comparable(p, q):
    return any(all(a == 0 or a == s*b for a,b in zip(p,q))
               for s in (-1,1)) or any(all(b == 0 or b == s*a for a,b in zip(p,q))
               for s in (-1,1))


def grid(n):
    vals = (-2,-1,0,1,2)
    out=[]
    for v in product(vals, repeat=n):
        if max(abs(z) for z in v) != 2:
            continue
        if next(z for z in v if z) < 0:
            continue
        out.append(v)
    return out


def max_clique(adj):
    # Exact Bron--Kerbosch search, sufficient for the small independent grid.
    best = 0
    def dfs(R,P,X):
        nonlocal best
        if len(R) + len(P) <= best:
            return
        if not P and not X:
            best = max(best, len(R))
            return
        U=P|X
        u=max(U, key=lambda z: len(P&adj[z])) if U else None
        for v in list(P - (adj[u] if u is not None else set())):
            dfs(R|{v}, P&adj[v], X&adj[v])
            P.remove(v)
            X.add(v)
    dfs(set(), set(range(len(adj))), set())
    return best


def main():
    layers=0; pairs=0; flags=0
    for n in range(1,9):
        for k in range(1,n+1):
            reps=list(ternary_layer(n,k))
            assert len(reps)==comb(n,k)*2**(k-1)
            assert len(set(active_pattern(x) for x in reps)) == len(reps)
            for x,y in combinations(reps,2):
                assert orthogonal(x,y) and orthogonal(y,x)
                assert not projectively_comparable(active_pattern(x),active_pattern(y))
                pairs+=1
            layers+=1
        r=max(comb(n,k)*2**(k-1) for k in range(1,n+1))
        k=(2*n+2)//3
        assert r == comb(n,k)*2**(k-1)
    # Independent exact computation on points not limited to ternary values.
    samples=[]
    for n in (2,3):
        V=grid(n)
        adj=[set() for _ in V]
        for i in range(len(V)):
            for j in range(i):
                x,y=V[i],V[j]
                related=orthogonal(x,y) and orthogonal(y,x)
                if related:
                    assert not projectively_comparable(active_pattern(x),active_pattern(y))
                    adj[i].add(j)
                    adj[j].add(i)
        expected=max(comb(n,k)*2**(k-1) for k in range(1,n+1))
        got=max_clique(adj)
        assert got==expected,(n,got,expected)
        samples.append((n,len(V),got))
    # Directly enumerate all full signed flags in dimension four; at each rank
    # the projective pattern appears uniformly 1/rank_size of the time.
    n=4
    count={p:0 for k in range(1,n+1) for p in map(active_pattern,ternary_layer(n,k))}
    for signs in product((-1,1),repeat=n):
        for perm in permutations(range(n)):
            x=[0]*n
            for i in perm:
                x[i]=signs[i]
                count[active_pattern(x)] += 1
            flags+=1
    for p, v in count.items():
        k=sum(a!=0 for a in p)
        assert v*comb(n,k)*2**(k-1)==flags
    print(f'VERIFY_OK layers={layers} ternary_mutual_pairs={pairs} rational_grids={samples} flags={flags}')

if __name__ == '__main__':
    main()
