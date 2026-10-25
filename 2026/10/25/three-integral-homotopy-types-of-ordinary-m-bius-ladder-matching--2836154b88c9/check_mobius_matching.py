#!/usr/bin/env python3
"""Exhaustive integral discrete-Morse certificate for matching complexes of M_12,M_14,M_16.
Standard library only; Python >= 3.8. Execution: python3 check_mobius_matching.py.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
import hashlib
import json

EXPECTED = {
    6: {"face_counts": [1,18,117,336,420,192,18], "critical_counts": {0:1,2:2,3:15,4:3}, "morse_ranks": {3:2,4:3}, "betti": {3:10}},
    7: {"face_counts": [1,21,168,644,1225,1085,371,31], "critical_counts": {0:1,3:8,4:24}, "morse_ranks": {4:8}, "betti": {4:16}},
    8: {"face_counts": [1,24,228,1096,2834,3880,2588,696,47], "critical_counts": {0:1,3:2,4:23,5:23}, "morse_ranks": {4:2,5:19}, "betti": {4:2,5:4}},
}

def edges_for(n):
    verts = 2*n
    return sorted({tuple(sorted((i,(i+1)%verts))) for i in range(verts)}
                  | {(i,i+n) for i in range(n)})

def generate_faces(edges):
    masks = [(1<<a)|(1<<b) for a,b in edges]
    levels = [[0]]
    frontier = [(0,0)]
    while frontier:
        nxt=[]
        for f,occupied in frontier:
            for j in range(f.bit_length(),len(edges)):
                if occupied & masks[j] == 0:
                    nxt.append((f|(1<<j),occupied|masks[j]))
        if not nxt:break
        levels.append([f for f,_ in nxt]);frontier=nxt
    assert all(len(a)==len(set(a)) for a in levels)
    return levels

def independent_faces(edges):
    # Generate independently using an include/exclude dynamic programme.
    states = {0:0}
    for j,(a,b) in enumerate(edges):
        bit=(1<<a)|(1<<b)
        add={f|(1<<j):used|bit for f,used in states.items() if not (used&bit)}
        assert states.keys().isdisjoint(add)
        states.update(add)
    return set(states)

def staged_matching(levels,edge_count):
    remaining=set().union(*map(set,levels))
    pairs=[]
    for j in range(edge_count):
        bit=1<<j
        for f in sorted(remaining,key=lambda f:(f.bit_count(),f)):
            u=f|bit
            if f in remaining and not(f&bit) and u in remaining:
                remaining.remove(f);remaining.remove(u);pairs.append((f,u))
    assert pairs and pairs[0][0]==0
    # Formal reduced pair (empty, vertex) is replaced by a critical vertex.
    geom_pairs=[(a,b) for a,b in pairs if a]
    critical=set(remaining)|{pairs[0][1]}
    return geom_pairs,critical

def acyclicity_and_coverage(levels,pairs,critical):
    cells=set().union(*map(set,levels))-{0}
    pairset=set(pairs)
    count=0
    incoming={f:0 for f in cells}
    outgoing=defaultdict(list)
    for high in cells:
        m=high
        while m:
            bit=m&-m;m-=bit;low=high^bit
            if not low:continue
            tail,head=(low,high) if (low,high) in pairset else (high,low)
            outgoing[tail].append(head);incoming[head]+=1;count+=1
    queue=deque(f for f,v in incoming.items() if not v)
    visited=0
    while queue:
        f=queue.popleft();visited+=1
        for g in outgoing[f]:
            incoming[g]-=1
            if not incoming[g]:queue.append(g)
    assert visited==len(cells), (visited,len(cells))
    matched={v for pair in pairs for v in pair}
    assert (cells-matched)==critical
    return len(cells),count,len(pairs)

def signed_morse_boundary(critical,pairs):
    top={low:up for low,up in pairs}
    bottom={up:low for low,up in pairs}
    @lru_cache(None)
    def project(f):
        if f in critical:return {f:1}
        if f in bottom:return {}
        upper=top[f]
        flip=upper^f
        s=(-1)**((upper&(flip-1)).bit_count())
        out=defaultdict(int)
        m=upper
        while m:
            bit=m&-m;m-=bit
            if bit==flip:continue
            coeff=(-1)**((upper&(bit-1)).bit_count())
            for g,v in project(upper^bit).items():out[g]-=s*coeff*v
        return {g:v for g,v in out.items() if v}
    boundary={}
    for f in critical:
        ans=defaultdict(int)
        m=f
        while m:
            bit=m&-m;m-=bit
            sign=(-1)**((f&(bit-1)).bit_count())
            low=f^bit
            if low==0:continue
            for g,v in project(low).items():ans[g]+=sign*v
        boundary[f]={g:v for g,v in ans.items() if v}
    for f,d in boundary.items():
        dd=defaultdict(int)
        for g,v in d.items():
            for h,w in boundary[g].items():dd[h]+=v*w
        assert not any(dd.values()),(f,dd)
    return boundary

def integer_unit_rank(matrix):
    if not matrix:return 0
    rows=len(matrix);cols=len(matrix[0]);t=0
    while t<min(rows,cols):
        pivot=next(((i,j) for i in range(t,rows) for j in range(t,cols)
                     if abs(matrix[i][j])==1),None)
        if pivot is None:break
        i,j=pivot
        matrix[t],matrix[i]=matrix[i],matrix[t]
        for r in range(rows):matrix[r][t],matrix[r][j]=matrix[r][j],matrix[r][t]
        unit=matrix[t][t];assert abs(unit)==1
        for r in range(t+1,rows):
            v=unit*matrix[r][t]
            if v:
                for c in range(t,cols):matrix[r][c]-=v*matrix[t][c]
        for c in range(t+1,cols):
            v=unit*matrix[t][c]
            if v:
                for r in range(rows):matrix[r][c]-=v*matrix[r][t]
        t+=1
    assert all(matrix[r][c]==0 for r in range(t,rows) for c in range(t,cols)), 'non-unit invariant'
    return t

def mod2_rank(columns):
    pivots={}
    for col in columns:
        while col:
            bit=col.bit_length()-1
            if bit in pivots:col^=pivots[bit]
            else:pivots[bit]=col;break
    return len(pivots)

def independent_mod2_homology(levels):
    ranks=[0]*len(levels)
    for k in range(2,len(levels)):
        rows={f:i for i,f in enumerate(levels[k-1])}
        cols=[]
        for f in levels[k]:
            col=0;m=f
            while m:
                bit=m&-m;m-=bit
                col^=1<<rows[f^bit]
            cols.append(col)
        ranks[k]=mod2_rank(cols)
    betti={k-1:len(levels[k])-ranks[k]-(ranks[k+1] if k+1<len(levels) else 0)
           for k in range(1,len(levels))}
    betti[0]-=1
    return {k:v for k,v in betti.items() if v}

def run_case(n):
    edges=edges_for(n)
    levels=generate_faces(edges)
    assert set().union(*(set(a) for a in levels))==independent_faces(edges)
    geom,critical=staged_matching(levels,len(edges))
    nc,relations,npairs=acyclicity_and_coverage(levels,geom,critical)
    counts=dict(sorted(Counter(f.bit_count()-1 for f in critical).items()))
    boundary=signed_morse_boundary(critical,geom)
    bydim=defaultdict(list)
    for f in critical:bydim[f.bit_count()-1].append(f)
    morse_ranks={}
    matrix_digests={}
    for dim in sorted(bydim):
        if dim-1 not in bydim:continue
        lower=sorted(bydim[dim-1]);higher=sorted(bydim[dim])
        mat=[[boundary[f].get(g,0) for f in higher] for g in lower]
        flat=json.dumps(mat,separators=(',',':'))
        matrix_digests[str(dim)]=hashlib.sha256(flat.encode()).hexdigest()
        morse_ranks[dim]=integer_unit_rank(mat)
    morse_betti={dim:len(faces)-morse_ranks.get(dim,0)-morse_ranks.get(dim+1,0)
                 for dim,faces in bydim.items() if dim>0}
    morse_betti={k:v for k,v in morse_betti.items() if v}
    # Completely independent chain calculation with mod-two elimination.
    mod2=independent_mod2_homology(levels)
    assert list(map(len,levels))==EXPECTED[n]['face_counts']
    assert counts==EXPECTED[n]['critical_counts']
    assert morse_ranks==EXPECTED[n]['morse_ranks']
    assert morse_betti==EXPECTED[n]['betti']==mod2
    return {"n":n,"vertices":2*n,"graph_edges":len(edges),"face_counts":list(map(len,levels)),
            "nonempty_simplices":nc,"Hasse_cover_relations":relations,"geometric_pairs":npairs,
            "critical_by_dimension":counts,"unit_pivot_ranks":morse_ranks,
            "morse_boundary_sha256":matrix_digests,"reduced_integral_betti":morse_betti,
            "independent_mod2_betti":mod2,"acyclic":True}

if __name__=='__main__':
    for n in (6,7,8):print(json.dumps(run_case(n),sort_keys=True,separators=(',',':')))
    print('ALL_CERTIFICATES_PASS')
