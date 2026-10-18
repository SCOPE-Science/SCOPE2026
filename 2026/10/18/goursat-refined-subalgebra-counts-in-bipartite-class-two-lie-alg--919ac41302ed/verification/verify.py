#!/usr/bin/env python3
"""Direct exhaustive finite-field enumeration of subalgebra profiles in bipartite two-step Lie algebras."""
from itertools import combinations, product
from collections import Counter

class Field:
    def __init__(self, q):
        assert q in (2,3,4,5)
        self.q=q
        self.char=2 if q==4 else q
    def add(self,x,y):
        return x^y if self.q==4 else (x+y)%self.q
    def neg(self,x):
        return x if self.char==2 else (-x)%self.q
    def sub(self,x,y):
        return self.add(x,self.neg(y))
    def mul(self,x,y):
        if self.q!=4:return x*y%self.q
        z=0
        for i in range(2):
            for j in range(2):
                if (x>>i)&1 and (y>>j)&1:
                    z^=1<<(i+j)
        if z&4:z^=0b111 # x^2+x+1=0
        return z
    def inv(self,x):
        assert x
        return next(y for y in range(1,self.q) if self.mul(x,y)==1)


def gaussian(n,k,q):
    if k<0 or k>n:return 0
    num=1; den=1
    for j in range(k):
        num*=q**(n-j)-1
        den*=q**(k-j)-1
    assert num%den==0
    return num//den

def gl_order(t,q):
    z=1
    for h in range(t):z*=q**t-q**h
    return z

def expected_strata(a,b,q):
    ans=Counter()
    for i in range(a+1):
      for j in range(b+1):
       for t in range(min(i,j)+1):
        dim_s=i+j-t
        dim_br=i*j-t*(t+1)//2
        d=a*b-dim_br
        count_s=gaussian(a,i,q)*gaussian(b,j,q)*gaussian(i,t,q)*gaussian(j,t,q)*gl_order(t,q)
        for e in range(d+1):
          ans[(i,j,t,e)]+=count_s*gaussian(d,e,q)*q**(dim_s*(d-e))
    return ans

def all_rref_subspaces(n,q):
    for k in range(n+1):
      for piv in combinations(range(n),k):
        taken=set(piv)
        positions=[(h,c) for h,p in enumerate(piv) for c in range(p+1,n) if c not in taken]
        for params in product(range(q),repeat=len(positions)):
          basis=[[0]*n for _ in range(k)]
          for h,p in enumerate(piv):basis[h][p]=1
          for (h,c),x in zip(positions,params):basis[h][c]=x
          yield basis,piv

def row_rank(rows,F):
    if not rows:return 0
    a=[r.copy() for r in rows]
    w=len(a[0]);p=0
    for col in range(w):
      h=next((i for i in range(p,len(a)) if a[i][col]!=0),None)
      if h is None:continue
      a[h],a[p]=a[p],a[h]
      inverse=F.inv(a[p][col])
      a[p]=[F.mul(inverse,v) for v in a[p]]
      for i in range(p+1,len(a)):
        c=a[i][col]
        if c:a[i]=[F.sub(a[i][j],F.mul(c,a[p][j])) for j in range(w)]
      p+=1
      if p==len(a):break
    return p

def is_in(v,rows,piv,F):
    x=v.copy()
    for r,p in zip(rows,piv):
        c=x[p]
        if c:
            for h in range(p,len(x)):
                x[h]=F.sub(x[h],F.mul(c,r[h]))
    return all(t==0 for t in x)

def bracket(x,y,a,b,F):
    out=[0]*(a+b+a*b)
    for i in range(a):
      for j in range(b):
       out[a+b+i*b+j]=F.sub(F.mul(x[i],y[a+j]),F.mul(y[i],x[a+j]))
    return out

def brute_strata(a,b,q):
    F=Field(q);out=Counter();total=0
    for rows,piv in all_rref_subspaces(a+b+a*b,q):
      ok=True
      for i in range(len(rows)):
       for j in range(i+1,len(rows)):
        if not is_in(bracket(rows[i],rows[j],a,b,F),rows,piv,F):
          ok=False;break
       if not ok:break
      if not ok:continue
      total+=1
      rank_s=row_rank([r[:a+b] for r in rows],F)
      rank_u=row_rank([r[:a] for r in rows],F)
      rank_v=row_rank([r[a:a+b] for r in rows],F)
      t=rank_u+rank_v-rank_s
      e=len(rows)-rank_s-(rank_u*rank_v-t*(t+1)//2)
      assert e>=0
      out[(rank_u,rank_v,t,e)]+=1
    return out

if __name__=='__main__':
 import time
 for a,b,q in [(1,1,2),(1,1,3),(1,1,4),(1,1,5),(1,2,2),(1,2,3),(2,1,2),(2,2,2)]:
  then=time.monotonic();expected=expected_strata(a,b,q);actual=brute_strata(a,b,q)
  assert expected==actual, [(x,expected[x],actual[x]) for x in expected.keys() | actual.keys() if expected[x]!=actual[x]][:20]
  profile=Counter()
  for (i,j,t,e),v in expected.items():profile[i+j-t+(i*j-t*(t+1)//2)+e]+=v
  print(f'PASS a={a} b={b} q={q} n={a+b+a*b} subalgebras={sum(actual.values())} strata={len(actual)} dimension_counts={sorted(profile.items())} seconds={time.monotonic()-then:.2f}',flush=True)
 print('ALL_EXACT_STRATUM_CHECKS_PASSED 8 cases')
