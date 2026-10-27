"""Exact integer/rational check of the tetrahedral torus fourth moment."""
from itertools import combinations
from collections import defaultdict
from fractions import Fraction
from math import isclose
E=list(combinations(range(4),2))
assert len(E)==6
D=defaultdict(list)
for i,e in enumerate(E):
 for j,f in enumerate(E[i:],i):
  v=tuple(int(k in e)+int(k in f) for k in range(4))
  D[v].append((i,j))
collisions=[v for v,p in D.items() if len(p)>1]
assert collisions==[(1,1,1,1)],collisions
assert len(D[(1,1,1,1)])==3
# All-six unit coefficients: direct fourth Fourier coefficient square sum.
a=[1]*6
v=defaultdict(int)
for i,e in enumerate(E):
 for j,f in enumerate(E):
  key=tuple(int(k in e)+int(k in f) for k in range(4))
  v[key]+=a[i]*a[j]
assert sum(c*c for c in v.values())==90
assert Fraction(sum(c*c for c in v.values()),6**2)==Fraction(5,2)
# Basis single edge: sharp ratio 1; random rational coefficients test the exact identity.
import random
rng=random.Random(719)
for trial in range(500):
 a=[rng.randrange(-3,4) for _ in E]
 s=sum(t*t for t in a)
 if not s:continue
 v=defaultdict(int)
 for i,e in enumerate(E):
  for j,f in enumerate(E):
   key=tuple(int(k in e)+int(k in f) for k in range(4))
   v[key]+=a[i]*a[j]
 u=a[0]*a[5];w=a[1]*a[4];q=a[2]*a[3]
 value=2*s*s-sum(t**4 for t in a)+8*(u*w+u*q+w*q)
 assert sum(z*z for z in v.values())==value
 assert 2*value<=5*s*s
print('PASS: 500 random exact integer tests, collision structure, and equality witness')
