#!/usr/bin/env python3
"""Exact enumerator for uniform permutation-tree degree/diameter statements.
No external dependencies; recomputes the inversion graph from an insertion word.
"""
from itertools import product,combinations
from collections import defaultdict
from fractions import Fraction as F
from math import comb

checks=0

def check(cond,msg):
 global checks
 checks+=1
 if not cond: raise AssertionError(msg)

def insertion_permutation(y):
 # y represents insertions of 3,...,n; 1 attaches a new maximum as a leaf,
 # 0 moves the prior maximum to final position.
 w=[2,1]
 for k,mode in enumerate(y,start=3):
  if mode:
   w=w[:-1]+[k,w[-1]]
  else:
   w=[k if v==k-1 else v for v in w]+[k-1]
 return w

def graph_stats(w):
 n=len(w); adj=[set() for _ in range(n)]
 for i in range(n):
  for j in range(i+1,n):
   if w[i]>w[j]:
    adj[w[i]-1].add(w[j]-1);adj[w[j]-1].add(w[i]-1)
 assert sum(map(len,adj))==2*(n-1)
 deg=tuple(sorted((len(x) for x in adj),reverse=True))
 diam=0
 for root in range(n):
  dist=[-1]*n;dist[root]=0;front=[root]
  for v in front:
   for u in adj[v]:
    if dist[u]<0:
     dist[u]=dist[v]+1;front.append(u)
  assert len(front)==n
  diam=max(diam,max(dist))
 return deg,diam,sum(d*d for d in deg)

def block_lengths(y):
 rs=[]
 for v in y:
  if not rs or v!=last:rs.append(1)
  else:rs[-1]+=1
  last=v
 return rs

def moments(n):
 N=n-2;data=defaultdict(list);values=[]
 for y in product((0,1),repeat=N):
  degree,diam,z=graph_stats(insertion_permutation(y))
  r=block_lengths(y);b=len(r)
  predicted=tuple(sorted([q+1 for q in r]+[1]*(n-b),reverse=True))
  check(degree==predicted,('degree encoding',n,y,degree,predicted))
  check(diam==b+1,('diameter',n,y,diam,b+1))
  check(z==3*n-4+sum(q*q for q in r),('Z sum',n,y,z))
  data[b].append(F(z));values.append((F(diam),F(z)))
 check(len(data)==N,('support',n,len(data)))
 for b,ls in data.items():
  check(len(ls)==2*comb(N-1,b-1) if N>1 else len(ls)==2,('counts',n,b,len(ls)))
  cond=F(sum(ls),len(ls))
  predicted=F(2*(n-1))*(1+F(n-2,b+1))
  check(cond==predicted,('conditional mean',n,b,cond,predicted))
 e_d=sum(v[0] for v in values)/len(values);e_z=sum(v[1] for v in values)/len(values)
 e_z2=sum(v[1]**2 for v in values)/len(values)
 cov=sum((d-e_d)*(z-e_z) for d,z in values)/len(values)
 var=e_z2-e_z*e_z
 cov_formula=F(6-2*N)-F(N+3,2**(N-1))
 ez_formula=F(3*n-4+3*N-4)+F(4,2**N)
 var_formula=F(24*N-120)+F(8*N*N+24*N+68,2**(N-1))-F(16,4**N)
 check(e_z==ez_formula,('mean',n,e_z,ez_formula))
 check(cov==cov_formula,('cov',n,cov,cov_formula))
 check(var==var_formula,('variance',n,var,var_formula))
 if N>1:check(cov<0,('negative cov',n))
 return (cov,var)

def conditional_coupling(n):
 # Generate every (b-1)-cut subset and each possible extra cut. Old degree
 # vector majorizes the refined degree vector by a Robin Hood splitting move.
 N=n-2
 for b in range(1,N):
  for cuts in combinations(range(1,N),b-1):
   old=tuple(sorted(cuts)); lengths=[v-u for u,v in zip((0,)+old,old+(N,))]
   old_deg=sorted([v+1 for v in lengths]+[1]*(n-b),reverse=True)
   for c in set(range(1,N))-set(cuts):
    refined=tuple(sorted((*cuts,c)))
    new_lengths=[v-u for u,v in zip((0,)+refined,refined+(N,))]
    new_deg=sorted([v+1 for v in new_lengths]+[1]*(n-b-1),reverse=True)
    check(sum(old_deg)==sum(new_deg),('degree sum',n,cuts,c))
    for k in range(1,n):
     check(sum(old_deg[:k])>=sum(new_deg[:k]),('majorization',n,cuts,c,k))
    check(sum(z*z for z in old_deg)>sum(z*z for z in new_deg),('strict convexity',n,cuts,c))

for n in range(3,13):
 co,va=moments(n)
 if n<=10:conditional_coupling(n)
 print('n',n,'cov',co,'variance',va)
print('PASS exact assertions:',checks)
