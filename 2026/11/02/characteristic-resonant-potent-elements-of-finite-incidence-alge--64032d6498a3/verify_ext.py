#!/usr/bin/env python3
from itertools import product

def mul4(x,y):
 a,b=x&1,(x>>1)&1
 c,d=y&1,(y>>1)&1
 return (a*c^b*d) | ((a*d^b*c^b*d)<<1)

def run(n,covers):
 r={(i,i) for i in range(n)}|set(covers)
 for k in range(n):
  for i in range(n):
   for j in range(n):
    if (i,k) in r and (k,j) in r:r.add((i,j))
 ix=sorted(r); ind={t:j for j,t in enumerate(ix)}
 def mult(a,b):
  return tuple(__import__('functools').reduce(lambda v,k:v^mul4(a[ind[(i,k)]],b[ind[(k,j)]]),[k for k in range(i,j+1) if (i,k) in r and (k,j) in r],0) for i,j in ix)
 count=0
 for a in product(range(4),repeat=len(ix)):
  a2=mult(a,a);a3=mult(a2,a)
  count+=a==a3
 print(n,covers,len(ix),count)
 return count

if __name__=='__main__':
 assert run(3,[(0,1),(1,2)])==269
 assert run(3,[(0,2),(1,2)])==89
 print('VERIFY_EXTENSION_OK')
