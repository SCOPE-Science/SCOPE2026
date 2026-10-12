#!/usr/bin/env python3
"""Finite-field consistency checks of the ideal polynomial for bipartite graph Lie algebras."""
from itertools import combinations, product
from collections import Counter
from math import prod

def gb(n,k,q):
    if k<0 or k>n:return 0
    num=prod(q**(n-i)-1 for i in range(k))
    den=prod(q**(k-i)-1 for i in range(k))
    assert num%den==0
    return num//den

def gl(k,q):return prod(q**k-q**i for i in range(k))

def predicted(a,b,q):
    h=Counter()
    for r in range(a+1):
      for s in range(b+1):
        for k in range(min(r,s)+1):
          d=r+s-k
          N=gb(a,r,q)*gb(b,s,q)*gb(r,k,q)*gb(s,k,q)*gl(k,q)
          c=(a-r)*(b-s)
          for t in range(c+1):
            z=a*b-c+t
            h[d+z]+=N*gb(c,t,q)*q**(d*(c-t))
    return dict(sorted(h.items()))

def rrefs(n,q):
    for k in range(n+1):
        for pivots in combinations(range(n),k):
            free=[(i,j) for i,p in enumerate(pivots) for j in range(p+1,n) if j not in pivots]
            for vals in product(range(q),repeat=len(free)):
                rows=[[0]*n for _ in pivots]
                for i,p in enumerate(pivots):rows[i][p]=1
                for (i,j),v in zip(free,vals):rows[i][j]=v
                yield tuple(tuple(r) for r in rows)

def idealcheck(rows,a,b,q):
    n=a+b+a*b
    rank=len(rows)
    # solve row-reduced inclusion using the pivot columns
    piv=[next(i for i,v in enumerate(row) if v) for row in rows]
    for row in rows:
      for j in range(a+b):
        out=[0]*n
        for i in range(a):
          if j>=a and j<a+b:out[a+b+i*b+(j-a)]+=row[i]
        for t in range(b):
          if j<a:out[a+b+j*b+t]-=row[a+t]
        out=[x%q for x in out]
        for k,p in enumerate(piv):
          if out[p]:
            v=out[p]
            out=[(x-v*y)%q for x,y in zip(out,rows[k])]
        if any(out):return False
    return True

def brute(a,b,p):
    n=a+b+a*b
    count=Counter()
    for rows in rrefs(n,p):
        if idealcheck(rows,a,b,p):count[len(rows)]+=1
    return dict(sorted(count.items()))

def verify():
 for a,b,p in [(1,1,2),(1,1,3),(1,2,2),(1,2,3),(2,2,2)]:
    actual=brute(a,b,p)
    expected=predicted(a,b,p)
    assert actual==expected, (a,b,p,actual,expected)
    print('PASS',a,b,p,'ideal_count',sum(actual.values()),'dimension_profile',actual)
 # symmetry in interchange of the two independent vertex parts
 for a,b,q in [(2,3,2),(3,3,3),(2,4,5),(1,4,7)]:
    assert predicted(a,b,q)==predicted(b,a,q)
 print('VERIFY_OK')
if __name__=='__main__':verify()
