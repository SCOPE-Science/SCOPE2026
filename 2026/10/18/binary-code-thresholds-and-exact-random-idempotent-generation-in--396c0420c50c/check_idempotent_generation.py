"""Finite-field direct multiplication checks for finite square-zero quiver algebras."""
from itertools import product
from collections import Counter
from math import comb

class Field:
 def __init__(self,q):
  assert q in (2,3,4,5)
  self.q=q
 def add(self,a,b):return a^b if self.q==4 or self.q==2 else (a+b)%self.q
 def mul(self,a,b):
  if self.q!=4:return (a*b)%self.q
  z=0
  for i in range(2):
   if (b>>i)&1:z^=a<<i
  if z&8:z^=0b1100 # x^3 = x^2+x, via x^2=x+1 gives x^3=1
  if z&4:z^=0b111 # x^2 = x+1, XOR x^2+x+1
  return z
 def inv(self,a):
  assert a
  for b in range(1,self.q):
   if self.mul(a,b)==1:return b
  raise AssertionError


def predicted(q,n,arrows,d):
 # arrow list of endpoints, repeated entries represent independent arrows
 bypair=Counter(arrows)
 if any(i==j for i,j in arrows):return 0
 def fullrank(hminus1,m):
  if hminus1<m:return 0
  z=q**m
  for j in range(m):z*=q**hminus1-q**j
  return z
 count=0
 for labels in product(range(1<<d),repeat=n):
  if len(set(labels))!=n:continue
  factors=[]
  for (i,j),m in bypair.items():
   h=(labels[i]^labels[j]).bit_count()
   factors.append(fullrank(h-1,m))
  x=1
  for f in factors:x*=f
  count+=x
 return count


def direct(q,n,arrows,d):
 F=Field(q)
 m=len(arrows);D=n+m
 def product_a(x,y):
  ans=[F.mul(x[i],y[i]) for i in range(n)]
  ans.extend(F.add(F.mul(x[i],y[n+a]),F.mul(x[n+a],y[j])) for a,(i,j) in enumerate(arrows))
  return tuple(ans)
 def independent_add(b,v):
  v=list(v)
  for pivot,old in b:
   if v[pivot]:
    t=v[pivot]
    v=[F.add(v[i],F.mul(t,old[i])) if q in (2,4) else (v[i]-F.mul(t,old[i]))%q for i in range(D)]
  if not any(v):return False
  j=next(i for i,x in enumerate(v) if x)
  inv=F.inv(v[j])
  v=tuple(F.mul(inv,x) for x in v)
  b.append((j,v))
  b.sort(key=lambda z:z[0])
  return True
 def generate(xs):
  b=[]
  one=tuple([1]*n+[0]*m)
  independent_add(b,one)
  for x in xs:independent_add(b,x)
  while True:
   before=len(b)
   old=[vec for _,vec in b]
   for x in old:
    for y in old:
     independent_add(b,product_a(x,y))
     if len(b)==D:return True
   if len(b)==before:break
  return len(b)==D
 idemps=[]
 for bits in product(range(2), repeat=n):
  choices=[([0] if bits[i]==bits[j] else list(range(q))) for i,j in arrows]
  for zs in product(*choices):
   v=tuple(bits+zs)
   assert product_a(v,v)==v, (q,arrows,v)
   idemps.append(v)
 answer=sum(generate(xs) for xs in product(idemps,repeat=d))
 return answer,len(idemps)

if __name__=='__main__':
 cases=[
 (2,2,[(0,1)],1),(2,2,[(0,1)],2),(2,2,[(0,1)],3),
 (3,2,[(0,1)],2),(4,2,[(0,1)],2),
 (2,2,[(0,1),(0,1)],2),(2,2,[(0,1),(0,1)],3),
 (2,2,[(0,1),(1,0)],2),(3,2,[(0,1),(1,0)],2),
 (2,2,[(0,0)],2),
 (2,3,[(0,1),(1,2)],2),(2,3,[(0,1),(1,2)],3),
 (2,3,[(0,1),(1,2),(2,0)],2),
 (3,3,[(0,1),(1,2)],2),
 ]
 for q,n,ar,d in cases:
  expected=predicted(q,n,ar,d)
  actual,total=direct(q,n,ar,d)
  assert actual==expected,(q,n,ar,d,expected,actual)
  print('MATCH',q,n,ar,d,'total_idempotents',total,'generating_tuples',actual,'denominator',total**d,flush=True)
 print('ALL_IDEMPOTENT_GENERATOR_CASES_PASSED',len(cases))
