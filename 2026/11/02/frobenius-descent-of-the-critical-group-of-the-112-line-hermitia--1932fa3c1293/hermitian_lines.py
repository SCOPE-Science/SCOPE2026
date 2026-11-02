#!/usr/bin/env python3
"""Reconstruct the 112 lines on the Hermitian quartic over F9 and compute Laplacian elementary divisors."""
import collections
from math import gcd

P=3
MUL = [[0]*9 for _ in range(9)]
for i in range(9):
 a,b=i%3,i//3
 for j in range(9):
  c,d=j%3,j//3
  MUL[i][j]=((a*c+2*b*d)%3)+3*((a*d+b*c)%3)
INV={a:next(b for b in range(1,9) if MUL[a][b]==1) for a in range(1,9)}
def add(a,b): return ((a%3+b%3)%3)+3*((a//3+b//3)%3)
def neg(a): return (-a%3)+3*(-(a//3)%3)
def mul(a,b): return MUL[a][b]
def conj(a): return (a%3)+3*((-(a//3))%3)
def norm(a):
 r=mul(a,conj(a)); assert r<3
 return r

def canonical(z):
 a=next(v for v in z if v)
 inv=INV[a]
 return tuple(mul(v,inv) for v in z)

def normzero(z):return sum(norm(v) for v in z)%3==0

def orthog(a,b):
 v=0
 for x,y in zip(a,b): v=add(v,mul(x,conj(y)))
 return v==0

def enumerator():
 points={canonical((a,b,c,d)) for a in range(9) for b in range(9) for c in range(9) for d in range(9) if (a,b,c,d)!=(0,0,0,0)}
 assert len(points)==820
 iso=sorted(p for p in points if normzero(p))
 assert len(iso)==280
 lines=set()
 for i,a in enumerate(iso):
  for b in iso[i+1:]:
   if not orthog(a,b):continue
   line=frozenset(canonical(tuple(add(mul(s,aa),mul(t,bb)) for aa,bb in zip(a,b))) for s in range(9) for t in range(9) if s or t)
   assert len(line)==10 and line.issubset(set(iso))
   lines.add(line)
 assert len(lines)==112, len(iso)
 return sorted(lines,key=lambda s:tuple(sorted(s)))

def adjacency(lines):
 n=len(lines)
 A=[[0]*n for _ in range(n)]
 for i in range(n):
  for j in range(i+1,n):
   if len(lines[i]&lines[j])==1:A[i][j]=A[j][i]=1
   else:assert not lines[i]&lines[j]
 assert all(sum(r)==30 for r in A)
 assert sum(map(sum,A))//2==1680
 # GQ pair count common neighbors from adjacency
 cc=collections.Counter()
 for i in range(n):
  for j in range(i+1,n):
   common=sum(A[i][k]*A[j][k] for k in range(n))
   cc[(A[i][j],common)]+=1
 assert cc=={(1,2):1680,(0,10):4536},cc
 # Minimal polynomial A^2=20I-8A+10J [lambda-mu=-8], precisely.
 for i in range(n):
  for j in range(n):
   common=sum(A[i][k]*A[j][k] for k in range(n))
   assert common == (30 if i==j else (2 if A[i][j] else 10))
 return A

def valuation(n,p,E):
 if n==0:return E
 v=0
 while n%p==0:
  n//=p;v+=1
 return v

def local_snf(A,p,E):
 n=len(A);mod=p**E
 B=[[((30 if i==j else 0)-A[i][j])%mod for j in range(n-1)] for i in range(n-1)]
 vals=[]
 for k in range(n-1):
  best=E; spot=None
  for i in range(k,n-1):
   for j in range(k,n-1):
    v=valuation(B[i][j],p,E)
    if v<best:best=v;spot=(i,j)
    if best==0:break
   if best==0:break
  if spot is None:raise RuntimeError(f'modulus {p}^{E} too small after {k} pivots')
  i,j=spot;B[i],B[k]=B[k],B[i]
  for row in B:row[j],row[k]=row[k],row[j]
  a=B[k][k]
  power=p**best
  inv=pow((a//power)%(mod//power),-1,mod//power)
  for i in range(k+1,n-1):
   if not B[i][k]:continue
   assert B[i][k]%power==0
   factor=((B[i][k]//power)*inv)%(mod//power)
   Bi=B[i];Bk=B[k]
   for j in range(k,n-1):Bi[j]=(Bi[j]-factor*Bk[j])%mod
   assert Bi[k]==0
  for j in range(k+1,n-1):
   if not B[k][j]:continue
   assert B[k][j]%power==0
   factor=((B[k][j]//power)*inv)%(mod//power)
   for i in range(k,n-1):B[i][j]=(B[i][j]-factor*B[i][k])%mod
   assert B[k][j]==0
  vals.append(best)
 counts=collections.Counter(vals)
 assert sum(vals)=={2:239,5:21,7:89}[p],(p,E,counts,sum(vals))
 return counts

if __name__=='__main__':
 import json,sys,time
 st=time.monotonic();lines=enumerator()
 A=adjacency(lines)
 print('LINES',len(lines),'EDGES',sum(map(sum,A))//2,'GQ(s,t)=GQ(9,3)','seconds',round(time.monotonic()-st,2),flush=True)
 data={}
 for p,E in [(2,16),(5,9),(7,9)]:
  c=local_snf(A,p,E)
  data[str(p)]={str(k):v for k,v in sorted(c.items())}
  print('PADIC',p,'counts',dict(sorted(c.items())),'seconds',round(time.monotonic()-st,2),flush=True)
 n=111
 # Combine elementary divisors by nondecreasing list for each prime.
 factors=[1]*n
 for pp,c in data.items():
  pp=int(pp)
  vls=[]
  for exp,count in sorted(((int(k),v) for k,v in c.items())):
   vls += [exp]*count
  assert len(vls)==n
  factors=[f*pp**e for f,e in zip(factors,vls)]
 assert all(b%a==0 for a,b in zip(factors,factors[1:]))
 fact_counts=collections.Counter(factors)
 print('INVARIANTS',sorted(fact_counts.items()),'seconds',round(time.monotonic()-st,2),flush=True)
 from pathlib import Path
 with (Path(__file__).resolve().parent/'hermitian_certificate.json').open('w') as f:
  json.dump({'field':'F3[T]/(T^2+1)','model':'sum_i x_i^4=0 over F9','points':280,'lines':112,'edges':1680,'adjacency_spectrum':{'30':1,'2':90,'-10':21},'local_smith':data,'invariant_factors':[[k,v] for k,v in sorted(fact_counts.items())]},f,indent=2)
