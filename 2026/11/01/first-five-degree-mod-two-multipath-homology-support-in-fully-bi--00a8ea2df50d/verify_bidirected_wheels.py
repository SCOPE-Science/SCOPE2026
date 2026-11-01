#!/usr/bin/env python3
"""Independent exhaustive face enumeration and exact GF(2) homology for bidirected wheel multipath complexes.
Run: python3 verify_bidirected_wheels.py (Python 3.9+, standard library only).
"""
from collections import Counter

EXPECTED = {
 3:(73,{1:7,2:6}),
 4:(261,{2:19,3:8}),
 5:(871,{2:2,3:23,4:10}),
 6:(2783,{3:29,4:26,5:12}),
 7:(8597,{4:43,5:30,6:14}),
 8:(25865,{4:37,5:32,6:34,7:16}),
 9:(76171,{5:71,6:36,7:38,8:18}),
 10:(220395,{5:49,6:40,7:40,8:42,9:20}),
}

def arcs_for(r):
    assert r>=3
    undirected=[(i,(i+1)%r) for i in range(r)] + [(i,r) for i in range(r)]
    return undirected, undirected+[(v,u) for u,v in undirected]

def directed_faces(r):
    """Direct arc recursion; noncycle test uses transitive reachability."""
    undirected,arcs=arcs_for(r)
    n=r+1
    faces={0}
    indeg=[0]*n
    outdeg=[0]*n
    def explore(i,mask,reach):
        if i==len(arcs):return
        explore(i+1,mask,reach)
        a,b=arcs[i]
        if indeg[b] or outdeg[a] or ((reach[b]>>a)&1):return
        updated=list(reach)
        predecessors=(v for v in range(n) if v==a or (reach[v]>>a)&1)
        for v in predecessors:updated[v]|=(1<<b)|reach[b]
        nextmask=mask|(1<<i)
        assert nextmask not in faces
        faces.add(nextmask)
        indeg[b]=1
        outdeg[a]=1
        explore(i+1,nextmask,updated)
        indeg[b]=0
        outdeg[a]=0
    explore(0,0,[0]*n)
    return faces

def undirected_path_faces(r):
    """Independent generator: enumerate undirected path forests, orient each path uniformly."""
    undirected,arcs=arcs_for(r)
    n=r+1
    ai={e:i for i,e in enumerate(arcs)}
    masks={0}
    degrees=[0]*n
    def submit(chosen):
        if not chosen:return
        neighbors=[[] for _ in range(n)]
        for u,v in chosen:
            neighbors[u].append(v);neighbors[v].append(u)
        seen=set()
        options=[]
        for start in range(n):
            if degrees[start]!=1 or start in seen:continue
            a=-1;b=start;p=0;q=0
            while True:
                seen.add(b)
                nxt=[x for x in neighbors[b] if x!=a]
                if not nxt:break
                c=nxt[0]
                p|=1<<ai[b,c]
                q|=1<<ai[c,b]
                a,b=b,c
            options.append((p,q))
        collection=[0]
        for p,q in options:
            collection=[x|a for x in collection for a in (p,q)]
        masks.update(collection)
    def rec(i,chosen,parent):
        if i==len(undirected):
            submit(chosen)
            return
        rec(i+1,chosen,parent)
        a,b=undirected[i]
        if degrees[a]>=2 or degrees[b]>=2:return
        def root(x):
            while x!=parent[x]:x=parent[x]
            return x
        ra,rb=root(a),root(b)
        if ra==rb:return
        newparent=list(parent);newparent[ra]=rb
        degrees[a]+=1;degrees[b]+=1;chosen.append((a,b))
        rec(i+1,chosen,newparent)
        chosen.pop();degrees[a]-=1;degrees[b]-=1
    rec(0,[],list(range(n)))
    return masks

def exact_binary_homology(faces):
    """Full simplicial matrices, column elimination over F_2, no probabilistic steps."""
    cells={}
    for face in faces:
        if face:cells.setdefault(face.bit_count()-1,[]).append(face)
    ranks={}
    for degree in sorted(cells):
        if degree==0:continue
        low_indices={face:i for i,face in enumerate(cells[degree-1])}
        basis={}
        for face in cells[degree]:
            boundary=0
            rest=face
            while rest:
                bit=rest&-rest
                rest-=bit
                boundary^=1<<low_indices[face^bit]
            while boundary:
                high=boundary.bit_length()-1
                if high in basis:boundary^=basis[high]
                else:
                    basis[high]=boundary
                    break
        ranks[degree]=len(basis)
    betti={degree:len(f)-ranks.get(degree,0)-ranks.get(degree+1,0) for degree,f in cells.items()}
    betti={degree:rank for degree,rank in betti.items() if rank}
    chi_cells=sum((-1)**degree*len(f) for degree,f in cells.items())
    chi_hom=sum((-1)**degree*rank for degree,rank in betti.items())
    assert chi_cells==chi_hom
    assert betti.get(0)==1
    return {d:rank for d,rank in betti.items() if d>0},ranks,chi_cells

if __name__=='__main__':
    for rim in EXPECTED:
        direct=directed_faces(rim)
        independent=undirected_path_faces(rim)
        assert direct==independent,('different face sets',rim)
        homology,ranks,chi=exact_binary_homology(direct)
        assert (len(direct),homology)==EXPECTED[rim]
        dims=Counter(x.bit_count()-1 for x in direct if x)
        print(f'r={rim} vertices={rim+1} arcs={4*rim} faces_including_empty={len(direct)} ' +
              f'face_counts={dict(sorted(dims.items()))} boundary_ranks={dict(sorted(ranks.items()))} ' +
              f'reduced_mod2_betti={homology} Euler={chi} independent_face_sets_equal=True',flush=True)
    assert all(len(EXPECTED[r][1])<=4 for r in range(3,10))
    assert len(EXPECTED[10][1])==5
    print('BIDIRECTED_WHEEL_FIRST_FIVE_DEGREES_EXACT_GF2_VERIFIED',flush=True)
