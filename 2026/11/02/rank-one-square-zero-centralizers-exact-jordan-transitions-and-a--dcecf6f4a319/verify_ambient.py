#!/usr/bin/env python3
"""Ambient verification independent of rank-one tensor parameterization."""
from collections import Counter
from itertools import product
from verify import F,jordan,rank,mm,formula

def test(q,parts):
    f=F(q)
    f.add_many=lambda v:__import__('functools').reduce(f.add,v,0)
    N,_,_=jordan(parts);n=len(N); nr=rank(N,f)
    seen=Counter()
    for coords in product(range(q),repeat=n*n):
        T=[list(coords[i*n:(i+1)*n]) for i in range(n)]
        if rank(T,f)!=1:continue
        if any(mm(T,T,f)[i][j] for i in range(n) for j in range(n)):continue
        if mm(N,T,f)!=mm(T,N,f):continue
        S=[[f.add(N[i][j],T[i][j]) for j in range(n)] for i in range(n)]
        seen[rank(S,f)-nr]+=1
    expected=formula(q,parts)
    assert all(seen[d]==expected[d] for d in (-1,0,1)), (q,parts,seen,expected)
    return tuple(seen[d] for d in (-1,0,1))

if __name__=='__main__':
    cases=[(2,[2,1]),(2,[2,2]),(2,[2,1,1]),(2,[3,1]),(2,[1,1,1,1]),(3,[2,1]),(3,[3]),(3,[1,1,1])]
    for q,p in cases:print('ambient q=%d partition=%s deltas=%s'%(q,','.join(map(str,p)),test(q,p)))
    print('AMBIENT_RANK_ONE_SQUAREZERO_CENTRALIZERS_OK %d_COMPLETE_MATRIX_SPACES'%len(cases))
