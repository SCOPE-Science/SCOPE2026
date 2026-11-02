#!/usr/bin/env python3
"""Independent GF(11) Cartier-matrix coefficient extraction and stable-rank census."""
from collections import Counter
P=11

def mul_poly(u,v):
 out=[0]*(len(u)+len(v)-1)
 for i,vi in enumerate(u):
  for j,vj in enumerate(v):out[i+j]=(out[i+j]+vi*vj)%P
 return out

def ppow(u,n):
 out=[1]
 for _ in range(n):out=mul_poly(out,u)
 return out

def matmul(A,B):
 return [[sum(A[i][k]*B[k][j] for k in range(len(B)))%P for j in range(len(B[0]))] for i in range(len(A))]

def rank(A):
 R=[r[:] for r in A];n=len(R);m=len(R[0]);r=0
 for j in range(m):
  k=next((i for i in range(r,n) if R[i][j]%P),None)
  if k is None:continue
  R[r],R[k]=R[k],R[r]
  inv=pow(R[r][j],-1,P); R[r]=[(v*inv)%P for v in R[r]]
  for i in range(n):
   if i!=r:
    v=R[i][j]
    R[i]=[(R[i][h]-v*R[r][h])%P for h in range(m)]
  r+=1
  if r==n:break
 return r

def det_poly(f):
 # Monic quintic is squarefree iff gcd(f,f')=1, using modular long division.
 def trim(v):
  while v and v[-1]%P==0:v.pop()
  return v
 def remainder(v,w):
  v=trim(v[:]);w=trim(w[:]);
  while len(v)>=len(w) and v:
   q=v[-1]*pow(w[-1],-1,P)%P;off=len(v)-len(w)
   for j,z in enumerate(w):v[off+j]=(v[off+j]-q*z)%P
   trim(v)
  return v
 d=trim([(i*f[i])%P for i in range(1,len(f))]);v=f[:]
 while d:
  v,d=d,remainder(v,d)
 return len(v)==1

C=Counter();examples={}
for a in range(P):
 for b in range(P):
  f=[1,b,0,a,0,1]
  if not det_poly(f):C['singular']+=1;continue
  f2=ppow(f,2);f5=ppow(f,5);f8=ppow(f,8)
  E=[[0]*6 for _ in range(6)]
  for i in range(3):E[0][3+i]=f2[10-i]
  for i in range(3):E[3+i][0]=f8[10+11*i]
  for i in range(2):
   for j in range(2):E[1+i][1+j]=f5[10+11*i-j]
  cur=[r[:] for r in E];
  for _ in range(5):cur=matmul(cur,E)
  ar=6-rank(E);fr=rank(cur)
  aa=a%P;bb=b%P
  # Characteristic-11 residue-form evaluations of the extracted blocks.
  V0=f8[10];V2=f8[32];m10=f5[21];m01=f5[9]
  L=(V0+2*pow(a,11,P)*V2)%P
  D=(f5[10]*f5[20]-m01*m10)%P
  # The 2x2 block indices are [10,9;21,20], and f5[20]=5.
  K=(pow(m10,11,P)*m01+3)%P
  assert f5[20]==5
  want_a=2+(D==0)
  want_f=2*(L!=0)+(2 if D else (1 if K else 0))
  assert (ar,fr)==(want_a,want_f),(a,b,ar,fr,want_a,want_f)
  C[(fr,ar)]+=1;examples.setdefault((fr,ar),(a,b))
assert C=={'singular':10,(4,2):86,(2,2):15,(3,3):10},C
print('DIRECT_GF11_121_CURVES_CARTIER_STABLE_RANK_OK',dict(C),examples)
