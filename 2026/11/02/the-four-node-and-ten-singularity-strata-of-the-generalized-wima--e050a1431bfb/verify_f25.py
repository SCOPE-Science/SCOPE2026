#!/usr/bin/env python3
"""Independent exact enumeration of all rational singularities over F_25 for selected parameters over F_5."""
from collections import Counter
p=5

def add(a,b):return ((a%5+b%5)%5)+5*((a//5+b//5)%5)
def neg(a):return (-a%5)+5*((-(a//5))%5)
def mul(a,b):
 x,y=divmod(a,5)[1],a//5; u,v=b%5,b//5
 return ((x*u+2*y*v)%5)+5*((x*v+y*u)%5)
def power(x,n):
 out=1
 for _ in range(n):out=mul(out,x)
 return out
P=[(x,y,1) for x in range(25) for y in range(25)]+[(x,1,0) for x in range(25)]+[(1,0,0)]
E=[(6,0,0),(0,6,0),(0,0,6),(4,2,0),(0,4,2),(2,0,4),(2,4,0),(0,2,4),(4,0,2),(2,2,2)]

def evaluate(xyz,a,b,d):
 cs=[1,1,1,a,a,a,b,b,b,(-3*(a+b+1))%5]
 out=0
 for c,ex in zip(cs,E):
  coef=c
  powers=list(ex)
  for idx,order in d:
   if order>powers[idx]:coef=0;break
   for j in range(order):coef=coef*powers[idx]%5; powers[idx]-=1
  if not coef:continue
  v=coef
  for ind,e in enumerate(powers):
   if e:v=mul(v,power(xyz[ind],e))
  out=add(out,v)
 return out

def hessian_node(point,a,b):
 if point[2]!=0:idxs=(0,1)
 elif point[1]!=0:idxs=(0,2)
 else:idxs=(1,2)
 i,j=idxs
 h11=evaluate(point,a,b,[(i,2)]); h12=evaluate(point,a,b,[(i,1),(j,1)]); h22=evaluate(point,a,b,[(j,2)])
 return add(mul(h11,h22),neg(mul(h12,h12)))!=0

stats=Counter()
for a in range(5):
 for b in range(5):
  L=(a+b+3)%5;R=(a*a+a*b+b*b)%5
  if not L or not R:continue
  D=(a*a*b*b-4*(a*a*a+b*b*b)+18*a*b-27)%5
  sing=[]
  for pt in P:
   if evaluate(pt,a,b,[])!=0:continue
   if all(evaluate(pt,a,b,[(i,1)])==0 for i in range(3)):
    sing.append(pt)
  node=sum(hessian_node(pt,a,b) for pt in sing)
  if D:
   assert (len(sing),node)==(4,4),(a,b,len(sing),node)
   stats['smooth_axis_parameters']+=1
  else:
   assert (len(sing),node)==((10,4) if (a,b)==(3,3) else (10,10)),(a,b,len(sing),node)
   stats['discriminant_parameters']+=1
   if (a,b)==(3,3):stats['six_cusps_parameters']+=1
print('FINITE_F25_VERIFY_OK',dict(stats))
