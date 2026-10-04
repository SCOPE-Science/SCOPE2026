from fractions import Fraction
from itertools import product
from math import pi

P=(2,3,5,7,11,13)
E=5

def divisors(a):
    return [d for d in range(1,a+1) if a%d==0]

def rho(p,a):
    if a==0:
        return Fraction(1,1)
    return Fraction(1+p**a, sum(p**d for d in divisors(a)))

def exact_v_prob(p,a):
    return Fraction(p-1,p**(a+1))

good=[]
weight=Fraction(0,1)
for exps in product(range(E+1), repeat=len(P)):
    R=Fraction(1,1)
    w=Fraction(1,1)
    for p,a in zip(P,exps):
        R *= rho(p,a)
        w *= exact_v_prob(p,a)
    if R >= 1:
        good.append((exps,R))
        weight += w

small_sqfree=Fraction(1,1)
for p in P:
    small_sqfree *= Fraction(p*p-1,p*p)
coeff = Fraction(6,1)*weight/small_sqfree
expected = Fraction(6097572635664749695003,819750822146736480000)
assert coeff == expected
assert len(good)==17230
eq=[e for e,R in good if R==1]
assert eq == [(0,0,0,0,0,0),(0,2,1,0,0,0),(0,3,1,2,0,0),(2,0,1,0,0,0),(3,1,2,2,0,1)]
assert rho(2,1)==Fraction(3,2)
assert rho(2,2)==Fraction(5,6)
assert rho(3,1)==Fraction(4,3)
assert rho(5,1)==Fraction(6,5)
print('VERIFY_OK')
print('patterns_total=46656 good_patterns=17230 equality_patterns=5')
print(f'coefficient={coeff.numerator}/{coeff.denominator}')
print(f'lower_bound={float(coeff)/(pi*pi):.15f}')
print(f'squarefree_baseline={6/(pi*pi):.15f}')
