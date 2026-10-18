#!/usr/bin/env python3
"""Independent integer-partition checks of the binomial-moment inversion proof."""
from collections import Counter,defaultdict
from math import comb, factorial
import sys

def intpart(n, cap=None):
    if not n:
        yield ()
        return
    if cap is None:cap=n
    for v in range(min(n,cap),0,-1):
        for tail in intpart(n-v,v):yield (v,)+tail

def recover(n, h):
    m={}
    for r in range(n,1,-1):
        v=h[r]-sum(comb(k,r)*m[k] for k in range(r+1,n+1))
        assert v>=0
        m[r]=v
    m[1]=n-sum(k*m[k] for k in range(2,n+1))
    assert m[1]>=0
    return tuple(sorted((k for k,v in m.items() for _ in range(v)),reverse=True))

def test(n):
    parts=list(intpart(n))
    seen={}
    for p in parts:
        h=tuple(sum(comb(s,r) for s in p if s>=r) for r in range(n+1))
        got=recover(n,h)
        assert got==p
        assert h not in seen or seen[h]==p
        seen[h]=p
    for r in range(3,n+1):
        group=[p for p in parts if len(p)==n-r+1]
        assert group
        maxval=max(sum(comb(s,2) for s in p) for p in group)
        maxima=[p for p in group if sum(comb(s,2) for s in p)==maxval]
        assert maxval==comb(r,2)
        assert maxima==[(r,)+(1,)*(n-r)]
    print(f'n={n} integer_partitions={len(parts)} moment_reconstruction=OK extrema=OK')

if __name__=='__main__':
    end=int(sys.argv[1]) if len(sys.argv)>1 else 30
    assert 1<=end<=60
    for n in range(1,end+1):test(n)
    print(f'MOMENT_CHECK_OK max_n={end}')
