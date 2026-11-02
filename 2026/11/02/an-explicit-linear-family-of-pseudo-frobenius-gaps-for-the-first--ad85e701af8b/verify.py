#!/usr/bin/env python3
"""Independent finite checks for explicit pseudo-Frobenius candidates.
The proof for all n is mathematical; this script tests finite instances only.
"""
from heapq import heappop, heappush

def distances(n):
    B=1<<n; A=7*B; m=A+1
    gens=[A*(1<<j)+1 for j in range(1,n+3)]
    d=[None]*m;d[0]=0;h=[(0,0)]
    while h:
        v,r=heappop(h)
        if d[r]!=v:continue
        for g in gens:
            z=(r+g)%m;nv=v+g
            if d[z] is None or nv<d[z]:d[z]=nv;heappush(h,(nv,z))
    assert all(v is not None for v in d)
    return d,gens

def candidate_ts(n):
    B=1<<n;A=7*B
    return sorted(set([4*B-n-2,6*B-n-2,A,A-1]+[A-d for d in range(5,n+3)]))

def run():
    count=0
    for n in range(3,10):
        B=1<<n; A=7*B;m=A+1
        d,gs=distances(n);cs=[(1<<j)-1 for j in range(1,n+3)]
        L=[None]*(A+1);L[0]=0
        for t in range(1,A+1):L[t]=min(L[t-c]+1 for c in cs if c<=t)
        assert all(d[(-t)%m]==A*t+m*L[t] for t in range(A+1))
        ts=candidate_ts(n);assert len(ts)==n+2
        assert L[4*B-n-2]==L[6*B-n-2]==n+2
        assert max(L[4*B-n-2:])==n+2
        assert L[A]==4 and L[A-1]==5
        for z in range(5,n+3):assert L[A-z]==z
        for t in ts:
            f=d[(-t)%m]-m
            assert all(f+g>=d[(f+g)%m] for g in gs)
            assert f>=0
            count+=1
        actual=[r for r in range(m) if all(d[r]+g-d[(r+g)%m]>=m for g in gs)]
        assert len(actual)>=n+2
        print(f'n={n} modulus={m} proposed={len(ts)} actual_type={len(actual)}')
    print(f'VERIFY_OK n_levels=7 candidate_instances={count}')
if __name__=='__main__':run()
