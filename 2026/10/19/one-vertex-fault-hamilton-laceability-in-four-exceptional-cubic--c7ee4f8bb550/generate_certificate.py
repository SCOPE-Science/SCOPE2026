#!/usr/bin/env python3
"""Construct finite Hamilton-path witnesses for four classical cubic incidence graphs."""
import json
from pathlib import Path
from functools import lru_cache
import networkx as nx

def graph(name):
 if name=='Heawood':
  n=14
  E=[((j+k)%7,7+j) for j in range(7) for k in (0,1,3)]
 elif name=='Pappus':
  n=18;E=[(3*x+y,9+3*m+(y-m*x)%3) for x in range(3) for y in range(3) for m in range(3)]
 else:
  N,K={'Mobius-Kantor':(8,3),'Desargues':(10,3)}[name]
  n=2*N;E=[]
  for j in range(N):E.extend(((j,(j+1)%N),(j,N+j),(N+j,N+(j+K)%N)))
 A=[set() for _ in range(n)]
 for u,v in E:A[u].add(v);A[v].add(u)
 assert all(len(a)==3 for a in A)
 return [sorted(t) for t in A]

def opposite(A):
 n=len(A);d=[-1]*n;d[0]=0;Q=[0]
 for v in Q:
  for w in A[v]:
   if d[w]<0:d[w]=d[v]+1;Q.append(w)
   else:assert (d[v]-d[w])%2!=0
 assert len(Q)==n
 return [v for v in range(n) if d[v]%2],d

def path(A,st,en,removed=None):
 n=len(A);full=(1<<n)-1
 if removed is not None:full^=1<<removed
 @lru_cache(None)
 def visit(u,mask):
  if mask==full:return (u,) if u==en else None
  if u==en:return None
  for v in A[u]:
   if full>>v&1 and not mask>>v&1:
    r=visit(v,mask|(1<<v))
    if r is not None:return (u,)+r
  return None
 return visit(st,1<<st)

def automorphisms(A):
 n=len(A);G=nx.Graph();G.add_nodes_from(range(n))
 G.add_edges_from((u,v) for u in range(n) for v in A[u] if u<v)
 result={}
 for m in nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter():
  result.setdefault(m[0],[m[i] for i in range(n)])
  if len(result)==n:break
 assert len(result)==n,(n,len(result))
 return [result[v] for v in range(n)]

def gen():
 C={'schema_version':1,'objects':{}}
 for name in ('Heawood','Mobius-Kantor','Pappus','Desargues'):
  A=graph(name); n=len(A); B,dis=opposite(A)
  full={str(e):list(path(A,0,e)) for e in B}
  assert all(len(p)==n for p in full.values())
  part={};zeros=[]
  for i,a in enumerate(B):
   for b in B[i+1:]:
    p=path(A,a,b,0)
    if p is not None:part[f'{a},{b}']=list(p)
    else:zeros.append((a,b))
  entry={'adjacency':A,'opposite_part':B,'distances_from_zero':dis,'unpunctured_paths_from_zero':full,
         'punctured_paths_from_zero':part,'missing_pairs_from_zero':zeros,'root_transitive_automorphisms':automorphisms(A)}
  C['objects'][name]=entry
  print(name,'order',n,'full paths',len(full),'punctured paths',len(part),'missing pairs',zeros,flush=True)
 with (Path(__file__).resolve().parent/'witness_certificate.json').open('w',encoding='utf8') as f:json.dump(C,f,sort_keys=True,separators=(',',':'));f.write('\n')
if __name__=='__main__':gen()
