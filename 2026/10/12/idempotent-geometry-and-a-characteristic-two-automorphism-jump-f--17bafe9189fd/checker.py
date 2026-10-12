from itertools import product
from collections import Counter

def mul(x,y,p):
 z=[0]*4
 for i,xi in enumerate(x):
  for j,yj in enumerate(y):
   z[(2*j-i)%4]=(z[(2*j-i)%4]+xi*yj)%p
 return tuple(z)
def rank4(cols,p):
 mat=[[cols[j][i] for j in range(4)] for i in range(4)]
 rank=0
 for j in range(4):
  i=next((r for r in range(rank,4) if mat[r][j]%p),None)
  if i is None:continue
  mat[rank],mat[i]=mat[i],mat[rank]
  inv=pow(mat[rank][j],-1,p)
  for t in range(j,4):mat[rank][t]=mat[rank][t]*inv%p
  for r in range(rank+1,4):
   s=mat[r][j]
   for t in range(j,4):mat[r][t]=(mat[r][t]-s*mat[rank][t])%p
  rank+=1
 return rank

def check(p):
 E=list(product(range(p),repeat=4))
 ids=[x for x in E if mul(x,x,p)==x]
 predicted=2*p*p if p==2 else 3*p-2
 print('p',p,'idempotents including zero',len(ids),'predicted nonzero',predicted,'observed nonzero',len(ids)-1)
 basis=[tuple(int(i==j) for i in range(4)) for j in range(4)]
 ij={(i,j):(2*j-i)%4 for i in range(4) for j in range(4)}
 aut=[]
 for cols in product((v for v in ids if any(v)), repeat=4):
  if rank4(cols,p)<4:continue
  if all(mul(cols[i],cols[j],p)==cols[ij[i,j]] for i in range(4) for j in range(4)):
   aut.append(cols)
 print('automorphisms',len(aut),'expected',2*p**4 if p==2 else 2*(p-1)**2)
 assert len(ids)-1==predicted
 assert len(aut)==(2*p**4 if p==2 else 2*(p-1)**2)
for p in (2,3,5):check(p)

from itertools import product
q=4
def add(x,y):return x^y
def mul(x,y):
 z=0
 for i in range(2):
  for j in range(2):
   if (x>>i)&1 and (y>>j)&1: z^=1<<(i+j)
 if z&8:z^=0b1110
 if z&4:z^=0b111
 return z

def vmul(v,w):
 out=[0]*4
 for i in range(4):
  for j in range(4): out[(2*j-i)%4]^=mul(v[i],w[j])
 return tuple(out)
E=list(product(range(4),repeat=4))
ids=[v for v in E if vmul(v,v)==v]
assert len(ids)==33
# Induced automorphisms: on basis p=e0,q=e1,u=e0+e2,v=e1+e3,
# permutation or identity on p,q and simultaneously u,v; arbitrary shifts t(p),t(q) in span u,v.
def phi(perm,a,b,c,d):
 # images of p,q are their permuted versions plus shifts
 p=(1,0,0,0); q=(0,1,0,0);u=(1,0,1,0);v=(0,1,0,1)
 shifts=[tuple(add(mul(a,u[i]),mul(b,v[i])) for i in range(4)),tuple(add(mul(c,u[i]),mul(d,v[i])) for i in range(4))]
 P=q if perm else p;Q=p if perm else q; U=v if perm else u;V=u if perm else v
 outP=tuple(add(P[i],shifts[0][i]) for i in range(4))
 outQ=tuple(add(Q[i],shifts[1][i]) for i in range(4))
 outE2=tuple(add(outP[i],U[i]) for i in range(4))
 outE3=tuple(add(outQ[i],V[i]) for i in range(4))
 return (outP,outQ,outE2,outE3)
seen=set()
for perm,a,b,c,d in product(range(2),range(4),range(4),range(4),range(4)):
 cols=phi(perm,a,b,c,d)
 assert cols not in seen
 seen.add(cols)
 for i in range(4):
  for j in range(4):
   assert vmul(cols[i],cols[j])==cols[(2*j-i)%4]
assert len(seen)==512
print('F4_IDEMPOTENTS',len(ids),'F4_VERIFIED_AUT_CONSTRUCTIONS',len(seen))

print("VERIFY_OK")
