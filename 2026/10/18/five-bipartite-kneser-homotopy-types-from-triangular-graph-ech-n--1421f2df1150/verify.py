#!/usr/bin/env python3
"""Recompute closed-neighborhood homotopy for triangular graphs through ten points."""
from itertools import combinations
from collections import Counter,defaultdict,deque
from functools import lru_cache
from math import comb
from time import monotonic
import sys

def run(n):
 start=monotonic()
 edges=list(combinations(range(n),2)); N=len(edges)
 facets=[]
 for e in edges:
  mask=0
  for j,f in enumerate(edges):
   if e[0] in f or e[1] in f: mask|=1<<j
  facets.append(mask)
 faces={0}
 for facet in facets:
  s=facet
  while s:
   faces.add(s)
   s=(s-1)&facet
 reduced_euler=-sum(1 if face.bit_count()%2==0 else -1 for face in faces)
 assert reduced_euler==comb(n-1,3),(n,reduced_euler,comb(n-1,3))
 print('faces',n,len(faces),'reduced_euler',reduced_euler,'t',round(monotonic()-start,1),flush=True)
 remains=set(faces);lowers={}; uppers={}
 for j in range(N):
  bit=1<<j
  for s in list(remains):
   if not s&bit and ((u:=s|bit) in remains):
    remains.remove(s);remains.remove(u)
    lowers[s]=u;uppers[u]=s
 crit=remains
 expected=Counter({4:comb(n-1,4),5:comb(n,4)})
 actual=Counter(s.bit_count() for s in crit)
 print('matched',len(lowers),'crit',actual,'expected',expected,'t',round(monotonic()-start,1),flush=True)
 assert actual==expected,(n,actual)
 assert (2*len(lowers)+len(crit))==len(faces)
 # Forman V-path DAG. Only matched lowers are nodes. All other facets of each matched upper are possible next steps.
 indeg={s:0 for s in lowers}
 for s,u in lowers.items():
  w=u
  while w:
   b=w&-w;w-=b
   t=u^b
   if t!=s and t in indeg:
    indeg[t]+=1
 print('indeg finished',n,round(monotonic()-start,1),flush=True)
 queue=deque(s for s,d in indeg.items() if d==0)
 seen=0
 while queue:
  s=queue.popleft();seen+=1
  u=lowers[s];w=u
  while w:
   b=w&-w;w-=b
   t=u^b
   if t!=s and t in indeg:
    indeg[t]-=1
    if indeg[t]==0:queue.append(t)
 print('dag',n,seen,len(lowers),'t',round(monotonic()-start,1),flush=True)
 assert seen==len(lowers),'Cyclic matching'
 # Signed integral Morse boundary from critical 4-faces to critical 3-faces.
 def boundary(s):
  j=0;w=s
  while w:
   bit=w&-w;w-=bit
   yield s^bit,(-1 if j%2 else 1)
   j+=1
 @lru_cache(maxsize=None)
 def project(s):
  if s in uppers:return {}
  if s not in lowers:return {s:1}
  u=lowers[s];pivot=None
  for f,c in boundary(u):
   if f==s:pivot=c;break
  assert pivot in (-1,1)
  acc=defaultdict(int)
  for f,c in boundary(u):
   if f==s:continue
   for key,val in project(f).items():acc[key]-=pivot*c*val
  return {k:v for k,v in acc.items() if v}
 count=0
 for s in crit:
  if s.bit_count()!=5:continue
  acc=defaultdict(int)
  for f,c in boundary(s):
   for k,v in project(f).items():acc[k]+=c*v
  assert not any(acc.values()),('Nonzero Morse differential',n,s,acc)
  count+=1
 print('SIGNED_ZERO',n,count,'projection_cache',project.cache_info().currsize,'t',round(monotonic()-start,1),flush=True)
 return n,len(faces),len(lowers),actual[4],actual[5]
if __name__=='__main__':
 for n in list(map(int,sys.argv[1:])) or range(6,11):print('DONE',run(n),flush=True)
 print('VERIFY_OK')
