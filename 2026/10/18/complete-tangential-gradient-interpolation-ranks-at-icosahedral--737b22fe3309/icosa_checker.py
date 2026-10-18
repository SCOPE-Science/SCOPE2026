#!/usr/bin/env python3
"""Exact finite-field nonvanishing checks for tangent harmonic sampling on an icosahedron.
No floating-point arithmetic is used for the finite-degree algebraic matrix calculations.
"""
from fractions import Fraction
from math import isqrt
P=10009
assert all(P%d!=0 for d in range(2,isqrt(P)+1)), "Modulus must be prime"
RT=next(v for v in range(P) if v*v%P==5)
assert RT*RT%P==5
inv=lambda a: pow(int(a)%P, -1, P)
phi=((1+RT)*inv(2))%P
L=(1+phi*phi)%P
qs=[(0,1,phi),(0,1,-phi),(1,phi,0),(1,-phi,0),(phi,0,1),(phi,0,-1)]
qs=[[v%P for v in q] for q in qs]
def dot(a,b): return sum(x*y for x,y in zip(a,b))%P
def cross(a,b):return [(a[1]*b[2]-a[2]*b[1])%P,(a[2]*b[0]-a[0]*b[2])%P,(a[0]*b[1]-a[1]*b[0])%P]
U=[]
for q in qs:
 k=q.index(0)
 e=[int(k==j) for j in range(3)]
 U += [(q,e),(q,cross(q,e))]
# Distinct icosahedron representatives have pairwise dot products +-1/sqrt(5).
tvals=sorted(set(dot(q,r)*inv(L)%P for i,q in enumerate(qs) for r in qs[i+1:]))
assert len(tvals)==2 and sum(tvals)%P==0
for t in tvals: assert 5*t*t%P==1
# Legendre recurrence for t=+-1/sqrt(5), and derivative identity.
cache={}
for t in tvals:
 seq=[1,t]
 for n in range(1,100): seq.append(((2*n+1)*t*seq[-1]-n*seq[-2])*inv(n+1)%P)
 cache[t]=seq

def matrix(l):
 n=l*(l+1)
 df=(n*inv(2))%P
 d={}
 for t in tvals:
  S=cache[t]
  a=(l*(S[l-1]-t*S[l])*inv(1-t*t))%P if l else 0
  b=((2*t*a-n*S[l])*inv(1-t*t))%P
  d[t]=(a,b)
 A=[]
 for i,(q,u) in enumerate(U):
  row=[]
  for j,(r,v) in enumerate(U):
   if i//2==j//2: z=df*dot(u,v)
   else:
    t=dot(q,r)*inv(L)%P
    a,b=d[t]
    z=a*dot(u,v)+b*dot(u,r)*dot(v,q)*inv(L)
   row.append(z%P)
  A.append(row)
 return A

def rank_mod(A):
 a=[x[:] for x in A]
 r=0; m=len(a);n=len(a[0])
 for j in range(n):
  i=next((v for v in range(r,m) if a[v][j]),None)
  if i is None:continue
  a[r],a[i]=a[i],a[r]
  s=inv(a[r][j]);a[r]=[x*s%P for x in a[r]]
  for i in range(r+1,m):
   fac=a[i][j]
   if fac:a[i]=[(x-fac*y)%P for x,y in zip(a[i],a[r])]
  r+=1
  if r==m:break
 return r
if __name__=='__main__':
 rs=[]
 for l in range(100):
  r=rank_mod(matrix(l));rs.append(r)
 print('modulus',P,'sqrt5',RT,'ranks0..25',rs[:26], 'below_full',[(i,v) for i,v in enumerate(rs) if v!=12])
 assert rs[:15]==[0,3,5,4,9,8,12,12,9,12,12,12,12,12,9]
 assert all(r==12 for r in rs[15:])
 print('PASS: all degrees 15..99 full rank modulo',P)
