#!/usr/bin/env python3
"""Verify finite shortest-path-distance certificates using local edge and predecessor conditions."""
import json,sys
from itertools import permutations
from collections import Counter
path=sys.argv[1] if len(sys.argv)>1 else 'orbit_distance_certificate.json'
with open(path,encoding='utf-8') as f:cert=json.load(f)
assert cert['schema_version']==1
summary={}
for n in (4,5,6):
 P=[p for p in permutations(range(n)) if all(i!=p[i] for i in range(n))]
 ind={p:i for i,p in enumerate(P)}
 # Build the bipartite matching switch graph from four-vertex alternations.
 E=set();N=[set() for p in P]
 for u,p in enumerate(P):
  for a in range(n):
   for b in range(a+1,n):
    if a==p[b] or b==p[a]:continue
    q=list(p);q[a],q[b]=q[b],q[a];v=ind[tuple(q)]
    N[u].add(v);N[v].add(u);E.add(tuple(sorted((u,v))))
 entry=cert['sizes'][str(n)];assert entry['vertices']==len(P)
 eccentricity=Counter();types=set();total=0;hist=Counter()
 for obj in entry['orbit_sources']:
  r=ind[tuple(obj['source'])]; d=obj['distances']; assert len(d)==len(P) and d[r]==0 and all(x>=0 for x in d)
  # Certified lower bound: d changes by at most 1 across every edge.
  assert all(abs(d[u]-d[v])<=1 for u,v in E)
  # Certified upper bound: each non-source vertex descends along an edge.
  assert all(any(d[v]==d[u]-1 for v in N[u]) for u in range(len(P)) if u!=r)
  # Together, the two local tests force exact graph distance from r to every vertex.
  eccentricity[max(d)]+=1;total+=1;hist[str(obj['cycle_type'])]=[d.count(k) for k in range(max(d)+1)]
 assert total=={4:2,5:2,6:4}[n]
 summary[str(n)]={'vertices':len(P),'edges':len(E),'checked_orbit_sources':total,'representative_eccentricities':dict(sorted(eccentricity.items())),'shells_by_cycle_type':hist}
print(json.dumps(summary,indent=2,sort_keys=True))
print('VERIFY_CERTIFICATE_OK')
