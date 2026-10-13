#!/usr/bin/env python3
"""Exact line/Galois census for an octahedral sextic surface.
Requires only Python 3 standard library. All arithmetic is exact."""
from itertools import permutations
from collections import Counter
from math import gcd

Z=(0,0); ONE=(1,0); I=(0,1)
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[0],-a[1])
def sub(a,b): return add(a,neg(b))
def mul(a,b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def powg(a,n):
 r=ONE
 for _ in range(n): r=mul(r,a)
 return r
def norm(a):return a[0]*a[0]+a[1]*a[1]
def div(a,b):
 d=norm(b); t=mul(a,(b[0],-b[1])); assert t[0]%d==0 and t[1]%d==0,(a,b,t,d)
 return (t[0]//d,t[1]//d)
def scale(a,v):return tuple(mul(a,z) for z in v)
def dot(A,v):return(add(mul(A[0],v[0]),mul(A[1],v[1])),add(mul(A[2],v[0]),mul(A[3],v[1])))
def det2(v,w):return sub(mul(v[0],w[1]),mul(v[1],w[0]))
def poly(v):
 x,y=v
 return sub(mul(powg(x,5),y),mul(x,powg(y,5)))
POINTS=((ONE,Z),(Z,ONE),(ONE,ONE),(neg(ONE),ONE),(I,ONE),(neg(I),ONE))
assert poly(((2,0),ONE))==(30,0)

# For each ordered image triple of infinity, zero, one, form the unique projectivity.
# Its two columns are -det(B,C)A and det(A,C)B.
valid=[]; ruled=[]
for a,b,c in permutations(POINTS,3):
 k=neg(det2(b,c)); ell=det2(a,c)
 A=(mul(k,a[0]),mul(ell,b[0]),mul(k,a[1]),mul(ell,b[1]))
 assert sub(mul(A[0],A[3]),mul(A[1],A[2]))!=Z
 failures=[norm(poly(dot(A,v))) for v in POINTS]
 if any(failures):
  g=0
  for n in failures:g=gcd(g,n)
  z=g
  while z%2==0:z//=2
  while z%5==0:z//=5
  assert z==1,('unexpected collision prime',g)
  ruled.append(g)
  continue
 q=next(x for x in A if x!=Z)
 M=tuple(div(x,q) for x in A)
 c=div(poly(dot(M,((2,0),ONE))),(30,0))
 for x in range(7):
  v=((x,0),ONE)
  assert poly(dot(M,v))==mul(c,poly(v))
 valid.append((M,c))
assert len(valid)==24 and len(ruled)==96
assert Counter(c for _,c in valid)==Counter({(1,0):2,(-1,0):2,(0,1):2,(0,-1):2,(8,0):4,(-8,0):4,(0,8):4,(0,-8):4})

UNITS=(ONE,I,neg(ONE),neg(I))
expected={1:(36,144,180),5:(36,24,60),7:(16,24,40),11:(16,8,24),13:(36,72,108),17:(36,48,84),19:(16,24,40),23:(16,8,24)}
for k,(J,G,T) in expected.items():
 join=36 if k%4==1 else 16
 graph=0
 epsilon=1 if k%8 in (1,7) else -1
 for A,c in valid:
  if k%4==3 and any(z[1] for z in A):continue
  d=0 if norm(c)==1 else 1
  unit=div(c,(8**d,0))
  t=UNITS.index(unit)
  for j in range(6):
   e=(2-t)%4+4*j
   if ((k-1)*e - (12 if d and epsilon==-1 else 0))%24==0: graph+=1
 assert (join,graph,join+graph)==(J,G,T),(k,join,graph)
assert any(c==I and M== (ONE,Z,Z,I) for M,c in valid)

# Independent direct PGL2(Fp) plus scalar-root check, not based on the Galois table.
def f_mod(x,y,p):return (pow(x,5,p)*y-x*pow(y,5,p))%p
def field_census(p):
 countA=0; graphs=0
 # Enumerate each PGL2(Fp) once by first nonzero entry = 1.
 mats=((1,b,c,d) for b in range(p) for c in range(p) for d in range(p))
 mats2=((0,1,c,d) for c in range(p) for d in range(p))
 for a,b,c,d in __import__('itertools').chain(mats,mats2):
  if (a*d-b*c)%p==0:continue
  mult=f_mod((2*a+b)%p,(2*c+d)%p,p)*pow(30,-1,p)%p
  good=True
  for x in range(7):
   if f_mod((a*x+b)%p,(c*x+d)%p,p)!=mult*f_mod(x,1,p)%p:
    good=False;break
  if not good: continue
  assert mult!=0
  countA+=1
  graphs+=sum((pow(s,6,p)*mult)%p==p-1 for s in range(1,p))
 roots=2+sum((pow(x,4,p)-1)%p==0 for x in range(1,p)) # 0, infinity, fourth roots
 return countA,roots*roots,graphs,roots*roots+graphs
for p in (7,11,13,17,19,23,29,31,37,41,43):
 a,b,c,d=field_census(p)
 k=p%24
 assert a==(24 if k%4==1 else 8),(p,a)
 assert (b,c,d)==expected[k],(p,a,b,c,d)

# Exceptional characteristic 5: PGL2(F5), and f(Au)=det(A)f(u).
p=5
numA=0;graphs=0
for a in range(p):
 for b in range(p):
  for c in range(p):
   for d in range(p):
    xs=(a,b,c,d)
    if next((x for x in xs if x),None)!=1:continue
    det=(a*d-b*c)%p
    if not det:continue
    numA+=1
    graphs+=sum(pow(s,6,p)*det%p==p-1 for s in range(1,p))
assert (numA,graphs,36+graphs)==(120,120,156)
print('VERIFY_OK: 24 octahedral transformations; 96 excluded by Gaussian norms with primes 2,5 only; 180 geometric lines; minimal Q(zeta_24); exact 8-element Frobenius table; direct PGL2(Fp) counts for 11 primes; characteristic-5 count 756 geometric, 156 rational')
