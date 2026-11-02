#!/usr/bin/env python3
"""Independent GF(25) semilinear Cartier-replay checks. Only finite sampling."""
import random
p=5
# Represent a+b*T, T^2=2 over F5. Integer encodes a+5*b.
def add(x,y):return ((x%5+y%5)%5)+5*((x//5+y//5)%5)
def sub(x,y):return ((x%5-y%5)%5)+5*((x//5-y//5)%5)
def mul(x,y):
 a,b=x%5,x//5;c,d=y%5,y//5
 return (a*c+2*b*d)%5+5*((a*d+b*c)%5)
def power(x,n):
 z=1
 while n:
  if n&1:z=mul(z,x)
  x=mul(x,x);n//=2
 return z
def inv(x):return power(x,23) if x else 0

def polytrim(a):
 while a and a[-1]==0:a.pop()
 return a

def polymul(a,b):
 z=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):z[i+j]=add(z[i+j],mul(x,y))
 return z

def polygcd(a,b):
 a=polytrim(a[:]);b=polytrim(b[:])
 while b:
  c=a[:];q=inv(b[-1]);n=len(b)
  while len(c)>=n:
   h=mul(c[-1],q);d=len(c)-n
   for j,y in enumerate(b):c[d+j]=sub(c[d+j],mul(h,y))
   polytrim(c)
  a,b=b,c
 return a

def rank(A):
 A=[row[:] for row in A]; h=0
 for j in range(len(A[0])):
  i=next((i for i in range(h,len(A)) if A[i][j]),None)
  if i is None:continue
  A[h],A[i]=A[i],A[h]
  z=inv(A[h][j]);A[h]=[mul(z,v) for v in A[h]]
  for i in range(len(A)):
   if i==h:continue
   z=A[i][j]
   if z:A[i]=[sub(x,mul(z,y)) for x,y in zip(A[i],A[h])]
  h+=1
  if h==len(A):break
 return h

def cartier_apply(v,V,W):
 # source basis: dx/y, dx/y^2, x dx/y^2, x^2 dx/y^2
 # C is 5^(-1)-linear; the inverse Frobenius in GF25 is u->u^5.
 r=[0]*4
 for i in range(3):
  r[0]=add(r[0],power(mul(v[i+1],W[i]),5))
  r[i+1]=power(mul(v[0],V[i]),5)
 return r

rng=random.Random(14052026); totals={}; tested=0
for _ in range(6000):
 c0,c1,c2,c3,c4=[rng.randrange(25) for i in range(5)]
 f=[c0,c1,c2,c3,c4,1]
 deriv=[mul(i%5,f[i]) for i in range(1,6)]
 if len(polygcd(f,deriv))>1:continue
 cube=polymul(polymul(f,f),f)
 V=[cube[j] for j in (4,9,14)];W=[c4,c3,c2]
 # Verify explicit coefficient expressions in GF25.
 e0=add(add(add(mul(3,mul(c4,mul(c0,c0))),mul(c3,mul(c1,c0))),mul(3,mul(c2,mul(c2,c0)))),mul(3,mul(c2,mul(c1,c1))))
 e1=0
 for x in [mul(c4,c0),mul(c3,c1),mul(3,mul(c2,c2)),mul(3,mul(mul(c4,c4),c1)),mul(c4,mul(c3,c2)),power(c3,3)]:e1=add(e1,x)
 assert V==[e0,e1,mul(3,c4)]
 H=0
 for u,w in zip(V,W):H=add(H,mul(u,power(w,5)))
 vectors=[]
 for i in range(4):
  v=[0]*4;v[i]=1
  for r in range(7):v=cartier_apply(v,V,W)
  vectors.append(v)
 R=rank([[vectors[j][i] for j in range(4)] for i in range(4)])
 expected=2 if H else 0
 assert R==expected,(f,V,W,H,R)
 first=[]
 for i in range(4):
  v=[0]*4;v[i]=1
  first.append(cartier_apply(v,V,W))
 a_number=4-rank([[first[j][i] for j in range(4)] for i in range(4)])
 assert a_number in (2,4)
 assert a_number==4 if W==[0,0,0] else a_number==2
 totals[(expected,a_number)]=totals.get((expected,a_number),0)+1
 tested+=1
print('GF25_SMOOTH_TESTS',tested,'STRATA',totals)
assert tested>4500 and all(v>0 for v in totals.values())
print('GF25_SEMILINEAR_CARTIER_OK')
