from itertools import product
from math import comb
from fractions import Fraction

def rank(arr):
    if not arr: return 0
    A=[[Fraction(x) for x in row] for row in arr]; m=len(A); n=len(A[0]); piv=0
    for c in range(n):
        ii=next((i for i in range(piv,m) if A[i][c]),None)
        if ii is None: continue
        A[piv],A[ii]=A[ii],A[piv]
        x=A[piv][c];A[piv]=[v/x for v in A[piv]]
        for i in range(piv+1,m):
            if A[i][c]:
                x=A[i][c];A[i]=[v-x*w for v,w in zip(A[i],A[piv])]
        piv+=1
        if piv==m:break
    return piv

def eval_formula(p,q,r):
    def A(k): return [comb(k,s)*2**s for s in range(1,k+1)]
    def mul(a,b):
        c=[0]*(len(a)+len(b)-1) if a and b else []
        for i,x in enumerate(a):
            for j,y in enumerate(b): c[i+j]+=x*y
        return c
    ans=[0]*(p+q+r+1)
    def add(poly,shift=0,scale=1):
        for i,x in enumerate(poly): ans[i+shift]+=scale*x
    add(mul(A(p),A(q+r))); add(mul(A(p+r),A(q)));add(mul(A(p),A(q)),scale=-1)
    for x in range(p+1):
      for y in range(q+1):
       for z in range(1,r+1):ans[x+y+z-1]+=comb(p,x)*comb(q,y)*comb(r,z)*2**(x+y+z)
    add(A(q),shift=p+r);add(A(p),shift=q+r)
    ans[-1]+=1
    return ans

def geometric(p,q,r):
 n=p+q+r;A=list(range(p))+list(range(p+q,n));B=list(range(p,p+q))+list(range(p+q,n))
 def picks(u,indices):
  maxv=max(abs(u[i]) for i in indices)
  return tuple(sorted((i,sign) for i in indices for sign in [-1,1] if sign*u[i]==maxv)) if maxv>0 else tuple(sorted((i,s) for i in indices for s in [-1,1]))
 def verts(sel):
  pts=[]
  for i,s in sel:
   v=[0]*n;v[i]=s;pts.append(v)
  return pts
 faces={}
 for u in product([-2,-1,0,1,2],repeat=n):
  S_A=picks(u,A); S_B=picks(u,B)
  key=(S_A,S_B)
  if key in faces:continue
  va=verts(S_A);vb=verts(S_B)
  dirs=[[x-y for x,y in zip(v,va[0])] for v in va[1:]]+[[x-y for x,y in zip(v,vb[0])] for v in vb[1:]]
  faces[key]=rank(dirs)
 counts=[0]*(n+1)
 for d in faces.values():counts[d]+=1
 return counts

cases=0
for n in range(1,6):
 for p in range(n+1):
  for q in range(n-p+1):
   r=n-p-q
   if p+r==0 or q+r==0:continue
   f=eval_formula(p,q,r)
   actual=geometric(p,q,r)
   if f!=actual: raise AssertionError((p,q,r,f,actual))
   cases+=1
print('TWO_CROSSPOLYTOPE_FVECTOR_OK valid_cases=',cases)
for t in [(1,1,1),(1,1,2),(2,1,1),(0,2,2),(2,2,1)]: print(t,eval_formula(*t))
