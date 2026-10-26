"""Reproduce exact base polynomial and independent 2-adic arithmetic checks."""
from math import comb
from fractions import Fraction
import sympy as s
n,r=s.symbols('n r', integer=True)
R=n*(n+1)*(n+2)/6
T=lambda f:s.factor(s.summation((2*n-r+1)*f.subs(n,r),(r,0,2*n)))
p1=2*n+1; p2=T(p1); p3=T(p2); p4=T(p3)
h=s.factor((p4-p2)/(8*R))
assert s.simplify(h-(2*n+1)*(512*n**3+1568*n**2+1596*n+489)/105)==0
assert h.subs(n,0)==s.Rational(489,105)
# Explicit symbolic normalization for the first twelve monomials of Z_(2)[n].
for j in range(13):
 v=s.cancel(T(R*n**j)/(2*R))
 assert s.denom(v).subs(n,0).is_integer
 num,den=s.fraction(v)
 poly=s.Poly(den,n,domain=s.QQ)
 assert poly.degree()==0 and int(poly.eval(0))%2==1,(j,v)
# Bernoulli-coefficient lemma: for all q>=2 (here representative q through 20)
# D_q(2s)/(2s) has 2-integral polynomial coefficients.
z=s.symbols('z')
for q in range(2,21):
 coeffs=[]
 for e in range(1,q+4):
  def bc(q,e):
   return s.binomial(q,e-1)*s.bernoulli(q+1-e) if e<=q+1 else 0
  # sympy Bernoulli uses B_1=+1/2; power-sum formula needs B_1=-1/2.
  def be(t):return -s.Rational(1,2) if t==1 else s.bernoulli(t)
  a=s.binomial(q+2,e-1)*be(q+3-e) if e<=q+3 else 0
  b=s.binomial(q,e-1)*be(q+1-e) if e<=q+1 else 0
  c=s.cancel(s.Rational(2)**e/s.Integer(e)*(a-b))
  assert s.denom(c)%2==1 if e>=2 else s.denom(c)%2==1,(q,e,c)
  # D_q(2z)/2z integral: coefficient of z^(e-1) = c/2
  assert s.denom(c/2)%2==1,(q,e,c)
N=9000
b=[0]*(N+1); S=[0]*(N+1); W=[0]*(N+1)
b[0]=S[0]=1
for i in range(1,N+1):
 j=i//2
 b[i]=(i+1)*S[j]-2*W[j]
 S[i]=S[i-1]+b[i]
 W[i]=W[i-1]+i*b[i]
assert b[:5]==[1,2,5,8,16],b[:5]
def v2(v):return (abs(v)&-abs(v)).bit_length()-1
count=0
for k in range(3,9):
 for a in range(1,N//2**(k+1)+1):
  d=b[(2**(k+1))*a]-b[(2**(k-1))*a]
  assert d and v2(d)==k+v2(a),(k,a,d)
  count+=1
print('PASS: symbolic p4-p2 = 8 R h and h mod 2 = 1')
print('PASS: normalized T action on R n^j, degrees 0..12; Bernoulli lemma degrees 2..20')
print('PASS: independent exact b_2 recurrence and dyadic valuations:',count,'pairs')
