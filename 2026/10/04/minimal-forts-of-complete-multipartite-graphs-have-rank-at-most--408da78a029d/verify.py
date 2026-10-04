#!/usr/bin/env python3
from itertools import combinations
from math import comb

def integer_partitions(n, lo=1):
    if n == 0:
        yield []
        return
    for x in range(lo, n+1):
        for tail in integer_partitions(n-x, x):
            yield [x] + tail

def graph(parts):
    part=[]
    for i,n in enumerate(parts): part += [i]*n
    N=len(part)
    adj=[set() for _ in range(N)]
    for u in range(N):
        for v in range(u+1,N):
            if part[u] != part[v]:
                adj[u].add(v); adj[v].add(u)
    return adj,part

def is_fort(adj,F):
    F=set(F)
    return bool(F) and all(len(adj[v] & F) != 1 for v in range(len(adj)) if v not in F)

def brute_minimal_forts(parts):
    adj,_=graph(parts); N=len(adj)
    forts=[]
    for k in range(1,N+1):
        for F in combinations(range(N),k):
            if is_fort(adj,F): forts.append(frozenset(F))
    minimal=[]
    for F in sorted(forts,key=len):
        if not any(H < F for H in minimal): minimal.append(F)
    return set(minimal)

def predicted(parts):
    _,part=graph(parts); N=len(part); ans=set()
    for F in combinations(range(N),2):
        i,j=part[F[0]],part[F[1]]
        if i==j or (parts[i]==1 and parts[j]==1): ans.add(frozenset(F))
    for F in combinations(range(N),3):
        I=[part[v] for v in F]
        if len(set(I))==3 and sum(parts[i]==1 for i in I)<=1: ans.add(frozenset(F))
    return ans

def formula(parts):
    q=sum(n==1 for n in parts); L=[n for n in parts if n>=2]
    ans=sum(comb(n,2) for n in L)+comb(q,2)
    ans += sum(L[i]*L[j]*L[k] for i in range(len(L)) for j in range(i+1,len(L)) for k in range(j+1,len(L)))
    ans += q*sum(L[i]*L[j] for i in range(len(L)) for j in range(i+1,len(L)))
    return ans

types=subsets=minimals=0
for N in range(2,10):
    for parts in integer_partitions(N):
        if len(parts)<2: continue
        b=brute_minimal_forts(parts); p=predicted(parts)
        if b != p: raise AssertionError((parts,b-p,p-b))
        if len(b) != formula(parts): raise AssertionError((parts,len(b),formula(parts)))
        types += 1; subsets += (1<<N)-1; minimals += len(b)
print(f"ALL CHECKS PASSED; multipartite_types={types}; nonempty_subsets={subsets}; minimal_forts={minimals}; max_order=9")
