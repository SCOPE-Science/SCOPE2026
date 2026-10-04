#!/usr/bin/env python3
from fractions import Fraction
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def sigma_pp(p,e):
    return (p**(e+1)-1)//(p-1)

# Algebraic identity behind the second-prime cutoff:
# (q^2+q-2)/(q-2) = q+3 + 4/(q-2).
for q in range(3,1000,2):
    assert Fraction(q*q+q-2, q-2) == q+3+Fraction(4,q-2)

# The cutoff leaves exactly the candidates used in the proof.
for q in [x for x in range(3,1000,2) if is_prime(x)]:
    bound = Fraction(q*q+q-2, q-2)
    candidates = [r for r in range(q+1, int(bound)+1) if is_prime(r) and Fraction(r,1) < bound]
    if q == 3:
        assert candidates == [5,7]
    elif q == 5:
        assert candidates == [7]
    else:
        assert candidates in ([], [q+2])

# Exact special-order check.
x=1
order=None
for k in range(1,20):
    x=(x*3)%7
    if x==1:
        order=k
        break
assert order==6

# Regression search: no two-prime square in a substantial finite grid.
for q in [x for x in range(3,150,2) if is_prime(x)]:
    for r in [x for x in range(q+2,250,2) if is_prime(x)]:
        for a in range(1,7):
            for b in range(1,7):
                left = Fraction(sigma_pp(q,2*a), q**(2*a))*Fraction(sigma_pp(r,2*b), r**(2*b))
                assert left != Fraction(q+2,q)

print('VERIFY_OK')
