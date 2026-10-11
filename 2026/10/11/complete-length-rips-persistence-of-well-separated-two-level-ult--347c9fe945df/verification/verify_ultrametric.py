#!/usr/bin/env python3
"""Exact finite verification of a two-level ultrametric length-Rips barcode theorem.
Uses subset dynamic programming for Hamiltonian-path weights and independent
GF(2) boundary-matrix reduction for the complete filtered simplicial complex.
Only finite tests; the general theorem rests on the accompanying proof.
"""
from itertools import combinations
from math import comb
from collections import Counter

def path_weights(u,v,a=1,b=10):
    n=u+v
    d=lambda x,y: 0 if x==y else a if (x<u)==(y<u) else b
    # Held-Karp: dp[(mask,last)] minimum length visiting mask, ending last.
    dp={}
    w={}
    for mask in range(1,1<<n):
        ls=[i for i in range(n) if mask>>i&1]
        if len(ls)==1:
            dp[(mask,ls[0])]=0
            w[mask]=0
            continue
        for j in ls:
            pm=mask^(1<<j)
            dp[(mask,j)]=min(dp[(pm,i)]+d(i,j) for i in ls if i!=j)
        w[mask]=min(dp[(mask,j)] for j in ls)
    return w

def bars(u,v,a=1,b=10):
    n=u+v
    weights=path_weights(u,v,a,b)
    for mask,w in weights.items():
        size=mask.bit_count()
        j=(mask>>u).bit_count()
        i=size-j
        expected=((size-1)*a if i==0 or j==0 else b+(size-2)*a)
        assert w==expected,(u,v,mask,w,expected)
    simplexes=sorted(weights,key=lambda m:(weights[m],m.bit_count(),m))
    index={m:i for i,m in enumerate(simplexes)}
    pivots={}; births=set(); pair={}
    for j,mask in enumerate(simplexes):
        if mask.bit_count()==1:
            col=set()
        else:
            col={index[mask^(1<<i)] for i in range(n) if mask>>i&1}
        while col:
            p=max(col)
            if p not in pivots: break
            col.symmetric_difference_update(pivots[p])
        if col:
            p=max(col)
            pivots[p]=col
            pair[p]=j
        else:
            births.add(j)
    ans=Counter()
    for j in births:
        birth=weights[simplexes[j]]
        death=weights[simplexes[pair[j]]] if j in pair else float('inf')
        if birth<death:
            ans[(simplexes[j].bit_count()-1,birth,death)]+=1
    return ans

def expected_bars(u,v,a=1,b=10):
    n=u+v
    ans=Counter({(0,0,float('inf')):1,(0,0,b):1})
    ans[(0,0,a)]+=n-2
    for h in range(1,max(u,v)-1):
        z=sum(comb(s-1,h+1) for s in (u,v) if s-1>=h+1)
        if z: ans[(h,h*a,(h+1)*a)]+=z
    for t in range(2,n):
        z=comb(n-1,t)-sum(comb(s-1,t) for s in (u,v) if s-1>=t)
        if z: ans[(t-1,b+(t-2)*a,b+(t-1)*a)]+=z
    return +ans

def run():
    tests=0
    for u in range(1,6):
        for v in range(1,6):
            if u+v>9: continue
            for a,b in ((1,9),(2,13)):
                actual=bars(u,v,a,b)
                expected=expected_bars(u,v,a,b)
                if actual!=expected:
                    print('MISMATCH',u,v,a,b,actual,expected)
                    raise SystemExit(1)
                tests+=1
    print('VERIFY_OK: two independent exact computations agreed on',tests,
          'instances, including all subset Hamiltonian-path weights and all persistent homology intervals')
    for u,v in ((3,4),(2,5)):
        print('TEST',u,v,'BARCODES',sorted(bars(u,v).items()))
if __name__=='__main__':run()
