"""Exact-rational checks for consecutive minimum-distance valley gaps.
Run using Python 3.10+; no external dependencies.
"""
from math import comb, factorial, pi
from fractions import Fraction
from decimal import Decimal, localcontext
from itertools import permutations

E = [1, 1]
for n in range(1, 69):
    value = sum(comb(n, j) * E[j] * E[n-j] for j in range(n+1))
    assert value % 2 == 0
    E.append(value // 2)
assert [E[n] for n in [3,5,7,9]] == [2,16,272,7936]

checks = 0
# A direct permutation enumeration, independent of the Euler recurrence.
for k in range(4):
    n = 2*k + 3
    count = 0
    for p in permutations(range(n)):
        if all((p[i] > p[i+1] if i % 2 == 0 else p[i] < p[i+1]) for i in range(n-1)):
            count += 1
    assert count == E[n], (k,n,count,E[n])
    checks += 1
p = [Fraction(3 * E[2*k+3], factorial(2*k+3)) for k in range(33)]
assert p[:4] == [Fraction(1), Fraction(2,5), Fraction(17,105), Fraction(62,945)]
checks += 4
r = [p[k+1]/p[k] for k in range(32)]
assert r[:3] == [Fraction(2,5), Fraction(17,42), Fraction(62,153)]
checks += 3
assert r[2] - r[1] == Fraction(1,2142)
checks += 1
for k in range(31):
    assert r[k] < r[k+1]
    checks += 1
with localcontext() as context:
    context.prec = 100
    def atan_inv(n):
        x = Decimal(1)/n
        return sum(((-1)**k)*x**(2*k+1)/Decimal(2*k+1) for k in range(160))
    pi_decimal = 16*atan_inv(5)-4*atan_inv(239)
    limit = Decimal(4)/(pi_decimal*pi_decimal)
    for k in range(32):
        exact_r = Decimal(r[k].numerator)/Decimal(r[k].denominator)
        assert exact_r < limit, (k, exact_r, limit)
        checks += 1
    assert Decimal(0) < limit - Decimal(r[-1].numerator)/Decimal(r[-1].denominator) < Decimal('1e-30')
    checks += 1
for k in range(32):
    assert p[k] > p[k+1]
    checks += 1
print(f'PASS {checks} exact/computational assertions; values p[0:4]={p[:4]}')
print(f'r[0:3]={r[:3]}; upper limit 4/pi^2={4/pi**2:.15f}; r[31]={float(r[31]):.15f}')
