#!/usr/bin/env python3
"""Reproducible finite checks for a three-step martingale moment comparison.

Run: python3 verify_power_threshold.py
Requires only the Python standard library. The infinite claims require the
analytic proof in RESULT.md; these checks do not replace that proof.
"""
from decimal import Decimal, localcontext
from fractions import Fraction
from math import cos, sin, hypot, pi

checks = 0

def check(condition, message):
    global checks
    assert condition, message
    checks += 1

def generalized_binomial(p, n):
    ans = Fraction(1)
    for j in range(n):
        ans *= (p-j)
        ans /= (j+1)
    return ans

# Coefficient signs: at powers epsilon^(2k), k>=2, both factors are negative.
for numerator, denominator in [(21, 10), (9, 4), (5, 2), (11, 4), (29, 10)]:
    p = Fraction(numerator, denominator)
    for k in range(2, 65):
        c = (2**k-2**(2*k-1))*generalized_binomial(p, 2*k)
        check(c > 0, f"sign failure at p={p}, k={k}")

check((2**2-2**3)*generalized_binomial(Fraction(5, 2), 4) == Fraction(5, 32),
      "leading coefficient at p=5/2")

# The complete difference is at least its positive quartic contribution.
with localcontext() as ctx:
    ctx.prec = 85
    rt2 = Decimal(2).sqrt()
    one = Decimal(1)
    two = Decimal(2)
    for p_string in ["2.05", "2.25", "2.5", "2.75", "2.95"]:
        p = Decimal(p_string)
        for eps_string in ["0.02", "0.1", "0.25", "0.4", "0.49"]:
            eps = Decimal(eps_string)
            L = ((one+rt2*eps)**p + (one-rt2*eps)**p)/two
            R = Decimal("0.5")+((one+two*eps)**p+(one-two*eps)**p)/Decimal(4)
            coeff = p*(p-one)*(p-two)*(Decimal(3)-p)/Decimal(6)
            check(L-R > coeff*eps**4, f"gap bound failed p={p}, eps={eps}")
    for p_string in ["3.05", "3.5", "4", "5"]:
        p = Decimal(p_string)
        for eps_string in ["0.025", "0.125", "0.25", "0.4"]:
            eps=Decimal(eps_string)
            L=((one+rt2*eps)**p+(one-rt2*eps)**p)/two
            R=Decimal("0.5")+((one+two*eps)**p+(one-two*eps)**p)/Decimal(4)
            check(L<R, "p>3 comparison sanity check")
    for eps_string in ["0.03", "0.1", "0.25", "0.4", "0.49"]:
        eps=Decimal(eps_string)
        for p_integer in [2,3]:
            p=Decimal(p_integer)
            L=((one+rt2*eps)**p+(one-rt2*eps)**p)/two
            R=Decimal("0.5")+((one+two*eps)**p+(one-two*eps)**p)/Decimal(4)
            check(abs(L-R) < Decimal("1e-75"), "quadratic/cubic endpoint")

# A representative grid of independent first/second steps; the proof handles
# arbitrary conditional mean-zero bounded steps, not just these samples.
for p in [2.0, 2.2, 2.5, 2.9, 3.0, 3.5, 5.0]:
    for a in [0.25, 1.0, 1.5]:
        for b in [0.25, 1.0, 1.5]:
            R=((a+b)**p+abs(a-b)**p)/2
            for angle_index in range(13):
                angle=pi*angle_index/12
                dot=cos(angle)
                L=((a*a+b*b+2*a*b*dot)**(p/2)
                   +(a*a+b*b-2*a*b*dot)**(p/2))/2
                check(L<=R+1e-10,"two-step directional sample")

# Orthogonal two-step witness gives strict reversal below quadratic order.
for p in [0.2, 0.5, 1.0, 1.5, 1.95]:
    check(2**(p/2)>2**(p-1), "subquadratic orthogonal witness")

print(f"PASS: {checks} deterministic assertions")
print("Numerical checks corroborate but do not certify the infinite sign proof.")
