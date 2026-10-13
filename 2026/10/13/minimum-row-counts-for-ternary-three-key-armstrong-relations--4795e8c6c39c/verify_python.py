#!/usr/bin/env python3
"""Exact minimum record counts for ternary strength-three Armstrong tables.

Enumerate partitions canonically, then enumerate pairwise single-witness
families using an increasing-index, bitset-intersection depth-first search.
An equal-cardinality row-pair/attribute-pair argument makes the excluded
multi-witness cases impossible in the lower-bound searches.
"""
from collections import Counter
from itertools import combinations

FANO = (
 (3,2,2,1,2,1,1), (1,3,2,2,1,2,1),
 (1,1,3,2,2,1,2), (2,1,1,3,2,2,1),
 (1,2,1,1,3,2,2), (2,1,2,1,1,3,2),
 (2,2,1,2,1,1,3),
)
FIVE_SIX = tuple(zip(*(
 (0,0,0,0,1,2), (0,0,1,2,0,0),
 (0,1,0,2,0,2), (0,1,1,2,2,2),
 (0,1,2,2,2,0),
)))
FOUR_FOUR = tuple(zip(*(
 (0,0,0,1), (0,0,1,0),
 (0,1,0,0), (0,1,1,1),
)))

def check_rows(rows):
    m=len(rows); n=len(rows[0]); assert len(set(rows))==m
    assert all(len(r)==n and all(c in (0,1,2,3) for c in r) for r in rows)
    assert all(len(set(r[col] for r in rows))<=3 for col in range(n))
    witnesses=Counter()
    for i,j in combinations(range(m),2):
        agrees=tuple(k for k in range(n) if rows[i][k]==rows[j][k])
        assert len(agrees)<=2, (i,j,agrees)
        if len(agrees)==2: witnesses[agrees]+=1
    assert len(witnesses)==n*(n-1)//2, (n,witnesses)
    return {''.join(map(str,k)):v for k,v in witnesses.items()}

def partitions(m):
    pairs=tuple(combinations(range(m),2)); choices=[]
    def extend(a,hi):
        if len(a)==m:
            mask=sum(1<<e for e,(i,j) in enumerate(pairs) if a[i]==a[j])
            if mask != (1<<len(pairs))-1:
                choices.append((mask,tuple(a)))
            return
        for v in range(min(2,hi+1)+1):extend(a+[v],max(hi,v))
    extend([0],0)
    return choices

def diagonal_census(m):
    """Count the potential diagonal tables with m records and m attributes."""
    cols=partitions(m); ne=len(cols)
    neighbours=[0]*ne
    for i,(a,_) in enumerate(cols):
        for j in range(i+1,ne):
            b=cols[j][0]
            if (a&b).bit_count()==1:
                neighbours[i]|=1<<j
                neighbours[j]|=1<<i
    levels=Counter(); valid=[]
    def search(pool,picked,once,twice):
        levels[len(picked)] +=1
        if len(picked)==m:
            valid.append(picked);return
        if len(picked)+pool.bit_count()<m:return
        while pool:
            b=pool&-pool; v=b.bit_length()-1;pool-=b
            mask=cols[v][0]
            if mask&twice: continue
            search(pool&neighbours[v],picked+(v,), (once^mask)&~twice, twice|(once&mask))
    search((1<<ne)-1,(),0,0)
    return ne,levels,valid

def main():
    lower=[]
    for m in (3,5,6):
        nv,levels,solutions=diagonal_census(m)
        assert not solutions
        expected={3:4,5:40,6:121}[m]
        assert nv==expected
        lower.append((m,nv,dict(levels)))
    # 4 by 4; 6 by 5; 7 by 7.
    assert len(check_rows(FOUR_FOUR))==6
    assert len(check_rows(FIVE_SIX))==10
    assert len(check_rows(FANO))==21
    # A 4-by-3 witness follows by projecting away any column from 4-by-4.
    assert len(check_rows(tuple(r[:3] for r in FOUR_FOUR)))==3
    # A 7-by-6 witness follows by projecting away a column from 7-by-7.
    assert len(check_rows(tuple(r[:6] for r in FANO)))==15
    print('PASS minimum-row profile n=3..7: 4 4 6 7 7')
    for m,nv,levels in lower:
        print(f'DIAGONAL_NONEXISTENCE m={m} candidates={nv} ' + ' '.join(f'{k}:{levels.get(k,0)}' for k in range(m+1)))
    print('PASS explicit 4x4 6x5 7x7 and projections')
if __name__=='__main__':main()
