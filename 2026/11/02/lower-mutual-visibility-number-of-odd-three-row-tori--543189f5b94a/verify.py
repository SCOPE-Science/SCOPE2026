#!/usr/bin/env python3
"""Self-contained graph-distance tests of the odd triangular-cylinder theorem."""
from collections import deque
from itertools import combinations


def graph(n):
    adj = [set() for _ in range(3*n)]
    for r in range(3):
        for j in range(n):
            v = r*n+j
            for rr in range(3):
                if rr != r:
                    adj[v].add(rr*n+j)
            adj[v].update((r*n+(j-1)%n, r*n+(j+1)%n))
    return [tuple(a) for a in adj]


def distances(adj, start, forbidden=()):
    f = set(forbidden)
    if start in f: raise ValueError('start forbidden')
    d = [-1]*len(adj)
    d[start] = 0
    q = deque([start])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if d[v] < 0 and v not in f:
                d[v] = d[u]+1
                q.append(v)
    return d


def mutual(adj, full_d, S):
    for a,b in combinations(S,2):
        if distances(adj,a,set(S)-{a,b})[b] != full_d[a][b]:
            return False
    return True


def maximal(adj, full_d, S):
    return mutual(adj,full_d,S) and all(not mutual(adj,full_d,(*S,v)) for v in range(len(adj)) if v not in S)


def test(n, exhaustive=False):
    adj=graph(n)
    full=[distances(adj,u) for u in range(len(adj))]
    k=(n-1)//2
    S=tuple(r*n+j for r,j in ((0,0),(0,1),(1,0),(2,k+1),(2,k+2)))
    assert maximal(adj,full,S), (n,S)
    if exhaustive:
        for size in range(1,5):
            for T in combinations(range(3*n),size):
                assert not maximal(adj,full,T),(n,T)
    print('PASS',n,'explicit_five_maximal',True,'exhaustive_below_five',exhaustive)

if __name__=='__main__':
    for n in (5,7,9,11,13,15,17,19,21,31,41,51):
        test(n, exhaustive=n<=9)
    print('VERIFY_OK')
