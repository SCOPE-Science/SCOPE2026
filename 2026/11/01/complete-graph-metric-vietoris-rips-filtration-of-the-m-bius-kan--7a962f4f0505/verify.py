"""Exact, standard-library verification of a finite graph-metric Rips theorem.
Run: python verify.py (from the directory containing certificates/r2_matching.json).
"""
from __future__ import annotations
import collections
import itertools
import json
from pathlib import Path

N = 16

def edges():
    result=set()
    for i in range(8):
        for a,b in ((i,(i+1)%8),(i,8+i),(8+i,8+(i+3)%8)):
            result.add(tuple(sorted((a,b))))
    return sorted(result)

def graph_and_distances():
    ee=edges()
    assert len(ee)==24
    adj=[set() for _ in range(N)]
    for a,b in ee:
        adj[a].add(b);adj[b].add(a)
    assert all(len(x)==3 for x in adj)
    dist=[]
    for source in range(N):
        d=[-1]*N;d[source]=0
        q=collections.deque([source])
        while q:
            v=q.popleft()
            for w in sorted(adj[v]):
                if d[w]<0:d[w]=d[v]+1;q.append(w)
        assert all(x>=0 for x in d)
        dist.append(d)
    counts=collections.Counter(dist[i][j] for i in range(N) for j in range(i+1,N))
    assert counts=={1:24,2:48,3:40,4:8},counts
    return adj,dist

def rips_faces(dist,r):
    close=[sum(1<<j for j in range(N) if j!=i and dist[i][j]<=r) for i in range(N)]
    faces=set()
    for mask in range(1,1<<N):
        tail=mask;valid=True
        while tail:
            low=tail&-tail;i=low.bit_length()-1;tail-=low
            if tail&~close[i]:valid=False;break
        if valid:faces.add(mask)
    return faces

def subfaces(mask):
    remaining=mask
    while remaining:
        low=remaining&-remaining
        yield mask-low
        remaining-=low

def verify_morse(faces,cert):
    assert cert['graph']=='GP(8,3)'
    assert cert['vertex_labels']==[f'u{i}' for i in range(8)]+[f'v{i}' for i in range(8)]
    assert [sum(f.bit_count()==k for f in faces) for k in range(1,5)]==cert['face_counts']
    alive=set(faces);pairs=[];crit=[]
    for step in cert['steps']:
        if step['kind']=='pair':
            a=step['lower'];b=step['upper']
            assert a in alive and b in alive
            assert a&b==a and b.bit_count()==a.bit_count()+1
            assert not any(b!=z and b&z==b for z in alive)
            assert not any(a!=z and z!=b and a&z==a for z in alive)
            alive.remove(a);alive.remove(b);pairs.append((a,b))
        elif step['kind']=='critical':
            a=step['cell'];assert a in alive
            assert not any(a!=z and a&z==a for z in alive)
            alive.remove(a);crit.append(a)
        else:raise ValueError('Unknown certificate action')
        assert all((f&~(1<<i)) in alive for f in alive for i in range(N) if f&(1<<i) and f.bit_count()>1)
    assert not alive
    assert len(pairs)==118
    assert len(crit)==12
    assert collections.Counter(x.bit_count()-1 for x in crit)=={0:1,2:9,3:2}
    matched={ab for p in pairs for ab in p}
    assert len(matched)==2*len(pairs)
    assert set(crit).isdisjoint(matched)
    assert set(crit)|matched==faces
    # Independent combinatorial check of acyclicity using the original Hasse graph.
    # Matched cover incidences point upward, unmatched incidences downward.
    match=set(pairs)
    successors={f:[] for f in faces};indegree={f:0 for f in faces}
    for b in faces:
        if b.bit_count()==1:continue
        for a in subfaces(b):
            if (a,b) in match:src,dst=a,b
            else:src,dst=b,a
            successors[src].append(dst);indegree[dst]+=1
    q=collections.deque(f for f in faces if indegree[f]==0)
    n=0
    while q:
        v=q.popleft();n+=1
        for w in successors[v]:
            indegree[w]-=1
            if indegree[w]==0:q.append(w)
    assert n==len(faces),('gradient cycle',n,len(faces))
    return pairs,crit

def orientation_sign(seq):
    inversions=sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
    return -1 if inversions%2 else 1

