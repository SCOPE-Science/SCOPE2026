#!/usr/bin/env python3
"""Exact, dependency-free verification of five finite Rips Morse certificates."""
import json
from collections import Counter, defaultdict, deque
from pathlib import Path

EXPECTED_VECTORS = {
    8:(16,68,104,58,8),
    9:(18,81,117,63,9),
    10:(20,90,140,80,12),
    11:(22,99,143,77,11),
    12:(24,108,160,84,12),
}
EXPECTED_MORSE = {
    8:{0:1,2:1}, 9:{0:1,1:1}, 10:{0:1,2:1},
    11:{0:1,1:1}, 12:{0:1,2:3},
}
EXPECTED_RANKS = {
    8:(15,53,50,8),
    9:(17,63,54,9),
    10:(19,71,68,12),
    11:(21,77,66,11),
    12:(23,85,72,12),
}

def graph(n):
    adj=[set() for _ in range(2*n)]
    def add_edge(a,b):
        assert a!=b
        adj[a].add(b);adj[b].add(a)
    for i in range(n):
        add_edge(i,(i+1)%n)
        add_edge(i,n+i)
        add_edge(n+i,n+(i+2)%n)
    assert all(len(a)==3 for a in adj)
    return adj

def faces_at_radius_two(n):
    adj=graph(n)
    within=[]
    for s in range(2*n):
        dist={s:0};q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if v not in dist:
                    dist[v]=dist[u]+1;q.append(v)
        assert len(dist)==2*n
        within.append({v for v in range(2*n) if v!=s and dist[v]<=2})
    faces=set()
    def build(face,candidates):
        for i,v in enumerate(candidates):
            t=face+(v,)
            assert t not in faces
            faces.add(t)
            build(t,[w for w in candidates[i+1:] if w in within[v]])
    build((),list(range(2*n)))
    return faces

def rank_mod_two(small,big):
    loc={x:i for i,x in enumerate(small)}
    piv={}
    for t in big:
        column=0
        for j in range(len(t)):
            column ^= 1<<loc[t[:j]+t[j+1:]]
        while column:
            leading=column.bit_length()-1
            if leading in piv:
                column ^= piv[leading]
            else:
                piv[leading]=column
                break
    return len(piv)

def certify(n,rec):
    fs=faces_at_radius_two(n)
    groups={d:sorted(f for f in fs if len(f)==d+1) for d in range(5)}
    assert tuple(len(groups[d]) for d in range(5))==EXPECTED_VECTORS[n]
    assert sum(len(v) for v in groups.values())==len(fs)
    pairs=[(tuple(a),tuple(b)) for a,b in rec['pairs']]
    critical=[tuple(x) for x in rec['critical']]
    all_used=[]
    for a,b in pairs:
        assert a in fs and b in fs
        assert len(b)==len(a)+1
        assert a==tuple(v for v in b if v not in set(b)-set(a))
        assert len(set(b)-set(a))==1
        all_used.extend((a,b))
    all_used.extend(critical)
    assert len(all_used)==len(fs) and set(all_used)==fs
    assert len(set(all_used))==len(all_used)
    assert dict(Counter(len(f)-1 for f in critical))==EXPECTED_MORSE[n]
    # Directed Hasse diagram: reverse exactly the certified matched incidences.
    match=set(pairs)
    edges={f:[] for f in fs}
    indegree={f:0 for f in fs}
    for top in fs:
        if len(top)==1:continue
        for j in range(len(top)):
            low=top[:j]+top[j+1:]
            a,b=(low,top) if (low,top) in match else (top,low)
            edges[a].append(b)
            indegree[b]+=1
    queue=deque(f for f in fs if indegree[f]==0)
    seen=0
    while queue:
        a=queue.popleft();seen+=1
        for b in edges[a]:
            indegree[b]-=1
            if indegree[b]==0:queue.append(b)
    assert seen==len(fs), 'Matching is not acyclic'
    ranks=tuple(rank_mod_two(groups[d-1],groups[d]) for d in range(1,5))
    assert ranks==EXPECTED_RANKS[n]
    betti=tuple(len(groups[d])-(ranks[d-1] if d>0 else 0)-(ranks[d] if d<4 else 0) for d in range(5))
    assert betti[0]==1
    print('n=%d; f=%s; pairs=%d; critical=%s; GF2_boundary_ranks=%s; Hasse_acyclic=yes' %
          (n,EXPECTED_VECTORS[n],len(pairs),EXPECTED_MORSE[n],ranks))


def main():
    path=Path(__file__).with_name('MORSE_CERTIFICATE.json')
    data=json.loads(path.read_text(encoding='utf8'))
    assert data['scale']==2 and sorted(map(int,data['cases']))==list(range(8,13))
    for n in range(8,13):
        certify(n,data['cases'][str(n)])
    print('GP_SMALL_EXCEPTIONS_EXACT_CERTIFICATE_OK')
if __name__=='__main__':main()
