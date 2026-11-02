"""Exact finite checks for four-cycle-supported one-edge spanning-tree exchanges."""
from itertools import combinations
from collections import deque, Counter
from math import comb
import sympy as sp


def graph(n):
    edges = [(a,b) for a in range(2) for b in range(n)]
    def tree(mask):
        p = list(range(n + 2))
        def root(x):
            while p[x] != x:
                x = p[x]
            return x
        for i,(a,b) in enumerate(edges):
            if mask & (1 << i):
                x,y = root(a),root(b + 2)
                if x == y:
                    return False
                p[x] = y
        return len({root(i) for i in range(n + 2)}) == 1
    trees = []
    for ix in combinations(range(2*n), n+1):
        mask = sum(1 << i for i in ix)
        if tree(mask):
            trees.append(mask)
    index = {v:i for i,v in enumerate(trees)}
    neighbors = [set() for _ in trees]
    for x, t in enumerate(trees):
        for j,k in combinations(range(n), 2):
            sq = (1 << j) | (1 << k) | (1 << (j+n)) | (1 << (k+n))
            used = t & sq
            if used.bit_count() != 3:
                continue
            new = sq ^ used
            for r in range(2*n):
                if used & (1 << r):
                    u = (t ^ (1 << r)) | new
                    assert u in index
                    neighbors[x].add(index[u])
    assert all(i not in neighbors[i] for i in range(len(trees)))
    assert all(i in neighbors[j] for i in range(len(trees)) for j in neighbors[i])
    return trees, neighbors


def encoding(t,n):
    both = [j for j in range(n) if t & (1 << j) and t & (1 << (j+n))]
    assert len(both) == 1
    star = both[0]
    bits = tuple(None if j==star else (1 if t & (1 << (j+n)) else 0) for j in range(n))
    return star,bits


def dformula(a,b):
    x,aa=a;y,bb=b
    return (x!=y)+sum(aa[k]!=bb[k] for k in range(len(aa)) if k!=x and k!=y)


def main():
    for n in range(2,6):
        trees,nbr=graph(n)
        enc=[encoding(x,n) for x in trees]
        N=len(trees)
        assert N == n * 2**(n-1)
        assert {len(s) for s in nbr} == {3*(n-1)}
        for i in range(N):
            distances=[-1]*N; distances[i]=0
            q=deque([i])
            while q:
                x=q.popleft()
                for y in nbr[x]:
                    if distances[y]==-1:
                        distances[y]=distances[x]+1;q.append(y)
            assert all(z>=0 for z in distances)
            assert all(z==dformula(enc[i],enc[j]) for j,z in enumerate(distances))
            for d in range(n):
                predicted=comb(n-1,d)+(2*(n-1)*comb(n-2,d-1) if d>=1 else 0)
                assert distances.count(d)==predicted
            assert max(distances)==n-1
        wiener=sum(dformula(enc[i],enc[j]) for i in range(N) for j in range(i))/1
        assert wiener==n*(n*n-1)*2**(2*n-4)
        if n<=4:
            A=sp.zeros(N)
            for i,adj in enumerate(nbr):
                for j in adj:A[i,j]=1
            L=3*(n-1)*sp.eye(N)-A
            char=sp.Poly(L.charpoly().as_expr(),sp.Symbol('lambda'))
            lam=char.gens[0]
            prod=1
            for r in range(0,n):
                prod*=(lam-4*r)**comb(n,r)
            for r in range(0,n-1):
                prod*=(lam-(2*n+2*r))**((n-r-1)*comb(n,r))
            assert sp.expand(char.as_expr()-prod)==0
            if n<=3:
                values=[4*r for r in range(1,n) for _ in range(comb(n,r))]
                values +=[2*(n+r) for r in range(n-1) for _ in range((n-r-1)*comb(n,r))]
                assert sp.prod(values)//N == L[:-1,:-1].det()
        print(f'PRIMARY_OK n={n} states={N} edges={sum(map(len,nbr))//2} diameter={n-1} wiener={int(wiener)}')
    print('PRIMARY_CERTIFICATE_OK')

if __name__=='__main__':main()
