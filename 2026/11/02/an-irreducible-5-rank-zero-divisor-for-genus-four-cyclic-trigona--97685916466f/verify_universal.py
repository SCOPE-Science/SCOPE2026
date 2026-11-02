#!/usr/bin/env python3
"""Independent finite polynomial and semilinear Cartier verification in characteristic five."""
from itertools import product
from collections import Counter
P=5

def pmul(a,b):
 out=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]=(out[i+j]+x*y)%P
 return out

def ptrail(a):
 a=a[:]
 while a and a[-1]==0:a.pop()
 return a

def premainder(a,b):
 a=ptrail(a);b=ptrail(b)
 if not b:raise ZeroDivisionError
 inv=pow(b[-1],-1,P)
 while len(a)>=len(b):
  coeff=a[-1]*inv%P;off=len(a)-len(b)
  for j,y in enumerate(b):a[off+j]=(a[off+j]-coeff*y)%P
  a=ptrail(a)
 return a

def pgcd(a,b):
 a=ptrail(a);b=ptrail(b)
 while b:a,b=b,premainder(a,b)
 return a

def rank(a):
 a=[r[:] for r in a];m=len(a);n=len(a[0]);h=0
 for c in range(n):
  piv=next((i for i in range(h,m) if a[i][c]),None)
  if piv is None:continue
  a[h],a[piv]=a[piv],a[h]
  inv=pow(a[h][c],-1,5)
  a[h]=[x*inv%5 for x in a[h]]
  for i in range(m):
   if i!=h and a[i][c]:
    w=a[i][c];a[i]=[(x-w*y)%5 for x,y in zip(a[i],a[h])]
  h+=1
  if h==m:break
 return h

def matmul(a,b):
 return [[sum(a[i][k]*b[k][j] for k in range(len(b)))%5 for j in range(len(b[0]))] for i in range(len(a))]

def coeff(f,j):return f[j] if 0<=j<len(f) else 0

cnt=Counter(); examples={}
for c0,c1,c2,c3,c4 in product(range(5),repeat=5):
 f=[c0,c1,c2,c3,c4,1]
 der=[f[i]*i%5 for i in range(1,6)]
 if len(pgcd(f,der))>1:
  cnt['singular']+=1;continue
 f3=pmul(pmul(f,f),f)
 V=(coeff(f3,4),coeff(f3,9),coeff(f3,14));W=(c4,c3,c2)
 E0=(3*c4*c0*c0+c3*c1*c0+3*c2*c2*c0+3*c2*c1*c1)%5
 E1=(c4*c0+c3*c1+3*c2*c2+3*c4*c4*c1+c4*c3*c2+c3**3)%5
 E2=(3*c4)%5
 assert V==(E0,E1,E2),(f,V,(E0,E1,E2))
 Pval=sum(V[i]*pow(W[i],5,5) for i in range(3))%5
 B=[[0,W[0],W[1],W[2]], [V[0],0,0,0],[V[1],0,0,0],[V[2],0,0,0]]
 a=4-rank(B)
 Q=B
 for _ in range(5): Q=matmul(Q,B)
 p_rank=rank(Q)
 assert p_rank==(2 if Pval else 0),(f,p_rank,Pval)
 cnt[f'p{p_rank}_a{a}']+=1
 examples.setdefault((p_rank,a),tuple(f))
print('CENSUS',dict(sorted(cnt.items())))
print('EXAMPLES',dict(sorted(examples.items())))
assert sum(cnt.values())==5**5
print('CHAR5_UNIVERSAL_EXACT_OK')
