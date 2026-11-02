#!/usr/bin/env python3
"""Exact finite-characteristic checks of the cyclic-octic coefficient identities.
Finite tests support, but do not replace, the infinite-characteristic proof.
"""
from math import comb

def add(a,b,p):
 c=[0]*max(len(a),len(b))
 for i,x in enumerate(a):c[i]=(c[i]+x)%p
 for i,x in enumerate(b):c[i]=(c[i]+x)%p
 return c

def mul(a,b,p):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
 return c

def sub(a,b,p):return add(a,[(-x)%p for x in b],p)
def power(a,n,p):
 v=[1]
 for _ in range(n):v=mul(v,a,p)
 return v

def same(a,b,p):
 n=max(len(a),len(b))
 return all(((a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0))%p==0 for i in range(n))

def T(m,k,p):
 if k<0 or k>2*m:return [0]
 c=[0]*(k+1)
 for j in range(max(0,k-m),(k//2)+1):c[k-2*j]=comb(m,j)*comb(m-j,k-2*j)%p
 return c

def evaluate(a,r,p):return sum(v*pow(r,i,p) for i,v in enumerate(a))%p

def rank(M,p):
 A=[row[:] for row in M];k=0
 for col in range(len(A[0])):
  piv=next((i for i in range(k,len(A)) if A[i][col]%p),None)
  if piv is None:continue
  A[piv],A[k]=A[k],A[piv]; v=pow(A[k][col],-1,p)
  A[k]=[(u*v)%p for u in A[k]]
  for i in range(len(A)):
   if i!=k:
    z=A[i][col]
    A[i]=[(a-z*b)%p for a,b in zip(A[i],A[k])]
  k+=1
 return k

for p in (17,41,73,89,97,113,137,193):
 h=(p-1)//8
 assert 8*h+1==p
 P=T(2*h,h,p); Q=T(4*h,2*h,p); C=T(6*h,5*h,p)
 A=T(6*h,h,p);B=T(6*h,h-1,p);D=T(6*h,3*h,p);E=T(6*h,3*h-1,p)
 delta=sub(mul(A,D,p),mul(B,E,p),p)
 kappa=comb(6*h,h)*comb(6*h,3*h)%p
 assert same(delta,[(kappa*x)%p for x in power([(-4)%p,0,1],2*h,p)],p),(p,'delta')
 scalar=comb(6*h,5*h)*pow(comb(2*h,h),-1,p)%p
 rhs=mul(power([(-4)%p,0,1],2*h,p),P,p)
 assert same(C,[(scalar*x)%p for x in rhs],p),(p,'C')
 # Independent finite-field matrices from the coefficient of f^m.
 for r in range(p):
  if r*r%p==4:continue
  groups=[]
  for j in (1,2,3):
   mm=(p-1)*j//4
   mat=[]
   for t in range(j):
    row=[]
    for i in range(j):
     expo=p*(t+1)-1-i-mm
     row.append(evaluate(T(mm,expo//2,p),r,p) if expo%2==0 else 0)
    mat.append(row)
   groups.append(mat)
  got=sum(rank(m,p) for m in groups)
  expected=2+2*bool(evaluate(P,r,p))+2*bool(evaluate(Q,r,p))
  assert got==expected,(p,r,got,expected)
print('VERIFY_OK: symbolic determinant and factorization, 8 prime characteristics, exhaustive rational parameters and independent Cartier ranks')
