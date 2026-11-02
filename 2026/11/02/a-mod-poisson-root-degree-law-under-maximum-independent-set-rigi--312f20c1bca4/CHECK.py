#!/usr/bin/env python3
"""Finite exact checks for root-essential recursive-tree degree laws."""
from fractions import Fraction as F
from itertools import product
from math import factorial

NMAX=12
# Basic generating-series operations, all exact rationals.
def mul(a,b,n=NMAX):
 c=[F(0)]*(n+1)
 for i,x in enumerate(a[:n+1]):
  for j,y in enumerate(b[:n+1-i]): c[i+j]+=x*y
 return c

def inv(a,n=NMAX):
 assert a[0]==1
 c=[F(1)]+[F(0)]*n
 for k in range(1,n+1):c[k]=-sum(a[j]*c[k-j] for j in range(1,k+1))
 return c

L=[F(0)]+[F(1,k) for k in range(1,NMAX+1)]
# exp(E)=1+L ==> E'=L'/(1+L)
Lprime=[F(k+1)*L[k+1] if k<NMAX else F(0) for k in range(NMAX+1)]
Eprime=mul(Lprime,inv([F(1)+L[0]]+L[1:]))
E=[F(0)]+[Eprime[k-1]/k for k in range(1,NMAX+1)]
N=[L[k]-E[k] for k in range(NMAX+1)]
# P_n(u) coefficients from F(z,u)=exp(u*N(z)); coeff of u^d is N(z)^d/d!.
power=[F(1)]+[F(0)]*NMAX
Fpoly={n:{} for n in range(1,NMAX+2)}
for d in range(NMAX+1):
 for n in range(1,NMAX+2):
  coeff=power[n-1]/factorial(d)
  if coeff: Fpoly[n][d]=coeff
 power=mul(power,N)

checks=0
for n in range(1,9):
 counts={}
 for parents in product(*[range(j) for j in range(1,n)]):
  children=[[] for _ in range(n)]
  for i,p in enumerate(parents,start=1):children[p].append(i)
  essential=[False]*n
  for v in range(n-1,-1,-1):essential[v]=all(not essential[w] for w in children[v])
  # Independent global check: enumerate all independent sets and their maxima.
  edges=[(i,p) for i,p in enumerate(parents,start=1)]
  best=-1; maximizers=[]
  for mask in range(1<<n):
   if any((mask>>i)&1 and (mask>>j)&1 for i,j in edges):continue
   size=mask.bit_count()
   if size>best:best=size;maximizers=[mask]
   elif size==best:maximizers.append(mask)
  essential_by_global=all(mask&1 for mask in maximizers)
  assert essential[0]==essential_by_global,(n,parents,essential[0],maximizers)
  checks+=1
  if essential[0]:
   d=len(children[0]);counts[d]=counts.get(d,0)+1
  checks+=1
 for d in set(counts)|set(Fpoly[n]):
  assert F(counts.get(d,0),factorial(n-1))==Fpoly[n].get(d,0),(n,d,counts,Fpoly[n]);checks+=1
 # Cross-check with the 2019 recurrence for unmarked root essential probability.
 if n>=2:
  p=lambda j:sum(Fpoly[j].values(),F(0))
  rhs=sum((1-p(j))*p(n-j) for j in range(1,n))/F(n-1)
  assert rhs==sum(Fpoly[n].values(),F(0));checks+=1

# Nontrivial second factorial moments from the same marked series via convolution.
for n in range(1,NMAX+2):
 for q in (0,1,2):
  marked=sum(Fpoly[n].get(d,0)*F(factorial(d),factorial(d-q)) if d>=q else 0 for d in range(NMAX+1))
  series=[F(1)]+[F(0)]*NMAX
  for i in range(q):series=mul(series,N)
  base=[F(1)]+[F(0)]*NMAX
  for i in range(1,NMAX+1):base[i]=sum(N[j]*base[i-j]*j for j in range(1,i+1))/i
  expected=mul(series,base)[n-1]
  assert marked==expected,(n,q,marked,expected);checks+=1
print('PASS',checks,'exact assertions and independent recursive-tree histories')
for n in range(2,11):
 p=sum(Fpoly[n].values(),F(0))
 mean=sum(Fpoly[n].get(d,0)*d for d in Fpoly[n])/p if p else 0
 print(n, str(p),str(mean))

# Numerical asymptotic diagnostic only; it does not prove an infinite limit.
from math import log,pi
M=1000
pr=[0.0]*(M+1); ar=[0.0]*(M+1); dr=[0.0]*(M+1)
pr[1]=1.0
for n in range(2,M+1):
    pr[n]=sum((1-pr[j])*pr[n-j] for j in range(1,n))/(n-1)
    ar[n-1]=(1-pr[n-1])/(n-1)
    dr[n]=sum(ar[j]*pr[n-j] for j in range(1,n))
fr=sum(ar[j]*dr[M-j] for j in range(1,M))
mn=dr[M]/pr[M]
vr=(fr+dr[M])/pr[M]-mn*mn
pred_m=log(M)-log(log(M))+0.5772156649015329
pred_v=pred_m-pi*pi/6
assert abs(mn-pred_m)<0.05
assert abs(vr-pred_v)<0.2
print('finite-size diagnostic n=',M,'mean=',round(mn,7),'pred=',round(pred_m,7),'variance=',round(vr,7),'pred=',round(pred_v,7))
