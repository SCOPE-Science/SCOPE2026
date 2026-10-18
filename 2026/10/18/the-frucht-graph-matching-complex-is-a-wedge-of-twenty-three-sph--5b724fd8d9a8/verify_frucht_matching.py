#!/usr/bin/env python3
"""Exact finite simplicial and acyclic-matching certificate for the Frucht-graph matching complex."""
from collections import Counter, deque
from itertools import combinations

EDGES = ((0,1),(0,6),(0,7),(1,2),(1,7),(2,3),(2,8),(3,4),(3,9),
         (4,5),(4,9),(5,6),(5,10),(6,10),(7,11),(8,9),(8,11),(10,11))
ORDER = (15,11,1,2,7,17,8,16,3,4,9,5,0,6,14,13,10,12)

def construct_faces():
    faces=[]
    for mask in range(1,1 << len(EDGES)):
        occupied=0
        for i,(u,v) in enumerate(EDGES):
            if mask & (1<<i):
                if occupied & ((1<<u)|(1<<v)):break
                occupied |= (1<<u)|(1<<v)
        else:faces.append(mask)
    return faces

def main():
    assert len(EDGES)==18 and len(set(EDGES))==18
    assert Counter(v for e in EDGES for v in e)=={v:3 for v in range(12)}
    assert sorted(ORDER)==list(range(18))
    faces=construct_faces()
    all_faces=set(faces)
    fvec=tuple(sum(f.bit_count()==k for f in faces) for k in range(1,7))
    assert len(faces)==1025 and fvec==(18,117,333,397,152,8)
    unmatched=set(faces); pairs=[]
    for i in ORDER:
        stage=[]
        for f in sorted(unmatched):
            if not (f & (1<<i)) and (f|(1<<i)) in unmatched:
                stage.append((f,f|(1<<i)))
        for a,b in stage:
            assert a in unmatched and b in unmatched and a.bit_count()+1==b.bit_count()
            unmatched.remove(a);unmatched.remove(b)
        pairs.extend(stage)
    assert len(pairs)==502 and len(unmatched)==21
    critical=Counter(f.bit_count()-1 for f in unmatched)
    assert critical=={0:1,3:20},critical
    matched={frozenset((a,b)) for a,b in pairs}
    assert len(matched)==len(pairs)
    # All codimension-one simplicial incidences: matched upward, all others downward.
    adj={f:[] for f in faces}; indeg={f:0 for f in faces}; covers=0
    for f in faces:
        for i in range(18):
            if not f & (1<<i):continue
            low=f ^ (1<<i)
            if low==0:continue
            assert low in all_faces
            covers+=1
            if frozenset((low,f)) in matched:
                a,b=low,f  # matched cover is directed upward
            else:
                a,b=f,low # unmatched cover is directed downward
            adj[a].append(b);indeg[b]+=1
    q=deque(f for f in faces if indeg[f]==0);visited=0
    while q:
        f=q.popleft();visited+=1
        for t in adj[f]:
            indeg[t]-=1
            if indeg[t]==0:q.append(t)
    assert visited==len(faces), (visited,len(faces))
    assert sum((-1)**(f.bit_count()-1) for f in faces)==-19
    print('FACES',len(faces),'FVECTOR',fvec)
    print('MATCHED_PAIRS',len(pairs),'HASSE_COVERS',covers,'ACYCLIC_VISITED',visited)
    print('CRITICAL_VERTEX',next(f for f in unmatched if f.bit_count()==1))
    print('CRITICAL_3_CELLS',tuple(sorted(f for f in unmatched if f.bit_count()==4)))
    print('FRUCHT_MATCHING_HOMOTOPY_OK')
if __name__=='__main__':main()
