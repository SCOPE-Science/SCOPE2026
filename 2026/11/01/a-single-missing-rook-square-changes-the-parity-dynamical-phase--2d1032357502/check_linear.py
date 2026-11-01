#!/usr/bin/env python3
"""Exact GF(2) rank/power tests of corner-deleted rook adjacency.
The finite tests supplement the dimension-independent invariant-subspace proof.
"""
def mm(A,B):
 out=[]
 for x in A:
  y=0
  while x:
   z=x&-x; k=z.bit_length()-1;x-=z;y^=B[k]
  out.append(y)
 return out

def rank(A):
 piv={}
 for v in A:
  while v:
   p=v.bit_length()-1
   if p in piv:v^=piv[p]
   else:piv[p]=v;break
 return len(piv)

def mat(a,b):
 ids=[(i,j) for i in range(a) for j in range(b) if i!=a-1 or j!=b-1]
 return [sum(1<<k for k,(u,v) in enumerate(ids) if (u==i) != (v==j)) for i,j in ids]

def expected(a,b):
 E=a*b-1
 if a%2 and b%2:
  return [E,a+b-2,a+b-2,a+b-2,a+b-2,a+b-2,a+b-2]
 if a%2==0 and b%2==0:
  return [E,a+b-2,1,0,0,0,0]
 s=b if b%2==0 else a
 return [E,a+b-1,s+1,s,s-1,s-2,s-2]

for a in range(2,12):
 for b in range(2,12):
  A=mat(a,b);E=len(A)
  P=[1<<i for i in range(E)]; rr=[]
  for t in range(7):
   rr.append(rank(P));P=mm(P,A)
  assert rr==expected(a,b),(a,b,rr,expected(a,b))
  if a%2 and b%2:
   assert mm(mm(A,A),A)==A
  elif a%2==0 and b%2==0:
   assert mm(mm(A,A),A)==[0]*E
  else:
   P=A
   for _ in range(4):P=mm(P,A)
   assert mm(P,A)==P
print('PASS punctured rook GF(2) matrix-power/rank checks: 100 parameter pairs, dimension <=120')
for a,b in [(2,2),(3,2),(3,3),(3,4),(4,4)]:
 print('base/illustration',a,b,'ranks',expected(a,b))
