#!/usr/bin/env python3
from itertools import combinations
from math import comb


def crown_edges(n):
    return [(i,j) for i in range(n) for j in range(n) if i != j]

def masks_after(n, deleted):
    d=set(deleted)
    rows=[]
    cols=[]
    for i in range(n):
        m=0
        for j in range(n):
            if i!=j and (i,j) not in d:
                m |= 1<<j
        rows.append(m)
    for j in range(n):
        m=0
        for i in range(n):
            if i!=j and (i,j) not in d:
                m |= 1<<i
        cols.append(m)
    return rows,cols

def no_isolates(n, deleted):
    rows,cols=masks_after(n,deleted)
    return all(rows) and all(cols)

def cover_number(masks,n):
    full=(1<<n)-1
    for k in range(1,n+1):
        for I in combinations(range(n),k):
            u=0
            for i in I: u |= masks[i]
            if u==full:
                return k
    return 10**9

def gamma_t(n,deleted):
    rows,cols=masks_after(n,deleted)
    if not all(rows) or not all(cols): return None
    return cover_number(rows,n)+cover_number(cols,n)

def witness(n):
    if n==3:
        return {(0,1),(1,2),(2,0)}
    W=[{i} for i in range(n)]
    W[0]=set(range(n))-{n-1}
    W[1]=set(range(n))-{n-2}
    W[n-2]={n-2,n-1}
    return {(i,j) for i in range(n) for j in W[i] if i!=j}

def lemma_min_cost(n):
    pairs=list(combinations(range(n),2))
    idx={p:k for k,p in enumerate(pairs)}
    full=(1<<len(pairs))-1
    blocks=[]
    for mask in range(1,1<<n):
        s=mask.bit_count()
        if 2<=s<=n-1:
            pm=0
            verts=[i for i in range(n) if mask>>i&1]
            for a,b in combinations(verts,2): pm |= 1<<idx[(a,b)]
            blocks.append((pm,s-1))
    INF=10**9
    dp=[INF]*(full+1); dp[0]=0
    for pm,w in blocks:
        ndp=dp[:]
        for st,c in enumerate(dp):
            if c==INF: continue
            ns=st|pm
            if c+w<ndp[ns]: ndp[ns]=c+w
        dp=ndp
    return dp[full]

def exhaustive_lower(n):
    E=crown_edges(n)
    target=2*n-3
    checked=0
    for k in range(target):
        for F in combinations(E,k):
            checked+=1
            if not no_isolates(n,F):
                continue
            g=gamma_t(n,F)
            if g>4:
                raise AssertionError((n,k,F,g))
    return checked

def main():
    ex=0
    for n in range(3,6):
        ex += exhaustive_lower(n)
        F=witness(n)
        assert len(F)==2*n-3
        assert no_isolates(n,F)
        assert gamma_t(n,F)>4
    lem=[]
    for n in range(3,7):
        v=lemma_min_cost(n)
        assert v==2*n-3,(n,v)
        lem.append(v)
    for n in range(3,31):
        F=witness(n)
        assert len(F)==2*n-3
        assert no_isolates(n,F)
        g=gamma_t(n,F)
        assert g is not None and g>4,(n,g)
    print(f"ALL CHECKS PASSED; exhaustive_orders=[3,4,5]; deletion_subsets_below_target={ex}; lemma_orders=[3,4,5,6]; lemma_minima={lem}; witness_range=3..30")
if __name__=='__main__': main()
