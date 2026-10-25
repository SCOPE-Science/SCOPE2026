#!/usr/bin/env python3
"""Independent exhaustive incidence sieve and generator-orbit Gröbner checks."""
import itertools,json,collections,time
from sympy import symbols,groebner
A,B,C=symbols('A B C')
vars=(A,B,C)
monoms=[(i,j,4-i-j) for i in range(4,-1,-1) for j in range(4-i,-1,-1)]
ids={e:i for i,e in enumerate(monoms)}
pts=[p for p in itertools.product((0,1),repeat=3) if any(p)]
def bit(c,p):
 v=0
 for k,(i,j,l) in enumerate(monoms):
  if c>>k&1:v^=(p[0]**i)*(p[1]**j)*(p[2]**l)
 return v
def gd(c,p,coord):
 v=0
 for k,e in enumerate(monoms):
  if c>>k&1 and e[coord]%2:
   prod=1
   for j in range(3):prod*=p[j]**(e[j]-(j==coord))
   v^=prod
 return v
def inspect(c):
 Q=[];T=[]
 for p in pts:
  if bit(c,p)==0:
   Q.append(p);grad=tuple(gd(c,p,i) for i in range(3))
   if not any(grad):return None
   T.append(grad)
 for p in pts:
  if not any(sum(u*v for u,v in zip(p,t))%2==0 for t in T):return None
 return (len(Q),len(set(T)),tuple(Q),tuple(T))
def polynomial_multiply(S,T):
 Z=set()
 for a in S:
  for b in T:
   e=tuple(a[i]+b[i] for i in range(3))
   if e in Z:Z.remove(e)
   else:Z.add(e)
 return Z
def trans(c,mat):
 bits=0
 for k,e in enumerate(monoms):
  if not(c>>k&1):continue
  S={(0,0,0)}
  for j in range(3):
   term={tuple(int(i==t) for i in range(3)) for t in range(3) if mat[j][t]}
   for _ in range(e[j]):S=polynomial_multiply(S,term)
  for f in S:bits^=1<<ids[f]
 return bits
# generators of GL3(F2): swapping first two, cycling 3, and an elementary shear
mats=[((0,1,0),(1,0,0),(0,0,1)),((0,1,0),(0,0,1),(1,0,0)),((1,1,0),(0,1,0),(0,0,1))]
def algebraic_smooth(c):
 F=sum(A**i*B**j*C**k for a,(i,j,k) in enumerate(monoms) if c>>a&1)
 for v,u,w in ((A,B,C),(B,A,C),(C,A,B)):
  H=F.subs(v,1);g=groebner([H,H.diff(u),H.diff(w)],u,w,order='grlex',modulus=2)
  if len(g.polys)!=1 or not g.polys[0].is_one:return False
 return True
def main():
 t=time.monotonic(); candidates={}
 for c in range(1,32768):
  P=inspect(c)
  if P is not None:candidates[c]=P
 assert len(candidates)==2782, len(candidates)
 visited=set();classes=[];counts=collections.Counter();negative=0;candidate_orbits=0
 for c in candidates:
  if c in visited:continue
  orb={c}; todo=[c]
  while todo:
   v=todo.pop()
   for m in mats:
    w=trans(v,m)
    if w not in orb:
     orb.add(w);todo.append(w)
  assert orb.issubset(candidates)
  visited|=orb
  candidate_orbits+=1
  s=algebraic_smooth(c)
  if s:
   counts[(candidates[c][0],candidates[c][1])]+=len(orb)
   classes.append({'rep':c,'size':len(orb),'N':candidates[c][0],'Gauss':candidates[c][1]})
  else:negative+=len(orb)
 print('direct candidate',len(candidates),'geometric smooth',sum(v for v in counts.values()),'singular candidate',negative,'smooth classes',len(classes),'candidate_orbits',candidate_orbits,'time',round(time.monotonic()-t,2))
 print('distribution',sorted(counts.items()))
 assert len(visited)==len(candidates)
 with open('direct_orbit_output.json','w') as f:json.dump({'candidate_count':len(candidates),'candidate_class_count':len(classes),'smooth_total':sum(counts.values()),'singular_candidates':negative,'distribution':[(list(k),v) for k,v in counts.items()],'smooth_orbits':classes},f,indent=2)
if __name__=='__main__':main()
