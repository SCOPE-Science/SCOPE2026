#!/usr/bin/env python3
"""Standalone exhaustive validation of forcing signatures against cycle/component criterion."""
from itertools import combinations
from math import isclose

def matchings(n,edges):
    ans=[]
    def rec(i,used,mask):
        if i==len(edges):
            ans.append((mask,used));return
        u,v=edges[i]
        rec(i+1,used,mask)
        if not ((used>>u)&1 or (used>>v)&1):
            rec(i+1,used|(1<<u)|(1<<v),mask|(1<<i))
    rec(0,0,0)
    return ans

def has_even_cycle(n,edges):
    # enumerate all simple cycles as a path (length>=4 even); no graph theory packages
    adj=[[] for _ in range(n)]
    for u,v in edges: adj[u].append(v);adj[v].append(u)
    for start in range(n):
        def rec(cur,seen,depth):
            for v in adj[cur]:
                if v==start and depth>=4 and depth%2==0: return True
                if v>start and not ((seen>>v)&1):
                    if rec(v,seen|(1<<v),depth+1):return True
            return False
        if rec(start,1<<start,1):return True
    return False

def valid(n,edges,S):
    m=len(edges)
    R=[(u,v) for i,(u,v) in enumerate(edges) if not (S>>i)&1]
    if has_even_cycle(n,R): return False
    parent=list(range(n))
    def find(x):
        while parent[x]!=x:x=parent[x]
        return x
    for u,v in R: parent[find(u)]=find(v)
    count={}
    for v in range(n):
        if not (S>>(m+v))&1:
            r=find(v)
            count[r]=count.get(r,0)+1
            if count[r]>1:return False
    return True

def check(n,edges,verbose=False):
    m=len(edges)
    mats=matchings(n,edges)
    patterns=[fm|((((1<<n)-1)^sat)<<m) for fm,sat in mats]
    best=m+n; cnt=0; min_masks=[]
    for S in range(1<<(m+n)):
        injective=len({s&S for s in patterns})==len(patterns)
        cond=valid(n,edges,S)
        if injective!=cond:
            raise AssertionError(('criterion',n,edges,S,injective,cond))
        if injective:
            k=S.bit_count()
            if k<best:best=k;cnt=0;min_masks=[]
            if k==best:cnt+=1;min_masks.append(S)
    b=-1
    for R in range(1<<m):
        H=[edges[i] for i in range(m) if (R>>i)&1]
        if has_even_cycle(n,H):continue
        par=list(range(n))
        def find(x):
            while par[x]!=x:x=par[x]
            return x
        for u,v in H:par[find(u)]=find(v)
        c=len({find(v) for v in range(n)})
        b=max(b,len(H)-n+c)
    if best!=m-b:
        raise AssertionError(('value',n,edges,b,best))
    if verbose:print('PASS',n,'m',m,'matches',len(mats),'min',best,'b',b,'min-set-count',cnt)
    return best,cnt

if __name__=='__main__':
    for n in range(1,5):
        pairs=list(combinations(range(n),2))
        for gm in range(1<<len(pairs)):
            edges=[pairs[i] for i in range(len(pairs)) if (gm>>i)&1]
            check(n,edges)
        print('ALL GRAPHS PASS n=',n,'graphs',1<<len(pairs),flush=True)
    for n in range(2,9):
        e=[(i,i+1) for i in range(n-1)]
        # no brute beyond 8 to keep script short
        if n<=7:
            val,sets=check(n,e,True)
            fib=[0,1]
            for i in range(2,2*n+1):fib.append(fib[-1]+fib[-2])
            assert sets==fib[2*n]
    for n in range(3,8):
        e=[(i,(i+1)%n) for i in range(n)]
        val,cnt=check(n,e,True)
        assert val==(n-1 if n%2 else n)
        if n%2:assert cnt==n
    special=[('complete5',5,list(combinations(range(5),2))),
             ('bowtie',5,[(0,1),(1,2),(2,0),(0,3),(3,4),(4,0)]),
             ('diamond',4,[(0,1),(1,2),(2,0),(0,3),(2,3)]),
             ('K33',6,[(u,v) for u in range(3) for v in range(3,6)]),
             ('twoTrianglesBridge',6,[(0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(2,3)]),
             ('cycle6plusChord',6,[(i,(i+1)%6) for i in range(6)]+[(0,3)]),]
    for name,n,e in special:
        print(name,end=': ',flush=True);check(n,e,True)
    print('VERIFY_OK')
