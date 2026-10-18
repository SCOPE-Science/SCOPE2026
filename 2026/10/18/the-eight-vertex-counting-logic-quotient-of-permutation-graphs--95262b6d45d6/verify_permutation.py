#!/usr/bin/env python3
"""Exact 1-WL/C2 equivalence census of permutation graphs through eight vertices.
Requires Python 3 and NetworkX 3; run python verify_permutation.py.
"""
from itertools import permutations
from collections import Counter,defaultdict
import networkx as nx

def inversions(p):
 n=len(p);A=[0]*n
 for i in range(n):
  for j in range(i+1,n):
   if p[i]>p[j]:A[i]|=1<<j;A[j]|=1<<i
 return tuple(A)

def multigraph_colours(graphs,rounds):
 n=len(graphs[0]);colors=[[0]*n for _ in graphs]
 for r in range(rounds):
  codes={};new=[]
  for adj,prior in zip(graphs,colors):
   child=[]
   for i in range(n):
    key=(prior[i],tuple(sorted(prior[j] for j in range(n) if adj[i]>>j &1)))
    if key not in codes:codes[key]=len(codes)
    child.append(codes[key])
   new.append(child)
  colors=new
 return [tuple(sorted(Counter(C).items())) for C in colors]

def graph(A):
 n=len(A);G=nx.Graph();G.add_nodes_from(range(n));G.add_edges_from((i,j) for i in range(n) for j in range(i+1,n) if A[i]>>j&1);return G

def census(n):
 graphs=[inversions(p) for p in permutations(range(n))]
 colors1=multigraph_colours(graphs,n)
 colors2=multigraph_colours(graphs,2*n)
 classes1=defaultdict(list);classes2=defaultdict(list)
 for i,(x,y) in enumerate(zip(colors1,colors2)):
  classes1[x].append(i);classes2[y].append(i)
 assert sorted(map(tuple,classes1.values()))==sorted(map(tuple,classes2.values()))
 iso_types=0;multis=[];witnesses=[]
 for members in classes2.values():
  reps=[]
  for i in members:
   G=graph(graphs[i])
   if not any(nx.is_isomorphic(G,H) for _,H in reps):reps.append((i,G))
  iso_types+=len(reps)
  if len(reps)>1:
   multis.append(len(reps));witnesses.append([graphs[i] for i,_ in reps])
 return len(graphs),iso_types,len(classes2),Counter(multis),witnesses

if __name__=='__main__':
 expect_iso=[1,2,4,11,33,142,776,5699]
 expect_c2=[1,2,4,11,33,140,770,5654]
 for n in range(1,9):
  presentations,iso,c2,multi,witnesses=census(n)
  print(f'n={n} presentations={presentations} isomorphism={iso} C2={c2} multiplicities={dict(sorted(multi.items()))}')
  assert iso==expect_iso[n-1] and c2==expect_c2[n-1]
  if n<=5:assert not multi
  if n==6:
   assert multi==Counter({2:2})
   assert sorted(sum(x.bit_count() for x in w[0])//2 for w in witnesses)==[7,8]
   for w in witnesses:print('FIRST_OBSTRUCTION',sum(x.bit_count() for x in w[0])//2,w)
  if n==8:assert multi==Counter({2:38,3:2,4:1})
 print('EXACT_PERMUTATION_VERIFY_OK')
