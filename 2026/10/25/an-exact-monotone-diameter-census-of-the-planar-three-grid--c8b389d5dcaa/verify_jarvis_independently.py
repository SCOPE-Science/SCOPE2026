# Independent gift-wrapping hull and integer-objective verification.
from itertools import combinations
from collections import Counter
from verify_monotone_census import POINTS, cross, monotone_diameter

def jarvis(S):
 S=list(S)
 if len(S)<3:return ()
 start=min(S)
 res=[];here=start
 while True:
  res.append(here)
  dest=next(q for q in S if q!=here)
  for q in S:
   if q==here:continue
   cr=cross(here,dest,q)
   if cr<0 or (cr==0 and ((q[0]-here[0])**2+(q[1]-here[1])**2)>((dest[0]-here[0])**2+(dest[1]-here[1])**2)):dest=q
  here=dest
  if here==start:break
  assert len(res)<=16
 if len(res)<3 or cross(*res[:3])<=0:
  if len(res)>=3 and cross(*res[:3])<0:res=[res[0]]+res[:0:-1]
  else:return ()
 return tuple(res)

def nearest_sink(poly,c):
 h=[c[0]*x+c[1]*y for x,y in poly]
 n=len(poly);D=[0]*n
 for i in sorted(range(n),key=lambda i:h[i],reverse=True):
  outgoing=[D[j]+1 for j in ((i-1)%n,(i+1)%n) if h[j]>h[i]]
  if outgoing:D[i]=min(outgoing)
  else:assert h[i]==max(h)
 return max(D)

out=set()
for mask in range(1<<16):
 if mask.bit_count()<3:continue
 vertices=[POINTS[i] for i in range(16) if mask>>i&1]
 q=jarvis(vertices)
 if q:out.add(q)
assert len(out)==2719,len(out)
print('independent hulls',len(out))
for poly in out:
 if monotone_diameter(poly)[0]>=4:print('high',poly)
# Cross-check every polygon against 1680 generic and boundary integer normals from a coarser grid.
for j,p in enumerate(out):
 exact=monotone_diameter(p)[0]
 crude=max(nearest_sink(p,(x,y)) for x in range(-8,9) for y in range(-8,9) if (x or y))
 assert crude==exact,(p,crude,exact)
print('independent objective sample consistency',len(out))
