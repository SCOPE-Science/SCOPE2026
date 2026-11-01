#!/usr/bin/env python3
"""Exact proof checker for the perfect-matching complex of the dodecahedral graph.

Python 3 standard library only. A facet is a perfect matching in generalized
Petersen graph GP(10,2). Uses complete enumeration, an explicit acyclic
coordinate-toggle matching, integral gradient-path boundary coefficients,
and two independent integer Smith-invariant witnesses.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from hashlib import sha256

N = 10
VERTICES = 20
EDGES = tuple(sorted({tuple(sorted(edge)) for i in range(N) for edge in
    ((i, (i+1)%N), (i, N+i), (N+i, N+(i+2)%N))}))
assert len(EDGES) == 30
INC = tuple(tuple(j for j, (a,b) in enumerate(EDGES) if v==a or v==b)
            for v in range(VERTICES))

def perfect_matchings():
    result = set()
    def visit(occupied, mask):
        if occupied == (1<<VERTICES)-1:
            result.add(mask)
            return
        v = next(u for u in range(VERTICES) if not (occupied>>u)&1)
        for e in INC[v]:
            a,b = EDGES[e]
            w = a^b^v
            if not (occupied>>w)&1:
                visit(occupied|(1<<v)|(1<<w), mask|(1<<e))
    visit(0,0)
    return result

def independent_matching_census(pm):
    # Independently enumerate all (not necessarily extendible) matchings.
    total = accepted = 0
    def visit(i, occupied, mask):
        nonlocal total, accepted
        if i == len(EDGES):
            total += 1
            if any((mask & perfect) == mask for perfect in pm):
                accepted += 1
            return
        visit(i+1, occupied, mask)
        a,b = EDGES[i]
        if not (occupied>>a)&1 and not (occupied>>b)&1:
            visit(i+1, occupied|(1<<a)|(1<<b), mask|(1<<i))
    visit(0,0,0)
    return total, accepted

def all_faces(pm):
    result = {0}
    for maximal in pm:
        sub = maximal
        while True:
            result.add(sub)
            if sub == 0:break
            sub = (sub-1)&maximal
    return result

def boundary(mask):
    terms=[]
    bits=mask
    pos=0
    while bits:
        bit=bits&-bits
        bits ^= bit
        terms.append((mask^bit, -1 if pos%2 else 1))
        pos+=1
    return terms

def toggle_matching(faces):
    remaining = set(faces)-{0}
    pairs = []
    for i in range(len(EDGES)):
        bit=1<<i
        lows=sorted(s for s in remaining if not s&bit and s|bit in remaining)
        for low in lows:
            high=low|bit
            if low in remaining and high in remaining:
                pairs.append((low,high))
                remaining.remove(low)
                remaining.remove(high)
    return remaining,pairs

def acyclic_hasse(faces,pairs):
    reversed_pairs = set(pairs)
    nodes = set(faces)-{0}
    adjacency={s:[] for s in nodes}
    indegree=dict.fromkeys(nodes,0)
    count=0
    for upper in nodes:
        if upper.bit_count() < 2:continue
        for lower,_ in boundary(upper):
            assert lower in nodes
            start,end=(lower,upper) if (lower,upper) in reversed_pairs else (upper,lower)
            adjacency[start].append(end)
            indegree[end]+=1
            count+=1
    q=deque(s for s in nodes if indegree[s]==0)
    visited=0
    while q:
        s=q.popleft();visited+=1
        for t in adjacency[s]:
            indegree[t]-=1
            if not indegree[t]:q.append(t)
    assert visited==len(nodes)
    return count,visited

def integral_morse_boundary(critical,pairs):
    low_high=dict(pairs)
    uppers={u for _,u in pairs}
    bydim=defaultdict(list)
    for s in sorted(critical):bydim[s.bit_count()-1].append(s)
    @lru_cache(None)
    def reduce(s):
        if s in critical:return {s:1}
        if s in uppers:return {}
        assert s in low_high
        upper=low_high[s]
        incidence=dict(boundary(upper))[s]
        assert abs(incidence)==1
        accum=defaultdict(int)
        for sub,sign in boundary(upper):
            if sub==s:continue
            for dest,val in reduce(sub).items():
                accum[dest]-=incidence*sign*val
        return {k:v for k,v in accum.items() if v}
    target={s:i for i,s in enumerate(bydim[2])}
    matrix=[[0]*len(bydim[3]) for _ in bydim[2]]
    for j,source in enumerate(bydim[3]):
        for sub,sign in boundary(source):
            for dest,coeff in reduce(sub).items():
                matrix[target[dest]][j] += sign*coeff
    return bydim,matrix

def rank_mod_prime(mat,p):
    a=[[x%p for x in row] for row in mat]
    rows=len(a);cols=len(a[0])
    rank=0
    for c in range(cols):
        k=next((r for r in range(rank,rows) if a[r][c]%p),None)
        if k is None:continue
        a[k],a[rank]=a[rank],a[k]
        pivot_inverse=pow(a[rank][c],-1,p)
        a[rank]=[(u*pivot_inverse)%p for u in a[rank]]
        for r in range(rank+1,rows):
            coeff=a[r][c]
            if coeff:a[r]=[(v-coeff*u)%p for u,v in zip(a[rank],a[r])]
        rank+=1
        if rank==rows:break
    return rank

def determinant_bareiss(square):
    a=[row[:] for row in square]
    n=len(a)
    sign=1
    denom=1
    for k in range(n-1):
        if a[k][k]==0:
            r=next((r for r in range(k+1,n) if a[r][k]),None)
            if r is None:return 0
            a[r],a[k]=a[k],a[r]
            sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                value=a[i][j]*pivot-a[i][k]*a[k][j]
                assert value%denom==0
                a[i][j]=value//denom
            a[i][k]=0
        denom=pivot
    return sign*a[n-1][n-1]

def full_boundary_mod2_ranks(faces):
    levels=defaultdict(list)
    for face in sorted(faces):
        if face:levels[face.bit_count()-1].append(face)
    ranks={}
    for k in range(1,10):
        lower_index={s:i for i,s in enumerate(levels[k-1])}
        pivots={}
        for cell in levels[k]:
            col=0
            for sub,_ in boundary(cell):col |= 1<<lower_index[sub]
            while col:
                i=col.bit_length()-1
                if i not in pivots:
                    pivots[i]=col
                    break
                col ^= pivots[i]
        ranks[k]=len(pivots)
    return ranks

def main():
    pm=perfect_matchings()
    assert len(pm)==36
    all_matchings,extendible=independent_matching_census(pm)
    assert (all_matchings,extendible)==(111376,30504)
    faces=all_faces(pm)
    assert len(faces)==extendible
    fvec=Counter(s.bit_count()-1 for s in faces)
    assert tuple(fvec[k] for k in range(-1,10))==(1,30,375,2180,5790,8352,7440,4320,1620,360,36)
    critical,pairs=toggle_matching(faces)
    assert len(pairs)==15231
    critical_counts=Counter(s.bit_count()-1 for s in critical)
    assert critical_counts=={0:1,2:10,3:30}
    incidence,verified=acyclic_hasse(faces,pairs)
    assert incidence==163650 and verified==30503
    bydim,boundary3=integral_morse_boundary(critical,pairs)
    assert len(boundary3)==10 and all(len(r)==30 for r in boundary3)
    assert Counter(v for row in boundary3 for v in row)=={-1:34,0:231,1:35}
    rank2=rank_mod_prime(boundary3,2)
    rank3=rank_mod_prime(boundary3,3)
    assert (rank2,rank3)==(9,10)
    columns=(0,2,4,5,6,7,8,10,11,26)
    det=determinant_bareiss([[r[c] for c in columns] for r in boundary3])
    assert det==2
    # Since some maximal minor is +/-2 and rank over F_2 is 9, the product
    # of the 10 nonzero Smith invariants is 2; nine are odd and one even.
    # Hence these invariants are exactly (1,1,1,1,1,1,1,1,1,2).
    # A connected CW complex with one 0-cell, 10 two-cells and 30 three-cells
    # has wedge-of-2-spheres 2-skeleton. Each 3-cell's attaching homotopy
    # class is determined by this integral boundary matrix, hence its SNF
    # identifies a Moore space M(Z/2,2) wedged with 20 three-spheres.
    ranks=full_boundary_mod2_ranks(faces)
    levels={k:fvec[k] for k in range(10)}
    betti={k:levels[k]-ranks.get(k,0)-ranks.get(k+1,0) for k in range(10)}
    assert betti=={0:1,1:0,2:1,3:21,4:0,5:0,6:0,7:0,8:0,9:0}
    sha=sha256(','.join(map(str,sorted(faces))).encode()).hexdigest()
    print('DODECAHEDRAL_PMC_MOORE_TWO_TORSION_VERIFIED')
    print('vertices=20 edges=30 perfect_matchings=36')
    print('all_graph_matchings=111376 extendible_faces_including_empty=30504')
    print('fvector='+str(tuple(fvec[k] for k in range(10))))
    print('morse_pairs=15231 critical_cells=(one_0,ten_2,thirty_3)')
    print('hasse_incidences=163650 acyclic=True')
    print('morse_boundary_matrix=10x30 entries='+str(dict(sorted(Counter(v for row in boundary3 for v in row).items()))))
    print('rank_mod2='+str(rank2)+' rank_mod3='+str(rank3))
    print('minor_columns='+str(columns)+' determinant='+str(det))
    print('smith_invariants=(1,1,1,1,1,1,1,1,1,2)')
    print('independent_mod2_boundary_ranks='+str(tuple(ranks[k] for k in range(1,10))))
    print('independent_mod2_betti='+str(tuple(betti[k] for k in range(10))))
    print('homotopy=Moore(Z/2,2)_wedge_20_S3')
    print('faces_sha256='+sha)

if __name__=='__main__':main()
