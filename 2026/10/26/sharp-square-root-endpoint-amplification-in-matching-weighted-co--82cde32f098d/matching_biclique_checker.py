"""Exact rational reconstruction of matching-weighted bipartite cut/cycle projections."""
from fractions import Fraction as F
from math import isqrt

def formula(n,x):
 t=x*x;d=n-1+t;h=n-2+2*t
 cd=(t*(2*d+n-2)+x*(n-1)*(2*d+n-4))/(d*h)
 u=(2*d*d-n)/(n*d*h)
 w=(2*d*(1-t)-n)/(n*d*h)
 co=x*(2*d+n-4)/(d*h)+u+abs(w)+F(2*(n-2),n)+F((n-2)*(n-3),1)/(d*h)
 pd=1+cd-2*t*(2*d-1)/(d*h)
 po=1+co-2*u
 return cd,co,pd,po

def solve(A,b):
 n=len(b); a=[list(A[i])+[b[i]] for i in range(n)]
 for k in range(n):
  h=next(i for i in range(k,n) if a[i][k]);a[k],a[h]=a[h],a[k]
  z=a[k][k];a[k]=[v/z for v in a[k]]
  for i in range(n):
   if i!=k:
    z=a[i][k]
    if z:a[i]=[y-z*v for y,v in zip(a[i],a[k])]
 return [a[i][-1] for i in range(n)]

def verify(n,x):
 assert isinstance(x,F)
 t=x*x; edges=[(i,n+j,x if i==j else F(1)) for i in range(n) for j in range(n)]
 lap=[[F(0) for _ in range(2*n)] for _ in range(2*n)]
 for a,b,r in edges:
  v=r*r
  lap[a][a]+=v;lap[b][b]+=v;lap[a][b]-=v;lap[b][a]-=v
 ecount=0
 for i,(a,b,r) in enumerate(edges):
  rhs=[F(0)]*(2*n-1)
  rhs[a]+=r
  if b<2*n-1:rhs[b]-=r
  z=solve([row[:-1] for row in lap[:-1]],rhs)
  z.append(F(0));q=[]
  for c,d,s in edges:q.append(s*(z[c]-z[d]))
  assert sum(q[j]*q[j] for j in range(len(q)))==q[i]  # projector self-adjoint and idempotent
  diag=q[i];cut=sum(map(abs,q)); cyc=1+cut-2*diag
  CD,CO,PD,PO=formula(n,x)
  if a==b-n:assert (cut,cyc)==(CD,PD),(n,x,a,b,cut,CD,cyc,PD)
  else:assert (cut,cyc)==(CO,PO),(n,x,a,b,cut,CO,cyc,PO)
  ecount+=1
 return ecount

if __name__=='__main__':
 combos=[(n,F(p,q)) for n in (3,4,5,6) for p,q in ((1,4),(1,2),(1,1),(3,2),(2,1),(4,1))]
 count=sum(verify(n,x) for n,x in combos)
 print(f'MATCHED_BICLIQUE_EXACT_OK graphs={len(combos)} columns={count}')
