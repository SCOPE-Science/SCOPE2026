#!/usr/bin/env python3
"""Reproduce elementary rational inequalities and finite Euler-product checks.

The finite prime products do not prove statements about infinitely many primes.
The mathematical proof supplies the monotone majorant for the infinite tail.
"""
from fractions import Fraction
from math import factorial, log, prod

# For x>=2, if sum_{k=0}^N r^k/k! > x, then log(x)<r.
bounds = {3: Fraction(11,10), 5: Fraction(161,100),
          7: Fraction(39,20), 11: Fraction(12,5),
          13: Fraction(257,100), 17: Fraction(71,25),
          19: Fraction(59,20)}
for p,r in bounds.items():
    truncated_exp = sum((r**k)/factorial(k) for k in range(9))
    assert truncated_exp > p, (p, r)

s_small = sum(2*bounds[p]/((p-1)*(p-2)) for p in bounds)
# For all x>=19, log x <= log(x-2)+2/(x-2).
# Integral tail: sum_{n>=20} f(n) <= integral_{19}^inf f(x) dx.
s_tail_upper = 2*(bounds[17]+1)/17 + Fraction(2,17*17)
s_upper = s_small + s_tail_upper
assert s_upper < Fraction(13,6)  # 1/2 + (5/2)(2/3)
# Euler gamma > H_6-log(7) > 1/2, since H_6=49/20,
# and log(7)<39/20, verified by rational exponential bound.
assert Fraction(49,20)-bounds[7] == Fraction(1,2)
# log 2 = 2*(1/3 + (1/3)^3/3 + ...) > 2/3.
assert s_upper < Fraction(1,2)+Fraction(5,2)*Fraction(2,3)

def primes_up_to(n):
    sieve = bytearray(b'\x01')*(n+1)
    sieve[:2] = b'\x00\x00'
    for i in range(2,int(n**0.5)+1):
        if sieve[i]:
            sieve[i*i:n+1:i] = b'\x00'*len(sieve[i*i:n+1:i])
    return [p for p in range(3,n+1) if sieve[p]]

ps=primes_up_to(30000)
S_part=sum(2*log(p)/((p-1)*(p-2)) for p in ps)
C2_part=prod(1-1/(p-1)**2 for p in ps)
def logG(s):
    return sum(log(1-2*p**(-s))-2*log(1-p**(-s)) for p in ps)
h=0.0001
deriv=(logG(1+h)-logG(1-h))/(2*h)
assert abs(deriv-S_part)<0.0005, (deriv,S_part)
assert S_part>0 and S_part<float(s_upper)
print('small-prime rational bound:',float(s_small))
print('full upper bound for prime logarithmic sum:',float(s_upper))
print('strict negativity threshold lower bound:',float(Fraction(13,6)))
print('finite partial prime logarithmic sum:',S_part)
print('finite partial twin-prime constant:',C2_part)
print('finite-product log derivative:',deriv)
print('RATIONAL SIGN CERTIFICATE AND FINITE EULER CHECKS: PASS')
