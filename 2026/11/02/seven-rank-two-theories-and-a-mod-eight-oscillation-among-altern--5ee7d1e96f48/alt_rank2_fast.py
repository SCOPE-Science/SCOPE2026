#!/usr/bin/env python3
"""Direct A_n two-move game one-pebble extension patterns; no power-root theorem used."""
from itertools import permutations
from alt_rank2_types import cats
import sys,time

def parity(p):
 a=0
 for i,x in enumerate(p):
  for y in p[i+1:]:a^=(x>y)
 return a

def sq(p):return tuple(p[p[i]] for i in range(len(p)))
def inv(p):
 q=[0]*len(p)
 for i,v in enumerate(p):q[v]=i
 return tuple(q)
def partition(p):
 s=set();ls=[]
 for i in range(len(p)):
  if i not in s:
   j=i;k=0
   while j not in s:s.add(j);k+=1;j=p[j]
   ls.append(k)
 return tuple(sorted(ls))

def types(n):
 t=time.monotonic();e=tuple(range(n)); all_even=[];bycycle={}; sqs=[]
 for p in permutations(range(n)):
  if parity(p):continue
  all_even.append(p);sqs.append(sq(p))
  bycycle.setdefault(partition(p),p)
 fingerprints={};global_types=set()
 for c,x in sorted(bycycle.items()):
  x2=sq(x);xinv=inv(x);sgs=set()
  for y,y2 in zip(all_even,sqs):
   sgs.add((y==e,y==x,x2==y,y2==x,xinv==y,y2==e,x2==e))
  sg=frozenset(sgs);fingerprints[c]=sg;global_types.add(sg)
 labels=cats(n)
 print('n',n,'elements',len(all_even),'cycle_classes',len(bycycle),'pointed_types',len(global_types),'categorical_types',len(labels),'elapsed',round(time.monotonic()-t,3),flush=True)
 assert len(global_types)==len(labels)
 by_label={}
 for p,typ in fingerprints.items():
  key=next(k for k,v in labels.items() if v==p) if p in labels.values() else None
  if key:by_label[key]=typ
 assert len(set(by_label.values()))==len(labels)
 for p,typ in fingerprints.items():
  from alt_rank2_types import category
  lab=category(p)
  assert typ==by_label[lab], (n,p,lab)
 print('PASS',n,flush=True)
 return global_types
if __name__=='__main__':
 for arg in sys.argv[1:]:types(int(arg))
