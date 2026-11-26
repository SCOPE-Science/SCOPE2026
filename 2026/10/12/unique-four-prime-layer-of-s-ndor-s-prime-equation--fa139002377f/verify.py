from fractions import Fraction
from math import isqrt, prod

def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))

assert 2*prod(Fraction(p-1,p) for p in (5,7,11,13)) > 1
assert Fraction(4,3)*Fraction(10,11)**3 > 1
assert 5 % 3 != 0
k = 240-5
assert k > 45
candidates = [(16+a,16+k//a) for a in range(1,isqrt(k)+1) if k%a==0]
assert [(r,s) for r,s in candidates if r<s and prime(r) and prime(s)] == [(17,251)]

p,q,r,s = (3,5,17,251)
assert all(map(prime,(p,q,r,s)))
P,F = p*q*r*s, prod(x-1 for x in (p,q,r,s))
assert P-2*F == 5
m = 16*P
phi,divisors = 32*F,7*16
assert phi+divisors == m+32
print(f'VERIFY_OK c=5:3,5,17,251 m={m} phi_plus_d={phi+divisors}')
