#!/usr/bin/env python3
"""Independent exhaustive tournament out-neighborhood homology census (no third-party dependencies)."""
from collections import Counter, defaultdict
from itertools import permutations, product
from functools import lru_cache


def signature(rows):
    n = len(rows)
    out=[]
    for i, r in enumerate(rows):
        c=sum(bool(r & (1<<j)) and bool(rows[j] & (1<<k)) and bool(rows[k] & (1<<i)) for j in range(n) for k in range(n))
        out.append((r.bit_count(),c))
    return out


def canon(rows):
    n=len(rows)
    sig=signature(rows)
    blocks=defaultdict(list)
    for v, s in enumerate(sig): blocks[s].append(v)
    blocks=[blocks[s] for s in sorted(blocks)]
    best=None
    for pp in product(*(permutations(b) for b in blocks)):
        v=[u for b in pp for u in b]
        word=0; bit=1
        for i in range(n):
            for j in range(i+1,n):
                if (rows[v[i]]>>v[j])&1: word|=bit
                bit<<=1
        if best is None or word<best: best=word
    return best


def extend(a, pattern):
    n=len(a)
    return tuple(a[i]|(((pattern>>i)&1)<<n) for i in range(n))+(sum((1-((pattern>>i)&1))<<i for i in range(n)),)


def all_classes():
    reps=[(0,)]
    counts=[1]
    for n in range(1,8):
        seen=set(); nxt=[]
        for a in reps:
            for bits in range(1<<n):
                b=extend(a,bits)
                k=canon(b)
                if k not in seen:
                    seen.add(k); nxt.append(b)
        reps=nxt
        counts.append(len(reps))
        print('n',n+1,'count',len(reps),flush=True)
    assert counts==[1,1,2,4,12,56,456,6880], counts
    return reps


def make_complex(rows):
    n=len(rows);fs=[[] for _ in range(n+1)]
    for subset in range(1,1<<n):
        if any((subset&r)==subset for r in rows): fs[subset.bit_count()].append(subset)
    return fs


def unit_reduce(mat):
    # Fraction-free integer row/column operations, with signed unimodular pivots.
    m=len(mat); n=len(mat[0]) if m else 0; rk=0
    while m>0 and n>0:
        pair=next(((i,j) for i in range(m) for j in range(n) if abs(mat[i][j])==1),None)
        if pair is None:break
        i,j=pair; pivot=mat[i][j]
        # Unimodular Schur complement after isolating a unit pivot
        for x in range(m):
            if x!=i:
                fac=mat[x][j]*pivot
                for y in range(n):
                    if y!=j:mat[x][y]-=fac*mat[i][y]
        mat[i],mat[m-1]=mat[m-1],mat[i]
        for row in mat[:m]: row[j],row[n-1]=row[n-1],row[j]
        m-=1;n-=1;rk+=1
    remaining=[mat[i][j] for i in range(m) for j in range(n) if mat[i][j]]
    return rk,remaining


def homology(fs):
    ranks=[0]*(len(fs)+1); torsion=False
    for k in range(2,len(fs)):
        lower,upper=fs[k-1],fs[k]
        if not upper:continue
        index={v:i for i,v in enumerate(lower)}
        b=[[0]*len(upper) for _ in range(len(lower))]
        for j,s in enumerate(upper):
            for pos,vertex in enumerate(v for v in range(len(fs)-1) if s>>v&1):
                b[index[s^(1<<vertex)]][j]=(-1)**pos
        rk, residual=unit_reduce(b)
        ranks[k]=rk
        if residual:torsion=True
    ranks[1]=int(bool(fs[1]))
    betti=tuple(len(fs[k])-ranks[k]-ranks[k+1] for k in range(1,len(fs)))
    assert all(x>=0 for x in betti)
    return betti,torsion


# Complete expected reduced integral Betti profile distribution.
EXPECTED = {
    (0,0,0):3558, (0,0,1):394, (0,0,2):60, (0,0,3):2,
    (0,1,0):1602, (0,1,1):218, (0,1,2):17,
    (0,2,0):623, (0,2,1):78, (0,2,2):36, (0,2,3):1,
    (0,3,0):181, (0,3,1):18, (0,3,2):2,
    (0,4,0):26, (0,4,1):2, (0,5,0):3, (0,5,1):2, (0,6,0):1,
    (1,0,0):34, (1,0,1):11, (1,0,2):4, (1,0,3):2,
    (1,0,4):1, (1,1,0):3, (1,1,1):1,
}

def test_known_torsion():
    # Six-vertex triangulation of the real projective plane (10 facets).
    triangles=('012','013','024','035','045','125','134','145','234','235')
    fs=[[] for _ in range(7)]
    for subset in range(1,1<<6):
        if any((subset & sum(1<<int(x) for x in face))==subset for face in triangles):
            fs[subset.bit_count()].append(subset)
    assert len(fs[3])==10
    _, torsion=homology(fs)
    assert torsion, 'The known projective-plane torsion must be detected'

def run():
    test_known_torsion()
    reps=all_classes()
    hist=Counter()
    for idx,r in enumerate(reps):
        bet,tor=homology(make_complex(r))
        assert not tor, ('torsion',idx,r)
        hist[bet]+=1
    assert {t[:3]:v for t,v in hist.items()}==EXPECTED, (hist,EXPECTED)
    assert len(hist)==26
    print('CENSUS',sum(hist.values()),'PROFILES',len(hist))
    for k,v in sorted(hist.items()):print(k,v)
    print('VERIFY_OK')
    return hist

if __name__=='__main__':run()
