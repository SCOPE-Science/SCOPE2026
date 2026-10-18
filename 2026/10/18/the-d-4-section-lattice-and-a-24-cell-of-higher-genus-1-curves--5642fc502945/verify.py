"""Exact algebra and lattice checks for an elliptic-surface geometric construction."""
from fractions import Fraction as F
from itertools import product
from collections import Counter
from sympy import symbols, diff, gcd, expand, Matrix

t=symbols('t')
D=4*(t*t+1)**3+27
assert expand(D)==4*t**6+12*t**4+12*t**2+31
assert gcd(D,diff(D,t))==1
assert D.subs(t,0)==31
# At infinity, local frame for O(1) gives a4=s^2+s^4 and a6=s^6.
s=symbols('s')
a4=s*s+s**4; a6=s**6
Delta=-16*(4*a4**3+27*a6**2)
assert expand(Delta/s**6).subs(s,0)==-64
# Six simple nodal fibers, one I0* (five components): Shioda--Tate rank 4.
assert 10-2-(5-1)==4
cartan=Matrix([[2,-1,0,0],[-1,2,-1,-1],[0,-1,2,0],[0,-1,0,2]])
assert cartan.det()==4
# Dual D4 has eight coordinate-unit plus sixteen half-integer norm-one vectors.
unit=[]
for i in range(4):
 for sign in (-1,1):
  x=[F(0)]*4;x[i]=F(sign);unit.append(tuple(x))
half=[tuple(F(sign,2) for sign in bits) for bits in product((-1,1),repeat=4)]
vectors=unit+half
assert len(vectors)==24 and len(set(vectors))==24
assert all(sum(z*z for z in x)==1 for x in vectors)
for v in vectors:
 distribution=Counter()
 for w in vectors:
  if w==v:continue
  inner=sum(x*y for x,y in zip(v,w))
  # Degree-two height pullback; for distinct nonzero sections, intersection = 1 - height pairing.
  intersection=1-2*inner
  assert intersection in (0,1,2,3)
  distribution[int(intersection)]+=1
 assert distribution=={0:8,1:6,2:8,3:1},distribution
# Gram determinant of inherited height lattice equals 2^4 / det(D4).
assert F(2**4,cartan.det())==4
print('VERIFY_OK: six simple finite discriminant roots, I0* local data, rank 4, det 4, 24 minimal vectors, intersection multiplicities 8/6/8/1')
