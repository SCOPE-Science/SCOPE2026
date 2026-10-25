#!/usr/bin/env python3
"""Reproducible finite checks for ordinary cut-complex rank formulae."""
from itertools import combinations
from math import comb


def transfer_connected(n):
    """Coefficient recurrence for connected ladder subsets, by final-column state."""
    single = {1: 1}  # one specified row
    both = {2: 1}
    total = {}
    for width in range(1, n + 1):
        for size, count in single.items():
            total[size] = total.get(size, 0) + 2 * (n - width + 1) * count
        for size, count in both.items():
            total[size] = total.get(size, 0) + (n - width + 1) * count
        new_single, new_both = {}, {}
        for size, count in single.items():
            new_single[size+1] = new_single.get(size+1, 0) + count
            new_both[size+2] = new_both.get(size+2, 0) + 2*count
        for size, count in both.items():
            new_single[size+1] = new_single.get(size+1, 0) + count
            new_both[size+2] = new_both.get(size+2, 0) + count
        single, both = new_single, new_both
    return total


def adjacency(n):
    adj = [set() for _ in range(2*n)]
    for i in range(n):
        a,b = 2*i,2*i+1
        adj[a].add(b);adj[b].add(a)
        if i+1<n:
            for s in range(2):
                x,y=2*i+s,2*(i+1)+s
                adj[x].add(y);adj[y].add(x)
    return adj


def connected(S, adj):
    S=set(S)
    if not S: return False
    seen={next(iter(S))};queue=list(seen)
    for u in queue:
        for v in adj[u].intersection(S):
            if v not in seen:
                seen.add(v);queue.append(v)
    return len(seen)==len(S)


def brute_counts(n,k,adj):
    N=2*n
    c=sum(connected(T,adj) for T in combinations(range(N),k))
    b=sum(all(connected(set(T)-{v},adj) for v in T) for T in combinations(range(N),k+1))
    return c,b


def actual_euler(n,k,adj):
    """Independently build all facet subfaces and take reduced Euler sum."""
    N=2*n;vertices=set(range(N));faces={frozenset()}
    for T in combinations(range(N),k):
        if connected(T,adj):continue
        F=vertices.difference(T)
        for j in range(len(F)+1):
            for f in combinations(F,j):faces.add(frozenset(f))
    return sum((-1)**(len(F)-1) for F in faces)


def check():
    tests=0
    for n in range(3,8):
        adj=adjacency(n);counts=transfer_connected(n)
        for k in range(3, min(2*n-3,8)+1):
            c,b=brute_counts(n,k,adj)
            assert c==counts.get(k,0),(n,k,'connected',c,counts)
            expected_b=n-(k-1)//2 if k%2 else 0
            assert b==expected_b,(n,k,'robust',b,expected_b)
            beta=comb(2*n-1,k-1)-c+b
            assert beta>=0,(n,k,beta)
            if n<=5:
                e=actual_euler(n,k,adj)
                assert e==(-1)**(2*n-k-1)*beta,(n,k,'Euler',e,beta)
            if k==5 and n>=4:
                assert beta==comb(2*n-1,4)-19*n+54,(n,k,beta)
            print(f'n={n}, k={k}: connected={c}, deletion_robust={b}, sphere_rank={beta}')
            tests+=1
    assert tests==21,tests
    print('VERIFY_OK: 21 parameter pairs; brute induced sets, transfer coefficients, deletion robustness, and small Euler characteristics agree.')

if __name__=='__main__':check()
