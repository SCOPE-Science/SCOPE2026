#!/usr/bin/env python3
"""Replay an exact acyclic Morse certificate and integral CW boundary.

Graph: K_2 joined to three independent vertices; every edge is bidirected.
No external scientific data is required.
"""
import json
from collections import Counter,deque
from pathlib import Path

HERE=Path(__file__).resolve().parent
ARCS=[(0,1),(1,0)]
for i in (2,3,4):
    ARCS.extend([(0,i),(i,0),(1,i),(i,1)])


def admissible(mask):
    indeg=[0]*5;outdeg=[0]*5;succ={}
    for j,(u,v) in enumerate(ARCS):
        if not mask>>j&1:continue
        indeg[v]+=1;outdeg[u]+=1
        if indeg[v]>1 or outdeg[u]>1:return False
        succ[u]=v
    for u in succ:
        x=u;seen=set()
        while x in succ:
            if x in seen:return False
            seen.add(x);x=succ[x]
    return True


def faces():
    return [m for m in range(1,1<<len(ARCS)) if admissible(m)]


def canonical_matching(fs):
    left=set(fs);pairs=[]
    order=[j for j,(u,v) in enumerate(ARCS) if u>=2]+[j for j,(u,v) in enumerate(ARCS) if u<2]
    for j in order:
        bit=1<<j
        for a in sorted(left):
            if a&bit:continue
            b=a|bit
            if b in left:
                left.remove(a);left.remove(b);pairs.append([a,b])
    return pairs,sorted(left),order


def incidence(fs,pairs):
    idx={f:i for i,f in enumerate(fs)}
    matched={tuple(p) for p in pairs}
    forward=[[] for _ in fs];indeg=[0]*len(fs);covers=0
    for b in fs:
        for j in range(len(ARCS)):
            if not (b>>j)&1:continue
            a=b^(1<<j)
            if a==0:continue
            if (a,b) in matched:x,y=b,a
            else:x,y=a,b
            forward[idx[x]].append(idx[y]);indeg[idx[y]]+=1;covers+=1
    Q=deque(k for k,v in enumerate(indeg) if v==0)
    count=0
    while Q:
        i=Q.popleft();count+=1
        for j in forward[i]:
            indeg[j]-=1
            if indeg[j]==0:Q.append(j)
    assert count==len(fs), ('Morse matching cyclic',count,len(fs))
    return covers


def signed_boundary(mask):
    bits=[j for j in range(len(ARCS)) if mask>>j&1]
    return {mask^(1<<j):1 if i%2==0 else -1
            for i,j in enumerate(bits) if mask^(1<<j)}


def integer_cancel(fs,pairs):
    D={m:signed_boundary(m) for m in fs};alive=set(fs);unit_pivots=[]
    for a,b in pairs:
        assert a in alive and b in alive
        pivot=D[b].get(a,0)
        assert abs(pivot)==1,(a,b,pivot)
        unit_pivots.append(int(pivot))
        for x in alive-{a,b}:
            t=D[x].get(a,0)
            if not t:continue
            t*=pivot
            for y,v in D[b].items():
                z=D[x].get(y,0)-t*v
                if z:D[x][y]=z
                else:D[x].pop(y,None)
        alive.remove(a);alive.remove(b)
        del D[a];del D[b]
        for x in alive:
            D[x].pop(a,None);D[x].pop(b,None)
    for x in alive:
        twice={}
        for y,c in D[x].items():
            for z,v in D[y].items():twice[z]=twice.get(z,0)+c*v
        assert not any(twice.values()), ('boundary squared',x)
    return {str(x):D[x] for x in sorted(alive)},Counter(unit_pivots)


def run():
    fs=faces()
    assert len(fs)==140
    f_vector=[sum(x.bit_count()==k for x in fs) for k in range(1,5)]
    assert f_vector==[14,54,60,12]
    cert=json.loads((HERE/'morse_certificate.json').read_text(encoding='utf8'))
    pairs,crit,order=canonical_matching(fs)
    assert cert['arcs']==[list(x) for x in ARCS]
    assert cert['pairs']==pairs
    assert cert['critical_masks']==crit
    assert cert['toggle_order']==order
    assert len(pairs)==65
    assert Counter(x.bit_count()-1 for x in crit)=={0:1,1:1,2:8}
    assert set(fs)==set(crit)|{x for p in pairs for x in p}
    covers=incidence(fs,pairs)
    D,pivot_counts=integer_cancel(fs,pairs)
    onecells=[x for x in crit if x.bit_count()==2]
    twocells=[x for x in crit if x.bit_count()==3]
    assert len(onecells)==1
    c=onecells[0]
    assert not D[str(c)]
    degree=[int(D[str(x)].get(c,0)) for x in twocells]
    assert sorted(degree)==[-2,-2]+[0]*6
    print(json.dumps({'f_vector':f_vector,'face_poset_cover_relations':covers,
         'acyclic_pairs':len(pairs),'critical_dimensions':{'0':1,'1':1,'2':8},
         'integer_pivot_counts':dict(pivot_counts),'attaching_degrees':degree,
         'homotopy':'RP^2 wedge 7 copies of S^2'},sort_keys=True))

if __name__=='__main__':run()
