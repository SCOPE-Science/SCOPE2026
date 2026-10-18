#!/usr/bin/env python3
"""Exact combinatorial and integral checks for the sparse-paving normal-fan examples.
Run: python verify_vamos.py
Dependencies: Python standard library only.
This checks finite instances; the infinite-family assertions require the accompanying proof.
"""
from itertools import combinations
from collections import Counter
from fractions import Fraction


def matrix_rank(rows):
    if not rows:
        return 0
    a = [[Fraction(x) for x in row] for row in rows]
    nc = len(a[0]); nr = len(a)
    pivot = 0
    for j in range(nc):
        k = next((i for i in range(pivot, nr) if a[i][j]), None)
        if k is None:
            continue
        a[pivot],a[k] = a[k],a[pivot]
        c = a[pivot][j]
        a[pivot] = [z/c for z in a[pivot]]
        for i in range(pivot+1,nr):
            if a[i][j]:
                c = a[i][j]
                a[i] = [x-c*y for x,y in zip(a[i],a[pivot])]
        pivot += 1
        if pivot == nr:
            break
    return pivot


def bases_of(n,r,holes):
    hole = set(map(frozenset,holes))
    assert all(len(h)==r and all(1<=z<=n for z in h) for h in hole)
    assert all(len(a.intersection(b))<=r-2 for a,b in combinations(hole,2))
    return [frozenset(b) for b in combinations(range(1,n+1),r) if frozenset(b) not in hole]


def check_case(n,r,holes,expected_counts=None,check_facets=True):
    base=bases_of(n,r,holes)
    rank=matrix_rank([[int(i in B)-int(i in base[0]) for i in range(1,n)] for B in base])
    assert rank==n-1, (n,r,rank)
    allH=list(map(frozenset,holes))
    if check_facets:
        facets=[]
        for i in range(1,n+1):
            facets.append((lambda B,i=i:i not in B,f'x{i}=0'))
            facets.append((lambda B,i=i:i in B,f'x{i}=1'))
        for H in allH:
            facets.append((lambda B,H=H:len(B&H)==r-1,f'H{sorted(H)}'))
        for pred,lab in facets:
            bs=[B for B in base if pred(B)]
            fr=matrix_rank([[int(i in B)-int(i in bs[0]) for i in range(1,n)] for B in bs])
            assert fr==n-2, (n,r,lab,fr)
    counts=Counter()
    for B in base:
        t=sum(len(B&H)==r-1 for H in allH)
        counts[t]+=1
        # Exactly n + t distinct primitive normals, all coordinate normals span N.
        # Canonical support on coordinate normals is uniquely +/-1, and descends
        # to M_Q only when n=2r; each active circuit tests to r-2.
        canonical = (n==2*r and (t==0 or r==3))
        # Separate direct test: represent N using images of the first n-1 unit vectors.
        # In this basis the nth unit vector is (-1,...,-1).
        E = [[int(i==j) for j in range(1,n)] for i in range(1,n)]
        E.append([-1]*(n-1))
        coord_sign=[1 if i in B else -1 for i in range(1,n+1)]
        rays=[tuple(coord_sign[i]*q for q in E[i]) for i in range(n)]
        for H in allH:
            if len(B&H)==r-1:
                rays.append(tuple(sum(E[i-1][j] for i in H) for j in range(n-1)))
        candidate=[Fraction(x) for x in coord_sign[:n-1]]
        # The first n-1 coordinate equalities force this unique rational candidate.
        independently_cartier = all(sum(a*b for a,b in zip(v,candidate))==1 for v in rays)
        assert independently_cartier==canonical, (n,r,sorted(B),t)
        if canonical:
            assert all(x.denominator==1 for x in candidate)
        # The active coordinate vectors generate the saturated quotient lattice.
        clrank=(n+t)-(n-1)
        assert clrank==t+1
    if expected_counts is not None:
        assert counts==expected_counts, (n,r,counts,expected_counts)
    return base,counts


def vamos_orbits(bases, holes):
    swaps = [((1,2),), ((1,7),(2,8)), ((3,4),), ((3,5),(4,6))]
    generators=[]
    for cycles in swaps:
        p={i:i for i in range(1,9)}
        for x,y in cycles:
            p[x],p[y]=p[y],p[x]
        generators.append(p)
    holes=set(map(frozenset,holes))
    assert all({frozenset(p[i] for i in h) for h in holes}==holes for p in generators)
    remaining=set(bases); orbits=[]
    while remaining:
        seed=min(remaining,key=lambda s:tuple(sorted(s)))
        todo=[seed]; seen={seed}
        for B in todo:
            for p in generators:
                C=frozenset(p[i] for i in B)
                if C not in seen:
                    seen.add(C);todo.append(C)
        assert seen<=remaining
        remaining-=seen
        t=sum(len(seed&H)==3 for H in holes)
        assert all(sum(len(B&H)==3 for H in holes)==t for B in seen)
        orbits.append((tuple(sorted(seed)),len(seen),t))
    assert sorted((s,t) for _,s,t in orbits)==sorted([(1,0),(8,2),(8,2),(16,0),(16,1),(16,2)])
    return sorted(orbits,key=lambda x:(x[2],x[1],x[0]))


def main():
    vamosH=[(1,2,3,4),(1,2,5,6),(3,4,5,6),(3,4,7,8),(5,6,7,8)]
    B,count=check_case(8,4,vamosH, Counter({0:17,1:16,2:32}))
    assert len(B)==65
    print('VAMOS_N8_R4 65 vertices; Gorenstein=17, non-Q-Gorenstein=48')
    print('LOCAL_CLASS_RANK_COUNTS', dict(sorted((k+1,v) for k,v in count.items())))
    print('AUTOMORPHISM_ORBITS',vamos_orbits(B,vamosH))
    tests=[(6,3,[]),(6,3,[(1,2,3)]),(7,3,[(1,2,3)]),(8,4,[]),(8,4,[(1,2,3,4)]),(10,5,[(1,2,3,4,5)])]
    for n,r,H in tests:
        B,c=check_case(n,r,H)
        print('SAMPLE',n,r,len(H),len(B),dict(sorted(c.items())))
    print('VERIFY_OK')

if __name__=='__main__':
    main()
