#!/usr/bin/env python3
"""Exhaustive checks for maximal closed-neighborhood packings of coronas."""
from itertools import combinations
from collections import Counter
import random

def distances(g):
    n=len(g)
    d=[[n+1]*n for _ in range(n)]
    for i in range(n):
        d[i][i]=0
        todo=[i]
        for v in todo:
            for w in range(n):
                if (g[v]>>w)&1 and d[i][w]>d[i][v]+1:
                    d[i][w]=d[i][v]+1
                    todo.append(w)
    return d

def corona(g):
    n=len(g)
    h=list(g)+[0]*n
    for u in range(n):
        h[u]|=1<<(n+u)
        h[n+u]|=1<<u
    return h

def is_packing(mask,d):
    v=[i for i in range(len(d)) if mask>>i&1]
    return all(d[i][j]>2 for i,j in combinations(v,2))

def exact_polynomial(g):
    h=corona(g)
    d=distances(h)
    n=len(g)
    ans=Counter()
    masks=set()
    for mask in range(1<<(2*n)):
        if not is_packing(mask,d):continue
        extendable=False
        for i in range(2*n):
            if (mask>>i)&1:continue
            if is_packing(mask|(1<<i),d):
                extendable=True
                break
        if not extendable:
            ans[mask.bit_count()]+=1
            masks.add(mask)
    return ans,masks

def prediction(g):
    n=len(g); d=distances(g)
    ans=Counter(); masks=set()
    for s in range(1<<n):
        if not is_packing(s,d):continue
        occupied=0
        for i in range(n):
            if (s>>i)&1:occupied|=(1<<i)|g[i]
        out=s
        for i in range(n):
            if not occupied>>i&1:out|=1<<(n+i)
        ans[out.bit_count()]+=1
        masks.add(out)
    return ans,masks

def graph_from_bits(n,bits):
    g=[0]*n;k=0
    for i,j in combinations(range(n),2):
        if bits>>k&1:
            g[i]|=1<<j;g[j]|=1<<i
        k+=1
    return g

def check(n,bits):
    g=graph_from_bits(n,bits)
    x,xa=exact_polynomial(g)
    y,ya=prediction(g)
    assert x==y and xa==ya,(n,bits,x,y,xa^ya)
    max_n=max(x)
    assert max_n==n
    assert min(x)==n-max(sum(g[i].bit_count() for i in range(n) if s>>i&1) for s in range(1<<n) if is_packing(s,distances(g)))
    return len(xa)

def main():
    instances=0; packings=0
    for n in range(1,6):
        for bits in range(1<<(n*(n-1)//2)):
            packings+=check(n,bits)
            instances+=1
    rng=random.Random(164829)
    for n,t in [(6,120),(7,30)]:
        for _ in range(t):
            packings+=check(n,rng.getrandbits(n*(n-1)//2));instances+=1
    print('VALIDATED_GRAPHS',instances)
    print('MATCHED_MAXIMAL_PACKINGS',packings)
    for n in range(2,7):
        g=[((1<<n)-1)^(1<<i) for i in range(n)]
        x,_=prediction(g)
        assert x==Counter({1:n,n:1}),x
        print('COMPLETE_BASE',n,sorted(x.items()))
    print('VERIFY_OK')
if __name__=='__main__':main()
