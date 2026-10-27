#!/usr/bin/env python3
"""Construct a compact complete set of distance labels for small derangement switch graphs."""
import json
from pathlib import Path
from itertools import permutations
from collections import deque,Counter

def ctype(p):
 seen=set(); lens=[]
 for i in range(len(p)):
  if i in seen:continue
  j=i;k=0
  while j not in seen:seen.add(j);j=p[j];k+=1
  lens.append(k)
 return tuple(sorted(lens,reverse=True))

def bfs(k,nbr):
 d=[-1]*len(nbr);d[k]=0;q=deque([k])
 while q:
  i=q.popleft()
  for j in nbr[i]:
   if d[j]<0:d[j]=d[i]+1;q.append(j)
 return d

cert={'schema_version':1,'description':'Exact distance labels indexed by lexicographically ordered fixed-point-free permutations on the integers from 0 to n-1. Each orbit source represents a conjugacy class.','sizes':{}}
for n in (4,5,6):
 P=[p for p in permutations(range(n)) if all(i!=p[i] for i in range(n))]; index={p:i for i,p in enumerate(P)}
 N=[]
 for p in P:
  neigh=[]
  for i in range(n):
   for j in range(i+1,n):
    if p[i]!=j and p[j]!=i:
     q=list(p);q[i],q[j]=q[j],q[i];neigh.append(index[tuple(q)])
  N.append(neigh)
 reps={}
 for i,p in enumerate(P):reps.setdefault(str(ctype(p)),i)
 entries=[]
 for cy,ix in sorted(reps.items()):
  d=bfs(ix,N)
  assert min(d)==0
  entries.append({'cycle_type':cy,'source':list(P[ix]),'distances':d})
 cert['sizes'][str(n)]={'vertices':len(P),'orbit_sources':entries}
with open(Path(__file__).with_name('orbit_distance_certificate.json'),'w',encoding='utf-8') as f:
 json.dump(cert,f,indent=2,sort_keys=True);f.write('\n')
print('CERT_GENERATED',sum(len(a['orbit_sources']) for a in cert['sizes'].values()))
