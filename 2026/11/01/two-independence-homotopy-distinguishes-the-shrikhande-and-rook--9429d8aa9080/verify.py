#!/usr/bin/env python3
"""Exact finite witness for two P3-devoid complexes. Pure Python 3.9+."""
from collections import Counter, deque
from itertools import combinations

VERTICES = tuple((i,j) for i in range(4) for j in range(4))
PIVOTS = (11,6,4,10,14,5,3,13,8,12,7,1,15,9,0,2)


def graph(kind):
    out=[0]*16
    for a,(i,j) in enumerate(VERTICES):
        for b,(k,l) in enumerate(VERTICES):
            if a==b: continue
            if kind=='rook':
                edge=(i==k or j==l)
            else:
                edge=((k-i)%4,(l-j)%4) in {(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
            if edge:out[a]|=1<<b
    return out


def valid_degrees(m,adj):
    return all((adj[i]&m).bit_count()<=1 for i in range(16) if m&(1<<i))


def valid_components(mask,adj):
    # Independent predicate: breadth-first search of connected components in induced graph
    unseen={i for i in range(16) if mask&(1<<i)}
    while unseen:
        root=next(iter(unseen));unseen.remove(root)
        queue=[root];size=1
        while queue:
            i=queue.pop()
            for j in tuple(unseen):
                if adj[i]&(1<<j):
                    unseen.remove(j);queue.append(j);size+=1
                    if size>2:return False
    return True


def check_parameters(adj):
    assert all(x.bit_count()==6 for x in adj)
    for a in range(16):
        for b in range(a+1,16):
            assert (adj[a]&adj[b]).bit_count()==2
    # Shrikhande vertex neighborhood has degree two; rook has degree two too,
    # but in the rook it splits into two triangles and in Shrikhande into C6.
    n=[v for v in range(16) if adj[0]&(1<<v)]
    seen=set();comps=[]
    for i in n:
        if i in seen:continue
        seen.add(i); stack=[i];c=0
        while stack:
            v=stack.pop();c+=1
            for w in n:
                if (adj[v]&(1<<w)) and w not in seen:
                    seen.add(w);stack.append(w)
        comps.append(c)
    return tuple(sorted(comps))


def enumerate_faces(adj):
    faces=[]
    for mask in range(1<<16):
        v=valid_degrees(mask,adj)
        assert v==valid_components(mask,adj), (mask, v)
        if v: faces.append(mask)
    return faces


def build_matching(faces):
    remaining=set(faces);pairs=[]
    for v in PIVOTS:
        b=1<<v
        candidates=[x for x in remaining if not x&b and x|b in remaining]
        for a in candidates:
            assert a in remaining and a|b in remaining
            remaining.remove(a);remaining.remove(a|b)
            pairs.append((a,a|b))
    assert len(pairs)==len(set(pairs))
    assert len(set(PIVOTS))==16
    special=[p for p in pairs if p[0]==0]
    assert len(special)==1 and special[0]==(0,1<<PIVOTS[0])
    pairs=[p for p in pairs if p[0]!=0]
    assert 0 not in remaining
    remaining.add(1<<PIVOTS[0])
    return pairs,remaining


def acyclic_test(faces,pairs):
    fset=set(faces)-{0}
    assert all(p and q in fset and (p&q)==p and (q^p).bit_count()==1 for p,q in pairs)
    assert len(set(x for p in pairs for x in p))==2*len(pairs)
    paired={(a,b) for a,b in pairs}
    outgoing={x:[] for x in fset}; indeg={x:0 for x in fset}
    incidences=0
    for high in fset:
        bits=high
        while bits:
            low=high^(bits&-bits);bits &=bits-1
            if low==0:continue
            assert low in fset
            incidences+=1
            src,dst=(low,high) if (low,high) in paired else (high,low)
            outgoing[src].append(dst);indeg[dst]+=1
    zero=deque(x for x in fset if indeg[x]==0)
    visited=0
    while zero:
        v=zero.popleft();visited+=1
        for w in outgoing[v]:
            indeg[w]-=1
            if indeg[w]==0:zero.append(w)
    assert visited==len(fset),f"cycle: {visited}/{len(fset)}"
    return incidences,visited


def mod2_bettis(faces):
    # Direct chain ranks over F2, entirely independent of the matching construction.
    fs={}
    for m in faces:
        if m: fs.setdefault(m.bit_count()-1,[]).append(m)
    ranks={}
    for dim in sorted(fs):
        if dim==0:continue
        ind={m:i for i,m in enumerate(fs[dim-1])}
        echelon={}
        rank=0
        for high in fs[dim]:
            vec=0;bits=high
            while bits:
                low=high^(bits&-bits);bits &= bits-1
                vec ^= 1<<ind[low]
            while vec:
                pivot=vec.bit_length()-1
                if pivot not in echelon:
                    echelon[pivot]=vec;rank+=1;break
                vec ^=echelon[pivot]
        ranks[dim]=rank
    bettis={d:len(fs[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in fs}
    bettis[0]-=1 # reduced H0 for connected complex
    return ranks,bettis


def main():
    for kind,fexpected,expected,faceexpected,local,facetexpected in (
        ('rook',(16,120,384,528,144),105,1192,(3,3),{3:96,4:144}),
        ('shrikhande',(16,120,384,544,240,32),57,1336,(6,),{3:64,4:48,5:32})):
        adj=graph(kind)
        lc=check_parameters(adj)
        assert lc==local,(kind,lc)
        faces=enumerate_faces(adj)
        fvec=tuple(Counter(m.bit_count()-1 for m in faces)[d] for d in range(len(fexpected)))
        assert fvec==fexpected
        assert len(faces)==faceexpected+1
        face_set=set(faces)
        facets=Counter(m.bit_count()-1 for m in faces if m and all(
            (m | (1<<i)) not in face_set for i in range(16) if not (m & (1<<i))))
        assert dict(facets)==facetexpected, (kind,facets)
        cycle=(0,1,2,3) if kind=='shrikhande' else (0,1,4,5)
        assert all(sum(bool(adj[i] & (1<<j)) for j in cycle if j!=i)==2 for i in cycle)
        pairs,crit=build_matching(faces)
        critdim=Counter(x.bit_count()-1 for x in crit)
        assert dict(critdim)=={0:1,3:expected}, (kind,critdim)
        assert len(pairs)==(len(faces)-len(crit)-1)//2
        incidences,seen=acyclic_test(faces,pairs)
        ranks,betti=mod2_bettis(faces)
        assert {d:v for d,v in betti.items() if v}=={3:expected},betti
        print(f"{kind}: connected_local_neighborhoods={lc}, faces_nonempty={len(faces)-1}, f_vector={fvec}, maximal_facet_dimensions={dict(sorted(facets.items()))}")
        print(f"{kind}: pivot_order={list(PIVOTS)}, matched_pairs={len(pairs)}, critical_cells={dict(sorted(critdim.items()))}")
        print(f"{kind}: incidence_edges={incidences}, acyclic_visited={seen}, F2_boundary_ranks={ranks}, reduced_F2_betti={betti}")
    print('ALL_CHECKS_PASS')

if __name__=='__main__':main()
