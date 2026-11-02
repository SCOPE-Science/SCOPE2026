#!/usr/bin/env python3
"""Independent adjacency-based checks of power domination on tensor clique products."""
from math import comb
from itertools import combinations

def predicted_count(m,n,k):
    if k == 0:
        return 0
    total = comb(m*n,k)
    if k == 1:
        return 0
    if 2 <= k <= n-3:
        total -= m*comb(n,k)
    if 2 <= k <= m-3:
        total -= n*comb(m,k)
    return total

def adjacency(m,n):
    return [sum(1<<q for q in range(m*n) if (p//n!=q//n and p%n!=q%n)) for p in range(m*n)]

def observed_after_first(m,n,adj,S):
    v=S
    x=S
    while x:
        bit=x&-x
        v|=adj[bit.bit_length()-1]
        x-=bit
    return v

def observed_after_forcing(N,adj,O):
    full=(1<<N)-1
    count=0
    while True:
        new=0
        for v in range(N):
            if (O>>v)&1:
                poss=adj[v] & (full^O)
                if poss and not (poss & (poss-1)):
                    new|=poss
        new &= (full^O)
        if not new:
            return O,count
        O|=new
        count+=1

def expected(m,n,S):
    if not S: return False
    inds=[i for i in range(m*n) if (S>>i)&1]
    if len(inds)==1:return False
    if any(a//n!=b//n and a%n!=b%n for a,b in combinations(inds,2)):
        return True
    rows={a//n for a in inds}; cols={a%n for a in inds}
    if len(rows)==1: return len(inds)>=n-2
    if len(cols)==1: return len(inds)>=m-2
    raise AssertionError('pairwise same-coordinate property failed')

def exhaustive(m,n):
    N=m*n;adj=adjacency(m,n);full=(1<<N)-1
    counts=[0]*(N+1)
    for S in range(1,1<<N):
        O=observed_after_first(m,n,adj,S)
        final,rounds=observed_after_forcing(N,adj,O)
        got=final==full
        want=expected(m,n,S)
        assert got==want,(m,n,S,got,want)
        assert rounds<=1,(m,n,S,rounds)
        if not got: assert O==final,(m,n,S,'nonstalled failed')
        counts[S.bit_count()]+=int(got)
    for k in range(N+1):
        assert counts[k]==predicted_count(m,n,k),(m,n,k,counts[k],predicted_count(m,n,k))
    print('EXHAUSTIVE_OK',m,n,(1<<N)-1,'success',sum(counts),'minimum',(next(k for k,c in enumerate(counts) if c)))

def sliced(m,n,max_k):
    N=m*n;adj=adjacency(m,n);full=(1<<N)-1
    for k in range(1,max_k+1):
        counts=0
        for inds in combinations(range(N),k):
            S=sum(1<<i for i in inds)
            O=observed_after_first(m,n,adj,S)
            final,rounds=observed_after_forcing(N,adj,O)
            got=(final==full)
            assert got==expected(m,n,S),(m,n,inds,got)
            assert rounds<=1
            if not got: assert O==final
            counts+=int(got)
        assert counts==predicted_count(m,n,k)
        print('SLICE_OK',m,n,k,'power_sets',counts)

if __name__=='__main__':
    for dims in [(3,3),(3,4),(3,5),(4,4),(4,5),(5,3)]:
        exhaustive(*dims)
    for dims in [(5,5,4),(5,6,3),(6,6,3)]:
        sliced(*dims)
    print('VERIFY_OK')
