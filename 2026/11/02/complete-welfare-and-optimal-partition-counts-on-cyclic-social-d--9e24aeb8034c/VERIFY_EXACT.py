#!/usr/bin/env python3
"""Exact arithmetic cross-checks of normalized social-distance welfare on paths and cycles.
Uses Fraction throughout; external packages not required.
"""
from fractions import Fraction as Q
from functools import lru_cache
from math import comb

def H(n):
    return sum((Q(1,k) for k in range(1,n+1)),Q(0))

def block(k):
    return 2*(H(k)-1) if k>0 else Q(0)

def path_w(n):
    if n==1: return Q(0)
    q,r=divmod(n,3)
    return Q(5*q,3)+(Q(0) if r==0 else Q(1,2) if r==1 else Q(1))

def path_count(n):
    if n==1:return 1
    q,r=divmod(n,3)
    if r==0:return 1
    if r==1:return q
    return q+1+(comb(q,2) if q>=2 else 0)

def cycle_grand(n):
    assert n>=3
    return 2*H((n-1)//2)+(Q(2,n) if n%2==0 else Q(0))

def cycle_count(n):
    assert n>=3
    if n<=5:return 1
    if n==6:return 4
    q,r=divmod(n,3)
    if r==0:return 3
    if r==1:return n
    return n*(q+1)//2

def all_partitions(n):
    arr=[0]*n
    def rec(i,maximum):
        if i==n:
            parts=[[] for _ in range(maximum+1)]
            for k,a in enumerate(arr):parts[a].append(k)
            yield parts
        else:
            for z in range(maximum+2):
                arr[i]=z
                yield from rec(i+1,max(maximum,z))
    yield from rec(1,0)

def welfare(parts,n,cycle):
    total=Q(0)
    for b in parts:
        k=len(b)
        if k<2:continue
        bs=set(b)
        for s in b:
            dist={s:0}
            queue=[s]
            for v in queue:
                nb=([(v-1)%n,(v+1)%n] if cycle else [v-1,v+1])
                for w in nb:
                    if 0<=w<n and w in bs and w not in dist:
                        dist[w]=dist[v]+1
                        queue.append(w)
            for t in b:
                if t>s and t in dist:
                    total+=Q(2,k*dist[t])
    return total

def exhaustive_general(n,cyc):
    optimum=None; count=0; counter=0
    for parts in all_partitions(n):
        v=welfare(parts,n,cyc)
        if optimum is None or v>optimum:
            optimum=v;count=1
        elif v==optimum:count+=1
        counter+=1
    expected= (cycle_grand(n) if n<=5 else path_w(n) if n>=6 else None) if cyc else path_w(n)
    if cyc and n==6:expected=cycle_grand(n)
    ec=(cycle_count(n) if cyc else path_count(n))
    assert optimum==expected,(n,cyc,'welfare',optimum,expected)
    assert count==ec,(n,cyc,'number',count,ec)
    return counter, count

@lru_cache(None)
def path_dp(n):
    if n==0:return Q(0),1
    best=Q(-1);count=0
    for k in range(1,n+1):
        val,cn=path_dp(n-k)
        x=val+block(k)
        if x>best:best=x;count=cn
        elif x==best:count+=cn
    return best,count

def cyclic_compositions(n):
    # Each chosen subset of cycle edges is the set of boundaries. For >1 cuts,
    # traverse arcs between consecutive cuts and add block(k).
    # Single cut leaves a grand coalition with cycle edges intact, handled separately.
    ans=0;top=Q(-1)
    for mask in range(1,1<<n):
        cut=[i for i in range(n) if mask>>i&1]
        if len(cut)==1:continue
        value=Q(0)
        for j,k in enumerate(cut):
            length=(cut[(j+1)%len(cut)]-k)%n
            value+=block(length)
        if value>top:top=value;ans=1
        elif value==top:ans+=1
    return top,ans

def main():
    for n in range(1,101):
        v,c=path_dp(n)
        assert v==path_w(n),(n,v,path_w(n))
        assert c==path_count(n),(n,c,path_count(n))
    print('PASS: exact dynamic programming for path lengths 1..100 (both optimum and count).')
    for n in range(3,17):
        v,c=cyclic_compositions(n)
        goal=path_w(n) if n>=5 else (block(2)+block(1) if n==3 else block(3)+block(1))
        if n>=5:assert v==goal,(n,v,goal)
        best=max(cycle_grand(n),v)
        assert best==(cycle_grand(n) if n<=6 else path_w(n))
        count=(c if v==best else 0)+(1 if cycle_grand(n)==best else 0)
        assert count==cycle_count(n),(n,count,cycle_count(n))
    print('PASS: exact cyclic cut enumeration for cycle lengths 3..16 (optimum and counts).')
    for n in range(1,10):
        total,count=exhaustive_general(n,False)
        print(f'PASS: all {total} set partitions of P_{n}; optimum count {count}.')
    for n in range(3,10):
        total,count=exhaustive_general(n,True)
        print(f'PASS: all {total} set partitions of C_{n}; optimum count {count}.')
    print('ALL EXACT TESTS PASS.')
if __name__=='__main__':main()
