#!/usr/bin/env python3
"""Independent finite checks for nilpotency-height/rank profiles of order-preserving partial translations.
Only Python standard library required.
"""
from collections import defaultdict
from itertools import product
from math import exp

def addpoly(a,b):
 c=[0]*max(len(a),len(b))
 for i,x in enumerate(a):c[i]+=x
 for i,x in enumerate(b):c[i]+=x
 return c

def mulpoly(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c

def powerpoly(a,d):
 c=[1]
 while d:
  if d&1:c=mulpoly(c,a)
  d>>=1
  if d:a=mulpoly(a,a)
 return c

def word_polynomials(maxlen,k):
 """Each coefficient tracks a binary word's number of ones, by a trailing-one automaton."""
 state=[[1]]+[[0] for j in range(k-1)]
 polys=[[1]]
 for m in range(1,maxlen+1):
  nxt=[[0] for _ in range(k)]
  for run,coef in enumerate(state):
   nxt[0]=addpoly(nxt[0],coef)
   if run+1<k:nxt[run+1]=addpoly(nxt[run+1],[0]+coef)
  state=nxt
  p=[0]
  for coef in state:p=addpoly(p,coef)
  polys.append(p)
 return polys

def predicted(n,k):
 A=word_polynomials(n,k)
 out=[1]
 for d in range(1,n):
  m=n-d;q,r=divmod(m,d)
  P=mulpoly(powerpoly(A[q+1],r),powerpoly(A[q],d-r))
  out=addpoly(out,[2*x for x in P])
  out[0]-=2
 return out

def compose(f,g):
 # f after g
 return tuple(-1 if y<0 else f[y] for y in g)

def index_of(f):
 zero=(-1,)*len(f)
 t=f; idx=1
 while t!=zero:
  t=compose(f,t);idx+=1
  assert idx<=len(f)+2, ('unexpected nonnilpotency',f)
 return idx

def observed(n):
 acc={};zero=(-1,)*n;acc[zero]=1
 for d in range(-n+1,n):
  if d==0:continue
  candidates=[i for i in range(n) if 0<=i+d<n]
  for bits in product((0,1), repeat=len(candidates)):
   if not any(bits):continue
   f=[-1]*n
   for i,bit in zip(candidates,bits):
    if bit:f[i]=i+d
   f=tuple(f);assert f not in acc
   acc[f]=index_of(f)
 return acc

def integer_run_avoidance(m_max,k):
 a=[1]
 for m in range(1,m_max+1):
  if m<k:a.append(2**m)
  elif m==k:a.append(2**k-1)
  else:a.append(2*a[-1]-a[m-k-1])
 return a

def cumulative_count(n,k):
 a=integer_run_avoidance(n,k)
 out=1
 for d in range(1,n):
  m=n-d;q,r=divmod(m,d)
  out+=2*(a[q+1]**r*a[q]**(d-r)-1)
 return out

def main():
 total=0
 for n in range(1,12):
  acc=observed(n)
  total+=len(acc)
  assert len(acc)==2**(n+1)-2*n-1,(n,len(acc))
  for k in range(1,n+1):
   p=predicted(n,k)
   tally=defaultdict(int)
   for f,idx in acc.items():
    if idx<=k:tally[sum(x>=0 for x in f)]+=1
   obs=[tally[t] for t in range(max(len(p), n+1))]
   assert obs[:len(p)]==p,(n,k,obs,p)
   assert sum(p)==cumulative_count(n,k)
  print('verified_n',n,'nilpotents',len(acc))
 for n in [128,256,512,1024,2048,4096]:
  k=n.bit_length()-1
  ratio=cumulative_count(n,k)/(2**(n+1)-2*n-1)
  print('lattice_limit_n',n,'k',k,'cdf',round(ratio,8),'target',round(exp(-0.5),8))
 print('ALL_ODP_NILPOTENCY_RANK_AND_EXTREME_CHECKS_PASSED',total)
if __name__=='__main__':main()
