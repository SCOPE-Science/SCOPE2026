from itertools import product
from collections import Counter
from sympy import Poly, symbols
p=5
z=symbols('z')
POLYS={1:[0,1]}
for d in range(2,7):
 for v in product(range(p),repeat=d):
  if v[0]==0: continue
  pol=Poly(z**d+sum(v[i]*z**i for i in range(d)),z,modulus=p)
  if pol.is_irreducible:
   POLYS[d]=list(v)+[1];break
print('poly',POLYS,flush=True)

def distrib(d):
 mod=POLYS[d]
 if d==1:
  return Counter({(x%p,x**3%p):1 for x in range(p)})
 q=p**d
 digits=[]
 for x in range(q):
  digs=[]; k=x
  for i in range(d):digs.append(k%p);k//=p
  digits.append(tuple(digs))
 def encode(v):return sum((e%p)*p**i for i,e in enumerate(v))
 def add(a,b):return encode([(x+y)%p for x,y in zip(digits[a],digits[b])])
 def mul(a,b):
  va=digits[a];vb=digits[b]; t=[0]*(2*d-1)
  for i,x in enumerate(va):
   if not x:continue
   for j,y in enumerate(vb):
    if y:t[i+j]=(t[i+j]+x*y)%p
  for k in range(2*d-2,d-1,-1):
   c=t[k]
   if c:
    for j in range(d):t[k-d+j]=(t[k-d+j]-c*mod[j])%p
  return encode(t[:d])
 def power(a,n):
  out=1
  while n:
   if n&1:out=mul(out,a)
   n//=2
   if n:a=mul(a,a)
  return out
 D=Counter()
 for a in range(q):
  tr=0;trc=0; b=a
  for i in range(d):
   tr=add(tr,b)
   b3=mul(mul(b,b),b)
   trc=add(trc,b3)
   b=power(b,p)
  assert b==a and tr<p and trc<p, (d,a,b,tr,trc)
  D[(tr,trc)]+=1
 return D
Ds={d:distrib(d) for d in range(1,7)}
for d,D in Ds.items():print('d',d,'total',sum(D.values()),'trace00',D[0,0],flush=True)
for cyc,a,b in [((1,1,1,1,1,1),6,-4),((2,1,1,1,1),0,4),((2,2,1,1),2,0),((2,2,2),4,0),((3,1,1,1),0,-1),((3,2,1),0,1),((3,3),3,2),((4,1,1),2,2),((4,2),0,2),((5,1),1,1),((6,),1,0)]:
 dp=Counter({(0,0):1})
 for d in cyc:
  nxt=Counter()
  for (s,t),v in dp.items():
   for (u,w),v2 in Ds[d].items():nxt[(s+u)%p,(t+w)%p]+=v*v2
  dp=nxt
 n=(dp[0,0]-1)//(p-1)
 assert n==p**3+a*p*p+b*p+1,(cyc,n,p**3+a*p*p+b*p+1)
 print('PASS',cyc,n,flush=True)
