#!/usr/bin/env python3
"""Finite-field validation of dihedral-quandle-algebra R4 automorphism formulas."""
from itertools import product
from collections import Counter

def prod(x,y,p):
 z=[0]*4
 for i,a in enumerate(x):
  if a:
   for j,b in enumerate(y):
    if b:
     z[(2*j-i)%4]=(z[(2*j-i)%4]+a*b)%p
 return tuple(z)

def rank(cols,p):
 A=[[c[r]%p for c in cols] for r in range(4)];rr=0
 for j in range(4):
  k=next((k for k in range(rr,4) if A[k][j]),None)
  if k is None:continue
  A[rr],A[k]=A[k],A[rr]
  z=pow(A[rr][j],-1,p)
  A[rr]=[a*z%p for a in A[rr]]
  for k in range(4):
   if k!=rr:
    t=A[k][j];A[k]=[(a-t*b)%p for a,b in zip(A[k],A[rr])]
  rr+=1
 return rr

def isauto(cols,p):
 if rank(cols,p)!=4: return False
 for i in range(4):
  for j in range(4):
   if cols[(2*j-i)%4]!=prod(cols[i],cols[j],p):return False
 return True

def parity_swap():
 return ((0,1,0,0),(1,0,0,0),(0,0,0,1),(0,0,1,0))

def sample_bases(p):
 # For char2: basis (a,b,u,s) with a=e0 b=e1 u=e0+e2 s=e1+e3
 e=lambda i: tuple(1 if j==i else 0 for j in range(4))
 if p==2:
  u=tuple((e(0)[i]+e(2)[i])%p for i in range(4));s=tuple((e(1)[i]+e(3)[i])%p for i in range(4))
  for swap in [0,1]:
   for t in product(range(p),repeat=4):
    A=e(swap);B=e(1-swap);U=s if swap else u;S=u if swap else s
    F0=tuple((A[i]+t[0]*u[i]+t[1]*s[i])%p for i in range(4))
    F1=tuple((B[i]+t[2]*u[i]+t[3]*s[i])%p for i in range(4))
    F2=tuple((F0[i]+U[i])%p for i in range(4))
    F3=tuple((F1[i]+S[i])%p for i in range(4))
    yield(F0,F1,F2,F3)
 else:
  # P=id / swap on U=span(e0+e2,e1+e3), R eigenbasis v=e0-e2,t=e1-e3
  inv2=pow(2,-1,p)
  u=(1,0,1,0);s=(0,1,0,1);v=(1,0,p-1,0);t=(0,1,0,p-1)
  for sw in [0,1]:
   for x,y in product(range(1,p),repeat=2):
    Uf,Sf=(s,u) if sw else (u,s)
    Vf,Tf=((tuple(y*t[i]%p for i in range(4)),tuple(x*v[i]%p for i in range(4))) if sw else
           (tuple(x*v[i]%p for i in range(4)),tuple(y*t[i]%p for i in range(4))))
    F0=tuple((Uf[i]+Vf[i])*inv2%p for i in range(4));F2=tuple((Uf[i]-Vf[i])*inv2%p for i in range(4))
    F1=tuple((Sf[i]+Tf[i])*inv2%p for i in range(4));F3=tuple((Sf[i]-Tf[i])*inv2%p for i in range(4))
    yield (F0,F1,F2,F3)

def main():
 for p in [2,3,5]:
  candidates=set(sample_bases(p))
  assert len(candidates)==(2*p**4 if p==2 else 2*(p-1)**2),(p,len(candidates))
  assert all(isauto(cols,p) for cols in candidates),p
  if p==2:
   pts=list(product(range(p),repeat=4)); brute=0; found=set();invertible=0
   for cols in product(pts,repeat=4):
    if rank(cols,p)!=4:continue
    invertible+=1
    if isauto(cols,p):brute+=1;found.add(cols)
   assert found==candidates,(len(found),len(candidates));print(f'GF({p}) invertible={invertible} automorphisms={brute} exhaustive_match=yes')
  else:
   import random
   random.seed(p)
   pts=list(product(range(p),repeat=4));tested=0
   for _ in range(5000):
    cols=tuple(random.choice(pts) for j in range(4))
    if cols not in candidates:
     assert not isauto(cols,p),('unexpected',cols)
     tested+=1
   print(f'GF({p}) predicted_automorphisms={len(candidates)} random_nonmembers_tested={tested} no_counterexample=yes')
if __name__=='__main__':main()

def check_gf4():
 def m(a,b):
  out=0
  for i in range(2):
   for j in range(2):
    if (a>>i)&1 and (b>>j)&1:out^=(1<<(i+j))
  if out&8:out^=14
  if out&4:out^=7
  return out
 def inv(a):return next(t for t in (1,2,3) if m(a,t)==1)
 def prod4(x,y):
  z=[0]*4
  for i,a in enumerate(x):
   for j,b in enumerate(y):
    z[(2*j-i)%4]^=m(a,b)
  return tuple(z)
 def rank4(cols):
  A=[[c[r] for c in cols] for r in range(4)];rr=0
  for j in range(4):
   k=next((k for k in range(rr,4) if A[k][j]),None)
   if k is None:continue
   A[rr],A[k]=A[k],A[rr];ii=inv(A[rr][j]);A[rr]=[m(a,ii) for a in A[rr]]
   for k in range(4):
    if k!=rr:
     t=A[k][j];A[k]=[a^m(t,b) for a,b in zip(A[k],A[rr])]
   rr+=1
  return rr
 def valid(cols):
  return rank4(cols)==4 and all(cols[(2*j-i)%4]==prod4(cols[i],cols[j]) for i in range(4) for j in range(4))
 e=lambda i: tuple(int(j==i) for j in range(4))
 u=(1,0,1,0);s=(0,1,0,1);fnd=set()
 for swap in [0,1]:
  for t in product(range(4),repeat=4):
   A=e(swap);B=e(1-swap);U=s if swap else u;S=u if swap else s
   F0=tuple(A[i]^(m(t[0],u[i])^m(t[1],s[i])) for i in range(4))
   F1=tuple(B[i]^(m(t[2],u[i])^m(t[3],s[i])) for i in range(4))
   F2=tuple(F0[i]^U[i] for i in range(4));F3=tuple(F1[i]^S[i] for i in range(4))
   fnd.add((F0,F1,F2,F3))
 assert len(fnd)==512 and all(valid(c) for c in fnd)
 import random
 random.seed(44);pts=list(product(range(4),repeat=4));cnt=0
 for _ in range(5000):
  cols=tuple(random.choice(pts) for _ in range(4))
  if cols not in fnd:assert not valid(cols);cnt+=1
 print(f'GF(4) predicted_automorphisms={len(fnd)} random_nonmembers_tested={cnt} no_counterexample=yes')

if __name__=='__main__':check_gf4()
