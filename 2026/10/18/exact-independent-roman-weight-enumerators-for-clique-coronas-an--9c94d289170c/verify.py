#!/usr/bin/env python3
"""Independent brute-force enumeration of Roman-independent labelings on graph coronas."""
from itertools import product
from collections import Counter
from fractions import Fraction
from math import comb, ceil


def cycle_edges(n):
    return [(i, (i+1)%n) for i in range(n)]


def path_edges(n):
    return [(i,i+1) for i in range(n-1)]


def complete_edges(n):
    return [(i,j) for i in range(n) for j in range(i+1,n)]


def corona(n, base_edges, m):
    edges=list(base_edges)
    for i in range(n):
        cells=[n+m*i+j for j in range(m)]
        edges.extend((i,v) for v in cells)
        edges.extend((u,v) for j,u in enumerate(cells) for v in cells[j+1:])
    return n*(m+1), edges


def brute(n, base_edges, m):
    N,edges=corona(n,base_edges,m)
    neigh=[set() for _ in range(N)]
    for u,v in edges:
        neigh[u].add(v);neigh[v].add(u)
    counts=Counter()
    for f in product((0,1,2),repeat=N):
        if any(f[u] and f[v] for u,v in edges):
            continue
        if any(f[u]==0 and all(f[v]!=2 for v in neigh[u]) for u in range(N)):
            continue
        counts[sum(f)]+=1
    return dict(counts)


def theoretical(n,edges,m):
    adj=[0]*n
    for u,v in edges:
        adj[u]|=1<<v;adj[v]|=1<<u
    c=Counter()
    for S in range(1<<n):
        if any(S&(1<<i) and S&adj[i] for i in range(n)):
            continue
        if m>=2:
            c[2*n]+=m**(n-S.bit_count())
        else:
            neighbor=0
            for i in range(n):
                if S&(1<<i):neighbor|=adj[i]
            r=neighbor.bit_count()
            for a in range(r+1):
                c[2*n-r+a]+=comb(r,a)
    return dict(c)


def trace_polys(nmax):
    # Polynomial transition matrix, calculated by integer coefficient convolutions.
    def mul(a,b):
        out=Counter()
        for d,x in a.items():
            for e,y in b.items():out[d+e]+=x*y
        return out
    Z={}
    T=[[{2:1},{1:1,2:1},Z],[Z,Z,{2:1}],[{1:1,2:1},{1:1,2:1},Z]]
    M=[[{0:1} if i==j else {} for j in range(3)] for i in range(3)]
    polynomials={}
    for n in range(1,nmax+1):
        M=[[sum_polys(*(mul(M[i][k],T[k][j]) for k in range(3))) for j in range(3)] for i in range(3)]
        if n>=3:
            polynomials[n]=dict(sum_polys(*(M[i][i] for i in range(3))))
    return polynomials


def sum_polys(*args):
    c=Counter()
    for p in args:c.update(p)
    return dict(c)


def min_count(n):
    if n%3==0:return 3
    if n%3==1:return n*(n+5)//6
    return n


def main():
    tests=[(3,cycle_edges(3),1),(4,cycle_edges(4),1),(5,cycle_edges(5),1),
           (6,cycle_edges(6),1),(2,path_edges(2),1),(3,path_edges(3),1),
           (4,path_edges(4),1),(1,[],1),
           (3,cycle_edges(3),2),(4,cycle_edges(4),2),(3,cycle_edges(3),3),
           (3,path_edges(3),2),(2,path_edges(2),3)]
    seen=0
    for n,edges,m in tests:
        obtained=brute(n,edges,m)
        expected=theoretical(n,edges,m)
        if obtained!=expected:raise AssertionError((n,edges,m,obtained,expected))
        seen+=3**(n*(m+1))
    p=trace_polys(25)
    for n in range(3,26):
        if n<=12:
            expected=theoretical(n,cycle_edges(n),1)
            if p[n]!=expected:
                raise AssertionError(('transfer',n,p[n],expected))
        k=min(p[n]); c=p[n][k]
        if k!=ceil(4*n/3) or c!=min_count(n):
            raise AssertionError(('optimum',n,k,c))
    print('VERIFICATION_OK raw_labelings_examined=%d graph_cases=%d transfer_cycles=3..25 optimum_cycles=3..25'%(seen,len(tests)))

if __name__=='__main__':main()
