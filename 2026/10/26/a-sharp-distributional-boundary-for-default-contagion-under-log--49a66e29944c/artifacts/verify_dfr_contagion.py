#!/usr/bin/env python3
"""Reproduce the finite numerical witness for the log-convex-survival result.

The general result is proved analytically in RESULT.md; this script checks only
representative finite values and the explicit two-rate witness.
"""
from decimal import Decimal, getcontext

getcontext().prec = 60

def S(t: Decimal) -> Decimal:
    return ( (-t).exp() + (-Decimal(10) * t).exp() ) / Decimal(2)

x = Decimal(1) / Decimal(5)
contagion = S(Decimal(2) * x)
direct = S(x) ** 2
gap = contagion - direct
assert gap > 0
# Algebraically, for this two-rate mixture, the gap equals (e^-x-e^-10x)^2/4.
exact_identity_rhs = ((-x).exp() - (-Decimal(10) * x).exp()) ** 2 / Decimal(4)
assert abs(gap - exact_identity_rhs) < Decimal('1e-55')

for m in range(1, 9):
    q = Decimal(m + 1)
    test_x = Decimal(1) / (Decimal(2) * q)
    assert q * test_x < 1
    assert S(q * test_x) > S(test_x) ** int(q)

print('two-rate witness: PASS')
print(f'S(2/5)={contagion}')
print(f'S(1/5)^2={direct}')
print(f'gap={gap}')
print('representative finite cases m=1..8: PASS')
