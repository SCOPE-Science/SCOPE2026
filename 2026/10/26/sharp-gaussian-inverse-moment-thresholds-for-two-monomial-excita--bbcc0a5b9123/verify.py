"""Independent algebraic and small-radius checks for two-row monomial designs."""
from fractions import Fraction
from itertools import combinations
from math import cos, sin, pi, sqrt
import random

rng=random.Random(271828)
checks=0
for m in range(2,8):
 for d in range(2,9):
  for trial in range(31):
   g=[Fraction(rng.randint(-6,6),rng.randint(1,7)) for _ in range(m)]
   aa=sum(x*x for x in g)
   bb=sum(x**(2*d) for x in g)
   ab=sum(x**(d+1) for x in g)
   lhs=aa*bb-ab*ab
   rhs=sum((g[i]*g[j]**d-g[j]*g[i]**d)**2 for i,j in combinations(range(m),2))
   assert lhs==rhs and lhs>=0
   checks+=1

def F(theta):
 a,b=cos(theta),sin(theta)
 return abs(a*b*(b-a))
zeros=[0,pi/2,pi,3*pi/2,pi/4,5*pi/4]
slopes=[1,1,1,1,1/sqrt(2),1/sqrt(2)]
for z,s in zip(zeros,slopes):
 for step in [1e-3,1e-4,1e-5]:
  assert abs(F(z+step)/step-s)<1e-2
  checks+=1
assert abs(sum(2/s for s in slopes)/(2*pi)-(4+2*sqrt(2))/pi)<1e-10
print(f'VERIFY_OK {checks} exact Gram-minor identities and 18 angular-root tests; exceptional logarithmic coefficient checked')
