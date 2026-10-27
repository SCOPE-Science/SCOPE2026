#!/usr/bin/env python3
"""Finite independent checks of the sharp cyclic three-state excitable automaton cutoff."""
from collections import deque
import random

def step(a):
    n=len(a)
    return tuple(2 if a[i]==1 else 0 if a[i]==2 else int(a[(i-1)%n]==1 or a[(i+1)%n]==1) for i in range(n))

def stable(a):
    b=step(a)
    return b==(0,)*len(a) or b==a[1:]+a[:1] or b==a[-1:]+a[:-1]

def bitstep(x,n):
    a=[(x//3**i)%3 for i in range(n)]
    return sum(y*3**i for i,y in enumerate(step(a)))

def all_depths(n):
    N=3**n
    succ=[bitstep(x,n) for x in range(N)]
    indeg=[0]*N
    for y in succ: indeg[y]+=1
    q=deque(x for x in range(N) if not indeg[x])
    order=[]
    while q:
        x=q.popleft();order.append(x)
        y=succ[x];indeg[y]-=1
        if not indeg[y]:q.append(y)
    dep=[0]*N
    for x in reversed(order):dep[x]=dep[succ[x]]+1
    return max(dep),dep.count(max(dep)),succ

def particles(a):
    n=len(a)
    right={i for i in range(n) if a[(i-1)%n]==2 and a[i]==1}
    left={i for i in range(n) if a[i]==1 and a[(i+1)%n]==2}
    return right,left

if __name__=='__main__':
    checked=0
    for n in range(3,12):
        m,count,succ=all_depths(n)
        assert m==n//2+2,(n,m)
        x=1
        for t in range(m):
            assert x!=0
            x=succ[x]
        assert x==0
        checked+=3**n
    for n in range(3,9):
        for x in range(3**n):
            a=tuple((x//3**i)%3 for i in range(n))
            b=step(a);c=step(b)
            r,l=particles(b);r2,l2=particles(c)
            assert all((j-1)%n in r and b[j]==0 for j in r2)
            assert all((j+1)%n in l and b[j]==0 for j in l2)
            if not r or not l:
                assert stable(c)
    rng=random.Random(20261021)
    for z in range(2000):
        n=rng.randrange(12,201)
        a=tuple(rng.randrange(3) for i in range(n))
        for t in range(n//2+2):a=step(a)
        assert step(a)==a or step(a)==a[1:]+a[:1] or step(a)==a[-1:]+a[:-1]
    print('VERIFY_OK exhaustive_states',checked,'local_particle_checks',sum(3**n for n in range(3,9)),'random_large',2000)
