#!/usr/bin/env python3
from fractions import Fraction as F


def q(a,b,k):
    return k*a/(k*a+b-1)

def mu(a,b):
    return a/(a+b)

def var(a,b):
    return a*b/((a+b)**2*(a+b+1))

for d1 in range(1, 21):
    a = F(d1,2)
    for d2 in range(3, 21):
        b = F(d2,2)
        for k in (F(11,10), F(3,2), F(2,1), F(5,1)):
            qq = q(a,b,k)
            dd = qq-mu(a,b)
            claimed = a*((k-1)*b+1)/((a+b)*(k*a+b-1))
            assert dd == claimed
            assert dd > 0
            assert qq > q(a,b,F(1,1))
            ratio = dd*dd/var(a,b)
            lb1 = (k-1)**2*a*b*(a+b)/(k*a+b)**2
            lb2 = (k-1)**2/(k*k)*a*b/(a+b)
            lb3 = (k-1)**2/(2*k*k)*min(a,b)
            assert ratio >= lb1 >= lb2 >= lb3 > 0

# Exact boundary-threshold identities used in the two one-parameter limits.
for d1 in range(1, 9):
    a = F(d1,2)
    k = F(3,2)
    for n in (10, 100, 1000):
        b = F(n,2)
        # b*q -> k*a; the displayed difference is exact and tends to zero.
        assert b*q(a,b,k) - k*a == k*a*(1-k*a)/(k*a+b-1)
for d2 in range(3, 10):
    b = F(d2,2)
    k = F(3,2)
    for n in (10, 100, 1000):
        a = F(n,2)
        # a*(1-q) -> (b-1)/k; this is direct from q's definition.
        lhs = a*(1-q(a,b,k))
        rhs = a*(b-1)/(k*a+b-1)
        assert lhs == rhs

print('VERIFY_OK')
