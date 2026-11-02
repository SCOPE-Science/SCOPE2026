#!/usr/bin/env python3
"""Independent direct generation of layered permutations and comparison traces."""
import itertools
from functools import lru_cache


def compositions3(n):
    for a in range(1,n-1):
        for b in range(1,n-a):
            yield a,b,n-a-b

def from_lengths(lengths):
    start = 1
    perm = []
    for length in lengths:
        perm.extend(range(start + length - 1, start - 1, -1))
        start += length
    return perm

def direct(n):
    perms = [from_lengths(c) for c in compositions3(n)]
    pairs = [(a,b) for a in range(n) for b in range(a+1,n)]
    qmask=[]
    for a,b in pairs:
        mask=sum(1<<i for i,p in enumerate(perms) if p[a]>p[b])
        if mask not in qmask:
            qmask.append(mask)
    size=len(perms)
    v=0
    for t in range(1,5):
        ok=False
        for qs in itertools.combinations(qmask,t):
            traces={sum(((M>>i)&1)<<j for j,M in enumerate(qs)) for i in range(size)}
            if len(traces)==(1<<t):ok=True;break
        if not ok:break
        v=t
    @lru_cache(None)
    def ld(W):
        return max((1+min(ld(W&M),ld(W^(W&M))) for M in qmask
                    if (W&M) and (W^(W&M))),default=0)
    rank=ld((1<<size)-1) if n<=6 else None
    return size, v, rank

if __name__=='__main__':
    expect_vc={3:0,4:1,5:2,6:2,7:3,8:3,9:4}
    expect_ld={3:0,4:1,5:2,6:3}
    for n,vc in expect_vc.items():
        size,v,l=direct(n)
        assert v==vc and size==(n-1)*(n-2)//2
        if n in expect_ld:assert l==expect_ld[n]
        print('DIRECT_LAYERED_PERMUTATIONS_PASS', 'order='+str(n),
              'count='+str(size), 'VC='+str(v), 'Ldim='+str(l))
    print('ALL_DIRECT_LAYERED_COMPARISON_CHECKS_PASS')
