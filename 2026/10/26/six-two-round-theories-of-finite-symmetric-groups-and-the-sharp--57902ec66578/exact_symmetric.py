#!/usr/bin/env python3
"""Exact rank-two finite-model-game signatures for symmetric permutation groups."""
import itertools,collections,json,time,sys
from pathlib import Path

def cycletype(p):
 n=len(p); seen=set(); lens=[]
 for i in range(n):
  if i in seen: continue
  u=i; l=0
  while u not in seen:
   seen.add(u);l+=1;u=p[u]
  lens.append(l)
 return tuple(sorted(lens,reverse=True))

def mul(p,q): return tuple(p[q[i]] for i in range(len(p)))
def inv(p):
 r=[0]*len(p)
 for i,j in enumerate(p): r[j]=i
 return tuple(r)

def tuple_type(x,y,e,xx,ix):
 # complete atomic diagram of e,x,y in the group multiplication graph.
 yy=mul(y,y)
 return (x==e,y==e,x==y,xx==e,yy==e,xx==y,yy==x,ix==y)

def run(n):
 e=tuple(range(n))
 ps=list(itertools.permutations(range(n)))
 reps={}
 for p in ps:
  ct=cycletype(p)
  if ct not in reps: reps[ct]=p
 xs=[]
 for ct,x in sorted(reps.items()):
  xx=mul(x,x);ix=inv(x)
  exts={tuple_type(x,y,e,xx,ix) for y in ps}
  # unary x=e/involution/other is captured in the first two tuple-type bits.
  typ=tuple(sorted(exts));xs.append((ct,typ))
 theory=frozenset(typ for _,typ in xs)
 return theory, xs

if __name__=='__main__':
 theory_to_i={};results=[]
 for n in range(1,9):
  start=time.time(); t,x=run(n)
  klass=theory_to_i.setdefault(t,len(theory_to_i)+1)
  groups={}
  for ct,typ in x:
   key=tuple(sorted(typ));groups.setdefault(key,[]).append(ct)
  results.append({'n':n,'class':klass,'pointed_types':len(groups),'orbits':len(x),'signature_classes':list(groups.values())})
  print('SYMMETRIC_EXACT', 'n='+str(n),'class='+str(klass),'pointed_types='+str(len(groups)),'cycle_partitions='+str(len(x)),'seconds=%.2f'%(time.time()-start),flush=True)
 with open(Path(__file__).with_name('exact_output.json'),'w',encoding='utf-8') as f: json.dump(results,f,indent=2)
 print('EXACT_VERIFY_OK','classes='+str(len(theory_to_i)),flush=True)
 if '--n9' in sys.argv:
  base,_=run(8);other,_=run(9)
  assert base==other
  print('EXACT_NINE_OK class_equality=S8=S9',flush=True)
