#!/usr/bin/env python3
"""Direct independent finite checks for maximal cluster induced sets on rook graphs."""
from functools import lru_cache
from collections import Counter
from math import comb, factorial

@lru_cache(None)
def full(a,b):
    """Return polynomial coefficients of spanning bipartite star forests using rooted-component recurrence."""
    if a==0 or b==0:
        return {0:1} if a==b==0 else {}
    ret=Counter()
    for r in range(1,b+1):
        for k,v in full(a-1,b-r).items(): ret[k+r]+=comb(b,r)*v
    for t in range(1,a):
        for k,v in full(a-1-t,b-1).items(): ret[k+t+1]+=b*comb(a-1,t)*v
    return dict(ret)

@lru_cache(None)
def blocks_ge2(n,k):
    if n==k==0:return 1
    if n<2*k or k==0:return 0
    return k*blocks_ge2(n-1,k)+(n-1)*blocks_ge2(n-2,k-1)

def falling(n,k):
    return factorial(n)//factorial(n-k)

def formula(a,b):
    out=Counter(full(a,b))
    for k in range(1,min(b-1,a//2)+1):out[a]+=falling(b,k)*blocks_ge2(a,k)
    for k in range(1,min(a-1,b//2)+1):out[b]+=falling(a,k)*blocks_ge2(b,k)
    return dict(out)

def direct(a,b):
    n=a*b
    adj=[0]*n
    for i in range(a):
        for j in range(b):
            u=i*b+j
            for p in range(a):
                for q in range(b):
                    if (p==i or q==j) and (p,q)!=(i,j):adj[u]|=1<<(p*b+q)
    def cluster(mask):
        # For every selected vertex v, its selected neighbors must be pairwise adjacent.
        for v in range(n):
            if not (mask>>v)&1:continue
            nb=adj[v]&mask
            while nb:
                bit=nb&-nb;nb-=bit
                w=bit.bit_length()-1
                if nb & ~adj[w]:return False
        return True
    out=Counter()
    for mask in range(1<<n):
        if not cluster(mask):continue
        if any(cluster(mask|(1<<v)) for v in range(n) if not (mask>>v)&1):continue
        out[mask.bit_count()]+=1
    return dict(out)

def run():
    checked=0; masks=0
    for a,b in [(1,1),(1,2),(1,5),(2,2),(2,3),(2,4),(2,5),(2,7),(3,3),(3,4),(3,5),(4,4)]:
        expected=formula(a,b); got=direct(a,b)
        assert got==expected,(a,b,got,expected)
        print(f'OK {a}x{b}: {got}')
        checked+=1;masks+=1<<(a*b)
    for a in range(1,14):
        for b in range(1,18):
            p=formula(a,b)
            assert all(v>0 for v in p.values())
            if a<=b and a>=2:
                assert set(p)==({a}|set(range(b,a+b-1))), (a,b,p)
            if a==1:
                assert p=={b:1}
    print(f'VERIFY_OK direct_graphs={checked} direct_subsets={masks} support_pairs={13*17}')
if __name__=='__main__':run()
