#!/usr/bin/env python3
"""Independent exact-cover and alternating-four-cycle graph metric enumeration."""
from collections import Counter,deque
import json

def derangement_matchings(n):
 """Recursively enumerate perfect matchings in K_(n,n) after its diagonal is removed."""
 result=[]
 def rec(row,free,matching):
  if row==n:result.append(tuple(matching));return
  for col in sorted(free):
   if row!=col:rec(row+1,free-{col},matching+[col])
 rec(0,set(range(n)),[])
 return result

def graph(matching_list):
 index={p:i for i,p in enumerate(matching_list)}; n=len(matching_list[0]);graph=[]
 for p in matching_list:
  neigh=set()
  for a in range(n):
   for b in range(a+1,n):
    # Replacing the two matching edges by the other matching on their 4 endpoints.
    if p[a]!=b and p[b]!=a:
     changed=list(p);changed[a]=p[b];changed[b]=p[a]
     neigh.add(index[tuple(changed)])
  graph.append(sorted(neigh))
 return graph

def bfs(start,adj):
 d={start:0};Q=deque([start]);prev={start:None}
 while Q:
  node=Q.popleft()
  for nb in adj[node]:
   if nb not in d:d[nb]=d[node]+1;prev[nb]=node;Q.append(nb)
 return d,prev
EXPECTED={4:(9,12,3,3),5:(44,120,4,4),6:(265,1260,5,6)}
summary={}
for n in (4,5,6):
 p=derangement_matchings(n);E=graph(p)
 v=len(p);edges=sum(map(len,E))//2
 all_ecc=Counter();paths=Counter();all_pairs=[]
 for k in range(v):
  D,_=bfs(k,E); assert len(D)==v
  all_ecc[max(D.values())]+=1
  for j in range(k+1,v):
   paths[D[j]]+=1
   if n==6 and D[j]==6:all_pairs.append((p[k],p[j]))
 assert (v,edges,min(all_ecc),max(all_ecc))==EXPECTED[n]
 if n==6:
  assert all_ecc=={5:225,6:40}
  assert paths=={1:1260,2:5310,3:11490,4:12100,5:4800,6:20}
  assert len(all_pairs)==20 and all(tuple(x.index(i) for i in range(n))==y for x,y in all_pairs)
 summary[str(n)]={'vertices':v,'edges':edges,'eccentricities':dict(sorted(all_ecc.items())),'distance_pairs':dict(sorted(paths.items()))}
# Construct one explicit exact length-six path from a pair of inverse double-3-cycles.
n=6;P=derangement_matchings(n);N=graph(P);index={p:i for i,p in enumerate(P)}
start=(1,2,0,4,5,3);end=(2,0,1,5,3,4)
D,prev=bfs(index[start],N);assert D[index[end]]==6
path=[];cur=index[end]
while cur is not None:path.append(P[cur]);cur=prev[cur]
path.reverse();assert len(path)==7
summary['witness_length_6_path']=[list(p) for p in path]
print(json.dumps(summary,sort_keys=True,indent=2))
print('VERIFY_MATCHINGS_OK')
