#!/usr/bin/env python3
"""Independent exhaustive verifier for super-domination enumerators."""
from collections import Counter
from itertools import combinations
from math import comb

def graph(a,b,t):
    n=a+b
    adj=[0]*n
    for i in range(a):
        for j in range(b):
            if i==j and i<t: continue
            adj[i]|=1<<(a+j)
            adj[a+j]|=1<<i
    return adj

def brute(a,b,t):
    nb=graph(a,b,t)
    n=a+b
    by_shape=Counter()
    for x in range(1<<n):
        omitted=[i for i in range(n) if x>>i&1]
        if all(any((nb[v] & x)==(1<<u) for v in range(n) if not(x>>v&1)) for u in omitted):
            alpha=sum(v<a for v in omitted)
            beta=len(omitted)-alpha
            by_shape[alpha,beta]+=1
    return by_shape

def formula(a,b,t):
    c2=comb(t,2)
    return {(0,0):1,(1,0):a,(0,1):b,
            (1,1):a*b,(2,0):c2,(0,2):c2,
            (2,1):c2*(b-2-(t-2 if a==3 else 0)),
            (1,2):c2*(a-2-(t-2 if b==3 else 0)),
            (2,2):c2*comb(t-2,2) if t>=2 else 0}

def verify():
    profiles=0; masks=0; omitted_total=0
    for a in range(3,8):
        for b in range(3,8):
            for t in range(min(a,b)+1):
                actual=brute(a,b,t)
                expected=Counter({k:v for k,v in formula(a,b,t).items() if v})
                assert actual==expected, (a,b,t,actual,expected)
                profiles+=1; masks+=1<<(a+b)
                omitted_total+=sum(actual.values())
    print('VERIFICATION_OK',f'profiles={profiles}',f'checked_vertex_subsets={masks}',f'super_dominating_sets={omitted_total}')
    for a,b,t in [(3,3,3),(3,4,3),(4,4,0),(4,4,2),(4,4,3),(4,4,4),(5,6,4),(7,7,7)]:
        print(f'profile=({a},{b},{t})', 'omitted_counts=',[sum(v for (i,j),v in brute(a,b,t).items() if i+j==k) for k in range(5)])

if __name__=='__main__':verify()
