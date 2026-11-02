#!/usr/bin/env python3
"""Independent finite-field Frobenius-iterate checks at all exceptional orbit degrees."""
from math import comb
p=7
class Field:
 def __init__(self,coef):
  self.mod=[z%7 for z in coef];self.n=len(coef)-1;assert self.mod[-1]==1
  self.q=7**self.n
 def digits(self,a):
  v=[]
  for _ in range(self.n):v.append(a%7);a//=7
  return v
 def encode(self,v):
  z=0
  for c in v[::-1]:z=z*7+(c%7)
  return z
 def add(self,a,b):return self.encode([(u+v)%7 for u,v in zip(self.digits(a),self.digits(b))])
 def neg(self,a):return self.encode([(-u)%7 for u in self.digits(a)])
 def sub(self,a,b):return self.add(a,self.neg(b))
 def mul(self,a,b):
  A=self.digits(a);B=self.digits(b);v=[0]*(2*self.n-1)
  for i,x in enumerate(A):
   for j,y in enumerate(B):v[i+j]=(v[i+j]+x*y)%7
  for k in range(len(v)-1,self.n-1,-1):
   c=v[k]
   if c:
    for j in range(self.n):v[k-self.n+j]=(v[k-self.n+j]-c*self.mod[j])%7
  return self.encode(v[:self.n])
 def power(self,a,k):
  ans=1
  while k:
   if k&1:ans=self.mul(ans,a)
   a=self.mul(a,a);k>>=1
  return ans
 def inv(self,a):assert a;return self.power(a,self.q-2)
 def poly(self,a,cs):
  v=0
  for c in cs[::-1]:v=self.add(self.mul(v,a),c%7)
  return v

def dot(A,B,F):
 m=len(A);n=len(B[0]);q=len(B)
 Z=[[0]*n for _ in range(m)]
 for i in range(m):
  for k in range(q):
   if A[i][k]:
    for j in range(n):
     if B[k][j]:Z[i][j]=F.add(Z[i][j],F.mul(A[i][k],B[k][j]))
 return Z

def rank(A,F):
 A=[row[:] for row in A];rows=len(A);cols=len(A[0]);r=0
 for j in range(cols):
  i=next((k for k in range(r,rows) if A[k][j]),None)
  if i is None:continue
  A[i],A[r]=A[r],A[i];c=F.inv(A[r][j]);A[r]=[F.mul(c,v) for v in A[r]]
  for k in range(rows):
   if k==r or not A[k][j]:continue
   c=A[k][j];A[k]=[F.sub(x,F.mul(c,y)) for x,y in zip(A[k],A[r])]
  r+=1
 return r

def cartier_matrix(F,a):
 B=[(j,i) for j in range(1,5) for i in range((6*j)//5)]
 M=[[0]*10 for _ in range(10)]
 for col,(j,i) in enumerate(B):
  J=next(z for z in range(1,5) if (7*z-j)%5==0)
  N=(7*J-j)//5
  coeff=[1]
  for _ in range(N):
   out=[0]*(len(coeff)+2)
   for k,c in enumerate(coeff):
    out[k]=F.add(out[k],c)
    out[k+1]=F.add(out[k+1],F.mul(c,a))
    out[k+2]=F.add(out[k+2],c)
   coeff=out
  for row,(jj,ii) in enumerate(B):
   exp=7*(ii+1)-1-i
   if jj==J and exp>=0 and exp%3==0 and exp//3<len(coeff):M[row][col]=coeff[exp//3]
 return M

def test(fpoly,a,expected):
 F=Field(fpoly);M=cartier_matrix(F,a)
 assert rank(M,F)==7,(fpoly,a,'Cartier rank')
 A=[[int(i==j) for j in range(10)] for i in range(10)]
 for k in range(1,11):
  twist=[[F.power(v,7**(k-1)) for v in row] for row in M]
  A=dot(twist,A,F)
  if k==10:final=rank(A,F)
 assert final==expected,(fpoly,a,final,expected)
 q=F.poly(a,[3,0,-1,0,0,0,0,0,3,0,0,0,0,0,-2,0,3])
 assert (q==0)==(expected==0),(fpoly,a,'Q condition',q)
 print('CHECK',F.n,'degree a',a,'qzero',q==0,'Cartier rank 7, stable rank',final)

# Four irreducible factors of the exceptional polynomial in F7[u].
# a=7 denotes the polynomial class of u; coefficients are low-to-high.
for f in ([1,1,0,1],[-1,1,0,1],[3,0,-1,0,1],[2,0,2,0,3,0,1]):
 test(f,7,0)
 test(f,Field(f).add(7,1),4)
for a in [0,1,3,4,6]:test([0,1],a,4)
print('EXTENSION_RANK_OK: all exceptional Frobenius orbit degrees and controls')
