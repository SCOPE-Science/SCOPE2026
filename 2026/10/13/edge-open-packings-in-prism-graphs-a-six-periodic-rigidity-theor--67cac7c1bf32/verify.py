#!/usr/bin/env python3
"""Independent exact tests for the edge-open-packing theorem on prism graphs.
Standard Python only; no source downloads or external packages.
"""
from functools import lru_cache
from itertools import product

def prism(n):
    assert n>=3
    edge={}
    for i in range(n):
        edge[('T',i)]=frozenset((i,(i+1)%n))
        edge[('B',i)]=frozenset((n+i,n+(i+1)%n))
        edge[('S',i)]=frozenset((i,n+i))
    return edge

def conflict_graph(n):
    edges=prism(n)
    ekeys=list(edges)
    actual=set(edges.values())
    adj=[0]*len(ekeys)
    for i in range(len(ekeys)):
        for j in range(i):
            first,second=edges[ekeys[i]],edges[ekeys[j]]
            conflict=any(frozenset((a,b)) in actual and frozenset((a,b))!=first and frozenset((a,b))!=second for a in first for b in second if a!=b)
            if conflict:
                adj[i]|=1<<j
                adj[j]|=1<<i
    return ekeys,adj

def pattern(n,phase):
    P=set()
    for i in range(n):
        j=(i+phase)%6
        if j in (0,1):P.add(('T',i))
        if j in (3,4):P.add(('B',i))
        if j in (1,4):P.add(('S',i))
    return P

def witness(n):
    if n==3:return {('T',1),('S',1)}
    r=n%6
    ph={0:0,1:2,2:1,3:0,4:2,5:2}[r]
    P=pattern(n,ph)
    if r in (2,3):P.remove(('T',n-2))
    return P

def valid(P,ekeys,adj):
    ids=[ekeys.index(x) for x in P]
    return all(not (adj[a]>>b)&1 for k,a in enumerate(ids) for b in ids[:k])

# Independently enumerate maximum independent sets for small conflict graphs.
def exact_optimum(adj):
    N=len(adj)
    @lru_cache(None)
    def f(avail):
        if avail==0:return 0
        # Choose a most constrained available candidate.
        bit=avail
        best=-1; degree=-1
        while bit:
            b=bit&-bit; v=b.bit_length()-1;bit-=b
            d=(adj[v]&avail).bit_count()
            if d>degree:degree=d;best=v
        omit=f(avail & ~(1<<best))
        take=1+f(avail & ~(1<<best) & ~adj[best])
        return max(omit,take)
    ans=f((1<<N)-1)
    return ans,f.cache_info().currsize

def equality_census(n):
    e,adj=conflict_graph(n)
    # Exactly one edge chosen from each of the n disjoint conflict triples.
    triples=[[e.index((a,i)) for a in ('T','B')] +[e.index(('S',(i+2)%n))] for i in range(n)]
    count=0
    def dfs(i,chosen):
        nonlocal count
        if i==n:
            count+=1;return
        for x in triples[i]:
            if all(not ((adj[x]>>j)&1) for j in chosen):dfs(i+1,chosen+[x])
    dfs(0,[])
    return count

def verify():
    t=0
    for n in range(3,181):
        keys,adj=conflict_graph(n)
        P=witness(n)
        assert len(P)==(n if n%6==0 else n-1),(n,len(P))
        assert valid(P,keys,adj),n
        t+=1
    print('witnesses_checked',t)
    # Independently cross-check the claimed complete local forbidden-pair table.
    for n in range(5,16):
        keys,adj=conflict_graph(n)
        for i,x in enumerate(keys):
            for j in range(i):
                y=keys[j]; typ,a=x; typ2,b=y
                if typ==typ2=='T' or typ==typ2=='B': bad=((a-b)%n in (2,n-2))
                elif typ==typ2=='S':bad=((a-b)%n in (1,n-1))
                elif typ in ('T','B') and typ2=='S':bad=((b-a)%n in (n-1,2))
                elif typ=='S' and typ2 in ('T','B'):bad=((a-b)%n in (n-1,2))
                else:bad=((a-b)%n in (0,1,n-1))
                assert bad==bool((adj[i]>>j)&1),(n,x,y,bad)
    print('local_conflict_table_checked',list(range(5,16)))
    for n in range(3,11):
        keys,adj=conflict_graph(n)
        optimum,states=exact_optimum(adj)
        expected=n if n%6==0 else n-1
        assert optimum==expected,(n,optimum,expected)
        print('exact_optimum',n,optimum,'states',states)
    for n in (3,6,9,12):
        cnt=equality_census(n)
        assert cnt==(6 if n%6==0 else 0),(n,cnt)
        print('upper_bound_equality_census',n,cnt)
    print('VERIFY_OK')

if __name__=='__main__': verify()
