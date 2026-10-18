#!/usr/bin/env python3
"""Exact finite-field cellular boundary verification for graph Hom complexes.
Scientific input: labelled complete graphs, m disjoint ordered nonempty subsets of n colors.
"""
from itertools import product
from collections import defaultdict
from math import comb

P=1000003

def make_cells(m,n):
  out=defaultdict(list)
  for z in product(range(m+1),repeat=n):
    if any(i not in z for i in range(1,m+1)):continue
    A=tuple(tuple(v for v in range(n) if z[v]==i) for i in range(1,m+1))
    out[sum(map(len,A))-m].append(A)
  return {k:out[k] for k in sorted(out)}

def boundary(A):
  d=0
  for i,X in enumerate(A):
    if len(X)>1:
      for j in range(len(X)):
        B=list(A);B[i]=X[:j]+X[j+1:]
        yield tuple(B),(-1)**(d+j)
    d+=len(X)-1

def rank_sparse(columns):
  pivots={}
  for col in columns:
    v={k:(x%P) for k,x in col.items() if x%P}
    while v:
      k=max(v)
      if k not in pivots:
        alpha=pow(v[k],-1,P)
        pivots[k]={j:(z*alpha)%P for j,z in v.items()}
        break
      factor=v[k]
      for j,x in pivots[k].items():
        new=(v.get(j,0)-factor*x)%P
        if new:v[j]=new
        elif j in v:del v[j]
  return len(pivots)

def test(m,n):
  C=make_cells(m,n)
  ranks={}
  for d in range(1,n-m+1):
    down={A:i for i,A in enumerate(C[d-1])}
    cols=[]
    for A in C[d]:
      col={}
      for B,s in boundary(A):col[down[B]]=s
      cols.append(col)
    ranks[d]=rank_sparse(cols)
  ranks[0]=1 # augmented C_0 -> Z, since every vertex maps to 1
  hom={d:len(C[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in C}
  expect={d:(sum((-1)**j*comb(m,j)*(j-1)**n for j in range(2,m+1))*(-1)**m if d==n-m else 0) for d in C}
  if hom!=expect:raise AssertionError((m,n,hom,expect))
  print('checked',m,n,'cell_counts',{d:len(x) for d,x in C.items()},'ranks',ranks,'reduced_betti',hom)

if __name__=='__main__':
  for m,n in [(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(3,6),(4,4),(4,5)]: test(m,n)
  print('VERIFY_CHAIN_OK')
