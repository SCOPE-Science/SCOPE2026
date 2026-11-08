#!/usr/bin/env python3
"""Exact independent enumeration for one-edge-deleted cube spread.
All arithmetic is integral; no optimizer or floating-point operations are used.
"""
from collections import deque

def graph(d):
    n=1 << d
    neighbors=[[] for _ in range(n)]
    for x in range(n):
        for i in range(d):
            y=x ^ (1 << i)
            if x < y and not (x==0 and y==1):
                neighbors[x].append(y)
                neighbors[y].append(x)
    return neighbors

def height_profiles(d):
    """All normalized f with |f(u)-f(v)|=1 on EVERY surviving edge."""
    ns=graph(d)
    n=len(ns)
    # BFS produces a spanning tree; each vertex already has a parent.
    parent={0:None}
    order=[0]
    for x in order:
        for y in ns[x]:
            if y not in parent:
                parent[y]=x
                order.append(y)
    assert len(order)==n
    f=[None]*n
    f[0]=0
    def rec(j):
        if j==n:
            yield tuple(f)
            return
        v=order[j]
        for value in (f[parent[v]]-1, f[parent[v]]+1):
            if all(f[w] is None or abs(value-f[w])==1 for w in ns[v]):
                f[v]=value
                yield from rec(j+1)
        f[v]=None
    yield from rec(1)

def integer_profiles(d):
    """All normalized integer 1-Lipschitz functions; a separate enumeration."""
    ns=graph(d)
    n=len(ns)
    dist=[None]*n
    dist[0]=0
    q=deque([0])
    while q:
        u=q.popleft()
        for v in ns[u]:
            if dist[v] is None:
                dist[v]=dist[u]+1
                q.append(v)
    order=[0]+sorted(range(1,n),key=lambda v:(dist[v],-len(ns[v]),v))
    f=[None]*n
    f[0]=0
    def rec(j):
        if j==n:
            yield tuple(f)
            return
        v=order[j]
        lo=-dist[v]
        hi=dist[v]
        for u in ns[v]:
            if f[u] is not None:
                lo=max(lo,f[u]-1)
                hi=min(hi,f[u]+1)
        for z in range(lo,hi+1):
            f[v]=z
            yield from rec(j+1)
        f[v]=None
    yield from rec(1)

def varnum(f):
    n=len(f)
    return n*sum(v*v for v in f)-sum(f)**2

def audit(d, generator, expected_count, expected_best, expected_winners):
    n=1<<d
    count=0
    high=-1
    winners=[]
    for f in generator(d):
        count+=1
        v=varnum(f)
        if v>high:
            high=v;winners=[f]
        elif v==high:
            winners.append(f)
    assert (count,high,len(winners))==(expected_count,expected_best,expected_winners),(d,count,high,len(winners))
    print('EXACT',generator.__name__,'d',d,'total',count,'maxnumer',high,'over',n*n,'winners',len(winners))
    return winners

def main():
    w2=audit(2,height_profiles,8,20,2)
    w3=audit(3,height_profiles,44,60,4)
    w4=audit(4,height_profiles,1080,256,16)
    assert set(w2)=={(0,3,1,2),(0,-3,-1,-2)}
    a=(0,3,1,2,1,2,0,1)
    b=(0,3,1,2,1,2,2,3)
    assert set(w3)=={a,b,tuple(-x for x in a),tuple(-x for x in b)}
    signed_sums={tuple(sum(sign[i]*((x>>i)&1) for i in range(4)) for x in range(16))
                 for sign in __import__('itertools').product((-1,1),repeat=4)}
    assert set(w4)==signed_sums
    # Independent search space: ALL integer Lipschitz profiles, not just tight heights.
    for d,count,best,win in ((2,27,20,2),(3,597,60,4),(4,221637,256,16)):
        alt=audit(d,integer_profiles,count,best,win)
        assert set(alt)==(set(w2) if d==2 else set(w3) if d==3 else set(w4))
    print('ALL_ONE_EDGE_DELETED_CUBE_BASE_CASES_EXACT_OK')
if __name__=='__main__':main()
