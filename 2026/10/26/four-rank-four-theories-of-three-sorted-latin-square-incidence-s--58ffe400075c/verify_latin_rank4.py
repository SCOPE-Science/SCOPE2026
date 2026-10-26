#!/usr/bin/env python3
"""Finite checks of 4-round Latin-square incidence types and a sharp rank-5 witness.
No external packages; structural proof is in RESULT.md, not inferred from this sampling.
"""
from collections import defaultdict
from itertools import product


def cyclic(n):
    return [[(i+j)%n for j in range(n)] for i in range(n)]


def klein_four():
    return [[i^j for j in range(4)] for i in range(4)]


def validate_latin(L):
    n=len(L)
    assert n>0
    target=set(range(n))
    assert all(set(row)==target for row in L)
    assert all({L[i][j] for i in range(n)}==target for j in range(n))


def atomic_type(L, xs):
    n=len(L)
    sorts=tuple(x//n for x in xs)
    eq=tuple((i,j) for i in range(len(xs)) for j in range(i+1,len(xs)) if xs[i]==xs[j])
    rel=[]
    for i,j,k in product(range(len(xs)), repeat=3):
        if sorts[i]==0 and sorts[j]==1 and sorts[k]==2:
            if L[xs[i]%n][xs[j]%n]==xs[k]%n:
                rel.append((i,j,k))
    return (sorts,eq,tuple(rel))


def extension_profiles(L):
    n=len(L)
    m=3*n
    profiles={}
    raw_tuples=[0,0,0,0]
    counts=[]
    for k in range(4):
        local={}
        for xs in product(range(m), repeat=k):
            pre=atomic_type(L,xs)
            successors={atomic_type(L,xs+(x,)) for x in range(m)}
            if pre in local:
                assert local[pre]==successors, (n,k,pre,local[pre]^successors)
            else:
                local[pre]=successors
        profiles[k]=local
        counts.append((k,len(local),sum(len(x) for x in local.values())))
    return profiles,counts


def rectangle_three(L):
    n=len(L)
    witnesses=[]
    for a,b,c,d in product(range(n),repeat=4):
        if a==b or c==d:
            continue
        vals=[L[a][c],L[a][d],L[b][c],L[b][d]]
        if len(set(vals))==3:
            witnesses.append((a,b,c,d,vals))
    return witnesses



def reduced_latin_squares(n):
    """Enumerate reduced Latin squares, first row/column fixed 0..n-1."""
    target=set(range(n))
    L=[[-1]*n for _ in range(n)]
    L[0]=list(range(n))
    for i in range(n): L[i][0]=i
    usedrow=[{i} for i in range(n)]
    usedcol=[{j} for j in range(n)]
    usedrow[0]=target.copy()
    usedcol[0]=target.copy()
    cells=[(i,j) for i in range(1,n) for j in range(1,n)]

    def rec(t):
        if t==len(cells):
            yield [r[:] for r in L]
            return
        i,j=cells[t]
        for a in sorted(target-usedrow[i]-usedcol[j]):
            L[i][j]=a
            usedrow[i].add(a);usedcol[j].add(a)
            yield from rec(t+1)
            usedrow[i].remove(a);usedcol[j].remove(a)
            L[i][j]=-1

    yield from rec(0)


def main():
    cases=[('C1',cyclic(1)),('C2',cyclic(2)),('C3',cyclic(3)),('C4',cyclic(4)),('V4',klein_four()),('C5',cyclic(5)),('C6',cyclic(6))]
    results={}
    for name,L in cases:
        validate_latin(L)
        profiles,counts=extension_profiles(L)
        results[name]=profiles
        print(f'{name}: order {len(L)}; extension profiles (pebbles, qf types, successor types): {counts}')
    for k in range(4):
        assert results['C4'][k]==results['V4'][k]==results['C5'][k]==results['C6'][k],k
        print(f'ALL_Q_GE_4_MATCH at k={k}: {len(results["C4"][k])} distinct atomic prefix types')
    assert not rectangle_three(klein_four())
    for q in (4,5,6):
        witness=rectangle_three(cyclic(q))
        assert witness
        print(f'C{q}: rank-5 rectangle witness',witness[0])
    print('V4: no three-symbol 2x2 rectangles')
    for n,expected in [(4,4),(5,56)]:
        count=0
        for L in reduced_latin_squares(n):
            validate_latin(L)
            p,_=extension_profiles(L)
            assert p==results['C4'], (n,count)
            count+=1
        assert count==expected,(n,count,expected)
        print(f'EXHAUSTIVE_REDUCED_LATIN_ORDER_{n}: {count} squares, all prefix-extension profiles match C4')
    assert len({(min(q,4)) for q in range(1,7)})==4
    print('VERIFY_OK')


if __name__=='__main__': main()
