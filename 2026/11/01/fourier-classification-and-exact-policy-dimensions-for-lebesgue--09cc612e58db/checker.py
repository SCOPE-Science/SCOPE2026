#!/usr/bin/env python3
"""Finite exact Fourier support checks supporting a separate analytical proof."""
import math
from fractions import Fraction


def classes(m, n, cutoff):
    assert math.gcd(m, n) == 1 and 2 <= m and 2 <= n
    result = {}
    for k in range(1, cutoff+1):
        r, a, b = k, 0, 0
        while r % m == 0:
            r //= m
            a += 1
        while r % n == 0:
            r //= n
            b += 1
        assert r % m != 0 and r % n != 0
        result.setdefault((r,a+b),set()).add(k)
    return result


def expected_dimension(m,n,N):
    return 1 + 2*sum(1 for r in range(1,N+1) if r%m and r%n
                     for ell in range(N.bit_length()+1)
                     if r*max(m,n)**ell <=N)


def independent_classes(m,n,N):
    # A support class must fit entirely below N. If a Fourier coefficient
    # is forced equal to one outside the support, the whole class vanishes.
    c=classes(m,n,N)
    return 1+2*sum(all(r*m**a*n**(level-a)<=N for a in range(level+1))
                   for r,level in c)

for m in range(2,9):
 for n in range(2,9):
  if math.gcd(m,n) != 1:continue
  for N in range(1,90):
   assert expected_dimension(m,n,N)==independent_classes(m,n,N)
   cl=classes(m,n,N)
   assert sum(len(s) for s in cl.values())==N
# For p=1/2+epsilon[cos(4pi x)+cos(6pi x)] with epsilon=1/8,
# transfer Fourier coefficients at the only nonzero input frequencies are:
epsilon=Fraction(1,8)
p_hat={0:Fraction(1,2),2:epsilon/2,-2:epsilon/2,
       3:epsilon/2,-3:epsilon/2}
for k in range(-100,101):
 assert p_hat.get(2*k,0)==p_hat.get(3*k,0)
assert 2*abs(epsilon)<=Fraction(1,2)
print('PASS: exact class coverage, cutoff dimensions and nonconstant feedback witness')
