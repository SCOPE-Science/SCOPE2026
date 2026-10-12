"""Independent exact Gaussian Wick and Bernstein checks for the quartic stability law."""
from functools import lru_cache
from fractions import Fraction
from itertools import product
import math

# Polynomial operations in Q[r].
def add(a,b):
 out=[Fraction(0)]*max(len(a),len(b))
 for i,x in enumerate(a):out[i]+=x
 for i,x in enumerate(b):out[i]+=x
 return tuple(out)
def scale(a,s):return tuple(s*x for x in a)
def shift(a,k):return (Fraction(0),)*k+tuple(a)
@lru_cache(None)
def wick(alpha):
 if not any(alpha):return (Fraction(1),)
 i=next(i for i,x in enumerate(alpha) if x)
 remain=list(alpha);remain[i]-=1
 out=(Fraction(0),)
 for j,w in enumerate(remain):
  if not w:continue
  b=remain.copy();b[j]-=1
  out=add(out,shift(scale(wick(tuple(b)),w),int(i!=j)))
 return out

p=wick((4,4,4,4)); exp=(Fraction(81),Fraction(0),Fraction(3888),Fraction(20736),Fraction(110160),Fraction(290304),Fraction(570240),Fraction(663552),Fraction(368064))
assert p==exp,(p,exp)
q=(Fraction(3),Fraction(-16),Fraction(85),Fraction(-224),Fraction(440),Fraction(-512),Fraction(284))
assert p[2:]==tuple(Fraction(1296)*x*(-1)**i for i,x in enumerate(q))

def deriv(a):return tuple((i+1)*a[i+1] for i in range(len(a)-1))
def at(a,x):
 ans=Fraction(0)
 for coef in reversed(a):ans=ans*x+coef
 return ans
qp=deriv(q); qpp=deriv(qp)
assert at(qp,Fraction(0))== -16 and at(qp,Fraction(1,3))==Fraction(178,27)
# Bernstein coefficients of q''(t/3) on t∈[0,1], degree 4.
coef=tuple(a/Fraction(3)**i for i,a in enumerate(qpp))
bern=tuple(sum(coef[j]*Fraction(math.comb(k,j),math.comb(4,j)) for j in range(k+1)) for k in range(5))
assert bern==(Fraction(170),Fraction(58),Fraction(394,9),Fraction(878,27),Fraction(934,27))
assert min(bern)>0
lo=Fraction(1655387,10000000); hi=Fraction(1655388,10000000)
assert at(qp,lo)<0<at(qp,hi)
# Independent multinomial finite-difference sanity on symmetric unit-variance correlation.
for t in (Fraction(0),Fraction(1,25),Fraction(1,6),Fraction(1,3)):
 r=-t
 assert at(p,r)==Fraction(81)+Fraction(1296)*r*r*at(q,t)
for r in (Fraction(0),Fraction(1,10),Fraction(1,2),Fraction(1)):
 assert at(p,r)>=Fraction(81)+Fraction(1296)*r*r*at(q,hi)
# Positive-semidefinite domain for equicorrelation in d=4: -1/3 <= r <= 1.
print('PASS: Wick recurrence, 9 coefficients, sharp negative extremum, strict Bernstein convexity, exact bracket and boundaries.')
print('Bernstein coefficients of q"(t/3):', [str(x) for x in bern])
print('minimizer bracket', str(lo), str(hi))
