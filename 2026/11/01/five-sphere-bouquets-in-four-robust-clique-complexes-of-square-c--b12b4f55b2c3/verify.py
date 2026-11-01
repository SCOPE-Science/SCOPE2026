#!/usr/bin/env python3
"""Exact finite matching certificate for the 3-square bouquet robustness complex.
Run: python3 verify.py matching_pairs.csv
"""
import csv, sys
from collections import deque,Counter
from pathlib import Path

N=10
EDGE=set()
for i in range(3):
 a,b,c=3*i+1,3*i+2,3*i+3
 EDGE.update([tuple(sorted(e)) for e in [(0,a),(a,b),(b,c),(c,0)]])

def admissible(mask):
 # Exact independent-set witness test: no independent four-set.
 v=[j for j in range(N) if mask>>j&1]
 from itertools import combinations
 for c in combinations(v,4):
  if all(tuple(sorted(e)) not in EDGE for e in combinations(c,2)):
   return False
 return True

faces={s for s in range(1<<N) if admissible(s)}
assert len(faces)==537, len(faces)

if len(sys.argv)==1 or sys.argv[1]=='--write':
 unmatched=set(faces);pairs=[]
 for v in range(N):
  bit=1<<v
  for lo in sorted(s for s in unmatched if not s&bit and s|bit in unmatched):
   if lo in unmatched and lo|bit in unmatched:
    unmatched.remove(lo);unmatched.remove(lo|bit);pairs.append((lo,lo|bit))
 assert len(unmatched)==1 and next(iter(unmatched)).bit_count()==6,(len(unmatched),unmatched)
 with open('matching_pairs.csv','w',newline='') as fo:
  w=csv.writer(fo);w.writerow(['lower_mask','upper_mask']);w.writerows(pairs)
 print('WROTE',len(pairs),'pairs; critical',next(iter(unmatched)))

with open(sys.argv[1] if len(sys.argv)>1 and sys.argv[1]!='--write' else 'matching_pairs.csv',newline='') as fi:
 rows=list(csv.DictReader(fi))
pairs=[(int(row['lower_mask']),int(row['upper_mask'])) for row in rows]
assert len(pairs)==268,len(pairs)
used=set()
for a,b in pairs:
 assert a in faces and b in faces and b.bit_count()==a.bit_count()+1 and (a&b)==a
 assert a not in used and b not in used
 used.update((a,b))
critical=faces-used
assert len(critical)==1
sole=next(iter(critical))
assert sole.bit_count()==6
matched=set(pairs)
# In the Morse directed Hasse graph, reversed matched edges point upward.
indegree={s:0 for s in faces}; out={s:[] for s in faces}
for big in faces:
 for bit in range(N):
  if big>>bit&1:
   small=big^(1<<bit)
   assert small in faces
   src,dest=(small,big) if (small,big) in matched else (big,small)
   out[src].append(dest);indegree[dest]+=1
q=deque(s for s in faces if indegree[s]==0)
seen=0
while q:
 v=q.popleft();seen+=1
 for w in out[v]:
  indegree[w]-=1
  if indegree[w]==0:q.append(w)
assert seen==len(faces), ('MATCHING IS CYCLIC',seen,len(faces))
print('PASS: 537 exact faces; 268 valid disjoint pairs; one dimension-5 critical cell; complete Hasse orientation acyclic', 'critical_mask='+str(sole), 'oriented_edges='+str(sum(map(len,out.values()))))
