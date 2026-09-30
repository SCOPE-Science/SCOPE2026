#!/usr/bin/env python3
"""Finite replay for the crown-graph proper conflict-free theorem.

This script exhaustively excludes colorings with too few colors for Cr_n at
n=2,3,4,5 (up to permutation of color names via restricted-growth search),
and directly checks the stated constructions for n=2,...,12.
"""
from collections import Counter


def crown(n):
    adj=[set() for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                adj[i].add(n+j)
                adj[n+j].add(i)
    return adj


def is_pcf(adj, col):
    for u, Nu in enumerate(adj):
        for v in Nu:
            if col[u]==col[v]:
                return False
        counts=Counter(col[v] for v in Nu)
        if Nu and not any(m==1 for m in counts.values()):
            return False
    return True


def exists_with_at_most(n, k):
    adj=crown(n)
    N=2*n
    col=[-1]*N
    col[0]=0
    order=[0]+[x for i in range(n) for x in (i,n+i) if x!=0]

    def rec(pos, max_used):
        if pos==len(order):
            return is_pcf(adj,col)
        u=order[pos]
        # Restricted-growth canonicalization of color names.
        upper=min(k-1,max_used+1)
        for c in range(upper+1):
            if any(col[v]==c for v in adj[u] if col[v]>=0):
                continue
            col[u]=c
            if rec(pos+1,max(max_used,c)):
                return True
            col[u]=-1
        return False

    return rec(1,0)


def construction(n):
    if n==2:
        return [0,0,1,1]
    if n==3:
        return [0,1,2,0,1,2]
    # a1,b1 share 0; a2,b2 share 1; remaining A use 2, remaining B use 3.
    return [0,1]+[2]*(n-2)+[0,1]+[3]*(n-2)


def main():
    expected={2:2,3:3,4:4,5:4}
    for n,target in expected.items():
        assert is_pcf(crown(n),construction(n))
        assert not exists_with_at_most(n,target-1), (n,target)
    for n in range(2,13):
        assert is_pcf(crown(n),construction(n)), n
    print('VERIFY_OK crown PCF exact small cases and constructions')


if __name__=='__main__':
    main()
