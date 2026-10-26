#!/usr/bin/env python3
"""Pure-Python Buchberger check of geometric singular support in the chart s=x+y+z=1.
Polynomial arithmetic is in F_11[x,y] with lexicographic term order x>y.
"""
from math import factorial
P=11

def mod(p):return {e:c%P for e,c in p.items() if c%P}
def plus(f,g,a=1):
 h=f.copy()
 for e,c in g.items():h[e]=(h.get(e,0)+a*c)%P
 return mod(h)
def monmul(f,e,c):
 return mod({(i+e[0],j+e[1]):v*c for (i,j),v in f.items()})
def lt(f):return max(f)
def mul(f,g):
 h={}
 for (a,b),c in f.items():h=plus(h,monmul(g,(a,b),c))
 return h
def reduce_poly(f,G):
 r={};f=f.copy()
 while f:
  e=lt(f);coef=f[e];match=False
  for g in G:
   E=lt(g)
   if e[0]>=E[0] and e[1]>=E[1]:
    f=plus(f,monmul(g,(e[0]-E[0],e[1]-E[1]), -coef*pow(g[E],-1,P)))
    match=True;break
  if not match:
   r[e]=coef;del f[e]
 return r
def S(f,g):
 a,b=lt(f),lt(g);L=(max(a[0],b[0]),max(a[1],b[1]))
 u=monmul(f,(L[0]-a[0],L[1]-a[1]),pow(f[a],-1,P))
 v=monmul(g,(L[0]-b[0],L[1]-b[1]),pow(g[b],-1,P))
 return plus(u,v,-1)
def binom(n,k):return factorial(n)//(factorial(k)*factorial(n-k))
def fact3(n,a,b,c):return factorial(n)//(factorial(a)*factorial(b)*factorial(c))
# s=1 and derivatives imply x^9=y^9=z^9=3.
# The remaining condition is (1-x-y)^9=3.
gens=[{(9,0):1,(0,0):-3},{(0,9):1,(0,0):-3}]
h={}
for a in range(10):
 for b in range(10-a):
  c=9-a-b
  h[(a,b)]=fact3(9,a,b,c)*(-1)**(a+b)
h=plus(mod(h),{(0,0):-3})
gens.append(h)
G=[mod(f) for f in gens]
pairs=[(i,j) for j in range(1,len(G)) for i in range(j)]
processed=0
while pairs:
 i,j=pairs.pop(0);processed+=1
 h=reduce_poly(S(G[i],G[j]),G)
 if h:
  e=lt(h);h=monmul(h,(0,0),pow(h[e],-1,P))
  # Avoid recomputing a Groebner generator with same polynomial.
  if h not in G:
   for k in range(len(G)):pairs.append((k,len(G)))
   G.append(h)
 assert len(G)<150
# A completed Buchberger basis generates the derivative ideal.
assert not reduce_poly({(1,0):1,(0,0):-4},G)
assert not reduce_poly({(0,1):1,(0,0):-4},G)
# Conversely the original generators vanish at (4,4).
for f in gens:assert sum(c*pow(4,a+b,P) for (a,b),c in f.items())%P==0
print('GEOMETRY_OK','groebner_generators',len(G),'S_pairs',processed,
      'singular_point_in_s_1_chart',(4,4,1-4-4))
