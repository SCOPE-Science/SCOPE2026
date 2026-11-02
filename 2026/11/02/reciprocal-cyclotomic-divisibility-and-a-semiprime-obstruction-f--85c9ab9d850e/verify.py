"""Finite checks for a cyclotomic divisibility lemma and a gcd-reciprocal sum."""
from fractions import Fraction
from math import gcd

def F(t):
    return t*t-t+1

def omega(n):
    count = 0
    d = 2
    while d*d <= n:
        while n % d == 0:
            count += 1
            n //= d
        d += 1
    return count + (n>1)

pairs_checked = 0
for a in range(1,1001):
    for b in range(1,1001):
        pair = F(b)%a == 0 and F(a)%b == 0
        assert pair == (a==b==1), (a,b)
        pairs_checked += 1
n_checked = 0
for n in range(2,1001):
    if omega(n)<=2:
        # Independently use the definition rather than the factorization identity.
        total = sum((Fraction(1,gcd(n,i)) for i in range(1,n+1)), Fraction())
        assert total.denominator != 1,n
        n_checked += 1
print(f'VERIFY_OK pairs={pairs_checked} n_with_omega_le_2={n_checked}')
