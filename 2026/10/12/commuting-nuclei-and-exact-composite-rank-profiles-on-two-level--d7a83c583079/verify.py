#!/usr/bin/env python3
"""Exact independent small-poset verification of the finite-height-two nucleus census."""
from itertools import combinations
from collections import Counter
from math import comb

def upsets(m,n):
    N=m+n
    return [u for u in range(1<<N) if not (u&((1<<m)-1)) or ((u>>m)==(1<<n)-1)]

def subset_nucleus(m,n,S,opens):
    N=m+n
    B=((1<<n)-1)<<m
    upcones=[(1<<i)|B if i<m else (1<<i) for i in range(N)]
    return tuple(sum(1<<x for x,c in enumerate(upcones) if ((c&S)&~u)==0) for u in opens)

def formula(m,n):
    # Poly (x,y), expanded by direct choosing subsets rather than algebra symbolic.
    out=Counter()
    for a in range(m+1):
      for b in range(n+1):
        def coef_pow(z,w,d,k):
          return comb(d,k)*z**(d-k)*w**k
        # A equality + arbitrary B
        z=coef_pow(1,1,m,a)*coef_pow(3,1,n,b)
        # A strict subset, B inclusion
        z+=2*(coef_pow(2,1,m,a)-coef_pow(1,1,m,a))*coef_pow(2,1,n,b)
        # A incomparable, B equality
        z+=(coef_pow(3,1,m,a)-2*coef_pow(2,1,m,a)+coef_pow(1,1,m,a))*coef_pow(1,1,n,b)
        out[(a,b)]=z
    return out

def check(m,n):
    N=m+n;opens=upsets(m,n)
    nuclei=[subset_nucleus(m,n,S,opens) for S in range(1<<N)]
    assert len(set(nuclei))==1<<N
    index={u:i for i,u in enumerate(opens)}
    data=Counter(); count=0
    for S,f in enumerate(nuclei):
      for T,g in enumerate(nuclei):
        fg=tuple(f[index[v]] for v in g)
        gf=tuple(g[index[v]] for v in f)
        works=(fg==gf)
        a=S&((1<<m)-1); c=T&((1<<m)-1)
        b=S>>m;d=T>>m
        cond=((not (a&~c)) or (d&~b)==0) and ((not(c&~a)) or (b&~d)==0)
        assert works==cond,(m,n,S,T)
        if not works: continue
        H=S&T; want=nuclei[H]
        assert fg==want, (m,n,S,T,'composite')
        aa=(H&((1<<m)-1)).bit_count();bb=(H>>m).bit_count()
        # nucleus image = number of upsets of the support induced order
        rank=len(set(fg))
        assert rank == 2**aa+2**bb-1,(m,n,S,T,rank,aa,bb)
        data[(aa,bb)]+=1;count+=1
    expected=formula(m,n)
    assert data==+expected,(m,n,data,expected)
    print('HEIGHT_TWO_OK',m,n,'upsets',len(opens),'nuclei',len(nuclei),'ordered_pairs',4**N,'commuting',count,'ranks',len(data))
    return len(opens),nuclei,index

def enumerate_all_nuclei(m,n,opens=None):
    # Independent direct nucleus test, no subset representation assumed.
    from itertools import product
    if opens is None:opens=upsets(m,n)
    top=(1<<(m+n))-1
    possible=[[v for v in opens if (v&u)==u] for u in opens]
    oidx={x:i for i,x in enumerate(opens)}
    hits=set(); candidates=0
    for choices in product(*possible):
        candidates+=1
        # closure/idempotence and finite meet preservation; preserves top automatic
        if any(choices[oidx[choices[i]]]!=choices[i] for i in range(len(opens))):continue
        if any(choices[oidx[u&v]]!=(choices[i]&choices[j]) for i,u in enumerate(opens) for j,v in enumerate(opens)):continue
        hits.add(choices)
    known={subset_nucleus(m,n,S,opens) for S in range(1<<(m+n))}
    assert hits==known,(m,n,len(hits),len(known))
    print('DIRECT_NUCLEI_OK',m,n,'candidate_closures',candidates,'all_nuclei',len(hits))

if __name__=='__main__':
    for m,n in ((1,1),(1,2),(2,1),(2,2),(1,3),(3,1),(2,3),(3,2),(3,3)):
        check(m,n)
    for m,n in ((1,1),(1,2),(2,1),(2,2)):
        enumerate_all_nuclei(m,n)
    print('VERIFY_OK')
