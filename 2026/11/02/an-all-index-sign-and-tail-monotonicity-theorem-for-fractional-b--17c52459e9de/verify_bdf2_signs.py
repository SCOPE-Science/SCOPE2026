"""Exact symbolic and rational verification of fractional BDF2 weight identities.

Run: python verify_bdf2_signs.py
Requires sympy. The inductive argument is documented in RESULT.md.
"""
from fractions import Fraction
import sympy as s

alpha,z=s.symbols('alpha z',real=True)
f=(1-s.Rational(4,3)*z+z**2/3)**alpha
q4=64*alpha**2-176*alpha+123
q5=64*alpha**2-208*alpha+183
q6=512*alpha**3-3264*alpha**2+7144*alpha-5475
forms={
 1:-4*alpha/3,
 2:alpha*(8*alpha-5)/9,
 3:-4*alpha*(alpha-1)*(8*alpha-7)/81,
 4:alpha*(alpha-1)*q4/486,
 5:-2*alpha*(alpha-2)*(alpha-1)*q5/3645,
 6:alpha*(alpha-2)*(alpha-1)*q6/65610,
}
checks=0
for n,v in forms.items():
 assert s.simplify(s.diff(f,z,n).subs(z,0)/s.factorial(n)-v)==0
 checks+=1
assert s.factor(q6+27*q5-(-512*(1-alpha)**3+8*(1-alpha)-30))==0
checks+=1
assert s.expand(q4-(64*(alpha-s.Rational(11,8))**2+2))==0
assert s.expand(q5-(64*(alpha-s.Rational(13,8))**2+14))==0
checks+=2
p=15*q4-4*(2-alpha)*q5
assert s.expand(p-(9+244*(1-alpha)+384*(1-alpha)**2-256*(1-alpha)**3))==0
checks+=1
for a in [Fraction(1,101),Fraction(1,2),Fraction(5,8),Fraction(7,10),Fraction(7,8),Fraction(9,10),Fraction(99,100)]:
 c=[Fraction(1),-Fraction(4,3)*a]
 for n in range(1,301):
  c.append((4*(n-a)*c[n]+(2*a-n+1)*c[n-1])/(3*(n+1)))
 for n in range(1,302):
  predicted= (-1 if n==1 else (0 if a==Fraction(5,8) else (-1 if a<Fraction(5,8) else 1)) if n==2 else (0 if a==Fraction(7,8) else (-1 if a<Fraction(7,8) else 1)) if n==3 else -1)
  observed= (c[n]>0)-(c[n]<0)
  assert observed==predicted,(a,n,observed,predicted)
  checks+=1
 for n in range(5,302):
  assert c[n]<0 and c[n-1]<0 and c[n]>c[n-1]
  checks+=1
 for n in range(6,301):
  assert c[n]<0 and c[n-1]<0 and 4*c[n]<=3*c[n-1]
  checks+=1
print('PASS:',checks,'symbolic/exact-rational identity, sign and ratio assertions')
