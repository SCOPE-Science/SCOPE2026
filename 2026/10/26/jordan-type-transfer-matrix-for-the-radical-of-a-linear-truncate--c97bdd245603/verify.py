#!/usr/bin/env python3
"""Independent matrix realization of left-regular multiplication; prime-field exhaustive tests."""
from itertools import product
from collections import defaultdict

def rank(A,q):
 n=len(A);m=len(A[0]); A=[row[:] for row in A];r=0
 for j in range(m):
  i=next((i for i in range(r,n) if A[i][j]%q),None)
  if i is None:continue
  A[r],A[i]=A[i],A[r]
  d=pow(A[r][j],-1,q); A[r]=[v*d%q for v in A[r]]
  for k in range(r+1,n):
   if A[k][j]:
    v=A[k][j];A[k]=[(u-v*w)%q for u,w in zip(A[k],A[r])]
  r+=1
  if r==n:break
 return r

def exact(n,q):
 d=3*n-3 if n>=2 else 1
 out=defaultdict(int)
 for coords in product(range(q),repeat=max(0,2*n-3)):
  aa=list(coords[::2]);bb=list(coords[1::2]);L=[[0]*d for _ in range(d)]
  # left action on vertex primitive idempotents: L_x e_j
  for i,a in enumerate(aa): L[n+i][i+1]=a
  for i,b in enumerate(bb): L[2*n-1+i][i+2]=b
  # left action on the arrows: L_x u_j
  for i in range(n-2):L[2*n-1+i][n+i+1]=aa[i]
  LL=[[sum(L[i][k]*L[k][j] for k in range(d))%q for j in range(d)] for i in range(d)]
  out[(rank(L,q),rank(LL,q))]+=1
 return dict(out)

def formula(n,q):
 if n==1:return {(0,0):1}
 c=q-1
 out=defaultdict(int)
 for aa in product((0,1),repeat=n-1):
  initial=c**sum(aa)
  k=sum(aa)+sum(aa[:-1])
  s=sum(aa[i]*aa[i+1] for i in range(n-2))
  temp={(0,0):initial}
  for i in range(n-2):
   if aa[i] or aa[i+1]:temp={key:val*q for key,val in temp.items()}
   else:
    upd=defaultdict(int)
    for (b,r),v in temp.items():
     upd[(b,r)]+=v
     upd[(b,r+1)]+=v*c
    temp=upd
  for (b,extra),v in temp.items():out[(k+extra,s)]+=v
 return dict(out)

def transfer(n,q):
 if n==1:return {(0,0):1}
 if n==2:return {(0,0):1,(1,0):q-1}
 c=q-1
 st={(0,0,0):1,(1,2,0):c} # previous a nonzero, rank, rank-square
 for j in range(2,n):
  nxt=defaultdict(int)
  for (a,r,s),v in st.items():
   for b in (0,1):
    new_r=r+b*(1 if j==n-1 else 2)
    new_s=s+a*b
    choices=q if a or b else 1+c # extra rank if both a,b zero
    if a or b:
     nxt[(b,new_r,new_s)]+=v*choices*c**b
    else:
     nxt[(b,new_r,new_s)]+=v
     nxt[(b,new_r+1,new_s)]+=v*c
  st=nxt
 out=defaultdict(int)
 for (a,r,s),v in st.items():out[(r,s)]+=v
 return dict(out)

for n in range(1,8):
 for q in (2,3,5):
  if q**max(0,2*n-3)>25000:continue
  brute=exact(n,q); via=formula(n,q); trans=transfer(n,q)
  assert brute==via==trans,(n,q,brute,via,trans)
  assert sum(brute.values())==q**max(0,2*n-3)
  D=3*n-3 if n>=2 else 1
  for (r,s) in brute:
   assert r-2*s>=0 and D-2*r+s>=0
  print('n',n,'q',q,'Jordan types',len(brute),'total',sum(brute.values()),'OK')
print('VERIFY_OK_REGULAR_NAKAYAMA_JORDAN')
