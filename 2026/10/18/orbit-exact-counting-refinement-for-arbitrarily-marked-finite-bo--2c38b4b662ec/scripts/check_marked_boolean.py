#!/usr/bin/env python3
"""Independent vertex-level directed Boolean Hasse 1-WL with named marked subsets."""
import random
from collections import Counter
from itertools import product

def test(n,marks):
 N=1<<n; low=[[x^(1<<j) for j in range(n) if x&(1<<j)] for x in range(N)]; high=[[x|(1<<j) for j in range(n) if not x&(1<<j)] for x in range(N)]
 patterns=[tuple(int(bool(z&(1<<j))) for z in marks) for j in range(n)]
 def orbit(x):
  c=Counter(patterns[j] for j in range(n) if x&(1<<j))
  return tuple(sorted(c.items()))
 v=[orbit(x) for x in range(N)]
 labels=[marks.index(x)+1 if x in marks else 0 for x in range(N)]
 for r in range(2*n+4):
  if len(set(labels))==len(set(v)):
   for i in range(N):
    for j in range(i):assert (labels[i]==labels[j])==(v[i]==v[j]),(n,marks,i,j,r)
   return r
  sig=[(labels[x],tuple(sorted(Counter(labels[y] for y in low[x]).items())),tuple(sorted(Counter(labels[y] for y in high[x]).items()))) for x in range(N)]
  d={a:i for i,a in enumerate(sorted(set(sig)))};labels2=[d[a] for a in sig]
  assert len(set(labels2))>len(set(labels)),(n,marks,r)
  labels=labels2
 raise AssertionError((n,marks))

def main():
 rng=random.Random(12092026);total=0; maxr=0
 for n in range(1,8):
  for m in range(0,4):
   confs=list(product(range(1<<n),repeat=m)) if n<=3 else []
   if n>=4:
    for i in range(100):confs.append(tuple(rng.sample(range(1<<n),m)))
   for z in confs:
    if len(set(z))!=m:continue
    r=test(n,z);total+=1;maxr=max(maxr,r)
  print(f'n={n} configurations_cumulative={total} maximal_rounds={maxr} PASS',flush=True)
 print(f'MARKED_BOOLEAN_ORBIT_REFINEMENT_PASS trials={total} maximal_rounds={maxr}')
if __name__=='__main__':main()
