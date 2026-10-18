#!/usr/bin/env python3
"""Exact finite checks for complete-graph perfect matching normal-fan invariants."""
from itertools import combinations
from math import comb

def matchings(vs):
    if not vs:
        yield ()
        return
    a=vs[0]
    for j in range(1,len(vs)):
        b=vs[j]
        for m in matchings(vs[1:j]+vs[j+1:]):
            yield ((a,b),)+m

def rank_mod(rows,p=1000003):
    if not rows:return 0
    a=[list(map(lambda x:x%p,row)) for row in rows]
    m=len(a); n=len(a[0]); i=0
    for j in range(n):
        r=next((r for r in range(i,m) if a[r][j]),None)
        if r is None:continue
        a[i],a[r]=a[r],a[i]
        q=pow(a[i][j],-1,p)
        a[i][j:]=[(x*q)%p for x in a[i][j:]]
        for k in range(i+1,m):
            if a[k][j]:
                z=a[k][j]
                a[k][j:]=[(b-z*c)%p for b,c in zip(a[k][j:],a[i][j:])]
        i+=1
        if i==m:break
    return i

def test(m):
    n=2*m; edges=list(combinations(range(n),2)); es={e:i for i,e in enumerate(edges)}
    verts=[]
    for M in matchings(tuple(range(n))):
        s={es[e] for e in M}
        verts.append(tuple(int(i in s) for i in range(len(edges))))
    d=len(edges)-n
    assert rank_mod([[x-y for x,y in zip(v,verts[0])] for v in verts[1:]])==d
    chosen={es[(2*j,2*j+1)] for j in range(m)}
    exemplar=tuple(int(i in chosen) for i in range(len(edges)))
    assert exemplar in verts
    candidate=[]
    for k,e in enumerate(edges):
        if k in chosen: continue
        vals=[v[k] for v in verts]
        assert rank_mod([[x-y for x,y in zip(v,verts[0])] for v in verts if v[k]==0][1:])==d-1
        candidate.append(("coordinate", e, 0))
    all_cuts=[]
    # S and S-complement identify one facet; insist least element 0 in S
    for sz in range(3,n-2,2):
        for S in combinations(range(n),sz):
            if 0 not in S:continue
            all_cuts.append(S)
    # For n even, taking S containing 0 gives unique representatives of complement pairs.
    for S in all_cuts:
        j=(len(S)-1)//2
        inds=[es[e] for e in edges if e[0] in S and e[1] in S]
        heights=[j-sum(v[z] for z in inds) for v in verts]
        assert min(heights)==0 and max(heights)>0
        base=next(v for v,h in zip(verts,heights) if h==0)
        rows=[[x-y for x,y in zip(v,base)] for v,h in zip(verts,heights) if h==0]
        assert rank_mod(rows)==d-1, (m,S,'not a facet')
        if sum(exemplar[z] for z in inds)==j: candidate.append(('odd',S,j))
    # Each projective Cartier support function gives consistent ray values.
    # Build its integer compatibility equations directly at EVERY vertex.
    cut_reps=[S for S in all_cuts]
    variables={('e',e):i for i,e in enumerate(edges)}
    for S in cut_reps:variables[('cut',S)]=len(variables)
    relations=[]
    for mat in verts:
        M=[edges[k] for k,b in enumerate(mat) if b]
        matched={edges[k] for k,b in enumerate(mat) if b}
        # Matched endpoints must yield the same tangent coordinate.
        for a,b in M:
            row=[0]*len(variables)
            for c in range(n):
                if c!=a and c!=b:
                    row[variables[('e',tuple(sorted((a,c))))]]+=1
                    row[variables[('e',tuple(sorted((b,c))))]]-=1
            relations.append(row)
        for S in cut_reps:
            j=(len(S)-1)//2
            if sum(1 for a,b in M if a in S and b in S)!=j:continue
            row=[0]*len(variables)
            row[variables[('cut',S)]]=1
            for e in edges:
                if not (e[0] in S and e[1] in S):continue
                if e not in matched:
                    row[variables[('e',e)]]+=1
                else:
                    a,b=e
                    for c in range(n):
                        if c!=a and c!=b:row[variables[('e',tuple(sorted((a,c))))]]-=1
            relations.append(row)
    pic_dim=len(variables)-rank_mod(relations)
    assert pic_dim==d+1,(m,pic_dim,d)
    print('support_function_space_dimension',pic_dim,'Picard_rank',pic_dim-d,'global_Cl_rank',len(variables)-d)
    assert len(variables)-d==2**(n-2)
    expected=m*(2**(m-1)-2)
    assert sum(a[0]=='odd' for a in candidate)==expected, (m,expected)
    assert len(candidate)==2*m*(m-1)+expected
    assert len(candidate)-d==m*(2**(m-1)-1)
    # Unique candidate Cartier vector from offmatching coordinate normals.
    y={i:(1 if i not in chosen else -(n-2)) for i in range(len(edges))}
    for v in range(n):
        assert sum(y[i] for i,e in enumerate(edges) if v in e)==0
    triple=next(S for typ,S,j in candidate if typ=='odd' and len(S)==3)
    height=-sum(y[es[e]] for e in edges if e[0] in triple and e[1] in triple)
    assert height==2*(m-2), (m,height)
    assert height!=1
    print(f'n={n} vertices={len(verts)} dimension={d} all_facets={len(edges)+len(all_cuts)} local_coord={2*m*(m-1)} local_odd={expected} local_rays={len(candidate)} Cl_rank={len(candidate)-d} triple_cartier_height={height}')

if __name__=='__main__':
    for m in (3,4):test(m)
    print('VERIFY_OK')
