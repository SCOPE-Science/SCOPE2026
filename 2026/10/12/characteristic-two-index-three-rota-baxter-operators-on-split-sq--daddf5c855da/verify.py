"""Finite-field verification of weight-zero Rota--Baxter operators on k+V.
Run: python3 verify.py  (standard Python only)."""
from itertools import product
from math import prod

def matmul(a,b,q):
 n=len(a)
 return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(n))%q for j in range(n)) for i in range(n))

def rank(a,q):
 a=[list(row) for row in a]; m=len(a); n=len(a[0]) if a else 0; r=0
 for j in range(n):
  k=next((k for k in range(r,m) if a[k][j]%q),None)
  if k is None:continue
  a[r],a[k]=a[k],a[r]
  z=pow(a[r][j],-1,q);a[r]=[(x*z)%q for x in a[r]]
  for k in range(m):
   if k!=r:
    z=a[k][j];a[k]=[(x-z*y)%q for x,y in zip(a[k],a[r])]
  r+=1
  if r==m:break
 return r

def gl(n,q):return prod(q**n-q**i for i in range(n))

def expected(n,q):
 s=0; nil3=0; strata=[]
 for r in range(n//2+1):
  t=n-2*r
  nr=gl(n,q)//(q**(r*r+2*r*t)*gl(r,q)*gl(t,q))
  assert nr*q**(r*r+2*r*t)*gl(r,q)*gl(t,q)==gl(n,q)
  s+=nr*q**n;nil3+=nr*(q**n-q**(n-r))
  sizes=[1]
  if r: sizes.extend([q**r-1,q**n-q**(n-r)])
  if t:sizes.append(q**(n-r)-q**r)
  strata.extend([nr*x for x in sizes])
 assert sum(strata)==s
 assert len(strata)==(2*n+1 if n%2==0 else 2*n)
 return s,nil3,sorted(strata)

def finite_test(n,q):
 matcount=0; opcount=0; nil3=0
 for entries in product(range(q),repeat=n*n):
  t=tuple(tuple(entries[i*n+j] for j in range(n)) for i in range(n))
  zero=all(x==0 for row in matmul(t,t,q) for x in row)
  if zero:matcount+=1
  for v in product(range(q),repeat=n):
   a=((0,)*(n+1),)+tuple((v[i],)+t[i] for i in range(n))
   # Check defining identity on every pair of basis vectors, not merely rank conditions.
   def prod_ring(x,y):
    return (x[0]*y[0]%q,)+tuple((x[0]*y[i]+y[0]*x[i])%q for i in range(1,n+1))
   def apply(x):return tuple(sum(a[i][j]*x[j] for j in range(n+1))%q for i in range(n+1))
   bs=[tuple(int(i==j) for i in range(n+1)) for j in range(n+1)]
   valid=True
   for x in bs:
    for y in bs:
     px=apply(x);py=apply(y)
     z=tuple((u+v)%q for u,v in zip(prod_ring(x,py),prod_ring(px,y)))
     if prod_ring(px,py)!=apply(z):valid=False;break
    if not valid:break
   assert valid == zero,('classification failure',n,q,t,v,valid,zero)
   if valid:
    opcount+=1
    if any(sum(t[i][j]*v[j] for j in range(n))%q for i in range(n)):
     nil3+=1
 assert (opcount,nil3)==expected(n,q)[:2],(n,q,opcount,nil3,expected(n,q))
 print('field',q,'radical_dimension',n,'squarezero_matrices',matcount,'operators',opcount,'nilpotency_index_three',nil3,'orbits',len(expected(n,q)[2]))

for n,q in ((1,2),(2,2),(3,2)):
 finite_test(n,q)
print('VERIFY_OK')
