#!/usr/bin/env python3
"""Recompute an integral Morse certificate and a cyclic Lefschetz character.

No data files or third-party modules are required; Python >=3.9.
"""
from array import array
from collections import Counter, deque
from itertools import combinations

N = 20
LIMIT = 1 << N

def make_graph():
    edges = set()
    for i in range(10):
        edges.add(tuple(sorted((i, (i+1) % 10))))
        edges.add((i, 10+i))
        edges.add(tuple(sorted((10+i, 10+(i+3) % 10))))
    assert len(edges)==30
    return edges

def closed_masks(edges):
    neighborhood=[1<<i for i in range(N)]
    for a,b in edges:
        neighborhood[a]|=1<<b
        neighborhood[b]|=1<<a
    assert all(x.bit_count()==4 for x in neighborhood)
    return neighborhood

def enumerated_faces(neighborhood):
    # This recurrence is exact: a subset is a face iff it contains no closed neighborhood.
    face=bytearray(LIMIT)
    face[0]=1
    for m in range(1,LIMIT):
        low=m&-m
        if face[m^low]:
            face[m]=int(not any((m&b)==b for b in neighborhood))
    return face

def build_matching(face):
    mate=array('i',[-1])*LIMIT
    counts=[]
    for v in range(N):
        bit=1<<v
        hits=0
        for m in range(1,LIMIT):
            upper=m|bit
            if not (m&bit) and face[m] and face[upper] and mate[m]==-1 and mate[upper]==-1:
                mate[m]=upper
                mate[upper]=m
                hits+=1
        counts.append(hits)
    return mate,counts

def acyclicity(face,mate):
    # Orient every Hasse arrow down, except matched arrows, which point up.
    indeg=array('i',[0])*LIMIT
    arrows=0
    for upper in range(1,LIMIT):
        if not face[upper]: continue
        bits=upper
        while bits:
            b=bits&-bits; bits^=b
            lower=upper^b
            if lower==0: continue
            assert face[lower]
            if mate[lower]==upper: indeg[upper]+=1
            else: indeg[lower]+=1
            arrows+=1
    todo=deque(m for m in range(1,LIMIT) if face[m] and indeg[m]==0)
    processed=0
    while todo:
        m=todo.popleft();processed+=1
        # The only upward outgoing arrow, if any, is to its matched coface.
        mate_m=mate[m]
        if mate_m>m:
            indeg[mate_m]-=1
            if indeg[mate_m]==0: todo.append(mate_m)
        # All nonmatched codimension-one face arrows point downward.
        bits=m
        while bits:
            b=bits&-bits;bits^=b
            low=m^b
            if low and mate[low]!=m:
                indeg[low]-=1
                if indeg[low]==0:todo.append(low)
    return processed,arrows

def perm_rot(t):
    return [((i+t)%10 if i<10 else 10+((i-10+t)%10)) for i in range(N)]

def sign_of_permutation_on_subset(p,m):
    images=[p[i] for i in range(N) if m&(1<<i)]
    inv=sum(images[i]>images[j] for i in range(len(images)) for j in range(i+1,len(images)))
    return 1 if inv%2==0 else -1

def trace_rotation(t,face):
    p=perm_rot(t)
    # A fixed simplex is a union of permutation orbits; enumerate only those.
    unvisited=set(range(N));orbits=[]
    while unvisited:
        i=min(unvisited);j=i;block=0
        while j in unvisited:
            unvisited.remove(j)
            block|=1<<j
            j=p[j]
        assert j==i
        orbits.append(block)
    lef=0;fixed_count=0
    for v in range(1,1<<len(orbits)):
        m=0
        for j,b in enumerate(orbits):
            if v>>j&1:m|=b
        if face[m]:
            fixed_count+=1
            lef += ((-1)**(m.bit_count()-1))*sign_of_permutation_on_subset(p,m)
    # Reduced Lefschetz number = nonempty alternating chain trace - 1.
    # Only reduced homology dimension 9 survives, so -tr_H9 = lef-1.
    return 1-lef,fixed_count

def independent_model_fvector():
    # Independent construction: canonical bipartite double cover of Petersen KG(5,2).
    two_subsets=list(combinations(range(5),2))
    edge_set=set()
    for i,a in enumerate(two_subsets):
        for j,b in enumerate(two_subsets):
            if not set(a).intersection(b):edge_set.add(tuple(sorted((i,10+j))))
    assert len(edge_set)==30
    iso=[0,17,6,11,9,10,7,16,1,19,18,3,12,5,14,8,13,2,15,4]
    transported={tuple(sorted((iso[a],iso[b]))) for a,b in make_graph()}
    assert edge_set==transported, 'Graph models not isomorphic under explicit vertex map'
    closed=closed_masks(edge_set)
    faces=enumerated_faces(closed)
    vec=Counter(m.bit_count()-1 for m in range(1,LIMIT) if faces[m])
    return vec

def main():
    faces=enumerated_faces(closed_masks(make_graph()))
    fvec=Counter(m.bit_count()-1 for m in range(1,LIMIT) if faces[m])
    total=sum(fvec.values())
    assert total==434220,(total, fvec)
    assert fvec==independent_model_fvector()
    mate,counts=build_matching(faces)
    assert all(mate[m]>=0 and mate[mate[m]]==m for m in range(1,LIMIT) if faces[m] and mate[m]>=0)
    assert sum(counts)==217103
    critical=Counter(m.bit_count()-1 for m in range(1,LIMIT) if faces[m] and mate[m]<0)
    assert critical==Counter({0:1,9:13}),critical
    processed,arrows=acyclicity(faces,mate)
    assert processed==total,('Directed Hasse graph contains a cycle',processed,total)
    char=[trace_rotation(k,faces)[0] for k in range(10)]
    assert char==[13,-1,3,-1,3,-11,3,-1,3,-1],char
    assert sum(char)==10 # invariant dimension one by character averaging
    print('GRAPH VERTICES: 20; EDGES: 30')
    print('NONEMPTY FACES:',total)
    print('F VECTOR:',','.join(str(fvec[k]) for k in range(max(fvec)+1)))
    print('MATCHING PAIRS:',sum(counts))
    print('PAIRS BY PIVOT:',counts)
    print('CRITICAL CELLS:',sorted(critical.items()))
    print('HASSE INCIDENCES:',arrows,'ACYCLIC NODES VISITED:',processed)
    print('C10 H9 TRACES:',char)
    print('RATIONAL MODULE: trivial(1) + sign(4) + cyclotomic10(2)')
    print('INDEPENDENT PETERSEN DOUBLE-COVER F-VECTOR: PASS')
    print('ALL ASSERTIONS PASSED')
if __name__=='__main__':main()
