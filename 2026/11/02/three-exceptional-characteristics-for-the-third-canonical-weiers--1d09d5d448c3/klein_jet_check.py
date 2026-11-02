"""Pointwise jet determinant for cubic-series ramification on Klein's quartic.
No dependencies other than Python; uses ordinary truncated power series mod p.
"""
from itertools import product

def mul(a,b,p,N):
 c=[0]*N
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b[:N-i]):
    if y:c[i+j]=(c[i+j]+x*y)%p
 return c

def power(a,n,p,N):
 r=[1]+[0]*(N-1)
 for _ in range(n):r=mul(r,a,p,N)
 return r

def det(M,p):
 a=[row[:] for row in M];d=1;n=len(M)
 for j in range(n):
  k=next((i for i in range(j,n) if a[i][j]%p),None)
  if k is None:return 0
  if k!=j:
   a[k],a[j]=a[j],a[k];d=-d
  v=a[j][j]%p;d=d*v%p; inv=pow(v,-1,p)
  for i in range(j+1,n):
   u=a[i][j]*inv%p
   if u:
    for h in range(j+1,n):a[i][h]=(a[i][h]-u*a[j][h])%p
    a[i][j]=0
 return d%p

def jets_at(p,a,b,N=10):
 assert (a*a*a*b+b*b*b+a)%p==0
 fy=(a*a*a+3*b*b)%p
 assert fy!=0
 x=[a,1]+[0]*(N-2);y=[b]+[0]*(N-1)
 for k in range(1,N):
  F=mul(power(x,3,p,N),y,p,N)
  G=power(y,3,p,N)
  c=(F[k]+G[k]+x[k])%p
  y[k]=-c*pow(fy,-1,p)%p
 basis=[(0,0),(1,0),(0,1),(2,0),(1,1),(0,2),(3,0),(2,1),(1,2),(0,3)]
 mats=[mul(power(x,i,p,N),power(y,j,p,N),p,N) for i,j in basis]
 mat=[[z[k] for z in mats] for k in range(10)]
 return det(mat,p)

if __name__=='__main__':
 for p in (13,17,79,139,277):
  F=[(a,b) for a in range(p) for b in range(p) if (a**3*b+b**3+a)%p==0 and (a**3+3*b*b)%p]
  z=next(((a,b,jets_at(p,a,b)) for (a,b) in F if jets_at(p,a,b)),None)
  print('p',p,'point_count',len(F),'first_nonzero_jet',z)
  assert z is not None
 print('VERIFY_OK')
