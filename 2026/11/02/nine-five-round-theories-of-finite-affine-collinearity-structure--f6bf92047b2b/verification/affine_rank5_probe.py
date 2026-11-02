"""Independent finite-rank EF orbit recursion for point-collinearity affine geometries."""
from itertools import product,combinations
from collections import defaultdict
import time
class FF:
 def __init__(self,q):
  self.q=q
  if q in (2,4,8,16):self.kind='binary';self.poly={2:3,4:7,8:11,16:19}[q];self.degree=q.bit_length()-1
  elif q==9:self.kind='nine'
  else:self.kind='prime'
  self.addT=[[self.add(a,b) for b in range(q)] for a in range(q)]
  self.mulT=[[self.mul(a,b) for b in range(q)] for a in range(q)]
  self.subT=[[self.add(a,self.neg(b)) for b in range(q)] for a in range(q)]
  self.invT=[0]+[next(b for b in range(1,q) if self.mul(a,b)==1) for a in range(1,q)]
 def add(self,a,b):
  if self.kind=='binary':return a^b
  if self.kind=='nine':return ((a%3+b%3)%3)+3*((a//3+b//3)%3)
  return (a+b)%self.q
 def neg(self,a):
  if self.kind=='binary':return a
  if self.kind=='nine':return ((-a)%3)+3*((-(a//3))%3)
  return (-a)%self.q
 def mul(self,a,b):
  if self.kind=='binary':
   x=0;h=1<<self.degree
   while b:
    if b&1:x^=a
    b>>=1;a<<=1
    if a&h:a^=self.poly
   return x
  if self.kind=='nine':
   a0,a1=a%3,a//3;b0,b1=b%3,b//3
   return (a0*b0+2*a1*b1)%3+3*((a0*b1+a1*b0)%3)
  return a*b%self.q
 def sub(self,a,b):return self.subT[a][b]
 def plus(self,a,b):return self.addT[a][b]
 def times(self,a,b):return self.mulT[a][b]

def solve(F,basis,vec):
 # coefficient solve over GF(q), basis affine vectors, assumed linearly independent
 if not basis:return () if not any(vec) else None
 d=len(vec);r=len(basis)
 a=[[basis[j][i] for j in range(r)]+[vec[i]] for i in range(d)];piv=[];row=0
 for col in range(r):
  found=next((k for k in range(row,d) if a[k][col]),None)
  if found is None:continue
  a[row],a[found]=a[found],a[row];inv=F.invT[a[row][col]]
  for j in range(col,r+1):a[row][j]=F.times(a[row][j],inv)
  for k in range(d):
   if k==row or not a[k][col]:continue
   v=a[k][col]
   for j in range(col,r+1):a[k][j]=F.sub(a[k][j],F.times(v,a[row][j]))
  piv.append(col);row+=1
 if any(a[i][-1] for i in range(row,d)):return None
 x=[0]*r
 for i,col in enumerate(piv):x[col]=a[i][-1]
 return tuple(x)

def orbit_key(F,tup):
 if not tup:return ()
 base=tup[0];basis=[];codes=[]
 for x in tup[1:]:
  diff=tuple(F.sub(v,u) for u,v in zip(base,x))
  a=solve(F,basis,diff)
  if a is None:
   basis.append(diff);a=(0,)*(len(basis)-1)+(1,)
  codes.append(a)
 r=len(basis)
 return (r,tuple(code+(0,)*(r-len(code)) for code in codes))

def atomic(F,tup):
 z=tuple(int(tup[i]==tup[j]) for i in range(len(tup)) for j in range(i+1,len(tup)))
 def iscol(i,j,k):
  A=tup[i];B=tup[j];C=tup[k]
  u=tuple(F.sub(y,x) for x,y in zip(A,B));v=tuple(F.sub(y,x) for x,y in zip(A,C))
  return solve(F,[u],v) is not None if any(u) else True
 c=tuple(int(iscol(i,j,k)) for i,j,k in combinations(range(len(tup)),3))
 return (z,c)

intern={}
def getid(t):
 x=intern.get(t)
 if x is None:x=len(intern)+1;intern[t]=x
 return x

def run(q,d):
 t0=time.time();F=FF(q)
 pts=tuple(product(range(q),repeat=d))
 rep=[{():()}]
 for k in range(4):
  nxt={}
  for tup in rep[-1].values():
   for x in pts:
    z=tup+(x,);key=orbit_key(F,z)
    if key not in nxt:nxt[key]=z
  rep.append(nxt)
  #print(q,d,'level',k+1,len(nxt))
 ids={}
 for key,tup in rep[4].items():
  atom=atomic(F,tup)
  ext=frozenset(atomic(F,tup+(p,)) for p in pts)
  ids[key]=getid((4,atom,ext))
 for k in range(3,-1,-1):
  nxt={}
  for key,tup in rep[k].items():
   ext=frozenset(ids[orbit_key(F,tup+(p,))] for p in pts)
   nxt[key]=getid((k,atomic(F,tup),ext))
  ids=nxt
 print('CASE',q,d,'root_id',ids[()],'orbits',[len(x) for x in rep],'sec',round(time.time()-t0,2),flush=True)
 return ids[()]

if __name__=='__main__':
 cases=[(2,2),(2,3),(3,2),(3,3),(4,2),(4,3),(5,2),(5,3),(7,2),(7,3),(8,2),(8,3),(9,2),(9,3),(11,2),(16,2)]
 res={(q,d):run(q,d) for q,d in cases}
 class_groups=[[(2,2)],[(2,3)],[(3,2)],[(3,3)],[(4,2)],[(4,3)],[(5,2),(7,2),(9,2),(11,2)],[(5,3),(7,3),(9,3)],[(8,2),(8,3),(16,2)]]
 for group in class_groups:
  assert len({res[x] for x in group})==1,group
 assert len({res[group[0]] for group in class_groups})==9
 print('NINE_CLASSES_VERIFIED_IN_SAMPLED_FINITE_FIELDS')
 print('ORBIT_VERIFY_OK')