def check_side_crosspolytope(part,dist,r2):
    assert len(part)==8
    antipodes=[(a,b) for a,b in itertools.combinations(part,2) if dist[a][b]==4]
    assert len(antipodes)==4
    assert sorted(x for p in antipodes for x in p)==sorted(part)
    assert all(dist[a][b]==2 for a,b in itertools.combinations(part,2) if (a,b) not in antipodes)
    sidefaces={f for f in r2 if all((f>>i)&1==0 for i in range(N) if i not in part)}
    assert [sum(f.bit_count()==k for f in sidefaces) for k in range(1,5)]==[8,24,32,16]
    chain={};dchain=collections.Counter()
    for picks in itertools.product([0,1],repeat=4):
        seq=[antipodes[i][picks[i]] for i in range(4)]
        simplex=sum(1<<i for i in seq)
        assert simplex in sidefaces
        coeff=(-1)**sum(p==0 for p in picks)*orientation_sign(seq)
        chain[simplex]=coeff
    assert len(chain)==16
    for t,c in chain.items():
        vertices=[i for i in range(N) if t>>i&1]
        for j,i in enumerate(vertices):
            dchain[t^(1<<i)]+=c*(-1)**j
    assert not any(dchain.values())
    return chain

def count_six_cycles(adj):
    cycles=set()
    for start in range(N):
        def walk(path):
            if len(path)==6:
                if start in adj[path[-1]]:
                    t=tuple(path)
                    rr=t[::-1]
                    shifts=[tuple(t[i:]+t[:i]) for i in range(6)]
                    shifts += [tuple(rr[i:]+rr[:i]) for i in range(6)]
                    cycles.add(min(shifts))
                return
            for w in adj[path[-1]]:
                if w not in path:walk(path+[w])
        walk([start])
    incidences=collections.Counter()
    for cyc in cycles:
        for a,b in zip(cyc,cyc[1:]+cyc[:1]):
            incidences[tuple(sorted((a,b)))]+=1
    assert len(cycles)==24
    assert set(incidences)==set(edges())
    assert set(incidences.values())=={6}
    return len(cycles)

def main():
    adj,dist=graph_and_distances()
    sixcycles=count_six_cycles(adj)
    bipartition=[];colors={0:0};q=collections.deque([0])
    while q:
        v=q.popleft()
        for w in adj[v]:
            if w in colors:assert colors[w]!=colors[v]
            else:colors[w]=1-colors[v];q.append(w)
    assert len(colors)==N
    parts=[sorted(i for i in range(N) if colors[i]==t) for t in [0,1]]
    assert [len(p) for p in parts]==[8,8]
    r1=rips_faces(dist,1);r2=rips_faces(dist,2);r3=rips_faces(dist,3)
    assert len(r1)==40 and [sum(f.bit_count()==k for f in r1) for k in [1,2]]==[16,24]
    assert len(r2)==248 and [sum(f.bit_count()==k for f in r2) for k in range(1,5)]==[16,72,112,48]
    assert len(r3)==6560
    assert [sum(f.bit_count()==k for f in r3) for k in range(1,9)]==[16,112,448,1120,1792,1792,1024,256]
    assert not any(f.bit_count()>8 for f in r3)
    far=[(i,j) for i in range(N) for j in range(i+1,N) if dist[i][j]==4]
    assert len(far)==8
    assert sorted(v for edge in far for v in edge)==list(range(N))
    with open(Path(__file__).parent/'certificates'/'r2_matching.json',encoding='utf8') as fh:
        cert=json.load(fh)
    pairs,crit=verify_morse(r2,cert)
    c1=check_side_crosspolytope(parts[0],dist,r2)
    c2=check_side_crosspolytope(parts[1],dist,r2)
    assert set(c1).isdisjoint(set(c2))
    # Both are nonzero integral 3-cycles. As r2 is three-dimensional,
    # there are no 4-boundaries. Together with two critical 3-cells,
    # these show that H_3 has rank exactly two. Primitive coefficients
    # on disjoint pure tetrahedra show that these cycles form a Z-basis.
    assert all(f.bit_count()<=4 for f in r2)
    print('GRAPH vertices=16 edges=24 distances={1:24,2:48,3:40,4:8}')
    print('SIX_CYCLES count=24 each_edge_in=6')
    print('RIPS_1 faces=40 f=(16,24) cycle_rank=9')
    print('RIPS_2 faces=248 f=(16,72,112,48)')
    print('MORSE_2 pairs=118 critical={0:1,2:9,3:2} acyclic=True')
    print('CANONICAL_3_CYCLES bipartition=(8,8) 16_top_facets_each primitive=True')
    print('RIPS_3 faces=6560 f=(16,112,448,1120,1792,1792,1024,256) crosspolytope_S7=True')
    print('RIPS_4 simplex_15=True')
    print('VERIFY_OK')

if __name__=='__main__':main()
