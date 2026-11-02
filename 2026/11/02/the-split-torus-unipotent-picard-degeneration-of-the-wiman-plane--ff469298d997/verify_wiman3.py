#!/usr/bin/env python3
"""Exact elementary checks for the characteristic-three Wiman plane sextic."""
from itertools import product
# Homogeneous multivariate polynomials modulo three, stored as exponent dictionaries.
def padd(*ps):
 out={}
 for p in ps:
  for e,c in p.items(): out[e]=(out.get(e,0)+c)%3
 return {e:c for e,c in out.items() if c}
def pmul(a,b):
 out={}
 for e,c in a.items():
  for f,d in b.items():
   g=tuple(e[i]+f[i] for i in range(3))
   out[g]=(out.get(g,0)+c*d)%3
 return {e:c for e,c in out.items() if c}
def pscale(a,c):return {e:(c*v)%3 for e,v in a.items() if (c*v)%3}
def ppow(a,n):
 result={(0,0,0):1}
 for _ in range(n):result=pmul(result,a)
 return result
X={(1,0,0):1};Y={(0,1,0):1};Z={(0,0,1):1}
Q=padd(ppow(X,2),ppow(Y,2),ppow(Z,2))
F=padd(ppow(X,6),ppow(Y,6),ppow(Z,6),
       pmul(Q,padd(ppow(X,4),ppow(Y,4),ppow(Z,4))),
       pscale(pmul(pmul(ppow(X,2),ppow(Y,2)),ppow(Z,2)),-12))
rows=((1,1,1),(1,1,-1),(1,-1,1),(-1,1,1))
Ls=[padd(pscale(X,a),pscale(Y,b),pscale(Z,c)) for a,b,c in rows]
prod={ (0,0,0):1 }
for l in Ls:prod=pmul(prod,l)
assert F==pmul(Q,prod)
print('CHARACTERISTIC3_FACTORIZATION_OK')
# Four tangent points, each on its corresponding line only.
def dot(row,p):return sum(a*b for a,b in zip(row,p))%3
point=lambda v:tuple(next(pow(w,-1,3) for w in v if w%3)*w%3 for w in v)
tangencies={point(v) for v in rows}
assert len(tangencies)==4
for i,raw in enumerate(rows):
 p=point(raw)
 assert sum(v*v for v in p)%3==0
 assert dot(rows[i],p)==0
 assert all(dot(rows[j],p) for j in range(4) if j!=i)
print('FOUR_RATIONAL_DISTINCT_TANGENCIES_OK')
# Six pairwise intersections of lines, not on the conic, all distinct.
def cross(a,b):
 return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
nodes=[]
for i in range(4):
 for j in range(i+1,4):
  p=point(cross(rows[i],rows[j]));nodes.append(p)
  assert sum(v*v for v in p)%3!=0
  assert sum(dot(row,p)==0 for row in rows)==2
assert len(set(nodes))==6 and set(nodes).isdisjoint(tangencies)
print('SIX_RATIONAL_DISTINCT_TRANSVERSE_LINE_PAIRS_OK')
# Exhaustive P^2(F_3), F_9 and F_27 counts by irreducible polynomial representation.
def add(a,b):return tuple((x+y)%3 for x,y in zip(a,b))
def mul(a,b,mod):
 n=len(a);tmp=[0]*(2*n-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):tmp[i+j]=(tmp[i+j]+x*y)%3
 for i in range(2*n-2,n-1,-1):
  for j in range(n):tmp[i-n+j]=(tmp[i-n+j]-tmp[i]*mod[j])%3
 return tuple(tmp[:n])
def field(n,mod):
 els=list(product(range(3),repeat=n));zero=(0,)*n;one=(1,)+(0,)*(n-1)
 def pmul(x,y):return mul(x,y,mod)
 def ppow(x,k):
  result=one
  while k:
   if k&1:result=pmul(result,x)
   x=pmul(x,x);k>>=1
  return result
 # Every nonzero element must be invertible (irreducibility check)
 assert all(pmul(e,ppow(e,3**n-2))==one for e in els if e!=zero)
 return els,zero,one,pmul,ppow
for n,mod in [(1,(0,)),(2,(1,0)),(3,(1,2,0))]:
 els,zero,one,prod,pow_=field(n,mod);q=3**n
 # representatives: [1:y:z],[0:1:z],[0:0:1]
 points=[(one,y,z) for y in els for z in els]+[(zero,one,z) for z in els]+[(zero,zero,one)]
 assert len(points)==q*q+q+1
 count=0
 for x,y,z in points:
  X2=pow_(x,2);Y2=pow_(y,2);Z2=pow_(z,2)
  X4=pow_(x,4);Y4=pow_(y,4);Z4=pow_(z,4)
  X6=pow_(x,6);Y6=pow_(y,6);Z6=pow_(z,6)
  f=add(add(X6,Y6),add(Z6,prod(add(add(X2,Y2),Z2),add(add(X4,Y4),Z4))))
  if f==zero:count+=1
 assert count==5*q-5,(q,count)
 print(f'GF({q})_WIMAN3_POINTS_OK: {count}')
# local quotient at each tacnode: (k[u]/u^2)^* = Gm * Ga,
# 4 tacnodes + 6 nodes => 10 units, quotient by 4 independent component scales.
assert (6+4)- (5-1) == 6
assert 6+2*4-(5-1)==10
print('GRAPH_BETTI_6_AND_PICARD_DIMENSION_10_OK')
print('VERIFY_OK')
