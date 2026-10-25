#!/usr/bin/env python3
"""Reproducible exact checks for fixed-cardinality assignment-polytope ellipsoids.

Only Python 3 standard library; this script checks finite instances and exact
algebraic inequalities. The proof of the all-dimensional result is in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations, permutations

def fmatrix(m,n,k):
    verts=[]
    for rows in combinations(range(m),k):
        for cols in combinations(range(n),k):
            for pc in permutations(cols):
                v=[0]*(m*n)
                for i,j in zip(rows,pc): v[i*n+j]=1
                verts.append(v)
    return verts

def projections(y,m,n):
    mean=sum(y,F(0))/(m*n)
    r=[sum(y[i*n+j] for j in range(n))/n-mean for i in range(m)]
    c=[sum(y[i*n+j] for i in range(m))/m-mean for j in range(n)]
    g=[mean]*(m*n)
    row=[r[i] for i in range(m) for j in range(n)]
    col=[c[j] for i in range(m) for j in range(n)]
    interaction=[y[i*n+j]-mean-r[i]-c[j] for i in range(m) for j in range(n)]
    return (row,col,interaction,g)

def dot(x,y):return sum((a*b for a,b in zip(x,y)),F(0))

def eigenvals(m,n,k):
    D=m*n
    return (F(k*(m-k),D*(m-1)),F(k*(n-k),D*(n-1)),
            F(k*((m-1)*(n-1)+k-1),D*(m-1)*(n-1)))

def check(m,n,k):
    vs=fmatrix(m,n,k); D=m*n; N=len(vs)
    center=[F(k,D)]*D
    z=[[F(v[i])-center[i] for i in range(D)] for v in vs]
    # An independently enumerated covariance, not substituted formulas.
    cov=[[sum((w[i]*w[j] for w in z),F(0))/N for j in range(D)] for i in range(D)]
    modes=[projections(w,m,n) for w in z]
    lam=eigenvals(m,n,k)
    ranks=[m-1,n-1,(m-1)*(n-1)]
    rank=sum(rank1 for rank1,lambda1 in zip(ranks,lam) if lambda1)
    for q in range(3):
        for modes_v in modes:
            y=modes_v[q]; e=lam[q]
            cy=[sum((cov[i][j]*y[j] for j in range(D)),F(0)) for i in range(D)]
            assert cy==[e*a for a in y],(m,n,k,q,'wrong eigenvalue')
    for w,mode in zip(z,modes):
        assert dot(mode[3],mode[3])==0
        assert sum((dot(u,u) for u in mode),F(0))==dot(w,w)
        contact=sum((dot(mode[q],mode[q])/lam[q] for q in range(3) if lam[q]),F(0))
        assert contact==rank,(m,n,k,'not Loewner contact',contact,rank)
    assert dot(z[0],z[0])==F(k)-F(k*k,D)
    return N,rank

cases=contacts=0
for m in range(2,5):
  for n in range(m,6):
    for k in range(1,m+1):
      nv,rank=check(m,n,k)
      cases+=1; contacts+=nv

# Algebraic regime classification checked by exact rational comparisons.
comparisons=0
for m in range(2,61):
 for n in range(m,101):
  for k in range(1,m):
   lam=eigenvals(m,n,k)
   ratio=lam[2]/lam[0]
   formula=F((m-1)*(n-1)+k-1,(n-1)*(m-k))
   assert ratio==formula and ratio>=1
   if k>1: assert ratio>1
   comparisons+=1
  sat=eigenvals(m,n,m)
  if n>m:
    ratio=sat[2]/sat[1]
    assert ratio==F(n,n-m)
  else:
    ratio=F(1)
  pre=F((m-1)*n-1,n-1)
  if m==2: sign=0 if n==m else +1
  elif n==m: sign=-1
  elif m==3: sign=+1 if n<=5 else -1
  else: sign=+1 if n==m+1 else -1
  assert (ratio>pre)-(ratio<pre)==sign,(m,n,ratio,pre)
  comparisons+=1
print(f'VERIFY_OK exact_enumerated_cases={cases} exact_vertex_contacts={contacts} rank_spectral_order_comparisons={comparisons}')
