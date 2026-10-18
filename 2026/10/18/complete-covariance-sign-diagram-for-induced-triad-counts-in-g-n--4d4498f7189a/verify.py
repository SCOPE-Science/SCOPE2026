"""Reproduce exact induced-triad covariance identities in independent-edge random graphs."""
from fractions import Fraction as F
from math import comb
from itertools import combinations

def formula(n,p):
 q=[F(comb(3,j))*p**j*(1-p)**(3-j) for j in range(4)]
 d=[q[j]*F(j-3*p,3*p*(1-p)) for j in range(4)]
 N=comb(n,3)
 return [[N*((q[i] if i==j else 0)-q[i]*q[j]+3*(n-3)*p*(1-p)*d[i]*d[j]) for j in range(4)] for i in range(4)]

def exhaustive(n,p):
 edges=list(combinations(range(n),2)); triples=list(combinations(range(n),3)); epos={e:k for k,e in enumerate(edges)}
 masks=[[epos[tuple(sorted(e))] for e in combinations(tri,2)] for tri in triples]
 Es=[F(0) for _ in range(4)]; M=[[F(0) for _ in range(4)] for _ in range(4)]
 for graph in range(1<<len(edges)):
  k=graph.bit_count();weight=p**k*(1-p)**(len(edges)-k)
  cnt=[0]*4
  for tri in masks:cnt[sum((graph>>e)&1 for e in tri)]+=1
  for i in range(4):
   Es[i]+=weight*cnt[i]
   for j in range(4):M[i][j]+=weight*cnt[i]*cnt[j]
 return [[M[i][j]-Es[i]*Es[j] for j in range(4)] for i in range(4)]

checks=0
for n in range(3,6):
 for p in [F(1,6),F(1,4),F(1,3),F(1,2),F(2,3),F(3,4),F(5,6)]:
  a=formula(n,p);b=exhaustive(n,p)
  for i in range(4):
   for j in range(4):
    assert a[i][j]==b[i][j],(n,p,i,j,a[i][j],b[i][j]);checks+=1
  if n>=4:
   D=3*n-8
   limits={(0,1):F(n-2,D),(0,2):F(2*n-5,D),(1,3):F(n-3,D),(2,3):F(2*(n-3),D)}
   for (i,j),x in limits.items():
    expected=(p>x if i==0 else p<x)
    if p!=x:assert (a[i][j]>0)==expected
    else:assert a[i][j]==0
    checks+=1
   assert a[0][3]<0;checks+=1
print('Exact triad covariance checks:',checks)
