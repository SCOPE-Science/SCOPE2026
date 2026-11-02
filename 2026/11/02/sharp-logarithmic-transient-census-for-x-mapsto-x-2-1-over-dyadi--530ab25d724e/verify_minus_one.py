#!/usr/bin/env python3
"""Exact finite checks for the functional graph of f(x)=x*x-1 modulo powers of 2.

The algebraic formulas are proved separately; finite verification is corroboration.
"""
from collections import Counter


def even_count(n, k):
    if k <= 1:
        return 1 << (n-1)
    return 1 << (n-min(n,k))


def odd_count(n, k):
    if k <= 3:
        return 1 << (n-1)
    assert k <= n
    return 1 << (n-k+2)


def ceildiv(a,b):
    return (a+b-1)//b


def cumulative(n, t):
    if t==0:
        return 2
    if t%2:
        r=(t-1)//2
        return even_count(n,ceildiv(n+2,1<<(r+1))-1)+odd_count(n,ceildiv(n+1,1<<r)-1)
    r=t//2
    return even_count(n,ceildiv(n+1,1<<r)-1)+odd_count(n,ceildiv(n+2,1<<r)-1)


def max_tail_formula(n):
    h=(n+1).bit_length()-1
    return 2*h-2 if (n+1)&n==0 else 2*h-1


def graph(n):
    m=1<<n
    nxt=[(x*x-1)%m for x in range(m)]
    depths=[-1]*m
    cycles=[]
    for x in range(m):
        if depths[x]!=-1: continue
        path=[]; idx={}; y=x
        while depths[y]<0 and y not in idx:
            idx[y]=len(path);path.append(y);y=nxt[y]
        if depths[y]<0:
            start=idx[y]
            cycles.append(path[start:]);
            for z in path[start:]: depths[z]=0
            path=path[:start]
        for z in path[::-1]: depths[z]=depths[nxt[z]]+1
    assert len(cycles)==1 and set(cycles[0])=={0,m-1},(n,cycles)
    return depths


def check():
    total=0
    for n in range(2,17):
        distances=graph(n); mx=max(distances)
        assert mx==max_tail_formula(n),(n,mx,max_tail_formula(n))
        cnt=Counter(distances); prefix=0
        for t in range(mx+1):
            prefix+=cnt[t]
            assert prefix==cumulative(n,t),(n,t,prefix,cumulative(n,t))
        assert prefix==1<<n
        print('n=%02d max_tail=%2d depth_counts=%s' %(n,mx,','.join(str(cnt[k]) for k in range(mx+1))))
        total+=1<<n
    print('VERIFY_OK n_levels=15 total_graph_vertices=%d sharp_tail_formulas=15' % total)

if __name__=='__main__':
    check()
