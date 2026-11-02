"""Independent finite numerical checks for canonical mixed zeta-star product gaps.

The all-parameter assertions are proved analytically; these checks only test
specified instances and the elementary rational inequalities used in the proof.
"""
from fractions import Fraction
from math import exp, fsum, log1p, pi

N = 3500
zeta2 = pi * pi / 6
zeta3 = fsum(1.0 / (n ** 3) for n in range(1, 100001))

def A(s):
    return exp(fsum(-log1p(-float(n ** (-s))) for n in range(2, N + 1)))

def gap_ratio(q):
    if q == 2:
        return 2 - 1 / zeta3
    f = 1.0
    prefix = 1.0
    correction = 0.0
    for n in range(2, N + 1):
        new_f = f / (1 - n ** (-q))
        correction += (new_f - f) * (zeta2 - prefix)
        prefix += 1 / (n * n)
        f = new_f
    return 1 + correction / zeta2

assert Fraction(1,8)+Fraction(1,27)+Fraction(1,64)+Fraction(1,32) < Fraction(7,33)
assert 1+Fraction(1,4)+Fraction(1,9)+Fraction(1,4) > Fraction(8,5)
assert 1+Fraction(1,4)+Fraction(2,5) == Fraction(33,20)
assert 1+Fraction(1,8)+Fraction(1,27)+Fraction(1,64) > Fraction(7,6)
assert 1+Fraction(1,8)+Fraction(1,27)+Fraction(1,18) < Fraction(91,74)
assert Fraction(48,43) < Fraction(8,7)
assert Fraction(108,91) == 2-Fraction(74,91)

for q in range(2, 31):
    ratio = gap_ratio(q)
    lo = A(q + 2)
    hi = A(q + 1)
    assert lo < ratio < hi, (q, lo, ratio, hi)
    if q in (2,3,4,5,10,20,30):
        print(f'q={q:2d}  A(q+2)={lo:.13f} < gap ratio={ratio:.13f} < A(q+1)={hi:.13f}')
print('VERIFY_OK cases=29 rational_inequalities=7 all_strict=True')
