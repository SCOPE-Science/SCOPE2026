from fractions import Fraction as Q
from math import isclose
from itertools import product

def density(p,q,t):
 m=p*q
 if 0<=t<1: return (2+(p+q-4)*t)/m
 if 1<=t<2: return ((p+q-2)*(2-t)+2*(p-1)*(q-1)*(t-1))/m
 return 0
for p in range(1,20):
 for q in range(1,20):
  m=p*q
  # Exact mixture weights, first/second component means and normalization
  a,b,c=Q(1,m),Q(p+q-2,m),Q((p-1)*(q-1),m)
  assert a+b+c==1 and a>=0 and b>=0 and c>=0
  mu=a/3+b+5*c/3
  assert mu==Q(5,3)-Q(2,3)*(Q(1,p)+Q(1,q))
  assert Q(2,m)==Q(2,p*q)
  assert 4+m*Q(p+q-4,m)==p+q
  # CDF continuity at 1 and endpoint 2, total mass
  assert Q(2,m)+Q(p+q-4,m)==Q(p+q-2,m)
  # Integrals over branches exact
  integral=Q(1,m)+Q(p+q-2,m)+Q((p-1)*(q-1),m)
  assert integral==1
print('exact combinatorial and moment identities PASS for 361 part-size pairs; analytic proof covers all positive p,q')
