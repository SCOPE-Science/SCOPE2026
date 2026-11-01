#!/usr/bin/env python3
"""Exact labelled and symmetry-fixed optimal Morse matching census for Delta^4.
Faces are nonempty bitmasks in 1..31, each matching pairs incident codimension-one faces.
The only critical face is {0}. Enumeration recursively pairs the first unmatched face.
Acyclicity is independently tested by directed V-path graphs at each dimension.
"""
from collections import Counter
from itertools import permutations

FACES=tuple(range(1,32))
COFACES={a:tuple(b for b in FACES if b.bit_count()==a.bit_count()+1 and (a&b)==a) for a in FACES}
NBR={a:tuple(b for b in FACES if b in COFACES[a] or a in COFACES[b]) for a in FACES}
GROUP=tuple((0,*p) for p in permutations(range(1,5)))
PMAPS=[]
for p in GROUP:
 PMAPS.append({a:sum(1<<p[i] for i in range(5) if a&(1<<i)) for a in FACES})
COUNTS=Counter();STAB=Counter();STAB_TYPES=Counter();accepted=0;perfect=0

def acyclic(matching):
 # Forman V-path digraph per rank: a -> c whenever (a,b) is paired and
 # c is another codimension-one face of b.
 up={a:[] for a in FACES}
 for a,b in matching:
  for c in FACES:
   if c!=a and c.bit_count()==a.bit_count() and (c&b)==c:
    up[a].append(c)
 colour={a:0 for a in FACES}
 def visit(a):
  if colour[a]==1:return False
  if colour[a]==2:return True
  colour[a]=1
  for c in up[a]:
   if not visit(c):return False
  colour[a]=2
  return True
 return all(visit(a) for a in FACES if colour[a]==0)

def rec(remaining,matching):
 global perfect,accepted
 if not remaining:
  perfect+=1
  if not acyclic(matching):return
  accepted+=1
  E=frozenset(matching)
  stabilizers=[]
  for p,mp in zip(GROUP,PMAPS):
   if all((mp[a],mp[b]) in E for a,b in matching):
    COUNTS[p]+=1
    stabilizers.append(p)
  order=len(stabilizers)
  STAB[order]+=1
  if order==2:
   p=next(p for p in stabilizers if p!=GROUP[0])
   moved=sum(p[a]!=a for a in range(1,5))
   typ="single_transposition" if moved==2 else "double_transposition"
  elif order==1:typ="trivial"
  elif order==6:typ="S3"
  elif order==24:typ="S4"
  else:raise AssertionError(("unexpected stabilizer order",order))
  STAB_TYPES[typ]+=1
  return
 a=min(remaining)
 for b in NBR[a]:
  if b in remaining:
   pair=(a,b) if a.bit_count()<b.bit_count() else (b,a)
   rec(remaining-{a,b},matching+(pair,))

if __name__=='__main__':
 rec(frozenset(FACES)-{1},())
 print('perfect',perfect,'acyclic',accepted)
 classcounts={}
 for p,v in COUNTS.items():
  lens=[];seen=set()
  for a in range(1,5):
   if a not in seen:
    t=a;ln=0
    while t not in seen:seen.add(t);t=p[t];ln+=1
    lens.append(ln)
  classcounts.setdefault(tuple(sorted(lens,reverse=True)),Counter())[v]+=1
 for cyc,c in sorted(classcounts.items()): print('cycle',cyc,'values',dict(c))
 assert perfect==117837
 assert accepted==76025
 assert classcounts=={
  (1,1,1,1):Counter({76025:1}),
  (2,1,1):Counter({243:6}),
  (2,2):Counter({21:3}),
  (3,1):Counter({8:8}),
  (4,):Counter({1:6})}
 orb=sum(COUNTS.values())//24
 assert orb==3234 and 24*orb==sum(COUNTS.values())
 print('stabilizer orders',dict(sorted(STAB.items())))
 print('orbits by stabilizer order', {o:c*o//24 for o,c in sorted(STAB.items())})
 print('stabilizer types and orbits', {k:(v,v*({'trivial':1,'single_transposition':2,'double_transposition':2,'S3':6,'S4':24}[k])//24) for k,v in sorted(STAB_TYPES.items())})
 assert STAB_TYPES=={'trivial':74568,'single_transposition':1368,'double_transposition':60,'S3':28,'S4':1}
 assert sum(STAB.values())==76025
 assert sum(c*o//24 for o,c in STAB.items())==3234
 print('S5 orbit count',orb,'total labelled',5*accepted)
