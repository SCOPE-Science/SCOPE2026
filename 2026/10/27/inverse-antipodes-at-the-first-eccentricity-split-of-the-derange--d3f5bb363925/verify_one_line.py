#!/usr/bin/env python3
"""Exhaustive restricted-swap derangement-graph distance certificate (Python standard library)."""
from itertools import permutations
from collections import Counter,deque
import hashlib,json
EXPECTED={
 4:{'v':9,'edges':12,'ecc':{3:9},'shell':{1:12,2:18,3:6}},
 5:{'v':44,'edges':120,'ecc':{4:44},'shell':{1:120,2:300,3:360,4:166}},
 6:{'v':265,'edges':1260,'ecc':{5:225,6:40},'shell':{1:1260,2:5310,3:11490,4:12100,5:4800,6:20}}
}
EDGE_SHA={4:'5bf2a38b24f98e8af0fd46d87ed90a7ee139f358c23145ac0822a05105c840ae',5:'da6f0ceed83acc47b4d0bce185bcbfc15d4ae1297b554051f4540f4a3bebffb9',6:'84d27cbc729c77f60bf228cc7375c850118e149b935b2de97d666126091d8c58'}
def ctype(p):
 seen=set(); lens=[]
 for start in range(len(p)):
  if start in seen:continue
  cur=start;length=0
  while cur not in seen:seen.add(cur);cur=p[cur];length+=1
  lens.append(length)
 return tuple(sorted(lens,reverse=True))
def inverse(p): return tuple(p.index(v) for v in range(len(p)))
def bfs(start,adj):
 dist=[-1]*len(adj);dist[start]=0;Q=deque([start])
 while Q:
  a=Q.popleft()
  for b in adj[a]:
   if dist[b]<0:dist[b]=dist[a]+1;Q.append(b)
 return dist
report={}
for n in (4,5,6):
 vertices=[p for p in permutations(range(n)) if all(p[i]!=i for i in range(n))]
 index={p:i for i,p in enumerate(vertices)}
 adj=[]
 for p in vertices:
  row=[]
  for a in range(n):
   for b in range(a+1,n):
    if p[a] != b and p[b] != a:
     q=list(p);q[a],q[b]=q[b],q[a]
     row.append(index[tuple(q)])
  adj.append(sorted(row))
 assert all(i in adj[j] for i,row in enumerate(adj) for j in row)
 edges=sorted((i,j) for i,row in enumerate(adj) for j in row if i<j)
 sha=hashlib.sha256(json.dumps(edges,separators=(',',':')).encode()).hexdigest()
 ecc=Counter();shell=Counter();pairs=[];orbit={};types=Counter()
 for i,p in enumerate(vertices):
  ty=ctype(p);types[ty]+=1
  d=bfs(i,adj)
  assert -1 not in d
  ecc[max(d)]+=1
  if ty not in orbit:orbit[ty]={'representative':list(p),'shells':[d.count(j) for j in range(max(d)+1)]}
  for j in range(i+1,len(vertices)):
   shell[d[j]]+=1
   if n==6 and d[j]==6:pairs.append((p,vertices[j]))
 e=EXPECTED[n]
 assert len(vertices)==e['v'] and len(edges)==e['edges'] and dict(ecc)==e['ecc'] and dict(shell)==e['shell'] and sha==EDGE_SHA[n]
 if n==6:
  assert len(pairs)==20 and all(ctype(p)==(3,3) and q==inverse(p) for p,q in pairs)
  assert dict(types)=={(2,2,2):15,(3,3):40,(4,2):90,(6,):120}
 report[str(n)]={'vertices':len(vertices),'edges':len(edges),'degree_distribution':dict(sorted(Counter(map(len,adj)).items())),'eccentricity_distribution':dict(sorted(ecc.items())),'unordered_distance_distribution':dict(sorted(shell.items())),'cycle_type_orbits':{str(k):v for k,v in sorted(orbit.items())},'edge_index_sha256':sha}
report['n6_diametral_pairs']=20
print(json.dumps(report,sort_keys=True,indent=2))
print('VERIFY_ONE_LINE_OK')
