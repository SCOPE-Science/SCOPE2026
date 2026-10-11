#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache

def partitions(n, lo=1):
    if n==0:
        yield ()
        return
    for x in range(lo,n+1):
        for rest in partitions(n-x,x):
            yield (x,)+rest

def words(counts):
    counts=tuple(counts)
    n=sum(counts)
    @lru_cache(None)
    def rec(state):
        if sum(state)==0:
            return ((),)
        out=[]
        for i,c in enumerate(state):
            if c:
                ns=list(state); ns[i]-=1
                for tail in rec(tuple(ns)):
                    out.append((i,)+tail)
        return tuple(out)
    return rec(counts)

def norm2(parts, w):
    N=sum(parts)
    used=[0]*len(parts)
    ans=Fraction(0,1)
    seen=0
    for p in w:
        indeg=seen-used[p]
        deg=N-parts[p]
        x=Fraction(2*indeg-deg,2)
        ans += x*x
        used[p]+=1
        seen+=1
    return ans

def math_factorial(n):
    z=1
    for i in range(2,n+1): z*=i
    return z

cases=0
orders=0
for N in range(2,9):
    for parts in partitions(N):
        if len(parts)<2:
            continue
        target=Fraction(N**3-sum(x**3 for x in parts),12)
        ws=words(parts)
        vals=[norm2(parts,w) for w in ws]
        mx=max(vals)
        assert mx==target,(parts,mx,target)

        maximizers=[w for w,v in zip(ws,vals) if v==mx]
        block=[]
        for perm in __import__('itertools').permutations(range(len(parts))):
            w=tuple(i for i in perm for _ in range(parts[i]))
            block.append(w)
        assert set(maximizers)==set(block),(parts,len(maximizers),len(block))
        assert len(maximizers)==math_factorial(len(parts))

        diameter2=4*target
        assert diameter2==Fraction(N**3-sum(x**3 for x in parts),3)
        cases+=1
        orders+=len(ws)

print(f"VERIFY_OK multipartite-graphical-zonotope cases={cases} topological_words={orders} N<=8")
