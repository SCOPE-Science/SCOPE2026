#!/usr/bin/env python3
"""Exact finite sanity checks for noncrossing perfect-matching edge sampling.

Python 3 standard library only. The finite checks do not prove the uniform theorem.
"""
from functools import lru_cache
from itertools import combinations
from math import comb

@lru_cache(None)
def cat(k):
    return comb(2*k, k)//(k+1)

@lru_cache(None)
def matchings(lo, hi):
    if lo > hi:
        return ((),)
    ans=[]
    for j in range(lo+1, hi+1, 2):
        for left in matchings(lo+1,j-1):
            for right in matchings(j+1,hi):
                ans.append(((lo,j),)+left+right)
    return tuple(ans)

def pair_count(n, e, f):
    if e==f:
        a,b=e
        j=(b-a-1)//2
        return cat(j)*cat(n-j-1)
    if len(set(e+f))<4:
        return 0
    t=sorted(e+f)
    a,b,c,d=t
    sorted_edges= {tuple(sorted(e)),tuple(sorted(f))}
    if sorted_edges == {(a,c),(b,d)}:
        return 0
    g0=b-a-1;g1=c-b-1;g2=d-c-1;g3=2*n-(d-a)-1
    if sorted_edges=={(a,b),(c,d)}:
        lengths=[g0,g2,g1+g3]
    elif sorted_edges=={(a,d),(b,c)}:
        lengths=[g1,g3,g0+g2]
    else:
        raise AssertionError((e,f))
    assert all(x>=0 and x%2==0 for x in lengths)
    z=1
    for x in lengths:
        z*=cat(x//2)
    return z

def check_flip_witnesses(n):
    """Every alternating four-point quadrilateral has two plane completions."""
    N=2*n
    valid=set(frozenset(m) for m in matchings(0,N-1))
    flips=0
    for a,b,c,d in combinations(range(N),4):
        if (a%2,b%2,c%2,d%2) not in ((0,1,0,1),(1,0,1,0)):
            continue
        gaps=[]
        for lo,hi in ((a,b),(b,c),(c,d),(d,a+N)):
            seq=list(range(lo+1,hi))
            assert len(seq)%2==0
            gaps.extend((seq[k]%N,seq[k+1]%N) for k in range(0,len(seq),2))
        gaps=[tuple(sorted(e)) for e in gaps]
        m1=frozenset(gaps+[(a,b),(c,d)])
        m2=frozenset(gaps+[(a,d),(b,c)])
        assert m1 in valid and m2 in valid,(n,a,b,c,d)
        flips+=1
    return flips

def rank_mod(a,p):
    b=[[x%p for x in row] for row in a]
    if not b: return 0
    h=0;w=len(b[0])
    for col in range(w):
        k=next((i for i in range(h,len(b)) if b[i][col]),None)
        if k is None:continue
        b[h],b[k]=b[k],b[h]
        inv=pow(b[h][col],-1,p)
        b[h][col:]=[(inv*x)%p for x in b[h][col:]]
        for i in range(h+1,len(b)):
            if b[i][col]:
                c=b[i][col]
                b[i][col:]=[(x-c*y)%p for x,y in zip(b[i][col:],b[h][col:])]
        h+=1
        if h==len(b):break
    return h

def test(n):
    m=matchings(0,2*n-1)
    assert len(m)==cat(n)
    edges=[(i,j) for i in range(2*n) for j in range(i+1,2*n) if (j-i)%2]
    row_vectors=[]
    ed_to_idx={e:i for i,e in enumerate(edges)}
    one=[0]*len(edges)
    two=[[0]*len(edges) for _ in edges]
    for M in m:
        v=[0]*len(edges)
        inds=[]
        for e in M:
            v[ed_to_idx[e]]=1
            inds.append(ed_to_idx[e])
        row_vectors.append(v)
        for x in inds:
            one[x]+=1
            for y in inds:
                two[x][y]+=1
    checks=0
    for i,e in enumerate(edges):
        assert one[i]==pair_count(n,e,e)
        for j,f in enumerate(edges):
            assert two[i][j]==pair_count(n,e,f),(n,e,f,two[i][j],pair_count(n,e,f))
            checks+=1
    want=(n-1)**2+1
    flips=check_flip_witnesses(n)
    rank=rank_mod(row_vectors,1000003)
    assert rank==want,(n,rank,want)
    return len(m),len(edges),checks,rank,flips

if __name__=='__main__':
    total=0
    flips_total=0
    for n in range(2,9):
        cnt,e,c,r,flips=test(n)
        flips_total+=flips
        total+=c
        print(f'n={n} matchings={cnt} eligible_edges={e} pair_tests={c} rank={r} flip_witnesses={flips}')
    print(f'PASS {total} exact integer pair-count comparisons, {flips_total} planar flip witnesses, 7 modular full-rank lower bounds')
