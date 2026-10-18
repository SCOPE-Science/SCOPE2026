#!/usr/bin/env python3
"""Independent Alexander-dual face and field homology check for Paley(13)."""
from itertools import combinations
from collections import defaultdict
q=13
squares={int(x*x%13) for x in range(1,13)}
edge=lambda u,v: (v-u)%q in squares
connected=lambda t: sum(edge(a,b) for a,b in combinations(t,2))>=2
faces={0:[()]}
for r in range(1,q+1):
 faces[r]=[subset for subset in combinations(range(q),r)
           if all(connected(t) for t in combinations(subset,3))]
 if not faces[r]:break
assert [len(faces[i]) for i in range(5)]==[1,13,78,143,78]
assert not faces[5]

def signed_boundary_rank(dim,p):
 lower={s:i for i,s in enumerate(faces[dim])}
 pivots={}
 for cell in faces[dim+1]:
  column={}
  for j in range(len(cell)):
   f=cell[:j]+cell[j+1:]
   column[lower[f]]=1 if j%2==0 else p-1
  while column:
   pivot=max(column)
   if pivot in pivots:
    scalar=column[pivot]*pow(pivots[pivot][pivot],-1,p)%p
    for row,c in pivots[pivot].items():
     value=(column.get(row,0)-scalar*c)%p
     if value:column[row]=value
     else:column.pop(row,None)
   else:
    pivots[pivot]=column
    break
 return len(pivots)
for p in (2,3,5,7,11,101):
 r1=signed_boundary_rank(1,p)
 r2=signed_boundary_rank(2,p)
 r3=signed_boundary_rank(3,p)
 assert (r1,r2,r3)==(12,66,76)
 assert 78-r1-r2==0
 assert 143-r2-r3==1
 assert 78-r3==2
print('DUAL_VERIFY_OK')
print('alexander_dual_face_sizes=[1,13,78,143,78]')
print('ranks_over_2_3_5_7_11_101=(12,66,76)')
print('dual_reduced_betti={2:1,3:2}')
print('cut_reduced_betti_by_alexander_duality={7:2,8:1}')
