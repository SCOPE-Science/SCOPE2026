#!/usr/bin/env python3
"""Independent exact audit of F_4 maximal-degree Frobenius-nonclassical sextic census.
Enumerate coefficient vectors by numpy vector filtering, and the orbit by generator BFS.
F4 is F2[t]/(t^2+t+1). No computer-algebra library needed.
"""
import numpy as np

def mul(a,b):
    # 2-bit F4 multiplication, independent of the compiled checker.
    a=np.asarray(a); b=np.asarray(b)
    u=(a&1)*(b&1)
    v=((a&1)*((b>>1)&1))^(((a>>1)&1)*(b&1))
    w=((a>>1)&1)*((b>>1)&1)
    return (u^w)|((v^w)<<1)

def exp(a,n):
    v=1
    for _ in range(n):v=int(mul(v,a))
    return v

points=[]
for x in range(4):
 for y in range(4):
  for z in range(4):
   if not x+y+z:continue
   a=next(t for t in (x,y,z) if t)
   k=exp(a,2)
   p=tuple(int(mul(t,k)) for t in (x,y,z))
   if p not in points:points.append(p)
assert len(points)==21
powers=[(3,0,0),(2,1,0),(2,0,1),(1,2,0),(1,1,1),(1,0,2),(0,3,0),(0,2,1),(0,1,2),(0,0,3)]
base=[]; vals=[]
for p in points:
 x,y,z=p
 base.append(int(mul(mul(x,y),z)))
 vals.append([int(mul(mul(exp(x,2*i),exp(y,2*j)),exp(z,2*k))) for i,j,k in powers])

ids=np.arange(1<<20,dtype=np.uint32)
for h,terms in zip(base,vals):
 f=np.full(len(ids),h,dtype=np.uint8)
 for j,b in enumerate(terms):
  if b:f^=mul((ids>>(2*j))&3,b).astype(np.uint8)
 ids=ids[f!=0]
print('admissible_coeff_vectors:',len(ids))
assert len(ids)==960

def ev(id):
 a=[(id>>(2*j))&3 for j in range(10)]
 return tuple(h^int(np.bitwise_xor.reduce(np.array([int(mul(a[j],v)) for j,v in enumerate(terms)],dtype=np.uint8))) for h,terms in zip(base,vals))
keys={ev(int(id)):int(id) for id in ids}
assert len(keys)==len(ids)
seed=next(iter(keys))
def proj(A,p):
 w=[]
 for row in A:
  r=0
  for a,b in zip(row,p):r^=int(mul(a,b))
  w.append(r)
 k=exp(next(a for a in w if a),2)
 return tuple(int(mul(a,k)) for a in w)

def det(A):
 r=0
 for i in range(3):
  for j in range(3):
   for k in range(3):
    if len({i,j,k})==3:r^=int(mul(mul(A[0][i],A[1][j]),A[2][k]))
 return r
G=[[[1,1,0],[0,1,0],[0,0,1]], [[1,0,0],[0,1,1],[0,0,1]],[[0,1,0],[1,0,0],[0,0,1]],[[2,0,0],[0,1,0],[0,0,1]]]
steps=[]
for A in G:
 d=det(A); assert d
 dinv=exp(d,2)
 permutation=[points.index(proj(A,p)) for p in points]
 steps.append((dinv,permutation))
seen={seed}; stack=[seed]
while stack:
 x=stack.pop()
 for dinv,perm in steps:
  y=tuple(int(mul(dinv,x[j])) for j in perm)
  assert y in keys
  if y not in seen:seen.add(y);stack.append(y)
print('generator_orbit_size:',len(seen))
assert len(seen)==960
print('PGL3(F4)_order:',60480)
print('projective_stabilizer_order:',60480//len(seen))
print('normalized_coefficients_example:',[(int(ids[0])>>(2*j))&3 for j in range(10)])
