#!/usr/bin/env python3
"""Finite proof certificate for the order-four permutahedron independence-complex vertex cofibration."""
import itertools
from collections import Counter,deque

perms=list(itertools.permutations(range(4)))
where={p:i for i,p in enumerate(perms)}
full=(1<<24)-1
adj=[0]*24
for i,p in enumerate(perms):
 for j in range(3):
  q=list(p);q[j],q[j+1]=q[j+1],q[j]
  k=where[tuple(q)]
  adj[i]|=1<<k
assert len(adj)==24 and all(a.bit_count()==3 for a in adj)
assert all((adj[i]>>j&1)==(adj[j]>>i&1) for i in range(24) for j in range(24))
assert sum(a.bit_count() for a in adj)//2==36

# Right-composition by adjacent transpositions and left-composition by arbitrary
# coordinate-label permutations commute. The latter action is vertex-transitive.
# Each vertex deletion therefore isomorphic to deletion at identity (index zero).
cases={
 'full': (full, {5:4}),
 'delete_vertex': (full & ~(1<<0),{5:3}),
 'delete_closed_neighborhood': (full & ~((1<<0)|adj[0]),{4:1}),
}

def verify_case(allowed,expected):
 faces=[0]
 for v in range(24):
  if allowed>>v&1:
   faces += [s|(1<<v) for s in faces if not(s & adj[v])]
 face_set=set(faces)
 assert len(face_set)==len(faces)
 assert all(not (s&~allowed) for s in faces)
 assert all(not(s&adj[v]) for s in faces for v in range(24) if s>>v&1)
 hist=Counter(s.bit_count()-1 for s in faces if s)
 # Match each remaining simplex with its add-v simplex if both remain;
 # the pairing is made once at its first eligible vertex stage.
 unmatched=set(faces); reverse_matched={};pairs=[]; stage=[]
 for v in range(24):
  if not (allowed>>v&1):continue
  lows=[s for s in unmatched if not(s>>v&1) and (s|(1<<v)) in unmatched]
  for s in lows:
   t=s|(1<<v);unmatched.remove(s);unmatched.remove(t)
   pairs.append((s,t));reverse_matched[t]=s
  stage.append((v,len(lows)))
 assert Counter(s.bit_count()-1 for s in unmatched)==Counter(expected)
 assert len(reverse_matched)==len(pairs)
 assert len(pairs)*2+len(unmatched)==len(faces)
 assert sum(s==0 for s,t in pairs)==1
 # Orient Hasse cover edges upward if matched, downward otherwise.
 indegree={s:0 for s in faces}; arcs={s:[] for s in faces}; incidences=0
 for big in faces:
  m=big
  while m:
   b=m&-m;small=big^b
   assert small in face_set
   if reverse_matched.get(big)==small:tail,head=small,big
   else:tail,head=big,small
   arcs[tail].append(head);indegree[head]+=1;incidences+=1;m^=b
 free=deque(v for v,d in indegree.items() if d==0);visited=0
 while free:
  s=free.popleft();visited+=1
  for t in arcs[s]:
   indegree[t]-=1
   if not indegree[t]:free.append(t)
 assert visited==len(faces),(visited,len(faces))
 return {
  'face_vector':tuple(hist[d] for d in range(12)),
  'nonempty_faces':len(faces)-1,
  'total_faces':len(faces),
  'pairs':len(pairs),
  'incidences':incidences,
  'critical_dimensions':dict(Counter(s.bit_count()-1 for s in unmatched)),
  'critical_bitmasks':sorted(unmatched),
  'stage_pairs':tuple(stage),
  'verified_topological_sort':visited,
 }

if __name__=='__main__':
 for name,(allowed,expected) in cases.items():
  out=verify_case(allowed,expected)
  print(name,out)
 print('PERMUTOHEDRON_LOCAL_GLOBAL_MORSE_OK')
