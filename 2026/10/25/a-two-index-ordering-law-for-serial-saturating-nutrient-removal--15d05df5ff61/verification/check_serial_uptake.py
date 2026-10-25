"""Reproducible checks for sequential saturating-removal maps.

Uses exact symbolic arithmetic and seeded randomized exhaustive comparisons for
finite sets. Numerical samples are consistency tests, not general proofs.
"""
from fractions import Fraction
from itertools import permutations
import random
import sympy as s

K,L,u,v,c=s.symbols('K L u v c',positive=True)
def T_sym(x,k,a):return x-a*x/(k+x)
P=(K-L)*c**2+((K-L)*(K+L)-K*u+L*v)*c+K*L*(K-L-u+v)
D=(K+c)*(L+c)*((K+c)*(L+c)-u*c)*((K+c)*(L+c)-v*c)
assert s.factor((T_sym(T_sym(c,K,u),L,v)-T_sym(T_sym(c,L,v),K,u))*D+u*v*c*c*P)==0

def T(x,k,a):return x-a*x/(k+x)
def run(x,items):
 for k,a in items:x=T(x,k,a)
 return x

# Exact witness, including the switching boundary.
h=(Fraction(2),Fraction(7,4)); low=(Fraction(1),Fraction(1,3))
assert run(Fraction(1),[h,low])==run(Fraction(1),[low,h])==Fraction(65,204)
assert run(Fraction(1,2),[low,h])<run(Fraction(1,2),[h,low])
assert run(Fraction(2),[h,low])<run(Fraction(2),[low,h])
assert s.expand(P.subs({K:2,L:1,u:s.Rational(7,4),v:s.Rational(1,3)})-(c-1)*(c+s.Rational(5,6)))==0

rng=random.Random(713055)
# Direct polynomial comparison, and at most one switch with exact sign criterion.
for _ in range(10000):
 k=rng.uniform(.1,20);ell=rng.uniform(.1,20)
 uu=k*rng.uniform(.01,.99);vv=ell*rng.uniform(.01,.99)
 x=10**rng.uniform(-5,3)
 d=run(x,[(k,uu),(ell,vv)])-run(x,[(ell,vv),(k,uu)])
 p=(k-ell)*x*x+((k-ell)*(k+ell)-k*uu+ell*vv)*x+k*ell*(k-ell-uu+vv)
 den=(k+x)*(ell+x)*((k+x)*(ell+x)-uu*x)*((k+x)*(ell+x)-vv*x)
 direct=-uu*vv*x*x*p/den
 assert abs(d-direct)<1e-7*max(1.,abs(direct),abs(d))
 if abs(k-ell)>1e-9 and abs((k-uu)-(ell-vv))>1e-9:
  disc=((k-ell)*(k+ell)-k*uu+ell*vv)**2-4*(k-ell)*k*ell*(k-ell-uu+vv)
  if (k-ell)*((k-uu)-(ell-vv))<0:
   assert disc>0
   import math
   roots=sorted([(-((k-ell)*(k+ell)-k*uu+ell*vv)+math.sqrt(disc))/(2*(k-ell)),(-((k-ell)*(k+ell)-k*uu+ell*vv)-math.sqrt(disc))/(2*(k-ell))])
   assert roots[0]<0<roots[1]

# Exact, strictly compared global permutation optima at both concentration extremes.
# Rational arithmetic prevents the underflow that could hide tiny order effects.
checked=0
for _ in range(140):
 n=rng.randrange(2,6)
 ks=rng.sample(range(2,24),n)
 items=[(Fraction(k), Fraction(k*rng.randrange(1,19),20)) for k in ks]
 residual=[k-a for k,a in items]
 if len(set(residual))!=n:continue
 checked+=1
 low_order=sorted(items,key=lambda p:p[0]-p[1],reverse=True)
 high_order=sorted(items,key=lambda p:p[0],reverse=True)
 xlow=Fraction(1,2)
 while True:
  valid=True
  for i in range(n):
   for j in range(i+1,n):
    k,uu=items[i];ell,vv=items[j]
    p=(k-ell)*xlow*xlow+((k-ell)*(k+ell)-k*uu+ell*vv)*xlow+k*ell*(k-ell-uu+vv)
    if p*((k-uu)-(ell-vv))<=0:valid=False
  if valid:break
  xlow/=2
  assert xlow>Fraction(1,10**40)
 xhigh=sum((a for k,a in items), Fraction(0))+max(k for k,a in items)*4
 while True:
  xmin=xhigh-sum((a for k,a in items), Fraction(0))
  valid=True
  for i in range(n):
   for j in range(i+1,n):
    k,uu=items[i];ell,vv=items[j]
    p=(k-ell)*xmin*xmin+((k-ell)*(k+ell)-k*uu+ell*vv)*xmin+k*ell*(k-ell-uu+vv)
    if p*(k-ell)<=0:valid=False
  if valid:break
  xhigh*=2
 for order in permutations(items):
  if order!=tuple(low_order):assert run(xlow,low_order)<run(xlow,order)
  if order!=tuple(high_order):assert run(xhigh,high_order)<run(xhigh,order)

# Equal residual scales: the larger half-saturation constant remains first.
assert run(Fraction(1,10),[(Fraction(2),Fraction(6,5)),(Fraction(1),Fraction(1,5))]) < run(Fraction(1,10),[(Fraction(1),Fraction(1,5)),(Fraction(2),Fraction(6,5))])
print(f'PASS: symbolic commutator, exact crossover, 10,000 pair comparisons, {checked} full rational permutation censuses, equal-index boundary')
