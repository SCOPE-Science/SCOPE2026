"""Exact finite checks of the first vertex Minkowski average of a cross-polytope.
The dimension-independent theorem uses a separate analytic proof.
"""
from fractions import Fraction as F
from itertools import combinations,product
from math import comb

def sites(d):
 s={tuple([0]*d)}
 for i in range(d):
  for a in (-2,2):
   v=[0]*d;v[i]=a;s.add(tuple(v))
 for i,j in combinations(range(d),2):
  for a,b in product((-1,1),repeat=2):
   v=[0]*d;v[i]=a;v[j]=b;s.add(tuple(v))
 return s

def min_dist_sq(y,S):
 return min(sum((a-b)**2 for a,b in zip(y,z)) for z in S)

def integer_compositions_leq(d,budget):
 def rec(i,rem,prefix):
  if i==d:
   yield tuple(prefix);return
  for v in range(rem+1):
   yield from rec(i+1,rem-v,prefix+[v])
 yield from rec(0,budget,[])

for d,denom in [(2,8),(3,6),(4,4),(5,4),(6,2),(7,2),(8,2)]:
 S=sites(d); checked=0; equality=[]
 for t in integer_compositions_leq(d,2*denom):
  y=tuple(F(v,denom) for v in t)
  q=min_dist_sq(y,S)
  assert q<=1, (d,y,q)
  if q==1:equality.append(t)
  checked+=1
 expected=set()
 for i in range(d):
  v=[0]*d;v[i]=denom;expected.add(tuple(v))
 if denom%2==0:
  for idx in combinations(range(d),4):
   v=[0]*d
   for i in idx:v[i]=denom//2
   expected.add(tuple(v))
 assert set(equality)==expected,(d,denom,equality,expected)
 print('dimension',d,'denominator',denom,'samples',checked,'sharp_points',len(equality))
print('ALL FINITE TESTS PASS')
