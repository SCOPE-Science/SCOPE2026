#!/usr/bin/env python3
"""Independent enumeration of cyclic column configurations in C7 strong Cn.
Pure finite arithmetic; no external dependencies.
"""
from collections import defaultdict
from math import comb

def matrices(n):
    # First axis is C7, second is cyclic Cn.
    states = [mask for mask in range(128)
              if all(not ((mask >> j & 1) and (mask >> ((j+1) % 7) & 1))
                     for j in range(7))]
    assert len(states) == 29
    adj = [[(a & b) == 0 and all(not (a>>i & 1 and b>>j & 1)
                    for i in range(7) for j in ((i-1)%7,(i+1)%7))
                for b in states] for a in states]
    return states, adj

def independent_sets_cyclic(n):
    st, adj = matrices(n)
    max_size, count = 0, 0
    # Exact enumeration by transfer over sizes; includes every independent set once.
    for start in range(len(st)):
        dp={(start,st[start].bit_count()):1}
        for _ in range(n-1):
            ndp=defaultdict(int)
            for (i,w),c in dp.items():
                for j,b in enumerate(st):
                    if adj[i][j]:ndp[j,w+b.bit_count()]+=c
            dp=ndp
        for (j,w),c in dp.items():
            if adj[j][start]:
                if w>max_size:max_size,count=w,c
                elif w==max_size:count+=c
    return max_size,count

def analytic_count(n):
    assert n %2==0 and n>=6
    k=n//2
    L=[[0]*7 for _ in range(7)]
    for i in range(7):
        L[i][i]=3
        L[i][(i+1)%7]=1
        L[i][(i-1)%7]=1
    mat=[[int(i==j) for j in range(7)] for i in range(7)]
    for _ in range(k):
        mat=[[sum(mat[i][l]*L[l][j] for l in range(7)) for j in range(7)] for i in range(7)]
    return 2*(7**k+sum(mat[i][i] for i in range(7)))

if __name__=='__main__':
 for n in range(6,15):
    opt,c=independent_sets_cyclic(n)
    t=analytic_count(n) if n%2==0 else None
    if n%2==0:assert opt==3*n//2 and c==t,(n,opt,c,t)
    print('n',n,'maximum',opt,'count',c,('formula='+str(t) if t is not None else 'odd control'),flush=True)
