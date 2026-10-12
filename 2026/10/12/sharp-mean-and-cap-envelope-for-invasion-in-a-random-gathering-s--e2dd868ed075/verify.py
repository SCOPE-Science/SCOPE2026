#!/usr/bin/env python3
from fractions import Fraction as F

def bounds(K, m):
    assert isinstance(K, int) and K >= 2
    assert F(1) < m <= K
    k = m.numerator // m.denominator
    delta = m - k
    lower = F(k*(k-1)) + F(2*k)*delta
    upper = m*(K-1)
    return k, delta, lower, upper

for K in range(2, 20):
    for den in range(1, 9):
        for num in range(den+1, K*den+1):
            m = F(num, den)
            if not (F(1) < m <= K):
                continue
            k, delta, lower, upper = bounds(K, m)
            # Pointwise inequalities.
            for n in range(K+1):
                g = F(n*(n-1))
                assert g >= F(2*k*n - k*(k+1))
                assert g <= F((K-1)*n)

            # Lower extremizer.
            p_hi = delta
            p_lo = 1-delta
            mean_lo = p_lo*k + p_hi*(k+1)
            fac_lo = p_lo*k*(k-1) + p_hi*(k+1)*k
            assert mean_lo == m
            assert fac_lo == lower

            # Upper extremizer.
            pK = m/K
            mean_hi = pK*K
            fac_hi = pK*K*(K-1)
            assert mean_hi == m
            assert fac_hi == upper
            assert lower <= upper

            # A rational convex mixture preserves mean and interpolates.
            t = F(3, 7)
            mix_mean = (1-t)*mean_lo + t*mean_hi
            mix_fac = (1-t)*fac_lo + t*fac_hi
            assert mix_mean == m
            assert mix_fac == (1-t)*lower + t*upper

# Threshold-separation certificate.
K = 10
m = F(3)
C = F(1,10)
_, _, lower, upper = bounds(K, m)
assert C*lower == F(3,5)
assert C*upper == F(27,10)
assert C*lower < 1 < C*upper

# Fixed mean with no cap is unbounded above.
m = F(3)
vals = []
for L in (3, 10, 100, 1000):
    pL = m/L
    assert pL <= 1
    assert pL*L == m
    vals.append(m*(L-1))
assert vals == sorted(vals)
assert vals[-1] > 1000

print("VERIFY_OK")
print("certificate_R0_min", float(F(3,5)))
print("certificate_R0_max", float(F(27,10)))
print("no_cap_factorial_moment_L1000", vals[-1])
