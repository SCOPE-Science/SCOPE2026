#!/usr/bin/env python3
"""Separate class-representative check of generating partner counts in sl3(F2)."""
from itertools import product
# 3x3 binary matrices represented by row-major bit patterns.
def mult(A,B):
 out=0
 for i in range(3):
  for j in range(3):
   if sum(((A>>(3*i+k))&1)*((B>>(3*k+j))&1) for k in range(3))&1:
    out |= 1 << (3*i+j)
 return out
identity=0b100010001
matrices=[A for A in range(512) if (((A>>0)&1)^((A>>4)&1)^((A>>8)&1))==0]
assert len(matrices)==256
GL=[]
for g in range(512):
 for h in range(512):
  if mult(g,h)==identity and mult(h,g)==identity:
   GL.append((g,h));break
assert len(GL)==168
# 0, rank-one nilpotent, nontrivial unipotent block, regular nilpotent,
# rank-two idempotent, quadratic+linear squarefree, irreducible cubic.
representatives=[0,2,10,12,17,85,95]
expected_orbits=[1,21,84,42,28,56,24]
expected_partners=[0,0,64,64,0,72,56]

def dimension(A,B):
 # Distinct algorithm from the full run: explicit closure of independent generators.
 vectors=[]
 piv=[0]*9
 def insert(V):
  for k in range(8,-1,-1):
   if V>>k&1:
    if piv[k]:V^=piv[k]
    else:
     piv[k]=V;vectors.append(V);return
 insert(A);insert(B)
 i=0
 while i<len(vectors):
  for j in range(i):
   C=mult(vectors[i],vectors[j])^mult(vectors[j],vectors[i])
   insert(C)
  i+=1
 return len(vectors)
all_orbits=set();total=0
for A,orbit_length,partner_num in zip(representatives,expected_orbits,expected_partners):
 orbit={mult(mult(g,A),h) for g,h in GL}
 assert len(orbit)==orbit_length
 assert not (orbit & all_orbits)
 all_orbits.update(orbit)
 counts=sum(dimension(A,B)==8 for B in matrices)
 assert counts==partner_num,(A,counts,partner_num)
 total+=len(orbit)*counts
 print(f'REP {A:03d} ORBIT {len(orbit)} PARTNERS {counts}')
assert all_orbits==set(matrices)
assert total==13440
print('TOTAL_PAIRS',total)
print('VERIFY_OK')
