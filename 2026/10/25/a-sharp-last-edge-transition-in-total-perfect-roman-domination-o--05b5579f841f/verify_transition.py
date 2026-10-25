#!/usr/bin/env python3
"""Direct exact low-weight census for total perfect Roman functions.
Reproducible with Python 3.8+ and standard library only.
"""
from itertools import combinations
from collections import Counter

def edges(n,k):
    return [[n+j for j in range(n) if (i!=j or i>=k)] for i in range(n)] + [[i for i in range(n) if (i!=j or i>=k)] for j in range(n)]

def valid(L,adj):
    for v,a in enumerate(L):
        if a==0:
            if sum(L[u]==2 for u in adj[v])!=1:return False
        else:
            if not any(L[u]>0 for u in adj[v]):return False
    return True

def exhaustive(n,k):
    N=2*n;adj=edges(n,k)
    found={}
    # Independent low-weight enumeration (all assignments with weight at most six).
    for t in range(0,4):
        for twos in combinations(range(N),t):
            T=set(twos)
            rem=[i for i in range(N) if i not in T]
            for o in range(0,7-2*t):
                for ones in combinations(rem,o):
                    L=[0]*N
                    for v in twos:L[v]=2
                    for v in ones:L[v]=1
                    if valid(L,adj):found[tuple(L)]=sum(L)
    return found

def expected(n,k):
    S=set();N=2*n
    def make(twos=(),ones=()):
        L=[0]*N
        for v in twos:L[v]=2
        for v in ones:L[v]=1
        S.add(tuple(L))
    if k<n:
        for i in range(k,n):
            for j in range(k,n): make((i,n+j))
    else:
        for i in range(n):
            for j in range(n):
                if i==j:
                    for u in range(n):
                        for v in range(n):
                            if u!=i and v!=i:make((i,n+i),(u,n+v))
                else:make((i,n+j),(j,n+i))
        if n==3:
            make((),range(N))
            for i in range(n):
                for j in range(n):
                    if i!=j:
                        make((i,),tuple(u for u in range(n) if u!=i)+(n+i,n+j))
                        make((n+i,),tuple(n+u for u in range(n) if u!=i)+(i,j))
    return S

if __name__=='__main__':
    runs=0
    for n in range(3,9):
        for k in range(n+1):
            all_low=exhaustive(n,k)
            ex=expected(n,k)
            best=4 if k<n else 6
            assert min(all_low.values()) == best,(n,k,"minimum disagreement")
            got={L:w for L,w in all_low.items() if w==best}
            assert len(got)==len(ex),(n,k,len(got),len(ex))
            assert set(got)==ex,(n,k,'classification-mismatch')
            assert set(got.values())=={best},(n,k,Counter(got.values()))
            count=(n-k)**2 if k<n else n*n*(n-1)+(13 if n==3 else 0)
            assert len(got)==count,(n,k,'count-mismatch')
            runs+=1
        print(f'PASS n={n}: k=0..{n}, exhaustive full low-weight classification')
    print('VERIFY_OK',runs,'n,k cases; all {0,1,2} labelings of total weight <=6 independently enumerated; exact optimizer witnesses checked')
