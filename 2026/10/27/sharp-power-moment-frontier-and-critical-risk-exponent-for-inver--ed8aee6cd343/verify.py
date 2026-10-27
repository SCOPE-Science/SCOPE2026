import math,random

def bound(n,p):
 if p==2:return n/2
 if p>2:return math.inf
 m=n-2
 lo=0.;hi=1.
 for _ in range(180):
  mid=(lo+hi)/2
  if m*p*mid*mid+4*mid**p >2*(2-p):hi=mid
  else:lo=mid
 x=(lo+hi)/2
 return (2-p)/(2*x**p),x

def measure(ds,p):
 s=min(ds)
 x=[s/d for d in ds]
 return sum(v**(2-p) for v in x)/sum(v*v for v in x)

cnt=0
for n in range(3,16):
 for p in (0.15,0.5,1.,1.33,1.75,1.99,2.):
  b=bound(n,p)
  cap=b[0] if isinstance(b,tuple) else b
  for _ in range(200):
   # Random finite metric from Euclidean points, hierarchical 2-level metric, and nonnegative weighted tree
   typ=random.randrange(3)
   if typ==0:
    xy=[(random.random()*15,random.random()*15) for i in range(n)]
    ds=[min(math.dist(xy[i],xy[j]) for j in range(n) if i!=j) for i in range(n)]
   elif typ==1:
    xs=random.uniform(1,100)
    ds=[1.,1.]+[xs]*(n-2)
   else:
    arr=[random.uniform(0.1,20) for _ in range(n)]
    ds=[arr[i]+min(arr[j] for j in range(n) if i!=j) for i in range(n)]
   mm=measure(ds,p)
   assert mm <=cap + 1e-9,(n,p,mm,cap,ds)
   cnt+=1
  if p<2:
   x=b[1]
   assert abs(measure([1.,1.]+[1./x]*(n-2),p)-cap)<1e-9
   cnt+=1
  else:
   assert cap>=measure([1.,1.]+[1e6]*(n-2),p)
print('moment checks',cnt,'p1 n4',bound(4,1),'p2 n4',bound(4,2))
# Specific exact rational for p=1, 2; verify 4-point metric distances: pair (0,1)=1, all others d=1/x
from fractions import Fraction
for n in range(3,14):
 for m in range(1,21):
  ds=[Fraction(1)]*2+[Fraction(m)]*(n-2)
  f=sum(1/d for d in ds)/sum(1/(d*d) for d in ds)
  f2=Fraction(n,1)/sum(1/(d*d) for d in ds)
  assert float(f) <=bound(n,1)[0]+1e-12
  assert f2<=Fraction(n,2)
  cnt+=2
print('all checks',cnt)
