#!/usr/bin/env python3
"""Exact integral Morse certificate for the ordinary matching complex of Mycielski(C5)."""
import itertools
import collections
from functools import lru_cache

def graph_edges():
    # 0..4 original C5; 5..9 clones; 10 universal clone apex.
    e=set()
    for i in range(5):
        e.add(tuple(sorted((i,(i+1)%5))))
        for j in ((i-1)%5,(i+1)%5):
            e.add(tuple(sorted((i+5,j))))
        e.add((i+5,10))
    return tuple(sorted(e))

def determinant(A):
    from math import prod
    if not A:return 1
    total=0
    for perm in itertools.permutations(range(len(A))):
        inv=sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))
        total+=(-1 if inv%2 else 1)*prod(A[i][perm[i]] for i in range(len(A)))
    return total

def certificate():
    E=graph_edges()
    assert len(E)==20 and len({i for e in E for i in e})==11
    masks=[(1<<u)|(1<<v) for u,v in E]
    faces_by_size={r:[] for r in range(1,6)}
    for r in range(1,6):
        for face in itertools.combinations(range(20),r):
            bits=0
            for i in face:
                if bits & masks[i]:break
                bits |= masks[i]
            else:faces_by_size[r].append(face)
    assert [len(faces_by_size[r]) for r in range(1,6)]==[20,135,365,360,87]
    F={f for fs in faces_by_size.values() for f in fs}
    remain=set(F)
    pairs={}
    # Repeated element matchings; the DAG verification below checks global acyclicity.
    for v in range(20):
        eligible=sorted((s for s in remain if v not in s),key=lambda z:(len(z),z))
        for s in eligible:
            t=tuple(sorted(s+(v,)))
            if s in remain and t in remain:
                remain.remove(s);remain.remove(t);pairs[s]=t
    assert len(pairs)==466 and collections.Counter(len(s)-1 for s in remain)=={0:1,2:5,3:29}
    # Complete oriented Hasse incidence graph: unmatched faces go downward; paired go upward.
    allfaces=[()]+[f for r in range(1,6) for f in faces_by_size[r]]
    ids={s:i for i,s in enumerate(allfaces)}
    out=[[] for _ in allfaces]; indeg=[0]*len(allfaces); incidence_count=0
    for t in F:
        for k in range(len(t)):
            s=t[:k]+t[k+1:]
            a,b=(ids[s],ids[t]) if pairs.get(s)==t else (ids[t],ids[s])
            out[a].append(b); indeg[b]+=1;incidence_count+=1
    assert incidence_count==3260
    from heapq import heappop,heappush
    queue=[]
    for i,d in enumerate(indeg):
        if d==0:heappush(queue,i)
    visit=0
    while queue:
        i=heappop(queue);visit+=1
        for j in out[i]:
            indeg[j]-=1
            if indeg[j]==0:heappush(queue,j)
    assert visit==len(allfaces)==968, f'cyclic orientation, visited {visit}'
    # Algebraic discrete Morse cancellation, signed simplex orientation by sorted indices.
    # A paired lower cell s is eliminated using the cellular relation from boundary(pairs[s]);
    # an upper cell of a pair one rank below projects to 0 in this rank.
    paired_upper={t:s for s,t in pairs.items()}
    @lru_cache(None)
    def project(s):
        if s in remain:return {s:1}
        if s in paired_upper:return {}
        assert s in pairs
        t=pairs[s]
        missing=next(i for i,v in enumerate(t) if v not in s)
        epsilon=(-1)**missing
        ans=collections.Counter()
        for j in range(len(t)):
            v=t[:j]+t[j+1:]
            if v==s:continue
            for w,c in project(v).items():ans[w] -= epsilon*((-1)**j)*c
        return {w:c for w,c in ans.items() if c}
    lower=sorted(f for f in remain if len(f)==3)
    upper=sorted(f for f in remain if len(f)==4)
    B=[]
    for s in lower:B.append([])
    for t in upper:
        d=collections.Counter()
        for j in range(len(t)):
            f=t[:j]+t[j+1:]
            for s,c in project(f).items():d[s]+=(-1)**j*c
        for i,s in enumerate(lower):B[i].append(d[s])
    minor_cols=(2,3,4,12,18)
    det=determinant([[row[j] for j in minor_cols] for row in B])
    assert det==-1,det
    assert len(B)==5 and all(len(row)==29 for row in B)
    assert set(c for row in B for c in row)<=set(range(-2,3))
    print('graph n,m:',11,len(E))
    print('simplex face counts by dimension:',[len(faces_by_size[r]) for r in range(1,6)])
    print('acyclic oriented Hasse:',visit,'faces (including empty),',incidence_count,'incidences')
    print('matching pairs:',len(pairs),'critical dimensions:',dict(collections.Counter(len(s)-1 for s in remain)))
    print('signed critical boundary dimensions:',len(B),'x',len(B[0]))
    print('unit minor columns:',minor_cols,'determinant:',det)
    print('homotopy type: wedge of 24 three-spheres')
    return E, B

if __name__=='__main__':certificate()
