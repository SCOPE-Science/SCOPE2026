#!/usr/bin/env python3
"""Independent brute-force checks of strict-neighbor binary majority on clique windmills.

A windmill consists of one hub and n disjoint peripheral cliques of even order m.
No advanced graph or numerical packages are required.
"""
from math import comb
from collections import Counter


def step(mask, n, m):
    z = n*m+1
    old = [(mask >> v) & 1 for v in range(z)]
    new = [0]*z
    # hub index zero; all peripheral vertices are consecutive by petal
    nbrs_hub = list(range(1,z))
    s = sum(old[j] for j in nbrs_hub)
    new[0] = (1 if 2*s > len(nbrs_hub) else 0 if 2*s < len(nbrs_hub) else old[0])
    for petal in range(n):
        vstart = 1 + petal*m
        for j in range(vstart,vstart+m):
            nbrs = [0] + [k for k in range(vstart,vstart+m) if k != j]
            cnt = sum(old[k] for k in nbrs)
            new[j] = 1 if 2*cnt > m else 0 if 2*cnt < m else old[j]
    return sum(bit<<j for j,bit in enumerate(new))


def verify(n,m):
    assert n%2==1 and n>=3 and m%2==0 and m>=4
    r=m//2
    u=2**(m-1)-comb(m,r)//2
    v=2**(m-1)+comb(m,r)//2
    counts=Counter()
    time2=False
    fixed=set()
    for state in range(1 << (n*m+1)):
        first=step(state,n,m)
        second=step(first,n,m)
        third=step(second,n,m)
        assert second==third,(n,m,state,first,second,third)
        if first != second:time2=True
        p=0
        for i in range(n):
            block=[(second>>(1+i*m+j))&1 for j in range(m)]
            assert len(set(block))==1,(state,second)
            p+=block[0]<<i
        assert (second & 1)==(2*p.bit_count()>n)
        counts[p]+=1
        fixed.add(second)
    assert len(fixed)==2**n
    for P in range(1<<n):
        p=P.bit_count()
        want=u**p*v**(n-p)+v**p*u**(n-p)
        assert counts[P]==want,(n,m,P,counts[P],want)
    assert sum(counts.values()) == 1<<(n*m+1)
    assert time2
    print(f'PASS n={n}, m={m}: states={1<<(n*m+1)}, fixed={len(fixed)}, basin_min={min(counts.values())}, basin_max={max(counts.values())}, sharp_two={time2}')

if __name__=='__main__':
    verify(3,4)
    verify(3,6)
