"""Independent numerical checks of the large-part sum-system threshold formula.

Requires Python 3 and mpmath (pip install mpmath). Finite tests do not prove
an infinite asymptotic; the mathematical proof is in RESULT.md.
"""
import mpmath as mp

mp.mp.dps = 90
a, b = mp.log(2), mp.log(3)
beta = mp.log(mp.mpf(3) / 2) / a
gamma = mp.log(mp.mpf(5) / 2) / a
theta = mp.log(mp.mpf(7) / 2) / a
A = 1 / (2 * a) - b / a**2
C = -b / a**2
D = (a**2 / 3 - 3 * a * b / 2 + 3 * b**2 / 2) / a**3


def root_shift(M):
    r0 = mp.log(M) / a
    lo, hi = mp.mpf(0), mp.mpf(1)
    assert M * (mp.zeta(r0 + lo) - 1) > 1
    assert M * (mp.zeta(r0 + hi) - 1) < 1
    for _ in range(310):
        mid = (lo + hi) / 2
        if M * (mp.zeta(r0 + mid) - 1) > 1:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


for power in (4, 6, 8, 10, 12):
    M = mp.mpf(10)**power
    u, v, w = M**(-beta), 1 / M, M**(-gamma)
    approximate = u/a + v/a + A*u*u + w/a + C*u*v + D*u*u*u
    actual = root_shift(M)
    scaled = (actual - approximate) * M**theta
    assert abs(scaled) < 3, (power, scaled)
    print(f"M=10^{power}: exact_shift={mp.nstr(actual, 22)}, residual/M^(-theta)={mp.nstr(scaled, 14)}")
print('VERIFY_OK')
