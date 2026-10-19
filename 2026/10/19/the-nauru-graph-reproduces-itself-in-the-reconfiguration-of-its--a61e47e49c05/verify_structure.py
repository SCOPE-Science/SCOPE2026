#!/usr/bin/env python3
"""Independent finite verification of the Nauru strong-resolving graph."""
from collections import Counter,deque
import json,hashlib

N=24
edges=set()
for i in range(12):
    for a,b in ((i,(i+1)%12),(i,12+i),(12+i,12+(i+5)%12)):
        edges.add(tuple(sorted((a,b))))
neigh=[set() for _ in range(N)]
for a,b in edges:
    neigh[a].add(b);neigh[b].add(a)
assert len(edges)==36 and all(len(z)==3 for z in neigh)

def bfs(source):
    ds=[-1]*N;ds[source]=0;q=deque([source])
    while q:
        u=q.popleft()
        for v in neigh[u]:
            if ds[v]<0: ds[v]=ds[u]+1;q.append(v)
    return ds
D=[bfs(v) for v in range(N)]
assert all(max(ds)==4 for ds in D)
assert all(tuple(Counter(ds)[i] for i in range(5))==(1,3,6,9,5) for ds in D)
MMD={(u,v)for u in range(N)for v in range(u+1,N)
     if all(D[w][v]<=D[u][v] for w in neigh[u])
     and all(D[w][u]<=D[u][v] for w in neigh[v])}
assert len(MMD)==60
assert MMD=={(u,v)for u in range(N)for v in range(u+1,N)if D[u][v]==4}
rows0=((0,4,8),(2,6,10),(13,17,21),(15,19,23))
cols0=((0,6,15,21),(2,8,17,23),(4,10,13,19))
rows1=tuple(tuple((u+1)%12 if u<12 else 12+(u-12+1)%12 for u in row) for row in rows0)
cols1=tuple(tuple((u+1)%12 if u<12 else 12+(u-12+1)%12 for u in col) for col in cols0)
expected=set()
for rows,cols in ((rows0,cols0),(rows1,cols1)):
    assert len(set().union(*[set(x) for x in rows]))==12
    assert len(set().union(*[set(x) for x in cols]))==12
    assert all(len(set(row)&set(col))==1 for row in rows for col in cols)
    for cls in list(rows)+list(cols):
        for a in cls:
            for b in cls:
                if a<b:expected.add((a,b))
assert expected==MMD

cert={"graph":"GP(12,5)","vertex_convention":"0..11=u_i,12..23=v_i", "graph_edges":[list(x)for x in sorted(edges)],
      "mmd_edges":[list(x)for x in sorted(MMD)],
      "rook_components":[{"rows":[list(r)for r in rows],"columns":[list(c)for c in cols]}
                         for rows,cols in ((rows0,cols0),(rows1,cols1))],
      "distance_profile":[1,3,6,9,5]}
# Extra certificate will be completed by separate enumeration of bases in verify_reconfiguration.py.
with open('structural_certificate.json','w',encoding='utf8')as f:
    json.dump(cert,f,sort_keys=True,separators=(',',':'));f.write('\n')
print('STRUCTURE_OK: 24 vertices, 36 edges; graph diameter 4 and profile (1,3,6,9,5).')
print('MMD_OK: all 60 mutually maximally distant pairs are precisely the diameter-4 pairs.')
print('ROOK_OK: strong resolving graph is two disjoint K4 Cartesian K3 graphs.')
print('STRUCTURE_CERT_SHA256:',hashlib.sha256(open('structural_certificate.json','rb').read()).hexdigest())
