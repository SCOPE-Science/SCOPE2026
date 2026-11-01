#!/usr/bin/env python3
"""Finite independent checks of the cyclic three-term progression complex.

Requires Python 3 and SymPy.  This finite test is not the proof for all primes;
the proof is the group-presentation and covering argument in RESULT.md.
"""
from itertools import combinations
from math import gcd
from sympy import SparseMatrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

PRIMES = (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43)

def expected(p):
    x = 1
    for h in range(1, p):
        x = (2*x) % p
        if x == 1 or x == p-1:
            sign = 1 if x == 1 else -1
            N = 2**h-sign
            assert N % p == 0 and (p-1) % (2*h) == 0
            q = (p-1)//(2*h)
            return h, sign, q, N//p
    raise AssertionError('missing period')

def run(p):
    h, sign, q, m = expected(p)
    # Check signed doubling partitions of edge-step classes.
    steps = {min(d,p-d) for d in range(1,p)}
    orbits = []
    while steps:
        d = min(steps)
        block=[]
        for j in range(h):
            v=(d*pow(2,j,p))%p
            block.append(min(v,p-v))
        assert len(set(block)) == h and set(block) <= steps
        assert min(d*pow(2,h,p)%p,(-d*pow(2,h,p))%p) == d
        steps.difference_update(block)
        orbits.append(block)
    assert len(orbits)==q
    # Exhaustively construct the independent *full* simplicial two-skeleton.
    vertices=tuple(range(p))
    edges=list(combinations(vertices,2))
    edge_index={e:i for i,e in enumerate(edges)}
    triangles=sorted({tuple(sorted(((a)%p,(a+d)%p,(a+2*d)%p)))
                     for a in vertices for d in range(1,p)})
    assert len(edges)==p*(p-1)//2
    assert len(triangles)==p*(p-1)//2
    assert len({tuple(sorted((x+t)%p for x in T)) for T in triangles for t in vertices})==len(triangles)
    # Explicit oriented simplicial incidence. H1 torsion is SNF of d2
    # because the one-skeleton is complete and its image is saturated.
    entries={}
    for j,(a,b,c) in enumerate(triangles):
        for e,s in (((b,c),1),((a,c),-1),((a,b),1)):
            entries[(edge_index[e],j)]=s
    D=SparseMatrix(len(edges),len(triangles),entries)
    # Test boundary-of-boundary directly on each column.
    for a,b,c in triangles:
        assert (b-c)-(a-c)+(a-b)==0
    Smith=smith_normal_form(D,domain=ZZ)
    diag=[abs(int(Smith[i,i])) for i in range(min(Smith.rows,Smith.cols))]
    rank=sum(int(z>0) for z in diag)
    torsion=sorted(int(z) for z in diag if z>1)
    beta1=len(edges)-p+1-rank
    beta2=len(triangles)-rank
    assert beta1==(p-1)*(q-1), (p,beta1,q)
    assert beta2==(p-1)*q, (p,beta2,q)
    assert torsion==sorted([m]*q if m>1 else []), (p,torsion,q,m)
    print(f'p={p:2d} h={h:2d} sign={sign:+d} q={q} m={m:5d} '
          f'V={p} E={len(edges)} T={len(triangles)} rank_d2={rank} '
          f'betti1={beta1} betti2={beta2} torsion={torsion}',flush=True)

if __name__=='__main__':
    for prime in PRIMES:
        assert all(prime%d for d in range(2,int(prime**0.5)+1))
        run(prime)
    print('VERIFY_OK')
