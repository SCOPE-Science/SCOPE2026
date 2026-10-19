#!/usr/bin/env python3
"""Check explicit Hamilton paths, vertex transitivity and the unique obstruction."""
import json
from itertools import combinations
from collections import deque
from pathlib import Path

ROOT=Path(__file__).resolve().parent
NAMES=('Heawood','Mobius-Kantor','Pappus','Desargues')

def expected_edges(name):
 if name=='Heawood':
  N=14;E=[((j+k)%7,j+7) for j in range(7) for k in (0,1,3)]
 elif name=='Pappus':
  N=18;E=[(x*3+y,9+3*m+(y-m*x)%3) for x in range(3) for y in range(3) for m in range(3)]
 else:
  t,s={'Mobius-Kantor':(8,3),'Desargues':(10,3)}[name]
  N=2*t;E=[]
  for i in range(t):E.extend([(i,(i+1)%t),(i,t+i),(t+i,t+(i+s)%t)])
 return N,{tuple(sorted(e)) for e in E}

def graph_dist(A,start):
 d=[-1]*len(A);d[start]=0;q=deque([start])
 while q:
  u=q.popleft()
  for v in A[u]:
   if d[v]<0:d[v]=d[u]+1;q.append(v)
 return d

def check_path(seq,available,st,en,A):
 assert seq and seq[0]==st and seq[-1]==en
 assert len(seq)==len(available)==len(set(seq)) and set(seq)==available
 assert all(seq[i+1] in A[seq[i]] for i in range(len(seq)-1))

def complement_obstruction(A):
 """A path from 10 to 14 in G-0 would leave an excluded-edge pattern.
    Forced path edges at 1,7,8 mean the excluded edges lie in G-N[0].
    Every such edge pattern gives two cycles/path components, never one path.
 """
 n=len(A);X=set(range(n))-{0,1,7,8}
 E=[(u,v) for u in X for v in A[u] if u<v and v in X]
 needed={u:(2 if u in (10,14) else 1) for u in X}
 candidates=0
 for bits in range(1<<len(E)):
  S=[edge for i,edge in enumerate(E) if bits>>i&1]
  if any(sum(u in edge for edge in S)!=needed[u] for u in X):continue
  candidates+=1
  adjacency=[set(neighbors) for neighbors in A]
  for w in adjacency[0]:adjacency[w].remove(0)
  adjacency[0].clear()
  for u,v in S:adjacency[u].remove(v);adjacency[v].remove(u)
  seen={10};q=[10]
  for u in q:
   for v in adjacency[u]:
    if v not in seen:seen.add(v);q.append(v)
  assert len(seen)<n-1,('false obstruction',S)
 assert candidates==6, candidates
 return candidates

def main():
 C=json.loads((ROOT/'witness_certificate.json').read_text(encoding='utf8'))
 assert C['schema_version']==1 and set(C['objects'])==set(NAMES)
 for name in NAMES:
  G=C['objects'][name]; A=[set(row) for row in G['adjacency']]
  n,E=expected_edges(name)
  assert len(A)==n
  assert {tuple(sorted((u,v))) for u in range(n) for v in A[u]}==E
  assert all(u in A[v] for v in range(n) for u in A[v])
  assert all(len(row)==3 for row in A)
  d=graph_dist(A,0); B=[v for v in range(n) if d[v]%2==1]
  assert G['opposite_part']==B and G['distances_from_zero']==d
  assert all((d[u]-d[v])%2==1 for u,v in E)
  autos=G['root_transitive_automorphisms']
  assert len(autos)==n
  for dest,p in enumerate(autos):
   assert len(p)==n and set(p)==set(range(n)) and p[0]==dest
   assert {tuple(sorted((p[u],p[v]))) for u,v in E}==E
  full=G['unpunctured_paths_from_zero']
  assert set(full)=={str(v) for v in B}
  for target in B:check_path(full[str(target)],set(range(n)),0,target,A)
  part=G['punctured_paths_from_zero']
  required={f'{a},{b}' for a,b in combinations(B,2)}
  missed=set(map(tuple,G['missing_pairs_from_zero']))
  assert set(part)==required-{f'{a},{b}' for a,b in missed}
  for a,b in combinations(B,2):
   key=f'{a},{b}'
   if key in part:check_path(part[key],set(range(1,n)),a,b,A)
  if name=='Mobius-Kantor':
   assert missed=={(10,14)}
   assert d[10]==d[14]==3 and graph_dist(A,10)[14]==4
   level3=[v for v in B if d[v]==3]
   assert [(a,b) for a,b in combinations(level3,2) if graph_dist(A,a)[b]==4]==[(10,14)]
   assert complement_obstruction(A)==6
  else:assert not missed
  print(f'{name}: VERIFY_OK | {len(full)} full witnesses, {len(part)} deleted-vertex witnesses, {len(autos)} automorphisms')
 print('ALL_VERIFY_OK')

if __name__=='__main__':main()
