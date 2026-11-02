#!/usr/bin/env python3
"""Independent finite checks for ternary triangle-spectrum and exact depth-four witnesses."""
from itertools import product,combinations

def mdist(x,y):return sum(a!=b for a,b in zip(x,y))
def triangle(a,b,c,k):return max(a,b,c)<=k and a<=b+c and b<=a+c and c<=a+b

def make_triangle(a,b,c,k):
 s=a+b+c
 t=(s%2 if s<=2*k else s-2*k)
 u=(b+c-a-t)//2 # x=y != z
 v=(a+c-b-t)//2 # x=z != y
 w=(a+b-c-t)//2 # y=z != x
 h=k-t-u-v-w
 assert min(t,u,v,w,h)>=0
 x=(0,)*k
 y=(1,)*t+(0,)*u+(1,)*v+(1,)*w+(0,)*h
 z=(2,)*t+(1,)*u+(0,)*v+(1,)*w+(0,)*h
 # fix coordinate pattern: v: x=z neq y -> y=1,z=0; w: y=z neq x -> y=1,z=1
 assert len(y)==len(z)==k
 assert (mdist(x,y),mdist(x,z),mdist(y,z))==(a,b,c)
 return x,y,z

def map_johnson(x):return frozenset(3*i+s for i,s in enumerate(x))
def jdist(x,y):return len(x)-len(x&y)

def gf2rank(vectors):
 p={}
 for v in vectors:
  while v:
   j=v.bit_length()
   if j in p:v^=p[j]
   else:p[j]=v;break
 return len(p)

def map_grass(x):
 return tuple(((1<<(2*i)) if s==0 else (1<<(2*i+1)) if s==1 else ((1<<(2*i))|(1<<(2*i+1)))) for i,s in enumerate(x))
def gdist(x,y):return gf2rank(x+y)-len(x)

for k in range(1,8):
 count=0
 for a,b,c in product(range(k+1),repeat=3):
  if not triangle(a,b,c,k):continue
  x,y,z=make_triangle(a,b,c,k)
  xs=[map_johnson(v) for v in (x,y,z)]
  ys=[map_grass(v) for v in (x,y,z)]
  assert (jdist(xs[0],xs[1]),jdist(xs[0],xs[2]),jdist(xs[1],xs[2]))==(a,b,c)
  assert (gdist(ys[0],ys[1]),gdist(ys[0],ys[2]),gdist(ys[1],ys[2]))==(a,b,c)
  count+=1
 print('TRIANGLE_CONSTRUCTION_OK',k,count)

# Direct enumeration, independently from the constructive routine.
for k in [2,3]:
 h=list(product(range(3),repeat=k));j=list(combinations(range(3*k),k))
 def spectrum(objects,d):
  D=[[d(x,y) for y in objects] for x in objects]
  return {(D[i][j],D[i][l],D[j][l]) for i in range(len(objects)) for j in range(len(objects)) for l in range(len(objects))}
 sh=spectrum(h,mdist);sj=spectrum(j,lambda x,y:k-len(set(x)&set(y)))
 th={(a,b,c) for a,b,c in product(range(k+1),repeat=3) if triangle(a,b,c,k)}
 assert sh==sj==th
 print('INDEPENDENT_HAMMING_JOHNSON_TRIANGLE_SUPPORT_OK',k,len(th))

# Explicit induced diamond in Johnson k-sets and binary Grassmann k-subspaces.
for k in range(2,8):
 B=set(range(4,k+2)) # k-2 base points independent of labels 0,1,2,3
 # x={0,1}, y={0,2}, u={0,3}, v={1,2}
 X=[B|{0,1},B|{0,2},B|{0,3},B|{1,2}]
 ds=[jdist(a,b) for i,a in enumerate(X) for b in X[i+1:]]
 assert ds == [1,1,1,1,1,2]
 # Grassmann basis: B spans coordinates 4...k+1; e0,e1,e2,e3 in fresh complement
 base=[1<<i for i in range(4,k+2)]
 G=[tuple(base+[1<<i,1<<j]) for i,j in [(0,1),(0,2),(0,3),(1,2)]]
 dg=[gdist(a,b) for i,a in enumerate(G) for b in G[i+1:]]
 assert dg==[1,1,1,1,1,2]
 print('DIAMOND_WITNESS_OK',k,'Johnson','Grassmann')
print('VERIFY_OK')
