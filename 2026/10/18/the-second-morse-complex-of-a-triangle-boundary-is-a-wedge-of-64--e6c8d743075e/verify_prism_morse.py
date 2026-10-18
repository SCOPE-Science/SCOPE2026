#!/usr/bin/env python3
"""Exact standard-library certificate for the Morse complex of C3 square K2.

Complex vertices are pairs (u,e) with u incident to e. A simplex is an
acyclic partial matching in the vertex-edge incidence Hasse graph.
"""
from collections import Counter, deque
from itertools import product

VERTICES = tuple(range(6))
EDGES = ((0,1),(1,2),(0,2),(3,4),(4,5),(3,5),(0,3),(1,4),(2,5))
# Incidence-vertex index 2*i selects (EDGES[i][0],EDGES[i]),
# incidence-vertex index 2*i+1 selects (EDGES[i][1],EDGES[i]).
ORDER = (8,17,9,2,10,1,5,12,14,13,0,7,3,6,4,16,15,11)

def enumerate_by_forest():
    faces = set()
    def rec(i, parents, used_sources, simplex):
        if i == len(EDGES):
            faces.add(simplex)
            return
        rec(i + 1, parents, used_sources, simplex)
        a,b = EDGES[i]
        def root(x):
            while parents[x] != x:
                x = parents[x]
            return x
        ra,rb = root(a),root(b)
        if ra == rb:
            return
        for j,u in enumerate((a,b)):
            if (used_sources >> u) & 1:
                continue
            newparents = list(parents)
            newparents[ra] = rb
            rec(i+1, newparents, used_sources | (1 << u), simplex | (1 << (2*i+j)))
    rec(0,list(VERTICES),0,0)
    return faces

def independent_validity_check(mask):
    """Second model: check incidence matching and directed cycles directly."""
    outgoing = {}
    chosen_edges = set()
    for j in range(2*len(EDGES)):
        if not (mask>>j)&1:continue
        edge_idx, side = divmod(j,2)
        u,v = EDGES[edge_idx]
        source,target = (u,v) if side==0 else (v,u)
        if source in outgoing or edge_idx in chosen_edges:
            return False
        outgoing[source] = target
        chosen_edges.add(edge_idx)
    for source in outgoing:
        seen = set()
        u=source
        while u in outgoing:
            if u in seen:return False
            seen.add(u)
            u=outgoing[u]
    return True

def lex_element_matching(faces):
    remaining=set(faces)
    paired={}
    for index in ORDER:
        bit=1<<index
        lows=sorted(f for f in remaining if f&bit==0 and (f|bit) in remaining)
        for low in lows:
            high=low|bit
            assert low in remaining and high in remaining
            remaining.remove(low)
            remaining.remove(high)
            paired[low]=high
            paired[high]=low
    return remaining,paired

def hasse_acyclic(faces,paired):
    """Reverse matched Hasse edges, then run Kahn's complete DAG test."""
    arcs={f:[] for f in faces}
    indeg={f:0 for f in faces}
    incidences=0
    for high in faces:
        x=high
        while x:
            bit=x & -x
            low=high^bit
            assert low in faces
            if paired.get(low)==high:
                frm,to=high,low
            else:
                frm,to=low,high
            arcs[frm].append(to)
            indeg[to]+=1
            incidences+=1
            x^=bit
    ready=deque(k for k,v in indeg.items() if v==0)
    processed=0
    while ready:
        v=ready.popleft();processed+=1
        for w in arcs[v]:
            indeg[w]-=1
            if indeg[w]==0:ready.append(w)
    assert processed==len(faces), ('directed Hasse cycle',processed,len(faces))
    return incidences

def gf2_boundary_rank(level, previous):
    rindex={face:j for j,face in enumerate(previous)}
    pivots={}
    for face in level:
        c=0
        x=face
        while x:
            bit=x&-x
            c ^= 1<<rindex[face^bit]
            x^=bit
        while c:
            pivot=c.bit_length()-1
            if pivot in pivots:c^=pivots[pivot]
            else:
                pivots[pivot]=c
                break
    return len(pivots)

def main():
    faces=enumerate_by_forest()
    assert len(faces)==1728
    # The unconstrained 9-edge 3-state assignment space has precisely 3^9 choices.
    alt={sum(1<<(2*i+(state-1)) for i,state in enumerate(states) if state)
         for states in product((0,1,2),repeat=len(EDGES))}
    assert len(alt)==3**len(EDGES)
    accepted={f for f in alt if independent_validity_check(f)}
    assert accepted==faces,('independent validity mismatch',len(accepted),len(faces))
    count=Counter(f.bit_count()-1 for f in faces)
    assert dict(count)=={-1:1,0:18,1:126,2:428,3:705,4:450},count
    critical,matching=lex_element_matching(faces)
    assert len(matching)==1664 and len(critical)==64
    assert Counter(f.bit_count()-1 for f in critical)=={4:64}
    assert 0 in matching and matching[0].bit_count()==1
    assert all(matching.get(matching[f])==f for f in matching)
    assert all((f^matching[f]).bit_count()==1 for f in matching)
    incidences=hasse_acyclic(faces,matching)
    levels=[[f for f in faces if f.bit_count()==k+1] for k in range(5)]
    rank=[None]+[gf2_boundary_rank(levels[k],levels[k-1]) for k in range(1,5)]
    betti={0:len(levels[0])-rank[1]-1}
    for k in range(1,4):betti[k]=len(levels[k])-rank[k]-rank[k+1]
    betti[4]=len(levels[4])-rank[4]
    assert betti=={0:0,1:0,2:0,3:0,4:64},betti
    assert sum(((-1) if d%2 else 1)*n for d,n in count.items())==64
    print('VERIFY_OK', 'augmented_faces',len(faces),'Hasse_incidences',incidences,
          'matched_pairs',len(matching)//2, 'critical_4',len(critical),
          'F2_boundary_ranks',rank[1:],'F2_reduced_betti',betti)

if __name__=='__main__':main()
