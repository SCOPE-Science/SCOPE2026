#!/usr/bin/env python3
"""Exact self-contained finite topological certificate for the 5x5 bishop complex.

The two component clique/independence complexes are reduced by explicit free
3-simplex/2-simplex collapses, then 2-complex cellular 1/2 cancellations.
No random choices, external data, or numerical approximations are used.
"""
from collections import Counter, deque
from itertools import combinations
import math

N = 5
SQUARES = [(r,c) for r in range(N) for c in range(N)]

def graph():
    adj = {}
    for i, (r,c) in enumerate(SQUARES):
        adj[i] = {j for j, (s,t) in enumerate(SQUARES)
                  if i != j and abs(r-s)==abs(c-t)}
    return adj

def faces_from_graph(vertices, adj):
    faces=[frozenset()]
    for v in vertices:
        faces += [f|{v} for f in faces[:] if not(f&adj[v])]
    return set(faces)

def free_tetra_collapses(faces):
    remain=set(faces)
    pairs=[]
    for sigma in sorted((s for s in remain if len(s)==4),key=lambda x:tuple(sorted(x))):
        candidates=[]
        for v in sorted(sigma):
            face=sigma-{v}
            other=[t for t in remain if len(t)==4 and face<=t]
            if len(other)==1 and other[0]==sigma:
                candidates.append(face)
        assert candidates, 'cannot collapse tetrahedron'
        tau=min(candidates,key=lambda x:tuple(sorted(x)))
        assert sigma in remain and tau in remain
        remain.remove(sigma)
        remain.remove(tau)
        pairs.append((tuple(sorted(tau)),tuple(sorted(sigma))))
    assert not any(len(x)>3 for x in remain)
    # The resulting collection is still downward closed.
    assert all(frozenset(s)<=set(remain) for s in [()]) # nonempty used below
    for f in remain:
        for v in f:
            assert f-{v} in remain
    return remain,pairs

def freely_reduce(word):
    s=[]
    for x in word:
        if s and s[-1] == -x: s.pop()
        else: s.append(x)
    return s

def inverse(word):
    return [-x for x in reversed(word)]

def presentation_certificate(faces):
    vertices=sorted(v for f in faces if len(f)==1 for v in f)
    edges=sorted(tuple(sorted(f)) for f in faces if len(f)==2)
    tris=sorted(tuple(sorted(f)) for f in faces if len(f)==3)
    nbr={v:[] for v in vertices}
    for a,b in edges:nbr[a].append(b);nbr[b].append(a)
    parent={vertices[0]:None}; queue=deque([vertices[0]])
    while queue:
        v=queue.popleft()
        for w in sorted(nbr[v]):
            if w not in parent:
                parent[w]=v;queue.append(w)
    assert len(parent)==len(vertices), 'complex not connected'
    tree={tuple(sorted((v,p))) for v,p in parent.items() if p is not None}
    non_tree=sorted(set(edges)-tree)
    gen={e:i+1 for i,e in enumerate(non_tree)}
    def oriented_edge(a,b):
        v=gen.get(tuple(sorted((a,b))))
        return [] if v is None else [v if a<b else -v]
    words=[]
    for a,b,c in tris:
        w=oriented_edge(a,b)+oriented_edge(b,c)+oriented_edge(c,a)
        words.append(freely_reduce(w))
    gset=set(gen.values()); steps=[]
    while True:
        words=[freely_reduce(w) for w in words]
        possibilities=[]
        for i,w in enumerate(words):
            multiplicities=Counter(abs(x) for x in w)
            for g in sorted(multiplicities):
                if multiplicities[g]==1: possibilities.append((len(w),i,g))
        if not possibilities:break
        _,which,g=min(possibilities)
        relation=words.pop(which)
        j=next(i for i,x in enumerate(relation) if abs(x)==g)
        before=relation[:j];letter=relation[j];after=relation[j+1:]
        replacement=inverse(before)+inverse(after)
        if letter<0: replacement=inverse(replacement)
        # Algebraic validation: relation becomes freely trivial after replacement.
        substituted = freely_reduce(before + (replacement if letter>0 else inverse(replacement)) + after)
        assert substituted == []
        new=[]
        for w in words:
            out=[]
            for x in w:
                if abs(x)==g:
                    out += replacement if x>0 else inverse(replacement)
                else:out.append(x)
            new.append(freely_reduce(out))
        words=new
        gset.remove(g)
        steps.append((g,len(relation),len(replacement)))
    assert all(not w for w in words), 'uncancelled nontrivial attaching word'
    assert len(steps) + len(gset) == len(gen)
    return dict(vertices=len(vertices),edges=len(edges),triangles=len(tris),
                graph_cycle_rank=len(gen),cancelled_generators=len(steps),
                surviving_circle_generators=len(gset),
                null_attached_2cells=len(words),
                collapse_steps=steps,
                remaining_generators=sorted(gset))

