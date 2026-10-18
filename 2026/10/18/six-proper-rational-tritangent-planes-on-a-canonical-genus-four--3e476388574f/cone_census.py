#!/usr/bin/env python3
"""Exhaustive canonical cubic sections of the rank-three quadric over F2.
An integer mask encodes the unique cubic representative modulo XZ+Y^2.
"""
from itertools import product
from collections import Counter,defaultdict
import json,sys,time
MON=[(i,j,k,l) for i in range(4) for j in range(4-i) for k in range(4-i-j) for l in [3-i-j-k] if not(i and k)]
MON=sorted(MON,reverse=True)
assert len(MON)==16
IDX={m:i for i,m in enumerate(MON)}
W3=1<<IDX[(0,0,0,3)]

def pmul(a,b):
 p=0
 while b:
  j=(b&-b).bit_length()-1;b&=b-1;p^=a<<j
 return p

def deriv(p):
 r=0
 for i in range(1,p.bit_length(),2):
  if p>>i&1:r|=1<<(i-1)
 return r

def pmod(a,b):
 while a and a.bit_length()>=b.bit_length():a^=b<<(a.bit_length()-b.bit_length())
 return a

def pgcd(a,b):
 while b:a,b=b,pmod(a,b)
 return a

# Precompute chart monomial evaluations a(t)*w^2+b(t)*w+c(t), +w^3
CHART=[]
for exps in MON:
 i,j,k,l=exps
 CHART.append(((j+2*k,l),(2*i+j,l)))

def polydata(mask,chart):
 p=[0,0,0,0]
 for m in range(16):
  if mask>>m&1:
   deg,l=CHART[m][chart];p[l]^=1<<deg
 return p

def smooth(mask):
 if mask&W3==0:return False
 for chart in (0,1):
  c,b,a,d=polydata(mask,chart)
  if d!=1:raise AssertionError
  D=pmul(a,b)^c
  E=pmul(deriv(a),b)^deriv(c)
  E=pmul(E,E)^pmul(pmul(deriv(b),deriv(b)),b)
  if pgcd(D,E)!=1:return False
 return True

def binary_sextic(mask,u,v,z):
 # W=u*s^2+v*s*t+z*t^2, X=s^2,Y=st,Z=t^2
 q=(u,v,z)
 arr=0
 for idx,exps in enumerate(MON):
  if not(mask>>idx&1):continue
  i,j,k,l=exps
  poly={(2*i+j,2*k+j):1}
  for _ in range(l):
   nxt={}
   for (s,t),c in poly.items():
    if u:nxt[(s+2,t)]=nxt.get((s+2,t),0)^c
    if v:nxt[(s+1,t+1)]=nxt.get((s+1,t+1),0)^c
    if z:nxt[(s,t+2)]=nxt.get((s,t+2),0)^c
   poly=nxt
  for (s,t),c in poly.items():
   if c:arr^=1<<t
 return arr

def is_sqfree_cubic(h):
 # h(r,u)=a*r^3+b*r^2*u+c*r*u^2+d*u^3
 a,b,c,d=((h>>i)&1 for i in range(4))
 return (a*d^b*c)==1

def tritangents(mask):
 # 3 tangent planes to quadric cone (one per rational ruling fiber)
 # Fiber cubic restricted to [lambda*s^2:lambda*st:lambda*t^2:mu].
 tangent=0
 for s,t in [(1,0),(0,1),(1,1)]:
  c=[0,0,0,0]
  for idx,(i,j,k,l) in enumerate(MON):
   if mask>>idx&1:
    if (s or not i) and ((s*t) or not j) and (t or not k):
     c[l]^=1
  # in ordered binary cubic lambda^3, lambda^2 mu, lambda mu^2, mu^3
  h=sum(c[l]<<l for l in range(4))
  tangent+=is_sqfree_cubic(h)
 # 8 transverse planes W+uX+vY+zZ=0
 transverse=0
 for u,v,z in product((0,1),repeat=3):
  h=binary_sextic(mask,u,v,z)
  if h & ((1<<1)|(1<<3)|(1<<5)):continue
  root=sum(((h>>(2*j))&1)<<j for j in range(4))
  transverse+=is_sqfree_cubic(root)
 return tangent,transverse

def pointcount(mask):
 n=0
 for s,t in [(1,0),(0,1),(1,1)]:
  for w in (0,1):
   val=0
   x,y,z=s,s*t,t
   for idx,(i,j,k,l) in enumerate(MON):
    if mask>>idx&1:val^=(x or i==0) and (y or j==0) and (z or k==0) and (w or l==0)
   if not val:n+=1
 return n

