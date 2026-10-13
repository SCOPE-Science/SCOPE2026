#!/usr/bin/env python3
"""Direct exhaustive check of a stated minimal-fort classification."""
from collections import Counter
from math import comb


def make_graph(r):
    n = 6*r+1
    adj = [0]*n
    for v in range(1,n):
        adj[0] |= 1 << v
        adj[v] |= 1
    for b in range(r):
        base = 1+6*b
        for i in range(6):
            for j in range(i+1,6):
                if i//2 == j//2:  # deleted perfect matching
                    continue
                u,v=base+i,base+j
                adj[u] |= 1 << v
                adj[v] |= 1 << u
    return adj


def fort(mask, adj):
    for v, a in enumerate(adj):
        if not ((mask >> v) & 1) and (mask & a).bit_count() == 1:
            return False
    return mask!=0


def check(r):
    adj=make_graph(r)
    n=len(adj)
    m=1<<n
    isfort=bytearray(m)
    contains=bytearray(m)
    for s in range(1,m):
        f=fort(s,adj)
        isfort[s]=f
        if f:
            contains[s]=1
        else:
            t=s
            while t:
                low=t&-t
                if contains[s^low]:
                    contains[s]=1
                    break
                t ^= low
    actual=Counter()
    numfort=0
    for s in range(1,m):
        if not isfort[s]:
            continue
        numfort+=1
        t=s
        minimal=True
        while t:
            low=t&-t
            if contains[s^low]:
                minimal=False
                break
            t ^=low
        if minimal:
            actual[s.bit_count()]+=1
    expected=Counter({2:3*r,3:8*r,2*r+1:12**r})
    if r==1:
        expected=Counter({2:3,3:20})
    assert actual==expected,(r,actual,expected)
    print(f'r={r} vertices={n} enumerated_subsets={m-1} forts={numfort} '
          f'minimal={sum(actual.values())} coefficient_profile={sorted(actual.items())}')


if __name__=='__main__':
    for r in (1,2,3):
        check(r)
    print('VERIFY_OK: exhaustive arbitrary-subfort checks, including non-singleton removals')
