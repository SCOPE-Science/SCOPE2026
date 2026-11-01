#!/usr/bin/env python3
"""Independent finite checks of open-neighborhood NOR join laws.
Purely finite verification; general theorem rests on the mathematical proof.
"""
from itertools import product
from random import Random

def all_graphs(n):
    edges=[(i,j) for i in range(n) for j in range(i+1,n)]
    for mask in range(1<<len(edges)):
        adj=[0]*n
        for k,(i,j) in enumerate(edges):
            if mask & (1<<k):
                adj[i] |= 1<<j;adj[j] |= 1<<i
        yield tuple(adj)

def join(g,h):
    n,m=len(g),len(h);a=(1<<n)-1;b=(1<<m)-1
    return tuple((row | (b<<n)) for row in g)+tuple((row<<n)|a for row in h)

def F(x,adj):
    y=0
    for i,mask in enumerate(adj):
        if x & mask==0:
            y|=1<<i
    return y

def census(adj):
    N=len(adj);states=1<<N;one=states-1
    fix=per=basin=0
    for x in range(states):
        y=F(x,adj);z=F(y,adj)
        assert F(z,adj)==y,('F3 != F',adj,x)
        fix += (y==x)
        per += (z==x)
        basin += (y==0 or y==one)
    assert (per-fix)%2==0
    totaldom=sum(all((x&u)!=0 for u in adj) for x in range(states))
    if all(mask != 0 for mask in adj):
        assert basin==totaldom+1
    return fix, (per-fix)//2, basin, totaldom

def check(g,h):
    n,m=len(g),len(h)
    fg,ng,bg,tg=census(g)
    fh,nh,bh,th=census(h)
    joint=join(g,h)
    fj,nj,bj,tj=census(joint)
    dg=int(all(a!=0 for a in g))
    dh=int(all(a!=0 for a in h))
    assert fj==fg+fh,('fix',g,h,(fj,fg+fh))
    assert nj==ng+nh+1-dg-dh,('cycles',g,h,(nj,ng+nh+1-dg-dh))
    assert bj==1+(2**n-1)*(2**m-1)+tg+th,('basin',g,h)
    return n+m

def main():
    cats={k:list(all_graphs(k)) for k in range(1,5)}
    count=0
    vertices=0
    for n in range(1,5):
        for m in range(1,5):
            for g,h in product(cats[n],cats[m]):
                vertices+=check(g,h)
                count+=1
    print('exhaustive labelled graph-pairs sizes 1..4:', count)
    print('total vertices across those pair checks:',vertices)
    r=Random(38475)
    larger=0
    for _ in range(120):
        n=r.randint(4,7);m=r.randint(3,7)
        def randgraph(k):
            adj=[0]*k
            for i in range(k):
                for j in range(i+1,k):
                    if r.getrandbits(1):
                        adj[i]|=1<<j;adj[j]|=1<<i
            return tuple(adj)
        check(randgraph(n),randgraph(m));larger+=1
    print('additional deterministic-seed random graph-pairs sizes 4..7 and 3..7:',larger)
    print('All exact orbit, transient, and basin checks passed.')
if __name__=='__main__':
    main()
