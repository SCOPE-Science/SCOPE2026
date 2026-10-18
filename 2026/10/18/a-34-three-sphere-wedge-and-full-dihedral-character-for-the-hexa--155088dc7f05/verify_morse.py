#!/usr/bin/env python3
"""Finite, exact acyclic-matching certificate checker for an explicit 12-vertex complex.
Run next to matching_pairs.json using standard Python 3.
"""
import json
from collections import Counter, deque
from pathlib import Path

N = 12
adj = [sum(1 << ((v+d) % N) for d in (-2,-1,1,2)) for v in range(N)]

def is_face(mask):
    return mask != 0 and all(((mask & adj[v]).bit_count() <= 1)
            for v in range(N) if mask & (1<<v))

faces = {mask for mask in range(1,1<<N) if is_face(mask)}
assert len(faces) == 521
assert [Counter(m.bit_count()-1 for m in faces)[j] for j in range(6)] == [12,66,172,207,60,4]
cert = json.loads(Path(__file__).with_name('matching_pairs.json').read_text(encoding='utf-8'))
assert cert['n_vertices'] == N
pairs = [tuple(p) for p in cert['pairs']]
critical = set(cert['critical'])
assert len(pairs) == 243 and len(critical) == 35
matched = set(); paired_edges = set()
for a,b in pairs:
    assert a in faces and b in faces and a != b and a & b == a and (b^a).bit_count()==1
    assert a not in matched and b not in matched
    matched.update((a,b));paired_edges.add((a,b))
assert faces-matched == critical
assert Counter(m.bit_count()-1 for m in critical) == {0:1,3:34}

# Complete Hasse graph, orient unmatched covers upward and matched covers downward.
# A directed cycle would be a forbidden closed gradient path.
indeg = {m:0 for m in faces}
out = {m:[] for m in faces}
num_covers = 0
for high in faces:
    for i in range(N):
        bit=1<<i
        if not (high & bit): continue
        low=high^bit
        if low == 0: continue
        assert low in faces
        u,v = (high,low) if (low,high) in paired_edges else (low,high)
        out[u].append(v);indeg[v]+=1;num_covers+=1
queue=deque(sorted(x for x in faces if indeg[x]==0))
processed = 0
while queue:
    u=queue.popleft(); processed+=1
    for v in out[u]:
        indeg[v]-=1
        if indeg[v]==0:queue.append(v)
assert processed == len(faces), (processed,len(faces))
assert num_covers == 1800, num_covers
print(json.dumps({'n_vertices':N,'faces':len(faces),'f_vector':[12,66,172,207,60,4],
 'matched_pairs':len(pairs),'critical_dimensions':{'0':1,'3':34},
 'hasse_covers':num_covers,'acyclic_dag_vertices':processed,
 'deduction':'one 0-cell and 34 3-cells yield a wedge of 34 three-spheres'},sort_keys=True))
