#!/usr/bin/env python3
from fractions import Fraction
from decimal import Decimal, getcontext

getcontext().prec = 80

def critical(d):
    lam = Fraction(d**d, (d-1)**(d+1))
    r = Fraction(1, d-1)
    assert lam == r * (1+r)**d
    assert Fraction(d) * r / (1+r) == 1
    p = lam / (1+lam)
    assert p == Fraction(d**d, d**d + (d-1)**(d+1))
    return lam, p

def iterate(d, lam, n=3000):
    r = Decimal(0)
    for j in range(n):
        r = lam / (Decimal(1)+r)**d
    return r

for d in range(2, 21):
    critical(d)

separations=[]
for d in range(2, 8):
    lc,_ = critical(d)
    lam = (Decimal(lc.numerator)/Decimal(lc.denominator))*Decimal('1.5')
    even = iterate(d, lam, 3000)
    odd = lam/(Decimal(1)+even)**d
    assert abs(odd-even) > Decimal('1e-20')
    q=d+1
    def P(r):
        return r**q / ((Decimal(1)+r)**q + lam)
    assert P(odd) != P(even)
    separations.append(abs(P(odd)-P(even)))

assert critical(2)[1] == Fraction(4,5)
print('VERIFY_OK exact_orders=2..20 parity_cases=6 min_local_gap=%s' % min(separations))
