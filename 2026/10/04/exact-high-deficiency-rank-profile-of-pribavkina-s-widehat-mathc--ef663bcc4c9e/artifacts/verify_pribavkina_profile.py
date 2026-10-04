#!/usr/bin/env python3
from itertools import product
from collections import deque

def unbordered(u):
    k=len(u)
    return all(u[:j]!=u[-j:] for j in range(1,k))

def trans_for(A,u):
    k=len(u); n=2*k
    T={}
    for a in A:
        t=[None]*n; t[0]=0
        for i in range(1,k):
            t[i]=i+1 if a==u[i-1] else k+i
        t[k]=0 if a==u[k-1] else 1
        for i in range(k+1,2*k-1): t[i]=i+1
        t[2*k-1]=1
        T[a]=t
    return T

def step(S,t):
    R=0
    while S:
        b=S & -S; i=b.bit_length()-1; S-=b; R |= 1<<t[i]
    return R

def bfs_thresholds(A,u):
    k=len(u); n=2*k; T=trans_for(A,u); start=(1<<n)-1
    dist={start:0}; q=deque([start]); best=[10**9]*(n+1); best[n]=0
    while q:
        S=q.popleft(); d=dist[S]
        for a in A:
            R=step(S,T[a])
            if R not in dist:
                dist[R]=d+1; q.append(R); r=R.bit_count(); best[r]=min(best[r],d+1)
    out=[]
    for s in range(k,2*k):
        out.append(min(d for R,d in dist.items() if R.bit_count()<=2*k-s))
    return out

def witness_rank(A,u,r,a):
    k=len(u); T=trans_for(A,u); S=(1<<(2*k))-1
    w=list(u)
    for _ in range(r): w.append(a); w.extend(u)
    for x in w: S=step(S,T[x])
    return len(w),S.bit_count()

def check_family(A,maxk):
    checked=0
    for k in range(2,maxk+1):
        for u in product(A, repeat=k):
            if not unbordered(u): continue
            got=bfs_thresholds(A,u)
            want=[k+r*(k+1) for r in range(k)]
            assert got==want,(A,u,got,want)
            for a in A:
                for r in range(k):
                    L,R=witness_rank(A,u,r,a)
                    assert (L,R)==(want[r],k-r),(A,u,a,r,L,R,want[r])
            checked+=1
    return checked

b=check_family((0,1),7)
t=check_family((0,1,2),5)
print(f'binary_unbordered_checked={b}')
print(f'ternary_unbordered_checked={t}')
print('VERIFY_OK')