def smith_invariants(faces):
    from sympy import Matrix, ZZ
    from sympy.matrices.normalforms import smith_normal_form
    by_dim={d:sorted((tuple(sorted(f)) for f in faces if len(f)==d+1)) for d in range(4)}
    data={}
    for d in (1,2,3):
        hi=by_dim[d];lo=by_dim[d-1]
        idx={t:i for i,t in enumerate(lo)}
        B=Matrix.zeros(len(lo),len(hi))
        for j,t in enumerate(hi):
            for k,v in enumerate(t):
                sub=t[:k]+t[k+1:]
                B[idx[sub],j] = (-1)**k
        diag=smith_normal_form(B,domain=ZZ)
        a=[abs(int(diag[i,i])) for i in range(min(B.rows,B.cols)) if diag[i,i]!=0]
        data[d]=Counter(a)
    return data

def main():
    adj=graph()
    full=faces_from_graph(range(N*N),adj)
    fullvec=[sum(len(f)==k for f in full) for k in range(10)]
    assert fullvec == [1,25,240,1124,2728,3368,1960,440,32,0],fullvec
    print('BOARD_F_VECTOR',fullvec)
    pieces=[]
    for color in (0,1):
        vertices=[i for i,(r,c) in enumerate(SQUARES) if (r+c)%2==color]
        part=faces_from_graph(vertices,adj)
        vec=[sum(len(f)==k for f in part) for k in range(6)]
        expected={0:[1,13,46,46,8,0],1:[1,12,38,32,4,0]}[color]
        assert vec==expected,(color,vec)
        print('COLOR',color,'F_VECTOR',vec)
        remain,pairs=free_tetra_collapses(part)
        p=presentation_certificate(remain)
        assert len(pairs)==vec[4]
        assert p['null_attached_2cells']=={0:5,1:3}[color]
        assert p['surviving_circle_generators']=={0:1,1:2}[color]
        assert p['graph_cycle_rank']=={0:34,1:27}[color]
        assert p['cancelled_generators']=={0:33,1:25}[color]
        print('COLOR',color,'TETRA_COLLAPSES',len(pairs),'FACET_PAIRS',pairs)
        print('COLOR',color,'PRESENTATION', {k:v for k,v in p.items() if k!='collapse_steps'})
        print('COLOR',color,'CELL_CANCELLATIONS',p['collapse_steps'])
        inv=smith_invariants(part)
        assert all(set(s)=={1} for s in inv.values()), inv
        ranks={d:sum(inv[d].values()) for d in inv}
        assert ranks==({1:12,2:33,3:8} if color==0 else {1:11,2:25,3:4}),ranks
        print('COLOR',color,'INTEGRAL_BOUNDARY_SMITH_UNIT_RANKS',ranks)
        pieces.append(p)
    # No bishop attacks squares of opposite parity; every union of valid
    # same-color placements is valid.  Consequently the complex is a join.
    c0,c1=pieces
    sphere_counts={a+b+1:s*t for a,s in [(1,c0['surviving_circle_generators']),(2,c0['null_attached_2cells'])]
                           for b,t in [(1,c1['surviving_circle_generators']),(2,c1['null_attached_2cells'])]}
    # Dimension four receives two summands; sum contributions explicitly.
    counts=Counter()
    for a,s in [(1,c0['surviving_circle_generators']),(2,c0['null_attached_2cells'])]:
       for b,t in [(1,c1['surviving_circle_generators']),(2,c1['null_attached_2cells'])]:
          counts[a+b+1] += s*t
    assert dict(counts)=={3:2,4:13,5:15},counts
    print('JOIN_SPHERE_COUNTS',dict(sorted(counts.items())))
    print('VERIFY_OK_BISHOP5_MIXED_WEDGE_HOMOTOPY')

if __name__=='__main__':main()
