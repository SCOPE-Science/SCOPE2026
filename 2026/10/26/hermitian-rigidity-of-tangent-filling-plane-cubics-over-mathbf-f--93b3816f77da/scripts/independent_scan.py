"""Independent vectorized incidence census for ternary cubics over GF(4).
Requires numpy; run from a writable working directory.
"""
import numpy as np
from collections import Counter
def mul(a,b):
    v=0
    for i in range(2):
        if (b>>i)&1:v^=a<<i
    if v&8:v^=12
    if v&4:v^=7
    return v
T=np.array([[mul(a,b) for b in range(4)]for a in range(4)],dtype=np.uint8)
def power(a,n):
    ans=1
    for _ in range(n): ans=int(T[ans,a])
    return ans
ex=[(i,j,3-i-j) for i in range(3,-1,-1) for j in range(3-i,-1,-1)]
pts=[(1,y,z)for y in range(4)for z in range(4)]+[(0,1,z)for z in range(4)]+[(0,0,1)]
line_masks=[]
for l in pts:
    bits=0
    for i,p in enumerate(pts):
        if T[l[0],p[0]]^T[l[1],p[1]]^T[l[2],p[2]]==0:bits|=1<<i
    line_masks.append(bits)
line_by_normal={}
for x in range(4):
 for y in range(4):
  for z in range(4):
   if (x,y,z)==(0,0,0):continue
   lead=next(a for a in (x,y,z) if a)
   inv=power(lead,2)
   q=tuple(int(T[t,inv])for t in (x,y,z))
   line_by_normal[(x,y,z)]=pts.index(q)
code=np.arange(1,1<<20,dtype=np.uint32)
co=np.empty((10,len(code)),dtype=np.uint8)
for j in range(10):co[j]=(code>>(2*j))&3
nz=co!=0
hi=9-nz[::-1].argmax(axis=0)
filter0=co[hi,np.arange(len(code))]==1
codes=code[filter0];co=co[:,filter0];n=len(codes)
cover=np.zeros(n,dtype=np.uint32);number=np.zeros(n,dtype=np.uint8);pointmask=np.zeros(n,dtype=np.uint32)
for pointindex,p in enumerate(pts):
    m=np.array([int(T[T[power(p[0],a),power(p[1],b)],power(p[2],c)])for a,b,c in ex],dtype=np.uint8)
    dm=[]
    for var in range(3):
        dd=[]
        for exp in ex:
            tmp=list(exp)
            if tmp[var]%2:
                tmp[var]-=1
                dd.append(int(T[T[power(p[0],tmp[0]),power(p[1],tmp[1])],power(p[2],tmp[2])]))
            else:dd.append(0)
        dm.append(np.array(dd,dtype=np.uint8))
    def eval_from(m):
        val=np.zeros(n,dtype=np.uint8)
        for j in range(10):val^=T[m[j],co[j]]
        return val
    f=eval_from(m); number+=(f==0).astype(np.uint8);pointmask |= np.where(f==0,1<<pointindex,0).astype(np.uint32)
    dx,dy,dz=[eval_from(d)for d in dm]
    lookup=np.zeros(64,dtype=np.uint32)
    for trip,l in line_by_normal.items():
        x,y,z=trip;lookup[x+4*y+16*z]=line_masks[l]
    tangent=lookup[dx+4*dy+16*dz]
    cover=np.bitwise_or(cover,np.where(f==0,tangent,0))
valid=codes[cover==(1<<21)-1]
print('normalized_forms',n,'tangent_filling',len(valid),'rational_point_counts',sorted((int(k),v) for k,v in Counter(number[cover==(1<<21)-1]).items()))

ok=cover==(1<<21)-1
lin=np.zeros(n,dtype=bool)
for bits in line_masks: lin |= (pointmask&bits)==bits
print("TANGENT smooth eligible no rational line",np.count_nonzero(ok&(~lin)), "line-divisible",np.count_nonzero(ok&lin))
open("tangent_noline_python.txt","w").write("".join(str(x)+"\n" for x in codes[ok&(~lin)]))
