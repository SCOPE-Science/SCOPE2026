#!/usr/bin/env python3
"""Independent shattering checker using hull avoidance, not concept enumeration."""
from itertools import combinations
from collections import Counter


def intervals(n):
    pairs = list(combinations(range(n), 2))
    N = len(pairs)
    adj = [[not set(pairs[i]) & set(pairs[j]) and i != j
            for j in range(N)] for i in range(N)]
    dist = [[999] * N for _ in range(N)]
    for i in range(N):
        dist[i][i] = 0
        for j in range(N):
            if adj[i][j]:
                dist[i][j] = 1
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    I = []
    for i,j in combinations(range(N),2):
        I.append((1<<i,1<<j,sum(1<<p for p in range(N)
                                    if dist[i][p]+dist[p][j]==dist[i][j])))
    return N,I


def hull(mask, I):
    while True:
        expanded = mask
        for a,b,mid in I:
            if mask & a and mask & b:
                expanded |= mid
        if expanded == mask:
            return mask
        mask = expanded


def shattered(S, I):
    T = S
    while True:
        if hull(T,I) & S != T:
            return False
        if T == 0:
            return True
        T = (T-1)&S


for n, expected, max_k in [
    (5,{0:1,1:10,2:45,3:90,4:15,5:0},5),
    (6,{0:1,1:15,2:105,3:255,4:0},4),
]:
    N,I=intervals(n)
    observed=Counter()
    for k in range(max_k+1):
        for ids in combinations(range(N),k):
            S=sum(1<<i for i in ids)
            if shattered(S,I):
                observed[k]+=1
    assert all(observed[k]==v for k,v in expected.items()), (n,observed)
    print('HULL_AVOIDANCE_INDEPENDENT_PASS n=%d profile=%s' % (n,dict(observed)))
print('ALL_INDEPENDENT_HULL_TRACE_CHECKS_PASS')
