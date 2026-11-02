#!/usr/bin/env python3
"""Independent rank-two atomic-extension enumeration of alternating groups."""
import sys
from itertools import permutations
from collections import defaultdict
from alt_rank2_types import cats

def mul(x,y):return tuple(x[y[i]] for i in range(len(x)))
def conj_type(x):
 seen=set();out=[]
 for i in range(len(x)):
  if i in seen:continue
  j=i; count=0
  while j not in seen:
   seen.add(j); j=x[j];count+=1
  out.append(count)
 return tuple(sorted(out))
def even(p):
 return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2==0

def atomic_signature(e,x,y):
 vals=(e,x,y)
 p={(0,0):e,(0,1):x,(0,2):y,(1,0):x,(2,0):y,
    (1,1):mul(x,x),(2,2):mul(y,y),(1,2):mul(x,y),(2,1):mul(y,x)}
 return tuple(int(p[i,j]==vals[k]) for i in range(3) for j in range(3) for k in range(3))

def run(n):
 e=tuple(range(n)); by_class={}
 all_even=[]
 for perm in permutations(range(n)):
  if not even(perm):continue
  all_even.append(perm)
  k=conj_type(perm)
  if k not in by_class:by_class[k]=perm
 fingerprints=set(); type_by_class={}
 for idx,(cycle,x) in enumerate(sorted(by_class.items())):
  s=set()
  for y in all_even:s.add(atomic_signature(e,x,y))
  tp=tuple(sorted(s)); fingerprints.add(tp);type_by_class[cycle]=tp
 print('n',n,'order',len(all_even),'S_n_even_cycle_partitions',len(by_class),'root_type_count',len(fingerprints), 'partition_categories',','.join(sorted(cats(n))),flush=True)
 for cat in sorted(cats(n)):
  witness=cats(n)[cat]
  if witness not in type_by_class:raise ValueError('missing '+str(witness))
  print('  ',cat,'witness',witness,'atomic_extensions',len(type_by_class[witness]))
 assert len(fingerprints)==len(cats(n)), ('fingerprint deviation',n)
 return fingerprints
if __name__=='__main__':
 for arg in sys.argv[1:]:run(int(arg))