def reduce(mon):
 i,j,k,l=mon
 if i and k:
  h=min(i,k)
  return(i-h,j+2*h,k-h,l)
 return mon

def quad_poly_map(mat,shift):
 a,b,c,d=mat;u,v,z=shift
 # X'=aX+bZ, Y'=acX+Y+bdZ, Z'=cX+dZ, W'=W+uX+vY+zZ
 return (
 {(1,0,0,0):a,(0,0,1,0):b},
 {(1,0,0,0):a*c,(0,1,0,0):1,(0,0,1,0):b*d},
 {(1,0,0,0):c,(0,0,1,0):d},
 {(0,0,0,1):1,(1,0,0,0):u,(0,1,0,0):v,(0,0,1,0):z})

def substitute(mask,basis):
 out={ (0,0,0,0):1 }
 for idx,exp in enumerate(MON):
  if not(mask>>idx&1):continue
  pol={(0,0,0,0):1}
  for i,e in enumerate(exp):
   for _ in range(e):
    nxt={}
    for m,p in pol.items():
     if not p:continue
     for k,c in basis[i].items():
      if c:
       mm=reduce(tuple(m[j]+k[j] for j in range(4)))
       nxt[mm]=nxt.get(mm,0)^1
    pol=nxt
  for k,v in pol.items():
   if v:out[k]=out.get(k,0)^v
  # Remove initial constant used as scratch only
 out[(0,0,0,0)]^=1
 ret=0
 for k,v in out.items():
  if v:ret^=1<<IDX[k]
 return ret

def matrix_maps():
 mats=[]
 for a,b,c,d in product((0,1),repeat=4):
  if (a*d^b*c)==1:mats.append((a,b,c,d))
 maps=[]
 for mat in mats:
  for shift in product((0,1),repeat=3):
   images=[substitute(1<<i,quad_poly_map(mat,shift)) for i in range(16)]
   assert images[IDX[(0,0,0,3)]]&W3
   maps.append(images)
 assert len(maps)==48
 return maps

def apply_map(mask,mapping):
 m=0
 while mask:
  low=mask&-mask;mask-=low;m^=mapping[low.bit_length()-1]
 return m

def run():
 t0=time.time(); counts=Counter();good=[]; byrep={};
 for mask in range(1<<16):
  if not(mask&W3):continue
  if smooth(mask):
   pair=tritangents(mask); n=pointcount(mask)
   counts[(n,*pair)]+=1;good.append(mask)
 print('smooth',len(good),'time',time.time()-t0,flush=True)
 print('tritangent_count',sorted(Counter((x[1]+x[2] for x in counts.elements())).items()))
 print('joint',sorted(counts.items()),flush=True)
 maps=matrix_maps()
 seen=set();orbits=[]; orbit_counts=Counter()
 for mask in good:
  if mask in seen:continue
  orbit={apply_map(mask,map_) for map_ in maps}
  assert mask in orbit
  assert all(smooth(x) for x in orbit)
  assert not(orbit&seen)
  seen|=orbit
  pair=tritangents(mask);n=pointcount(mask)
  assert all((tritangents(x),pointcount(x))==(pair,n) for x in orbit)
  orbit_counts[(n,*pair)]+=1
  orbits.append(dict(representative=mask,orbit_size=len(orbit),rational_points=n,tangent_tritangents=pair[0],transverse_tritangents=pair[1]))
 assert len(seen)==len(good)
 print('orbits',len(orbits),'time',time.time()-t0,'extrema',sorted([r for r in orbits if r['tangent_tritangents']+r['transverse_tritangents']==max(k[1]+k[2] for k in counts)],key=lambda a:a['representative']),flush=True)
 out={'basis':MON,'smooth_total':len(good),'all_sections_with_vertex_avoided':1<<15,'group_order':len(maps),'joint_equations':[{'rational_points':k[0],'tangent':k[1],'transverse':k[2],'count':v,'orbits':orbit_counts[k]} for k,v in sorted(counts.items())],'orbits':sorted(orbits,key=lambda a:a['representative'])}
 with open(sys.argv[1] if len(sys.argv)>1 else 'cone_results.json','w') as f:json.dump(out,f,indent=2);f.write('\n')
 print('finished',time.time()-t0,flush=True)
if __name__=='__main__':run()
