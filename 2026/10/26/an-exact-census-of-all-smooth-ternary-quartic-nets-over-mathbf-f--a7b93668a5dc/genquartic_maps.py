import itertools,collections,time,json,math,sys
import sympy as s
start=time.monotonic()
vs=s.symbols('x y z');x,y,z=vs
EXPS=sorted(((a,b,4-a-b) for a in range(5) for b in range(5-a)),reverse=True)
INDEX={e:i for i,e in enumerate(EXPS)}
mono=[x**a*y**b*z**c for (a,b,c) in EXPS]

def mpoly(A,B):
 C=set()
 for a in A:
  for b in B:
   e=tuple(a[i]+b[i] for i in range(3))
   if e in C:C.remove(e)
   else:C.add(e)
 return C

def mulpow(A,n):
 res={(0,0,0)}
 for i in range(n):res=mpoly(res,A)
 return res

def genmat(k):
 if k==0: return ({(0,1,0)},{(1,0,0)},{(0,0,1)})
 if k==1: return ({(0,1,0)},{(0,0,1)},{(1,0,0)})
 if k==2: return ({(1,0,0),(0,1,0)},{(0,1,0)},{(0,0,1)})
trans=[]
for k in range(3):
 X,Y,Z=genmat(k)
 arr=[]
 for a,b,c in EXPS:
  rep=mpoly(mpoly(mulpow(X,a),mulpow(Y,b)),mulpow(Z,c))
  n=0
  for e in rep:n ^=1<<INDEX[e]
  arr.append(n)
 trans.append(arr)

def apply(mask,gen):
 ans=0
 while mask:
  i=(mask&-mask).bit_length()-1
  ans^=trans[gen][i];mask&=mask-1
 return ans

def issmooth(mask):
 F=sum(mono[i] for i in range(15) if (mask>>i)&1)
 for chart in range(3):
  others=[vs[i] for i in range(3) if i!=chart]
  f=s.Poly(F.subs({vs[chart]:1}),*others,modulus=2).as_expr()
  if list(s.groebner([f]+[s.diff(f,r) for r in others],*others,order='lex',modulus=2))!=[1]:return False
 return True

seen=bytearray(32768);smooth=bytearray(32768);orbits=[];reps=[];smoothorbits=[]
for f in range(1,32768):
 if seen[f]:continue
 seen[f]=1;orb=[f]
 for a in orb:
  for k in range(3):
   b=apply(a,k)
   if not seen[b]:
    seen[b]=1;orb.append(b)
 sm=issmooth(f)
 if sm:
  for a in orb:smooth[a]=1
  smoothorbits.append((f,len(orb)))
 orbits.append((f,len(orb),int(sm)))
print('group_orbits',len(orbits),'smooth_orbits',len(smoothorbits),'smooth_forms',sum(smooth),'smooth_orbit_sizes',collections.Counter(sz for f,sz in smoothorbits),'sec',round(time.monotonic()-start,3),flush=True)

open("smoothquartic.bin","wb").write(smooth)
import json
json.dump({"smooth_orbits":smoothorbits,"all_orbits":len(orbits)},open("smoothquartic_orbits.json","w"))

import struct
with open("quartic_gentable.bin","wb") as q:
 for k in range(3):
  q.write(struct.pack("<32768H",*(apply(f,k) for f in range(32768))))
