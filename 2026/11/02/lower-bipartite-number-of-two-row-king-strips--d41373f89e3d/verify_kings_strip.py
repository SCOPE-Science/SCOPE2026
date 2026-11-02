#!/usr/bin/env python3
"""Independent brute-force check of lower bipartite number on two-row king strips."""
from collections import Counter
from itertools import product

def is_bipartite(S,adj):
    marked={}
    for v in S:
        if v in marked:continue
        marked[v]=0
        stack=[v]
        while stack:
            u=stack.pop()
            for w in adj[u]:
                if w not in S:continue
                if w in marked:
                    if marked[w]==marked[u]:return False
                else:marked[w]=1-marked[u];stack.append(w)
    return True

def direct(n):
    N=2*n
    adj=[set() for _ in range(N)]
    for u in range(N):
        i,r=divmod(u,2)
        for v in range(N):
            j,s=divmod(v,2)
            if u!=v and abs(i-j)<=1:adj[u].add(v)
    out=Counter()
    for bit in range(1<<N):
        S={i for i in range(N) if bit>>i&1}
        if not is_bipartite(S,adj):continue
        if all(not is_bipartite(S|{i},adj) for i in range(N) if i not in S):
            out[len(S)]+=1
    return out

def by_occupancy(n):
    out=Counter()
    for t in product((0,1,2),repeat=n):
        if any(t[i]+t[i+1]>2 for i in range(n-1)):continue
        if any(x==0 and not ((i>0 and t[i-1]==2) or (i+1<n and t[i+1]==2)) for i,x in enumerate(t)):continue
        if any(x==1 and not ((i>0 and t[i-1]==1) or (i+1<n and t[i+1]==1)) for i,x in enumerate(t)):continue
        out[sum(t)]+=2**t.count(1)
    return out

def main():
    total=0
    for n in range(1,9):
        a=direct(n);b=by_occupancy(n)
        assert a==b,(n,a,b)
        assert min(a)==2*((n+2)//3),(n,a)
        total+=1<<(2*n)
    for n in range(9,13):
        a=by_occupancy(n)
        assert min(a)==2*((n+2)//3),(n,a)
    print('VERIFY_OK graph_orders=8 graph_subsets=%s occupancy_orders=12'%total)

if __name__=='__main__':main()
