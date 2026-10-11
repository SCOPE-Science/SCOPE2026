#!/usr/bin/env python3
"""Independent finite checks for closed-neighborhood complexes of Cartesian powers of complete graphs."""
from itertools import product,combinations
from collections import Counter,defaultdict

def construct(n,q):
    verts=list(product(range(q),repeat=n)); index={v:i for i,v in enumerate(verts)}
    facets=[]; faces={0}; lines={}
    for i,x in enumerate(verts):
        M=1<<i
        for k in range(n):
            line=0
            for a in range(q):
                y=x[:k]+(a,)+x[k+1:];line|=1<<index[y]
            lines[line]=None;M|=line
        facets.append(M)
        F=M
        while F:
            faces.add(F);F=(F-1)&M
    return verts,index,facets,faces,sorted(lines)

def all_supersets_one_step(face,live,vertices):
    return [face|(1<<i) for i in range(vertices) if not face&(1<<i) and face|(1<<i) in live]

def free_pair(face,upper,live,vertex_count):
    assert face in live and upper in live
    assert face.bit_count()+1==upper.bit_count()
    assert all_supersets_one_step(face,live,vertex_count)==[upper], ('face not free',face)
    assert not all_supersets_one_step(upper,live,vertex_count), ('upper not maximal',upper)
    live.remove(face);live.remove(upper)

def collapse(n,q):
    V,lookup,facets,faces,lines=construct(n,q)
    live=set(faces);d=n*(q-1);v=len(V)
    line_masks=set(lines)
    p1=p2=0
    for x,M in enumerate(facets):
        noncenter=M ^ (1<<x)
        cand=[];F=noncenter
        while F:
            if F.bit_count()>=3 and not any(F & L==F for L in line_masks):
                cand.append(F)
            F=(F-1)&noncenter
        for F in sorted(cand,key=lambda s:(-s.bit_count(),s)):
            free_pair(F,F|(1<<x),live,v);p1+=1
    for L in lines:
        root=(L&-L)
        F=L^root;cand=[];T=F
        while T:
            if T.bit_count()>=3:cand.append(T)
            T=(T-1)&F
        for T in sorted(cand,key=lambda s:(-s.bit_count(),s)):
            free_pair(T,T|root,live,v);p2+=1
    # Independently reconstruct exactly the predicted surviving two-faces.
    triangles=set()
    for x,Vx in enumerate(V):
        for i,j in combinations(range(n),2):
            for a in range(q):
                if a==Vx[i]:continue
                yi=Vx[:i]+(a,)+Vx[i+1:]
                for b in range(q):
                    if b==Vx[j]:continue
                    yj=Vx[:j]+(b,)+Vx[j+1:]
                    triangles.add((1<<x)|(1<<lookup[yi])|(1<<lookup[yj]))
    for L in lines:
        r=L&-L
        ids=[i for i in range(v) if (L&(1<<i)) and (1<<i)!=r]
        for i,j in combinations(ids,2):triangles.add(r|(1<<i)|(1<<j))
    assert {f for f in live if f.bit_count()==3}==triangles
    predicted_edges={ (1<<i)|(1<<j) for i in range(v) for j in range(i+1,v)
        if sum(a!=b for a,b in zip(V[i],V[j])) in (1,2)}
    assert {f for f in live if f.bit_count()==2}==predicted_edges
    assert max(F.bit_count() for F in live)==3
    assert all((F&-F) in live for F in live if F)
    c=Counter(F.bit_count() for F in live)
    reduced_euler = c[1]-c[2]+c[3]-1
    s=q-1
    numerator = v*(4-4*n*s+n*(n+1)*s*s)-2*n*q**(n-1)*s*s*(s-1)-4
    assert numerator%4==0
    beta=numerator//4
    assert reduced_euler==beta,(reduced_euler,beta)
    return {'q':q,'n':n,'original_faces':len(faces)-1,'collapse_pairs_by_stage':(p1,p2),'remaining_faces':len(live)-1,'remaining_f_vector':(c[1],c[2],c[3]),'beta2':beta,'discrete_collapse_valid':True},live

def gf2_homology_2d(live):
    by={k:sorted(f for f in live if f.bit_count()==k+1) for k in (0,1,2)}
    ranks={};
    for k in (1,2):
        idx={f:i for i,f in enumerate(by[k-1])};pivots={}
        for f in by[k]:
            col=0;T=f
            while T:
                v=T&-T;T^=v;col^=1<<idx[f^v]
            while col:
                top=col.bit_length()-1
                if top not in pivots:pivots[top]=col;break
                col^=pivots[top]
        ranks[k]=len(pivots)
    assert ranks[1]==len(by[0])-1
    return {'boundary_ranks':ranks,'betti2_mod2':len(by[2])-ranks[2], 'betti1_mod2':len(by[1])-ranks[1]-ranks[2]}

if __name__=='__main__':
    import json,sys
    pairs=[(2,3),(2,4),(3,2),(3,3),(4,2),(3,4),(4,3)]
    for n,q in pairs:
        result,remain=collapse(n,q)
        result.update(gf2_homology_2d(remain))
        assert result['betti2_mod2']==result['beta2'] and result['betti1_mod2']==0
        print(json.dumps(result,sort_keys=True),flush=True)
    print('VERIFY_OK')
