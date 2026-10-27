"""Exact rank verification for the icosidodecahedral Legendre evaluation kernel.
Only Python's standard library is required. All arithmetic is exact.
"""
from fractions import Fraction as Q
from math import isqrt

Z = (Q(0), Q(0)); O=(Q(1),Q(0)); R=(Q(0),Q(1))
def a(x,y):return (x[0]+y[0], x[1]+y[1])
def neg(x):return (-x[0],-x[1])
def sub(x,y):return a(x,neg(y))
def mul(x,y):return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def scale(x,c):return (x[0]*c,x[1]*c)
def div(x,y):
 d=y[0]*y[0]-5*y[1]*y[1]
 assert d!=0
 return ((x[0]*y[0]-5*x[1]*y[1])/d,(x[1]*y[0]-x[0]*y[1])/d)
def vecneg(v):return tuple(neg(x) for x in v)
def dot(v,w):
 t=Z
 for x,y in zip(v,w):t=a(t,mul(x,y))
 return t

def geometry():
 phi=scale(a(O,R),Q(1,2))
 V=[]
 for i in (-1,1):
  for j in (-1,1):
   x=scale(O,i);y=scale(O,j);z=scale(phi,j)
   V += [(Z,x,z),(x,z,Z),(z,Z,x)]
 edges=[]
 for i in range(12):
  for j in range(i+1,12):
   if dot(tuple(sub(u,v) for u,v in zip(V[i],V[j])),
          tuple(sub(u,v) for u,v in zip(V[i],V[j])))==scale(O,4):
    edges.append(tuple(a(u,v) for u,v in zip(V[i],V[j])))
 assert len(edges)==30
 Y=[];used=set()
 for i,w in enumerate(edges):
  if i in used:continue
  other=[j for j,v in enumerate(edges) if v==vecneg(w)]
  assert len(other)==1
  used.update((i,other[0]));Y.append(w)
 assert len(Y)==15 and len(used)==30
 fac=(Q(3,8),Q(-1,8))
 T=[[mul(dot(v,w),fac) for w in Y] for v in Y]
 assert all(T[i][i]==O for i in range(15))
 assert all(T[i][j]==T[j][i] for i in range(15) for j in range(15))
 # Every row has the exact 1,2,4,4,4 absolute-dot-product valencies.
 low=(Q(-1,4),Q(1,4));mid=(Q(1,2),Q(0));high=(Q(1,4),Q(1,4))
 for row in T:
  squares=[mul(z,z) for z in row]
  assert squares.count(O)==1
  assert squares.count(Z)==2
  assert squares.count(mul(low,low))==4
  assert squares.count(mul(mid,mid))==4
  assert squares.count(mul(high,high))==4
 return T

T=geometry();levels=sorted(set(sum(T,[])))
print('vertices=30 antipodal_pairs=15 dot_levels=',len(levels))

def legendre_exact(n):
 vals={t:[O,t] for t in levels}
 for k in range(1,n):
  for t in levels:
   z=sub(scale(mul(t,vals[t][-1]),2*k+1),scale(vals[t][-2],k))
   vals[t].append(scale(z,Q(1,k+1)))
 return {t:vals[t][n] for t in levels}

def rank_exact(A):
 A=[list(row) for row in A];n=len(A);r=0
 for col in range(n):
  idx=next((k for k in range(r,n) if A[k][col]!=Z),None)
  if idx is None:continue
  A[r],A[idx]=A[idx],A[r]
  pivot=A[r][col]
  A[r]=[div(x,pivot) for x in A[r]]
  for k in range(r+1,n):
   if A[k][col]!=Z:
    factor=A[k][col]
    A[k]=[sub(x,mul(factor,y)) for x,y in zip(A[k],A[r])]
  r+=1
  if r==n:break
 return r

exact=[]
for n in range(15):
 vals=legendre_exact(n)
 M=[[vals[t] for t in row] for row in T]
 exact.append(rank_exact(M))
 if n in (8,14):assert all(sum((z[0] for z in row),Q(0))==0 and sum((z[1] for z in row),Q(0))==0 for row in M)
assert exact == [1,3,5,7,9,11,10,15,14,15,15,15,15,15,14]
print('exact_ranks_0_to_14=',exact)

p=1000000009;root=383008016
assert root*root%p==5 and p>200
assert all(p%j for j in range(2,isqrt(p)+1))
def fmap(t):
 def rr(q):return (q.numerator*pow(q.denominator,-1,p))%p
 return (rr(t[0])+root*rr(t[1]))%p
verts={t:fmap(t) for t in levels}
vals={t:[1,verts[t]] for t in levels}
for n in range(1,200):
 iv=pow(n+1,-1,p)
 for t in levels:
  q=vals[t]
  q.append(((2*n+1)*verts[t]*q[-1]-n*q[-2])*iv%p)

def rank_mod(A):
 A=[row[:] for row in A];n=len(A);r=0
 for j in range(n):
  k=next((i for i in range(r,n) if A[i][j]!=0),None)
  if k is None:continue
  A[r],A[k]=A[k],A[r]
  factor=pow(A[r][j],-1,p)
  A[r]=[v*factor%p for v in A[r]]
  for i in range(r+1,n):
   if A[i][j]!=0:
    f=A[i][j]
    A[i]=[(x-f*y)%p for x,y in zip(A[i],A[r])]
  r+=1
  if r==n:break
 return r
ranks=[]
for n in range(200):
 ranks.append(rank_mod([[vals[t][n] for t in row] for row in T]))
assert ranks[:15]==exact
assert all(x==15 for x in ranks[15:])
print('modular_prime=',p,'square_root_of_5=',root)
print('modular_ranks_0_to_14=',ranks[:15])
print('modular_full_rank_15_to_199=',len(ranks[15:]))
print('Bernstein: for n>=200, offdiagonal row sum < (1046/63)/sqrt(300) < 1.')

# Additional exact spectral certificate for the exceptional sextic degree.
V6=legendre_exact(6)
G6=[[scale(V6[t],2) for t in row] for row in T]

def mm(A,B):
 return [[sumfield([mul(A[i][k],B[k][j]) for k in range(15)])
          for j in range(15)] for i in range(15)]
def sumfield(vs):
 q=Z
 for x in vs:q=a(q,x)
 return q

def minus_scalar(A,c):
 return [[sub(A[i][j],scale(O,c) if i==j else Z) for j in range(15)] for i in range(15)]
F=[[O if i==j else Z for j in range(15)] for i in range(15)]
for c in [Q(0),Q(315,512),Q(165,128),Q(21,4)]:
 F=mm(F,minus_scalar(G6,c))
assert all(x==Z for row in F for x in row)
print('sextic_gram_spectral_polynomial= x(x-315/512)(x-165/128)(x-21/4) : exact zero')
print('PASS')
