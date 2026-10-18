#!/usr/bin/env python3
"""Independently compute S4 action on first homology of Hom(K3,K4)."""
from itertools import product, permutations
from collections import deque

def parity(a):
 return -1 if sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))%2 else 1

def cell_sets(m=3,n=4):
 out=[[],[]]
 for assign in product(range(m+1),repeat=n):
  if not all(i in assign for i in range(1,m+1)): continue
  A=tuple(tuple(x for x in range(n) if assign[x]==i) for i in range(1,m+1))
  d=sum(len(x)-1 for x in A)
  out[d].append(A)
 return out

verts,edges=cell_sets()
vi={x:i for i,x in enumerate(verts)}
ei={x:i for i,x in enumerate(edges)}
adj=[[] for _ in verts]
ends=[]
for i,E in enumerate(edges):
  face=[]
  for c,A in enumerate(E):
    if len(A)==2:
      B=list(E);B[c]=(A[0],);face.append((vi[tuple(B)],1))
      B[c]=(A[1],);face.append((vi[tuple(B)],-1))
      break
  assert len(face)==2
  neg=next(v for v,s in face if s==-1)
  pos=next(v for v,s in face if s==1)
  ends.append((neg,pos))
  adj[neg].append((pos,i));adj[pos].append((neg,i))

parent={0:(-1,-1)};que=deque([0]);tree=set()
while que:
  v=que.popleft()
  for w,i in adj[v]:
    if w not in parent:
      parent[w]=(v,i);tree.add(i);que.append(w)
assert len(parent)==len(verts)
chords=sorted(set(range(len(edges)))-tree)
assert len(chords)==13

def path(a,b):
 # source a to destination b, tree edge coefficients
 anc={};v=a
 while v!=-1:
   anc[v]=True;v=parent[v][0]
 l=b
 while l not in anc:l=parent[l][0]
 coeff={};v=a
 while v!=l:
  w,edge=parent[v]
  coeff[edge]=1 if ends[edge]==(v,w) else -1
  v=w
 back=[];v=b
 while v!=l:
  w,edge=parent[v]
  back.append((edge,1 if ends[edge]==(w,v) else -1))
  v=w
 for edge,s in reversed(back):coeff[edge]=s
 return coeff

cycles=[]
for i in chords:
  source,target=ends[i]
  z={i:1};z.update(path(target,source))
  bd={v:0 for v in range(len(verts))}
  for edge,s in z.items():
    u,v=ends[edge];bd[u]-=s;bd[v]+=s
  assert all(x==0 for x in bd.values())
  cycles.append(z)

def act_edge(i,p):
 A=edges[i]; B=tuple(tuple(sorted(p[x] for x in X)) for X in A)
 sign=1
 for X in A:sign*=parity([p[x] for x in X])
 return ei[B],sign

def count_cycles(p):
 seen=set();count=0
 for x in range(len(p)):
  if x in seen: continue
  count+=1
  while x not in seen:
   seen.add(x);x=p[x]
 return count

for p in permutations(range(4)):
 trace=0
 for e,z in zip(chords,cycles):
  trace+=sum(coeff*s for j,coeff in z.items() for mapped,s in [act_edge(j,p)] if mapped==e)
 prediction=parity(p)*(2**count_cycles(p)-3)
 assert trace==prediction,(p,trace,prediction)
print('VERIFY_HOMOLOGY_ACTION_OK',len(verts),'vertices',len(edges),'edges',len(chords),'cycles',24,'automorphisms')
