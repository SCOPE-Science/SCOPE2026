#!/usr/bin/env python3
from itertools import product, combinations
from math import comb


def canon(v,q):
    for x in v:
        if x%q:
            inv=pow(x,-1,q)
            return tuple((inv*y)%q for y in v)
    raise ValueError

def pg3(q):
    pts=sorted({canon(v,q) for v in product(range(q), repeat=4) if any(v)})
    hypers=pts[:]  # nonzero linear forms modulo scalar
    blocks=[]
    for a in hypers:
        B={i for i,x in enumerate(pts) if sum(ai*xi for ai,xi in zip(a,x))%q==0}
        blocks.append(B)
    return pts,blocks

def verify_pg3(q):
    pts,blocks=pg3(q)
    v=len(pts); k=len(blocks[0]); lam=(q+1)
    assert v==q**3+q**2+q+1
    assert k==q**2+q+1
    assert len(blocks)==v
    assert all(len(B)==k for B in blocks)
    for i,j in combinations(range(v),2):
        assert sum(i in B and j in B for B in blocks)==lam
    for a,b in combinations(range(v),2):
        assert len(blocks[a]&blocks[b])==lam
    # Every triple lies in at least one hyperplane.
    for T in combinations(range(v),3):
        assert any(set(T)<=B for B in blocks)
    rhs=lam*(k-2)-(lam-1)*(lam-2)
    assert rhs==v-2
    # Every pair has its remaining points covered by blocks through the pair.
    for x,y in combinations(range(v),2):
        through=[B for B in blocks if x in B and y in B]
        U=set().union(*(B-{x,y} for B in through))
        assert len(through)==lam and len(U)==v-2==rhs
    return v,k,lam

def verify_scalar_inequality():
    for lam in range(1,51):
        for m in range(1,lam+1):
            assert 2*comb(m,2) <= lam*(m-1)

if __name__=='__main__':
    verify_scalar_inequality()
    # q=2 and q=3 provide independent finite incidence checks; q=3 is also
    # in the storage paper's p=3 feasibility range k >= 2*lambda+2.
    for q in (2,3):
        print('PG(3,%d): v,k,lambda ='%q, verify_pg3(q))
    print('VERIFY_OK')
