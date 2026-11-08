#!/usr/bin/env python3
"""Independent checks of flat rectangular quotient normal-radius laws."""
import math, random
random.seed(20261105)
A=[0.6,1.,1.9,3.4]
B=[0.2,0.5,0.51,0.7,1.,1.5,1.9,2.3,4.2]
def formula(a,b,y,kind):
  boundary=b-abs(y)
  if kind=='M':
    return min(boundary,a,0.5*math.hypot(a,2*y))
  return min(boundary,a/2)
def loops(a,y,kind):
    if kind=='C': return min(abs(k*a)/2 for k in range(-12,13) if k)
    return min(math.hypot(k*a,(((-1)**k)-1)*y)/2 for k in range(-12,13) if k)
def tail(a,b,r,kind):
    if kind=='C':return max(0,1-r/b) if 0<=r<=a/2 else 0.
    if r<0:return 1
    if 0<=r<=a/2:return max(0,1-r/b)
    if a/2<r<=a:return max(0,(b-r-math.sqrt(r*r-a*a/4))/b)
    return 0
cases=0
for a in A:
 for b in B:
  for kind in ['M','C']:
   for j in range(77):
    y=(j+.17)*b/77
    assert abs(formula(a,b,y,kind)-min(b-y,loops(a,y,kind)))<1e-12
   for r in [0,b/4,b/2,b*0.8,a*0.5,a*0.6,a*0.85,a, a*1.03]:
    val=tail(a,b,r,kind)
    exact=sum(formula(a,b,(k+.5)*b/10000,kind)>=r-1e-12 for k in range(10000))/10000
    assert abs(val-exact)<0.00025,(kind,a,b,r,val,exact)
   cases+=1
for a in [1.]:
 for b in [0.2,0.499,0.5,0.501,0.8,1.8660254037844386,2.3,4.]:
  if b<=a/2: m=b
  elif b<=(1+math.sqrt(3)/2)*a:m=b/2+a*a/(8*b)
  else:m=a
  test=max(formula(a,b,k*b/30000,'M') for k in range(30001))
  assert abs(m-test)<4e-5, (a,b,m,test)
print('FLAT_QUOTIENT_LOCAL_NORMAL_RADIUS_OK',cases)
