#!/usr/bin/env python3
"""Standalone finite checks for the two-independence Kneser complex theorem."""
from collections import Counter
from itertools import combinations,permutations
from math import comb


def faces_for(n):
    edges=list(combinations(range(n),2))
    disj={(i,j) for i,j in combinations(range(len(edges)),2) if not(set(edges[i])&set(edges[j]))}
    forbidden=[]
    for i,j,k in combinations(range(len(edges)),3):
        if sum(pair in disj for pair in [(i,j),(i,k),(j,k)])>=2:
            forbidden.append((1<<i)|(1<<j)|(1<<k))
    masks=[[] for _ in edges]
    for f in forbidden:
        for i in range(len(edges)):
            if f>>i&1:masks[i].append(f)
    faces=[0]
    for i in range(len(edges)):
        for face in list(faces):
            new=face|(1<<i)
            if all(new&bad!=bad for bad in masks[i]):faces.append(new)
    return edges,faces


def rank_gf2(columns):
    pivots={}
    for c in columns:
        while c:
            lead=c.bit_length()-1
            if lead not in pivots:
                pivots[lead]=c
                break
            c^=pivots[lead]
    return len(pivots)


def reduced_homology_gf2(faces):
    levels={}
    for f in faces: levels.setdefault(f.bit_count(),[]).append(f)
    maxdim=max(levels)-1
    ranks={1:0}
    for size in range(2,maxdim+2):
        targets={f:i for i,f in enumerate(levels[size-1])}
        cols=[]
        for f in levels[size]:
            c=0
            for i in range(f.bit_length()):
                if f>>i&1:c^=1<<targets[f^(1<<i)]
            cols.append(c)
        ranks[size]=rank_gf2(cols)
    betti={dim:len(levels[dim+1])-ranks.get(dim+1,0)-ranks.get(dim+2,0) for dim in range(maxdim+1)}
    betti[0]-=1
    return {d:b for d,b in betti.items() if b},dict(sorted(Counter(f.bit_count()-1 for f in faces if f).items()))


def character_from_faces(n,permutation,edges,faces):
    index={e:i for i,e in enumerate(edges)}
    onvertices=[index[tuple(sorted((permutation[a],permutation[b])))] for a,b in edges]
    lefschetz=0
    for f in faces:
        if not f: continue
        vertices=[i for i in range(len(edges)) if f>>i&1]
        image=[onvertices[i] for i in vertices]
        if set(image)!=set(vertices):continue
        inversions=sum(image[i]>image[j] for i in range(len(image)) for j in range(i+1,len(image)))
        lefschetz+=(-1)**(len(vertices)-1+inversions)
    return 1-lefschetz


def exterior_standard_character(n,permutation):
    unseen=set(range(n));cycles=[]
    while unseen:
        i=min(unseen);j=i;length=0
        while j in unseen:
            unseen.remove(j);length+=1;j=permutation[j]
        cycles.append(length)
    # det(I+tP)/(1+t) where permutation eigenvalue cycles give (1-(-t)^length)
    coeff=[1,0,0,0,0]
    for length in cycles:
        if length>4:continue
        factor=(-1)**(length+1)
        for k in range(4,length-1,-1):coeff[k]+=factor*coeff[k-length]
    for k in range(1,5):coeff[k]-=coeff[k-1]
    return coeff[4]


def octahedron_check():
    # On the 4-index set, four triangles of pairwise intersecting edges
    # represent the boundary of a tetrahedron after four star facets vanish.
    E=list(combinations(range(4),2))
    triangles=[tuple(sorted(E.index(e) for e in combinations(T,2))) for T in combinations(range(4),3)]
    stars=[tuple(sorted(E.index(tuple(sorted((i,j)))) for j in range(4) if i!=j)) for i in range(4)]
    facets=triangles+stars
    edge_rows=list(combinations(range(6),2))
    bd=[[sum((-1)**k for k in range(3) if tuple(f[:k]+f[k+1:])==edge) for f in facets] for edge in edge_rows]
    c=(1,-1,1,-1,-1,1,-1,1)
    assert all(sum(a*b for a,b in zip(row,c))==0 for row in bd)
    assert c[:4]==(1,-1,1,-1)
    index={e:i for i,e in enumerate(E)}
    for p in permutations(range(4)):
        on_vertices=[index[tuple(sorted((p[i],p[j])))] for i,j in E]
        chain={f:val for f,val in zip(facets,c)}
        mapped={}
        for f,val in zip(facets,c):
            ims=[on_vertices[i] for i in f]
            inversions=sum(ims[i]>ims[j] for i in range(3) for j in range(i+1,3))
            mf=tuple(sorted(ims))
            mapped[mf]=mapped.get(mf,0)+val*(-1)**inversions
        sgn=(-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        assert all(mapped.get(f)==sgn*val for f,val in chain.items()),(p,mapped,sgn)
    print('octahedral integral 2-cycle and tetrahedron boundary: PASS; all 24 relabeling orientations: PASS')


def main():
    octahedron_check()
    for n in (5,6,7,8):
        E,F=faces_for(n)
        betti, fvec=reduced_homology_gf2(F)
        expected={3:comb(n-1,4)}
        assert betti==expected,(n,betti,expected)
        allowed=[]
        stars=[{e for e in E if i in e} for i in range(n)]
        fours=[set(combinations(Q,2)) for Q in combinations(range(n),4)]
        covered=[set(E[j] for j in range(len(E)) if f>>j&1) for f in F]
        assert all(any(s<=st for st in stars) or any(s<=f for f in fours) for s in covered)
        permutations=[tuple(range(n)),tuple([1,0]+list(range(2,n))),tuple([1,2,0]+list(range(3,n)))]
        if n>=5:permutations.append(tuple([1,2,3,4,0]+list(range(5,n))))
        chars=[]
        for p in permutations:
            a=character_from_faces(n,p,E,F)
            b=exterior_standard_character(n,p)
            assert a==b,(n,p,a,b)
            chars.append(a)
        print('n=%d faces=%d fvector=%s reduced_Betti_F2=%s character_samples=%s PASS'%(n,len(F)-1,tuple(fvec.get(i,0) for i in range(max(fvec)+1)),betti,chars))
    print('ALL CHECKS PASS (finite checks do not replace the infinite proof)')

if __name__=='__main__':main()
