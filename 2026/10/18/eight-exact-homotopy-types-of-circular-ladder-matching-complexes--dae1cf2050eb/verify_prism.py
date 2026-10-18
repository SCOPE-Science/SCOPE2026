#!/usr/bin/env python3
"""Reproducible exact verification for ordinary matching complexes of circular ladders.

No external dependencies; all arithmetic is integral except an independent F_2 chain check.
"""
from __future__ import annotations
from collections import Counter, defaultdict, deque
from functools import lru_cache

EXPECTED = {
    3: {1:6},
    4: {2:4},
    5: {2:2,3:2},
    6: {3:12},
    7: {4:14},
    8: {4:3,5:7},
    9: {5:24},
    10:{6:40},
}
EXPECTED_FACES = {3:32,4:108,5:342,6:1104,7:3544,8:11396,9:36626,10:117732}
EXPECTED_MORSE_CRITICAL={
    3:{1:6},4:{2:4},5:{2:2,3:2},6:{3:12},7:{4:14},
    8:{4:4,5:8},9:{5:26,6:2},10:{6:40}
}
EXPECTED_BOUNDARY_RANK={3:0,4:0,5:0,6:0,7:0,8:1,9:2,10:0}


def edges_of_circular_ladder(n):
    assert 3 <= n <= 10
    edge_set = set()
    for level in range(2):
        for i in range(n):
            u, v = level*n+i, level*n+(i+1)%n
            edge_set.add(tuple(sorted((u,v))))
    for i in range(n):
        edge_set.add((i,i+n))
    return tuple(sorted(edge_set))


def all_faces(edges):
    adjacent = []
    for e in edges:
        adjacent.append(sum((1 << j) for j, f in enumerate(edges) if e!=f and (set(e)&set(f))))
    all_f={0}
    ordered=[0]
    for i in range(len(edges)):
        added=[s|(1<<i) for s in ordered if (s&adjacent[i])==0]
        all_f.update(added)
        ordered.extend(added)
    assert len(ordered)==len(all_f)
    return all_f


def toggle_matching(faces,n):
    # Exhaust the final n edges of the lexicographically ordered edge list,
    # then the first 2n edges. This deterministic order gives compact certificates.
    edges=edges_of_circular_ladder(n)
    ordered_edges=list(edges[2*n:])+list(edges[:2*n])
    index={e:i for i,e in enumerate(edges)}
    remaining=set(faces)
    pairing={}; reversed_pairing={}
    for edge in ordered_edges:
        bit=1<<index[edge]
        stage_pairs=[f for f in remaining if not f&bit and f|bit in remaining]
        for f in stage_pairs:
            assert f in remaining and f|bit in remaining
            remaining.remove(f);remaining.remove(f|bit)
            pairing[f]=f|bit
            reversed_pairing[f|bit]=f
    assert len(pairing)==len(reversed_pairing)
    assert 2*len(pairing)+len(remaining)==len(faces)
    return pairing,reversed_pairing,remaining


def boundary(face):
    pos=0
    rest=face
    while rest:
        bit=rest&-rest
        rest^=bit
        yield face^bit, (1 if pos%2==0 else -1)
        pos+=1


def acyclic_check(faces, pairing):
    # Orientation is reversed on each matched cover, down on all others.
    indegree={s:0 for s in faces}
    covers=0
    for s in faces:
        for lower,coef in boundary(s):
            if lower not in faces:continue
            if pairing.get(lower)==s:
                indegree[s]+=1
            else:
                indegree[lower]+=1
            covers+=1
    stack=deque(x for x,d in indegree.items() if d==0)
    visited=0
    while stack:
        s=stack.pop(); visited+=1
        if s in pairing:
            t=pairing[s]; indegree[t]-=1
            if indegree[t]==0:stack.append(t)
        for lower,coef in boundary(s):
            if lower not in faces:continue
            if pairing.get(lower)!=s:
                indegree[lower]-=1
                if indegree[lower]==0:stack.append(lower)
    assert visited==len(faces), ('not acyclic',visited,len(faces))
    return covers


