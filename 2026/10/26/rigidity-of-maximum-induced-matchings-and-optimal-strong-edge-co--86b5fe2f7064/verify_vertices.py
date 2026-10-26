"""Cross-check via vertex subsets, not edge incompatibility search.
Enumerates induced one-regular vertex sets of half the cube, for d=2..4.
"""
from itertools import combinations
for d in (2,3,4):
 n=1<<d; k=n//2
 adjacency=[sum(1<<(v^(1<<j)) for j in range(d)) for v in range(n)]
 found=set()
 for X in combinations(range(n),k):
  mask=sum(1<<x for x in X)
  if all((adjacency[x]&mask).bit_count()==1 for x in X):
   found.add(mask)
 expected=set()
 for j in range(d):
  for parity in (0,1):
   mask=sum(1<<x for x in range(n) if ((x&~(1<<j)).bit_count()&1)==parity)
   expected.add(mask)
 assert found==expected
 print(f'd={d}: induced-one-regular half-vertex sets={len(found)}, exactly {2*d} coordinate-parity sets')
