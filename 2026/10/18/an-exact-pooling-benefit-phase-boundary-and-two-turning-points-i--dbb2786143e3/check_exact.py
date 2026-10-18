"""Reproducible exact checks for beta-correlated two-stage screening costs."""
from fractions import Fraction as F
from math import comb

def rf(x,n):
    z=F(1)
    for j in range(n): z*=x+j
    return z

def q(a,b,k): return rf(b,k)/rf(a+b,k)
def cost(a,b,k): return F(1) if k==1 else 1+F(1,k)-q(a,b,k)
def f(a,b,k): return k*q(a,b,k)
def h(a,b,k): return a*k*(k+1)*q(a,b,k)/(a+b+k)

def pmf(a,b,k,j):
    return comb(k,j)*rf(a,j)*rf(b,k-j)/rf(a+b,k)

checks=0
for a2 in range(1,12):
 for b2 in range(1,12):
  a,b=F(a2,2),F(b2,2)
  for k in range(2,26):
   p=[pmf(a,b,k,j) for j in range(k+1)]
   assert sum(p)==1
   assert p[0]==q(a,b,k)
   assert cost(a,b,k)==(1+k*(1-p[0]))/k
   assert cost(a,b,k+1)-cost(a,b,k)==(h(a,b,k)-1)/F(k*(k+1))
   assert f(a,b,k+1)/f(a,b,k)== F(k+1,k)*F(b+k,a+b+k)
   assert h(a,b,k+1)/h(a,b,k)== F(k+2,k)*F(b+k,a+b+k+1)
   checks+=5

a,b=F(3,2),F(5,2)
assert h(a,b,4)==F(495,512) and h(a,b,5)==F(2145,2048)
assert h(a,b,28)==F(145207923735888321,144115188075855872)
assert h(a,b,29)==F(575174243369427765,576460752303423488)
assert cost(a,b,5)==F(10143,10240)
assert all(cost(a,b,k)>cost(a,b,5) for k in range(2,5))
assert all(cost(a,b,k)>cost(a,b,5) for k in range(6,1001))
print('PASS: exact beta-binomial sum and first difference/ratio identities; checks:',checks)
print('PASS: two-turn witness a=3/2,b=5/2: min cost k=5 =',cost(a,b,5),'min boundary H4 H5',h(a,b,4),h(a,b,5))
print('PASS: later local max k=29; boundary H28 H29',h(a,b,28),h(a,b,29))
print('NOTE: finite checks only; global classification relies on algebraic ratio proof.')
