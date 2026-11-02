#!/usr/bin/env python3
"""Exact certificate for the size-refined P3-convex-set polynomial of cyclic prisms."""
from collections import defaultdict
from itertools import product

ACTIVE=(0,3,5,7,10,11,12,13,14,15)

def bit_count(x):return x.bit_count()
def good(left,middle,right):
    for row in (0,1):
        if middle & (1<<row):
            nbr=bool(left&(1<<row))+bool(right&(1<<row))+bool(middle&(1<<(1-row)))
            if nbr<2:return False
    return True

def trace_poly(n):
    d={}
    for first in range(4):
      for second in range(4):
        dp={(first,second,bit_count(first)+bit_count(second)):1}
        for i in range(2,n):
          nxt=defaultdict(int)
          for (prev,cur,w),num in dp.items():
            for cand in range(4):
              if good(prev,cur,cand):nxt[cur,cand,w+bit_count(cand)]+=num
          dp=nxt
        for (prev,cur,w),num in dp.items():
          if good(prev,cur,first) and good(cur,first,second):d[w]=d.get(w,0)+num
    return d

def graph_poly(n):
    adj=[]
    for row in (0,1):
      for j in range(n):
        adj.append((row*n+(j-1)%n,row*n+(j+1)%n,(1-row)*n+j))
    p=defaultdict(int)
    for mask in range(1<<(2*n)):
      feasible=True
      for v in range(2*n):
        if not (mask>>v)&1:
          if sum((mask>>u)&1 for u in adj[v])>=2:
            feasible=False;break
      if feasible:p[2*n-mask.bit_count()]+=1
    return dict(p)

def poladd(p,q):
 d=p.copy()
 for k,v in q.items():d[k]=d.get(k,0)+v
 return {k:v for k,v in d.items() if v}
def polmul(p,q):
 d=defaultdict(int)
 for (a,b),v in p.items():
  for (c,e),w in q.items():d[a+c,b+e]+=v*w
 return {k:v for k,v in d.items() if v}

def determinant_poly():
 # Sparse 10x10 permanent-like row-subset determinant, with inversion parity.
 indices={u:i for i,u in enumerate(ACTIVE)}
 rows=[]
 for u in ACTIVE:
  a,b=divmod(u,4)
  row={}
  for v in ACTIVE:
   p={}
   if u==v:p[(0,0)]=1
   c=v%4
   if v//4==b and good(a,b,c):p=poladd(p,{(1,c.bit_count()):-1})
   if p:row[indices[v]]=p
  rows.append(row)
 dp={0:{(0,0):1}}
 for r,row in enumerate(rows):
  nd={}
  for mask,p in dp.items():
   for j,q in row.items():
    if (mask>>j)&1:continue
    larger=(mask>>(j+1)).bit_count()
    prod=polmul(p,q)
    if larger&1:prod={k:-v for k,v in prod.items()}
    key=mask|(1<<j)
    nd[key]=poladd(nd.get(key,{}),prod)
  dp=nd
 return dp[(1<<10)-1]

def expected_poly():
 # (1-yz+y³z²)*(1-(1+y+y²)z+(y+y²)z²-(y⁴+y⁵)z³+2y⁵z⁴+y⁷z⁵)
 a={(0,0):1,(1,1):-1,(2,3):1}
 b={(0,0):1,(1,0):-1,(1,1):-1,(1,2):-1,(2,1):1,(2,2):1,(3,4):-1,(3,5):-1,(4,5):2,(5,7):1}
 return polmul(a,b)

def main():
 d=determinant_poly();e=expected_poly()
 assert d==e,(d,e)
 print('DET_OK',len(d),'nonzero bivariate coefficients')
 for n in range(3,9):
  p=trace_poly(n);q=graph_poly(n)
  assert p==q,(n,p,q)
  print('GRAPH_OK',n,sum(q.values()))
 for n in range(10,19):
  p=trace_poly(n)
  assert [p.get(i,0) for i in range(10)]==[1,0,0,0,n,0,n,0,n*(n-3)//2,2*n],(n,p)
 print('TOP_COEFFICIENTS_OK n=10..18')
 print('VERIFY_OK')

if __name__=='__main__':main()
