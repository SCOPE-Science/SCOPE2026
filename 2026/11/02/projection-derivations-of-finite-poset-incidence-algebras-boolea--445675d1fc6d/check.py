#!/usr/bin/env python3
"""Exhaustive independent idempotent-derivation census for small incidence algebras."""
from itertools import product
from collections import Counter

class Field:
 def __init__(self,q):self.q=q;self.p=2 if q==4 else q
 def add(self,a,b):return (a^b) if self.p==2 else (a+b)%self.p
 def neg(self,a):return a if self.p==2 else (-a)%self.p
 def mul(self,a,b):
  if self.q!=4:return (a*b)%self.p
  v=0
  for i in range(2):
   for j in range(2):
    if ((a>>i)&1) and ((b>>j)&1):v ^=1<<(i+j)
  if v&8:v^=0b1100
  if v&4:v^=0b111
  return v
 def inv(self,a):
  for b in range(1,self.q):
   if self.mul(a,b)==1:return b
  raise AssertionError

def rnk(B,F):
 B=[row[:] for row in B]; R=len(B); C=len(B[0]); r=0
 for j in range(C):
  k=next((i for i in range(r,R) if B[i][j]),None)
  if k is None:continue
  B[k],B[r]=B[r],B[k]
  z=F.inv(B[r][j]);B[r]=[F.mul(z,x) for x in B[r]]
  for i in range(R):
   if i==r or not B[i][j]:continue
   c=F.neg(B[i][j]);B[i]=[F.add(v,F.mul(c,w)) for v,w in zip(B[i],B[r])]
  r+=1
  if r==R:break
 return r

def make_poset(n,cover):
 p=[[i==j for j in range(n)] for i in range(n)]
 for i,j in cover:p[i][j]=True
 for k in range(n):
  for i in range(n):
   for j in range(n):p[i][j]|=p[i][k] and p[k][j]
 for i in range(n):
  for j in range(n):assert i==j or not(p[i][j] and p[j][i])
 return [(i,j) for i in range(n) for j in range(n) if p[i][j]]

def verify(label,n,cover,q):
 F=Field(q);pairs=make_poset(n,cover);strict=[z for z in pairs if z[0]!=z[1]]; m=len(strict)
 E={v:i for i,v in enumerate(pairs)};d=len(pairs)
 # Generate all diagonal cocycles by the actual equation alpha(i,k)=alpha(i,j)+alpha(j,k),
 # rather than assuming they come from vertex potentials.
 cocycles=[]
 for values in product(range(q),repeat=m):
  alpha={p:0 for p in pairs};alpha.update(zip(strict,values))
  if all(alpha[(i,k)]==F.add(alpha[(i,j)],alpha[(j,k)]) for i,j in strict for jj,k in strict if j==jj and (i,k) in E):
   cocycles.append(alpha)
 obs=Counter(); preds=Counter(); nonzero=0
 for alpha in cocycles:
  flag=all(a in (0,1) for a in alpha.values())
  w=sum(alpha[z]==1 for z in strict)
  if flag:preds[w]+=q**w
  for values in product(range(q),repeat=m):
   X=dict(zip(strict,values));D=[[0]*d for _ in range(d)]
   for ci,(i,j) in enumerate(pairs):
    D[ci][ci]=alpha[(i,j)]
    for (a,b),v in X.items():
     if b==i and (a,j) in E:D[E[(a,j)]][ci]=F.add(D[E[(a,j)]][ci],v)
     if a==j and (i,b) in E:D[E[(i,b)]][ci]=F.add(D[E[(i,b)]][ci],F.neg(v))
   # Check composition for every basis vector of the original incidence algebra.
   ok=True
   for i in range(d):
    for j in range(d):
     z=0
     for k in range(d):z=F.add(z,F.mul(D[i][k],D[k][j]))
     if z!=D[i][j]:ok=False;break
    if not ok:break
   if ok:
    nonzero+=1;obs[rnk(D,F)]+=1
 assert obs==preds,(label,q,obs,preds)
 print(f'{label} q={q} n={n} comparable={m} cocycles={len(cocycles)} checked={len(cocycles)*q**m} idempotent_derivations={nonzero} ranks={dict(sorted(obs.items()))}')

cases=[('chain3',3,[(0,1),(1,2)],2),('chain3',3,[(0,1),(1,2)],3),('chain3',3,[(0,1),(1,2)],4),
 ('chain4',4,[(0,1),(1,2),(2,3)],2),('diamond',4,[(0,1),(0,2),(1,3),(2,3)],2),
 ('diamond',4,[(0,1),(0,2),(1,3),(2,3)],3),('height2cycle',4,[(0,2),(0,3),(1,2),(1,3)],2),
 ('height2cycle',4,[(0,2),(0,3),(1,2),(1,3)],3),('star',4,[(0,1),(0,2),(0,3)],2),
 ('star',4,[(0,1),(0,2),(0,3)],3), ('disconnected',4,[(0,1),(2,3)],2),('discrete',3,[],3)]
for case in cases:verify(*case)
print('INCIDENCE_PROJECTION_DERIVATIONS_OK',len(cases),'EXHAUSTIVE_CONFIGURATIONS')
