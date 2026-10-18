#!/usr/bin/env python3
"""Exact finite checks for the Tietze independence-complex homotopy and symmetry statement."""
import itertools
from collections import Counter,deque

LABELS=list(itertools.combinations(range(5),2))
ROOT=(0,1)
SURVIVORS=[p for p in LABELS if p!=ROOT]
NEIGHBORS=sorted([p for p in SURVIVORS if not(set(p)&set(ROOT))])
assert len(SURVIVORS)==9 and len(NEIGHBORS)==3
EDGES={tuple(sorted((i,j))) for i,a in enumerate(SURVIVORS) for j,b in enumerate(SURVIVORS) if i<j and not(set(a)&set(b))}
for k,p in enumerate(NEIGHBORS): EDGES.add(tuple(sorted((SURVIVORS.index(p),9+k))))
for i in range(9,12):
 for j in range(i+1,12):EDGES.add((i,j))
assert len(EDGES)==18
ADJ=[set() for i in range(12)]
for i,j in EDGES:ADJ[i].add(j);ADJ[j].add(i)
assert all(len(a)==3 for a in ADJ)
assert sorted([tuple(c) for c in itertools.combinations(range(12),3) if all(tuple(sorted(e)) in EDGES for e in itertools.combinations(c,2))])==[(9,10,11)]
FACES=set()
for m in range(1,1<<12):
 v=[i for i in range(12) if m>>i&1]
 if not any(j in ADJ[i] for i,j in itertools.combinations(v,2)):
  FACES.add(m)
C=Counter(m.bit_count()-1 for m in FACES)
assert [C[d] for d in range(5)]==[12,48,75,39,3] and len(FACES)==177
ORDER=(6,2,10,11,7,5,1,4,9,0,8,3)
FREE=set(FACES); PAIRS=[]
for j in ORDER:
 for a in sorted(tuple(FREE)):
  b=a|(1<<j)
  if not(a&(1<<j)) and a in FREE and b in FREE:
   assert b.bit_count()==a.bit_count()+1
   PAIRS.append((a,b));FREE.remove(a);FREE.remove(b)
assert len(PAIRS)==87 and sorted((m.bit_count()-1,m) for m in FREE)==[(0,64),(2,388),(2,2096)]
# Directly verify the reversed-matching Hasse diagram is acyclic.
mat={(a,b) for a,b in PAIRS}
inc={m:0 for m in FACES}; outs={m:[] for m in FACES}
for big in FACES:
 for j in range(12):
  if big&(1<<j):
   small=big^(1<<j)
   if small not in FACES:continue
   if (small,big) in mat:a,b=small,big
   else:a,b=big,small
   outs[a].append(b);inc[b]+=1
queue=deque(k for k,v in inc.items() if v==0);visited=0
while queue:
 x=queue.popleft();visited+=1
 for y in outs[x]:
  inc[y]-=1
  if inc[y]==0:queue.append(y)
assert visited==len(FACES), ('cycle',visited,len(FACES))

def parity(arr):return -1 if sum(arr[i]>arr[j] for i in range(len(arr)) for j in range(i+1,len(arr)))%2 else 1

def char_two(p):
 # signed Lefschetz trace on the full simplicial chains minus H_0.
 L=0
 for m in FACES:
  seq=[i for i in range(12) if m>>i&1]
  mapped=[p[i] for i in seq]
  if set(mapped)==set(seq):L+=(-1)**(len(seq)-1)*parity(mapped)
 return L-1

checks=[]
for pairperm in itertools.permutations((0,1)):
 for otherperm in itertools.permutations((2,3,4)):
  f={0:pairperm[0],1:pairperm[1],2:otherperm[0],3:otherperm[1],4:otherperm[2]}
  def move_label(a):return tuple(sorted((f[a[0]],f[a[1]])))
  p=[SURVIVORS.index(move_label(a)) for a in SURVIVORS]
  p += [9+NEIGHBORS.index(move_label(a)) for a in NEIGHBORS]
  assert len(set(p))==12
  assert {tuple(sorted((p[i],p[j]))) for i,j in EDGES}==EDGES
  expected=parity(otherperm)*(1+parity(pairperm))
  actual=char_two(p)
  assert actual==expected,(pairperm,otherperm,expected,actual)
  checks.append((pairperm,otherperm,expected))
assert len(checks)==12
assert Counter(x[2] for x in checks)==Counter({2:3,-2:3,0:6})
print('VERIFY_OK F_VECTOR_12_48_75_39_3 MORSE_87_PAIRS_3_CRITICAL')
print('GROUP_12 H2_S3_SIGN_TENSOR_S2_REGULAR CHARACTER_COUNTS_2_3_MINUS2_3_ZERO_6')
