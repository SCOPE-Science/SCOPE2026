import json,time
from collections import deque
# The two transformations generate all 168 invertible ternary binary matrices.
def matmul(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3))%2 for j in range(3)) for i in range(3))
I=((1,0,0),(0,1,0),(0,0,1))
T=((1,1,0),(0,1,0),(0,0,1))
S=((0,1,0),(0,0,1),(1,0,0))
mat_seen={I};mat_queue=deque([I])
while mat_queue:
 g=mat_queue.popleft()
 for h in (T,S):
  gh=matmul(g,h)
  if gh not in mat_seen:mat_seen.add(gh);mat_queue.append(gh)
assert len(mat_seen)==168
from sympy import symbols, Poly, groebner
x,y,z=symbols('x y z')
mons=[(i,j,4-i-j) for i in range(4,-1,-1) for j in range(4-i,-1,-1)]
idx={m:i for i,m in enumerate(mons)}
def shift(poly,v):
 out={}
 for m in poly:
  key=tuple(m[i]+v[i] for i in range(3))
  out[key]=1-out.get(key,0)
 return {m for m,val in out.items() if val}
def mul(a,b):
 out={}
 for m in a:
  for n in b:
   k=tuple(m[i]+n[i] for i in range(3));out[k]=1-out.get(k,0)
 return {m for m,val in out.items() if val}
def applymono(e,rows):
 a={(0,0,0)}
 for i in range(3):
  for _ in range(e[i]):a=mul(a,rows[i])
 return sum(1<<idx[m] for m in a)
rowsA=({(1,0,0),(0,1,0)},{(0,1,0)},{(0,0,1)})
rowsB=({(0,1,0)},{(0,0,1)},{(1,0,0)})
trans=[[applymono(m,rows) for m in mons] for rows in (rowsA,rowsB)]
def transform(mask,trans):
 out=0
 while mask:
  low=mask & -mask;i=low.bit_length()-1;out^=trans[i];mask-=low
 return out
n=1<<len(mons)
assert n==32768
seen=bytearray(n);orbits=[]
for k in range(1,n):
 if seen[k]:continue
 q=deque([k]);seen[k]=1;size=0
 while q:
  v=q.popleft();size+=1
  for tr in trans:
   v2=transform(v,tr)
   if not seen[v2]:seen[v2]=1;q.append(v2)
 orbits.append([k,size])
print('orbits',len(orbits),'sum',sum(s for _,s in orbits),flush=True)

def is_smooth(k):
 P=sum((x**a*y**b*z**c for i,(a,b,c) in enumerate(mons) if k>>i &1),0)
 for u,v,w in ((x,y,z),(x,z,y),(y,z,x)):
  f=P.subs(w,1)
  basis=groebner([f,f.diff(u),f.diff(v)],u,v,modulus=2)
  if len(basis.polys)!=1 or basis.polys[0].as_expr()!=1:return False
 return True
z1=time.monotonic();smooth=[]
for i,(k,size) in enumerate(orbits):
 sm=is_smooth(k)
 if sm:smooth.append([k,size])
 if i%50==0:print('smoothprogress',i,len(smooth),flush=True)
print('smooth',len(smooth),sum(s for _,s in smooth))
with open('quartic_orbits.json','w') as f:json.dump(dict(mons=mons,orbits=orbits,smooth=smooth),f)

with open('smooth_orbits.txt','w') as f:
 for k,n in smooth:f.write(f'{k} {n}\n')
