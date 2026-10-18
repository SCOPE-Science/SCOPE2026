#!/usr/bin/env python3
"""Standalone finite checker for maximum Grundy dominating sets of rook graphs.
No external dependencies. Validates the hypothesis for finite parameter pairs only.
"""
import itertools, math
from functools import lru_cache

def stirling(n,k):
    if n == k == 0:return 1
    if n == 0 or k == 0 or k>n:return 0
    return k*stirling(n-1,k)+stirling(n-1,k-1)

def count_formula(m,n):
    assert m>=2 and n>=2
    omit_row=m*(m-1)**(n-1)*(n**(m-2)-math.factorial(n)*stirling(m-2,n))
    omit_col=n*(n-1)**(m-1)*(m**(n-2)-math.factorial(m)*stirling(n-2,m))
    detached=m*n*(m-1)**(n-2)*(n-1)**(m-2)
    if m==n==2:detached//=2
    return omit_row,omit_col,detached

def adjacency(m,n):
    return [sum(1<<j for j in range(m*n) if i//n==j//n or i%n==j%n) for i in range(m*n)]

def subsets_class(m,n):
    neigh=adjacency(m,n); total=(1<<(m*n))-1; K=m+n-2
    @lru_cache(None)
    def possible(chosen_mask,dominated):
        if not chosen_mask:return dominated==total
        for i in range(m*n):
            if chosen_mask>>i&1 and neigh[i]&~dominated:
                if possible(chosen_mask^(1<<i),dominated|neigh[i]):return True
        return False
    counts=[0,0,0]
    for S in itertools.combinations(range(m*n),K):
        bits=sum(1<<i for i in S)
        valid=possible(bits,0)
        rowset={i//n for i in S}; colset={i%n for i in S}
        if len(rowset)==m-1 and len(colset)==n: typ=0
        elif len(rowset)==m and len(colset)==n-1:typ=1
        elif len(rowset)==m and len(colset)==n: typ=2
        else: typ=-1
        if valid:
            assert typ>=0,(m,n,S)
            counts[typ]+=1
        # Validate the spanning-tree structural characterization as well.
        # A selected rook vertex is an edge of K_(m,n).
        idx={('r',r) for r in rowset}|{('c',c) for c in colset}
        adj={v:set() for v in idx}
        for p in S:
            a=('r',p//n); b=('c',p%n)
            adj[a].add(b);adj[b].add(a)
        components=[];todo=set(idx)
        while todo:
            start=todo.pop();stack=[start];comp={start}
            while stack:
                v=stack.pop()
                for w in adj[v]:
                    if w in todo:
                        todo.remove(w);comp.add(w);stack.append(w)
            components.append(comp)
        expect=False
        if typ in [0,1]:
            if len(components)==1:
                full_side='c' if typ==0 else 'r'
                expect=any(len(adj[v])==1 for v in idx if v[0]==full_side)
        elif typ==2:
            expect=len(components)==2 and any(len(c)==2 for c in components)
        assert valid==expect,(m,n,S,valid,expect)
    return tuple(counts)

if __name__=='__main__':
    for m,n in [(2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(4,4)]:
        brute=subsets_class(m,n);f=count_formula(m,n)
        assert brute==f,(m,n,brute,f)
        print(f'{m}x{n}: optimal-set cases {brute}, total {sum(brute)}')
    print('VERIFY_OK')
