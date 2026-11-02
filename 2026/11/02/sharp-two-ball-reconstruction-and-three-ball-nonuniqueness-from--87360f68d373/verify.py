from fractions import Fraction as F
from math import sqrt, pi, gamma
from random import Random

def p(z):return max(z,F(0))

def support(balls,t): return max(r+c*t for c,r in balls)

A=[(F(0),F(2,5)),(F(1),F(3,10)),(F(2),F(1,10))]
B=[(-F(1),F(1,5)),(F(0),F(2,5)),(F(1),F(3,10))]
for k in range(-1000,1001):
 t=F(k,1000)
 ha=F(2,5)+p(t-F(1,10))+p(t-F(1,5))
 hb=F(2,5)+p(t-F(1,10))+p(-t-F(1,5))
 assert ha==support(A,t),(t,ha,support(A,t))
 assert hb==support(B,t),(t,hb,support(B,t))
 wa=support(A,t)+support(A,-t)
 wb=support(B,t)+support(B,-t)
 expected=F(4,5)+p(abs(t)-F(1,10))+p(abs(t)-F(1,5))
 assert wa==wb==expected
assert sum([F(1,10),F(1,10),F(4,5)])==1
assert len({r for _,r in A})==3 and set(r for _,r in A)!=set(r for _,r in B)
for balls in (A,B):
 assert all(abs(balls[i][0]-balls[j][0])>balls[i][1]+balls[j][1] for i in range(3) for j in range(i+1,3))

# Check two-active-ball inversion for a rational grid, with dimension three F_3(t)=t.
for Ri in range(3,11):
 for ri in range(1,Ri+1):
  for li in range(Ri-ri+1,Ri+ri+8):
   R,r,L=F(Ri,3),F(ri,3),F(li,3)
   de=R-r
   if not L>de:continue
   q=de/L; m=2*R; M=R+r+L
   LL=(M-m)/(1-q)
   rr=m/F(2)-q*LL
   assert LL==L and rr==r

# Dim3 empirical distribution: alpha portion at min, density 1 and 1/2 over adjacent ranges.
rng=Random(20261026)
samples=120000
counts=[0,0,0]
for _ in range(samples):
 t=rng.random()
 w=F(4,5)+p(F.from_float(t)-F(1,10))+p(F.from_float(t)-F(1,5))
 j=(0 if w==F(4,5) else (1 if w<F(9,10) else 2))
 counts[j]+=1
for got,desired in zip(counts,[.1,.1,.8]):assert abs(got/samples-desired)<.007,(got,desired)
print('EXACT_DIRECTIONWISE_THREE_BALL_IDENTITY_PASSED')
print('PAIRWISE_DISJOINT_EXPOSED_RADIUS_MULTISETS_PASSED')
print('EXACT_TWO_BALL_INVERSION_PASSED')
print('THREE_DIMENSIONAL_ATOM_AND_TWO_DENSITY_REGIMES_PASSED')
print('ALL_CHECKS_PASSED')
