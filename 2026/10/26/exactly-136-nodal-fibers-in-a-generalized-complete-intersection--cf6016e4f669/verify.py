#!/usr/bin/env python3
"""Exact Chern coefficient and quadratic two-point jet arithmetic (Python stdlib)."""
from itertools import combinations_with_replacement
from fractions import Fraction

def add(a,b):
 c=dict(a)
 for k,v in b.items(): c[k]=c.get(k,0)+v
 return {k:v for k,v in c.items() if v}
def mul(a,b):
 c={}
 for (i,j),v in a.items():
  for (k,l),w in b.items():
   if i+k<=2 and j+l<=4:
    t=(i+k,j+l);c[t]=c.get(t,0)+v*w
 return {k:v for k,v in c.items() if v}
def power(a,n):
 r={(0,0):1}
 for _ in range(n):r=mul(r,a)
 return r
one={(0,0):1}; h={(1,0):1}; H={(0,1):1}
# Chern classes of Q(2H) plus O(h+H); total Chern c(E)=1+c1+c2+c3.
c1={(1,0):3,(0,1):5};c2={(2,0):5,(1,1):10,(0,2):8};c3={(2,1):7,(1,2):8,(0,3):4}
cE=add(add(add(one,c1),c2),c3)
TB=mul(power(add(one,h),3),power(add(one,H),5))
# Degree-by-degree formal inverse truncated at total degree three.
inv=one; term=one; neg={k:-v for k,v in add(cE,{(0,0):-1}).items()}
for _ in range(3):
 term=mul(term,neg); inv=add(inv,term)
cTX=mul(TB,inv)
c3TX={k:v for k,v in cTX.items() if sum(k)==3}
assert c3TX=={(2,1):3,(1,2):-9,(0,3):-4}, c3TX
assert mul(c3,c3TX).get((2,4),0)==-88
assert 2*24-(-88)==136
# homogeneous degree-2 monomials in five variables: ordered value+derivatives at e0,e1.
mon=list(combinations_with_replacement(range(5),2))
rows=[]
for point in [0,1]:
 rows.append([int(pair==(point,point)) for pair in mon])
 for tangent in range(5):
  if tangent!=point:
   rows.append([int(pair==tuple(sorted((point,tangent)))) for pair in mon])
def rank(a):
 a=[[Fraction(t) for t in r] for r in a]
 row=0
 for col in range(len(a[0])):
  pivot=next((i for i in range(row,len(a)) if a[i][col]),None)
  if pivot is None:continue
  a[row],a[pivot]=a[pivot],a[row]
  v=a[row][col];a[row]=[x/v for x in a[row]]
  for i in range(len(a)):
   if i!=row and a[i][col]:
    v=a[i][col];a[i]=[x-v*y for x,y in zip(a[i],a[row])]
  row+=1
  if row==len(a):break
 return row
assert rank(rows)==9
print('VERIFY_OK euler=-88 nodal_fibers=136 quadric_two_point_first_jet_rank=9')
