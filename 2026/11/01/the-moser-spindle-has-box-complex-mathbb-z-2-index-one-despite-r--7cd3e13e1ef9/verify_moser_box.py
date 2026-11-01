#!/usr/bin/env python3
"""Exact finite certificate for the equivariant Lovasz-complex collapse of a seven-vertex graph."""
from itertools import combinations
from collections import defaultdict, deque
import json

V = tuple(range(7))
EDGES = ((0,1),(0,2),(1,2),(1,3),(2,3),
         (0,4),(0,5),(4,5),(4,6),(5,6),(3,6))
adj={v:set() for v in V}
for a,b in EDGES:
    assert a < b and a in V and b in V
    adj[a].add(b);adj[b].add(a)

def CN(s):
    return frozenset.intersection(*(frozenset(adj[v]) for v in s)) if s else frozenset(V)

# Closed nonempty faces of the neighborhood complex.
closed = {CN(CN(S)) for k in range(1,8) for S in combinations(V,k) if CN(S)}
ordered = sorted(closed, key=lambda s:(len(s),tuple(sorted(s))))
assert len(ordered)==18
idof={s:i for i,s in enumerate(ordered)}
complement={i:idof[CN(s)] for i,s in enumerate(ordered)}
assert all(complement[complement[i]]==i and complement[i]!=i for i in complement)

chains_by_size = {1:{(i,) for i in range(len(ordered))}}
for k in (2,3,4):
    nxt={a+(j,) for a in chains_by_size[k-1] for j in range(len(ordered))
         if ordered[a[-1]] < ordered[j]}
    if not nxt:break
    chains_by_size[k]=nxt
assert [len(chains_by_size.get(k,[])) for k in (1,2,3,4)] == [18,38,16,0]

def tau(face):
    images=[complement[i] for i in face]
    return tuple(sorted(images,key=lambda k:(len(ordered[k]),tuple(sorted(ordered[k])))))

for k,cs in chains_by_size.items():
    assert all(tau(c) in cs and tau(tau(c))==c and tau(c)!=c for c in cs)
assert all(set(e)!=set(tau(e)) for e in chains_by_size[2])

tri=set(chains_by_size[3]);edges=set(chains_by_size[2])
pairs=[]
while tri:
    candidates=[]
    for e in sorted(edges):
        cofaces=[t for t in tri if set(e).issubset(t)]
        if len(cofaces)==1:
            candidates.append((e,cofaces[0]))
    for e,t in candidates:
        ee,tt=tau(e),tau(t)
        if ee==e or tt==t or ee not in edges or tt not in tri:continue
        if len([u for u in tri if set(ee).issubset(u)])==1:
            edges.remove(e);edges.remove(ee);tri.remove(t);tri.remove(tt)
            pairs.append((e,t,ee,tt))
            break
    else:
        raise AssertionError('Cannot complete equivariant free-orbit collapse')
assert len(pairs)==8 and not tri and len(edges)==22
assert all(tau(e) in edges for e in edges)
# Undirected graph connectedness, and no edge with an involution-invariant realization.
neighbor={i:set() for i in range(len(ordered))}
for a,b in edges:
    neighbor[a].add(b);neighbor[b].add(a)
seen={0};queue=deque([0])
while queue:
    u=queue.popleft()
    for v in neighbor[u]-seen:
        seen.add(v);queue.append(v)
assert len(seen)==18
# Exactly nine vertex orbits and eleven edge orbits in the quotient.
vertorbits={frozenset((i,complement[i])) for i in range(18)}
edgeorbits={frozenset((e,tau(e))) for e in edges}
assert len(vertorbits)==9 and len(edgeorbits)==11
# H_1 graph rank 22-18+1=5; quotient rank 11-9+1=3.
assert 22-18+1==5 and 11-9+1==3
# A direct exact coloring check, independent of geometric folklore.
def colorable(k):
    colors={}
    order=sorted(V,key=lambda v:-len(adj[v]))
    def rec(t):
        if t==len(V):return True
        v=order[t]
        for c in range(k):
            if all(colors.get(w)!=c for w in adj[v]):
                colors[v]=c
                if rec(t+1):return True
                colors.pop(v)
        return False
    return rec(0)
assert not colorable(3) and colorable(4)
if __name__=='__main__':
    cert={'vertices':list(V),'edges':list(map(list,EDGES)),
          'closed_sets':[sorted(s) for s in ordered],
          'involution':[complement[i] for i in range(18)],
          'equivariant_collapse_orbits':[
           {'edge':list(e),'triangle':list(t),'partner_edge':list(ee),'partner_triangle':list(tt)}
           for e,t,ee,tt in pairs],
          'initial_f_vector':[18,38,16], 'residual_f_vector':[18,22],
          'quotient_f_vector':[9,11], 'connected':True,
          'chromatic_number':4, 'box_index':1}
    with open('moser_collapse_certificate.json','w',encoding='utf8') as f:
        json.dump(cert,f,indent=2,ensure_ascii=False);f.write('\n')
    print('MOSER_BOX_INDEX_VERIFY_OK closed=18 chains=(18,38,16) orbit_collapses=8 residual=(18,22) quotient=(9,11) index=1 chi=4')
