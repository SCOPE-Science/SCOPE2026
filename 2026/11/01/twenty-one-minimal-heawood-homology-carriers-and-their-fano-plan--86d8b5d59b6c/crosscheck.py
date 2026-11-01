#!/usr/bin/env python3
"""Independent stacked-matrix check of induced Heawood homology images over GF(2).
Uses the rank-nullity formula, NOT a basis of local three-cycles.
"""
from itertools import combinations
from collections import Counter

n=14
edge_masks=[]
for u in range(7):
 for a in range(7):
  if ((u+1)&(a+1)).bit_count()%2==0:
   edge_masks.append((1<<u)|(1<<(7+a)))
assert len(edge_masks)==21
faces={k:[] for k in range(8)}
for x in range(1<<n):
 if all(x&e!=e for e in edge_masks):faces[x.bit_count()].append(x)
assert tuple(map(lambda k:len(faces[k]),range(8)))==(1,14,70,154,147,56,14,2)
tri={x:i for i,x in enumerate(faces[3])}
tet={x:i for i,x in enumerate(faces[4])}

def boundary(face,lower):
 out=0
 for v in range(n):
  if (face>>v)&1:out^=1<<lower[face^(1<<v)]
 return out
D3=[boundary(x,tri) for x in faces[4]]
D4=[boundary(x,tet) for x in faces[5]]

def gaussian_rank(cols):
 pivots={}
 for v in cols:
  while v:
   p=v.bit_length()-1
   if p not in pivots:
    pivots[p]=v
    break
   v^=pivots[p]
 return len(pivots)

def quotient_vectors(cols,dim):
 pivots={}
 for v in cols:
  while v:
   p=v.bit_length()-1
   if p not in pivots:
    pivots[p]=v
    break
   v^=pivots[p]
 def reduced(z):
  for p in sorted(pivots,reverse=True):
   if (z>>p)&1:z ^=pivots[p]
  return z
 return [reduced(1<<j) for j in range(dim)]

Q=quotient_vectors(D4,len(D3))
assert gaussian_rank(D4)==44
assert gaussian_rank(D3)==97
assert gaussian_rank(Q)==len(D3)-44
records=Counter()
for S in range(1<<14):
 J=[j for j,v in enumerate(faces[4]) if v&S==v]
 H=[h for h,v in enumerate(faces[5]) if v&S==v]
 low=gaussian_rank(D3[j] for j in J)
 local_beta=len(J)-low-gaussian_rank(D4[h] for h in H)
 # Each stacked column consists of the 154 triangle coordinates and the
 # quotient projection of its 147 tetrahedron coordinates.
 stacked=gaussian_rank(D3[j] | (Q[j]<<154) for j in J)
 image_dim=stacked-low
 assert image_dim==local_beta,(S,local_beta,image_dim)
 records[(S.bit_count(),image_dim)]+=1
want={
 (0,0):1,(1,0):14,(2,0):91,(3,0):364,(4,0):1001,(5,0):2002,
 (6,0):3003,(7,0):3432,(8,0):3003,(9,0):2002,
 (10,0):980,(10,1):21,(11,0):280,(11,1):84,
 (12,0):21,(12,1):42,(12,2):28,(13,3):14,(14,6):1,
}
assert dict(records)==want
print('independent_rank_nullity_stacked_matrix_method=PASS')
print('all_16384_induced_inclusions_injective=PASS')
print('minimum_10vertex_nonzero_carriers=21')
print('global_dimension=6')
print('CROSSCHECK_OK')
