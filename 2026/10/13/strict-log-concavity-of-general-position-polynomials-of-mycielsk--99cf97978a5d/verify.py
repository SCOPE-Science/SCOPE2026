#!/usr/bin/env python3
"""Reproducible finite checks for GP polynomials of Mycielski complete graphs.

Python 3 standard library only. The infinite assertions are proved in RESULT.md;
these checks are finite diagnostics, not an automated infinite certificate.
"""
from collections import Counter
from math import comb


def graph(n):
    N = 2*n+1
    adj = [set() for _ in range(N)]
    def edge(i,j):
        adj[i].add(j); adj[j].add(i)
    for i in range(n):
        for j in range(i+1,n):
            edge(i,j)
    for i in range(n):
        for j in range(n):
            if i != j:
                edge(i,n+j)
        edge(n+i,2*n)
    return adj


def distances(adj):
    N=len(adj)
    d=[]
    for s in range(N):
        ds=[N+1]*N
        ds[s]=0
        q=[s]
        for u in q:
            for v in adj[u]:
                if ds[v]>ds[u]+1:
                    ds[v]=ds[u]+1
                    q.append(v)
        d.append(ds)
    return d


def direct_gp_counts(n):
    d=distances(graph(n))
    N=2*n+1
    assert max(max(row) for row in d)==2
    forbidden_by_top=[[] for _ in range(N)]
    for a in range(N):
        for b in range(a+1,N):
            for c in range(b+1,N):
                if (d[a][b]+d[b][c]==d[a][c] or
                    d[a][c]+d[c][b]==d[a][b] or
                    d[b][a]+d[a][c]==d[b][c]):
                    forbidden_by_top[c].append((1<<a)|(1<<b)|(1<<c))
    valid=bytearray(1<<N)
    valid[0]=1
    result=[0]*(N+1)
    result[0]=1
    for m in range(1,1<<N):
        v=m.bit_length()-1
        p=m^(1<<v)
        if valid[p] and all((m&t)!=t for t in forbidden_by_top[v]):
            valid[m]=1
            result[m.bit_count()]+=1
    return result


def formula(n):
    p=[0]*(2*n+2)
    for a in range(n+1):
        p[a]+=2*comb(n,a)
        p[a+1]+=comb(n,a)
    p[0]-=1
    for a in range(n):
        p[a+1]+=n*comb(n-1,a)
    p[1]-=n
    p[2]+=2*n
    p[3]+=n*n
    return p


def inspect():
    total=0
    for n in range(2,9):
        d=direct_gp_counts(n)
        c=formula(n)
        assert d==c, (n,d,c)
        assert all(v==0 for v in c[n+2:])
        print(f'n={n}: {1<<(2*n+1)} subsets, polynomial={c[:n+2]}')
        total+=1<<(2*n+1)
    print('TOTAL independent shortest-path subset comparisons:',total)
    for n in range(2,251):
        a=formula(n)[:n+2]
        assert a[0]==1
        assert a[1]==2*n+1
        assert a[2]==n*(2*n+1)
        assert a[3]==n*(5*n*n-6*n+7)//6
        for k in range(4,n+2):
            assert a[k]*(n+1)==comb(n+1,k)*(2*(n+1)+k*(n-k))
        assert all(a[k]>0 for k in range(n+2))
        assert all(a[k]**2>a[k-1]*a[k+1] for k in range(1,n+1))
    print('Exact coefficient, support, and strict log-concavity checks: n=2..250 OK')
    print('FINITE VERIFICATION PASS (not an infinite proof)')

if __name__=='__main__':
    inspect()
