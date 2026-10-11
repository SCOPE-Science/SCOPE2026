#!/usr/bin/env python3
from fractions import Fraction
from decimal import Decimal, getcontext
from math import gcd
from functools import reduce

# Polynomials are ascending coefficient lists in s with Fraction coefficients.
def add(p, q):
    n=max(len(p),len(q)); out=[Fraction(0) for _ in range(n)]
    for i,c in enumerate(p): out[i]+=c
    for i,c in enumerate(q): out[i]+=c
    while len(out)>1 and out[-1]==0: out.pop()
    return out

def mul(p, q):
    out=[Fraction(0) for _ in range(len(p)+len(q)-1)]
    for i,a in enumerate(p):
        for j,b in enumerate(q): out[i+j]+=a*b
    while len(out)>1 and out[-1]==0: out.pop()
    return out

def scale(p,c): return [c*x for x in p]

def pval_int(coeff_desc, x):
    y=Decimal(0)
    for c in coeff_desc: y=y*x+Decimal(c)
    return y

a=Fraction(109,20)
S=[Fraction(0),Fraction(1)]
AplusS=[a,Fraction(1)]
# numerator of A2: a^3+a^2*s+a^2+2*a*s^2+a*s+s^3
numA2=[a**3+a**2, a**2+a, 2*a, Fraction(1)]
# numerator of H=(a+2)A2-A3 over a(a+s):
# Hnum=(a+2)*numA2 - 2*a*s*((a+s)^2-a)
term=mul(S, add(mul(AplusS,AplusS), [ -a ]))
Hnum=add(scale(numA2,a+2), scale(term,-2*a))
# clear denominators and primitive-normalize
L=1
for c in Hnum:
    L=L*c.denominator//gcd(L,c.denominator)
ints=[int(c*L) for c in Hnum]
g=reduce(gcd,[abs(x) for x in ints if x])
ints=[x//g for x in ints]
# H numerator should be positive constant then negative coefficients.
assert ints == [228364701, -394580, -6016800, -552000], ints

# R(s)=-primitive(Hnum), descending coefficients.
R=[552000,6016800,394580,-228364701]
# R'(s)>0 for s>=0 because every coefficient is positive.
assert all(c>0 for c in [3*R[0],2*R[1],R[2]])
assert R[-1] < 0

getcontext().prec=70
lo=Decimal('5.0677311499000689')
hi=Decimal('5.0677311499000691')
assert pval_int(R,lo)<0<pval_int(R,hi)
for _ in range(220):
    mid=(lo+hi)/2
    if pval_int(R,mid)<0: lo=mid
    else: hi=mid
s=(lo+hi)/2
A=Decimal(109)/Decimal(20)
b=s+A/(A+s)
# A2=(a^3+a^2*s+a^2+2*a*s^2+a*s+s^3)/(a*(a+s))
A2=(A**3+A**2*s+A**2+Decimal(2)*A*s**2+A*s+s**3)/(A*(A+s))
freq=A2.sqrt()
assert abs(s-Decimal('5.06773114990006899770030398847109644')) < Decimal('1e-34')
assert abs(b-Decimal('5.58590374076837442176219399692937207')) < Decimal('1e-34')
assert abs(freq-Decimal('3.68836641582839074732836104161314200')) < Decimal('1e-34')
print('VERIFY_OK')
print('s_H='+str(s))
print('b_H='+str(b))
print('omega_H='+str(freq))