def morse_boundary(pairs, critical):
    levels=defaultdict(list)
    for cell in critical:
        if cell and cell.bit_count()>1:levels[cell.bit_count()-1].append(cell)
    levels={k:sorted(v) for k,v in levels.items()}
    if len(levels)==1:return levels, []
    assert len(levels)==2
    upper=max(levels);lower=upper-1
    assert lower in levels
    lower_ids={f:i for i,f in enumerate(levels[lower])}
    @lru_cache(None)
    def flow(f):
        if f in lower_ids:return {lower_ids[f]:1}
        if f not in pairs:return {}
        top=pairs[f]
        eps=next(co for a,co in boundary(top) if a==f)
        accum=defaultdict(int)
        for a,co in boundary(top):
            if a==f:continue
            for idx,entry in flow(a).items():
                accum[idx]-=eps*co*entry
        return {i:v for i,v in accum.items() if v}
    matrix=[[0]*len(levels[upper]) for _ in levels[lower]]
    for j,top in enumerate(levels[upper]):
        for f,co in boundary(top):
            for i,v in flow(f).items():matrix[i][j]+=co*v
    return levels,matrix


def rank_and_unit_minor(matrix):
    if not matrix:return 0
    a=[list(map(int,row)) for row in matrix]
    rows=len(a);cols=len(a[0]);rank=0
    # Only integral additions and sign changes, no fractions. Search unit pivots.
    for c in range(cols):
        unit=next((r for r in range(rank,rows) if abs(a[r][c])==1),None)
        if unit is None:continue
        a[rank],a[unit]=a[unit],a[rank]
        if a[rank][c]==-1:a[rank]=[-v for v in a[rank]]
        for r in range(rows):
            if r!=rank and a[r][c]:
                fac=a[r][c]
                a[r]=[x-fac*y for x,y in zip(a[r],a[rank])]
        rank+=1
        if rank==rows:break
    # Verify after unit eliminations there is no nonzero residual integer block.
    assert all(a[r][c]==0 for r in range(rank,rows) for c in range(cols))
    return rank


def direct_mod2_homology(faces):
    levels=defaultdict(list)
    for f in faces:
        if f:levels[f.bit_count()-1].append(f)
    levels={k:sorted(v) for k,v in levels.items()}
    ranks={}
    for k in range(1,max(levels)+1):
        below={f:i for i,f in enumerate(levels[k-1])}
        pivot={}
        for f in levels[k]:
            col=0
            for sub,co in boundary(f):col^=1<<below[sub]
            while col:
                v=col.bit_length()-1
                if v not in pivot:
                    pivot[v]=col
                    break
                col^=pivot[v]
        ranks[k]=len(pivot)
    bettis={}
    for k,items in levels.items():
        betti=len(items)-ranks.get(k,0)-ranks.get(k+1,0)
        if k==0:betti-=1
        if betti: bettis[k]=betti
    return bettis


def main():
    for n in EXPECTED:
        edges=edges_of_circular_ladder(n)
        assert len(edges)==3*n
        faces=all_faces(edges)
        assert len(faces)==EXPECTED_FACES[n]
        paired,reverse,augmented_critical=toggle_matching(faces,n)
        actual=dict(sorted(Counter(f.bit_count()-1 for f in augmented_critical).items()))
        assert actual==EXPECTED_MORSE_CRITICAL[n],(n,actual)
        assert 0 in paired
        # Convert the augmented matching to the ordinary face poset:
        # omit the empty face and leave its former partner as one critical vertex.
        base_vertex=paired.pop(0)
        del reverse[base_vertex]
        critical=set(augmented_critical)|{base_vertex}
        assert Counter(f.bit_count()-1 for f in critical)[0]==1
        covers=acyclic_check(faces-{0},paired)
        levels,matrix=morse_boundary(paired,critical)
        rank=rank_and_unit_minor(matrix)
        assert rank==EXPECTED_BOUNDARY_RANK[n]
        homotopy={}
        for k,simplices in levels.items():
            b=len(simplices)
            if k==max(levels):b-=rank
            if k==min(levels) and len(levels)>1:b-=rank
            if b:homotopy[k]=b
        assert homotopy==EXPECTED[n],(n,homotopy)
        reduced_euler=-1+sum((1 if (f.bit_count()-1)%2==0 else -1) for f in faces if f)
        expected_euler=sum((-1)**k*v for k,v in homotopy.items())
        assert reduced_euler==expected_euler
        if n<=10:
            direct=direct_mod2_homology(faces)
            assert direct==homotopy,(n,direct,homotopy)
        print('n',n,'faces',len(faces),'covers',covers,'matched_pairs',len(paired),
              'critical_positive',actual,'critical_vertices',1,'Morse_boundary_rank',rank,'homotopy',homotopy,
              'euler',reduced_euler,'direct_F2',n<=10,flush=True)
    print('VERIFY_OK: eight complete acyclic matchings, exact Morse differentials and Euler checks; F2 cross-check through n=10')

if __name__=='__main__':main()
