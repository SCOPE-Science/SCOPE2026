#!/usr/bin/env python3
import math

rho = 1.0 + math.sqrt(2.0)
p0 = math.log(rho, 2.0)
K = 8.0 * math.log(2.0) * (1.0 / rho + 1.0 / (rho * rho))
assert abs(2.0 / rho + 1.0 / (rho * rho) - 1.0) < 1e-14

def q(p, z):
    if z <= 0.0 or z >= 1.0:
        return p
    f = z**p + (1.0-z)**p + (z*(1.0-z))**p
    return (1.0-f)/(z*(1.0-z))

def balanced(p):
    return 4.0 * (1.0 - 2.0**(1.0-p) - 2.0**(-2.0*p))

h = 1e-7
fd = (balanced(p0+h)-balanced(p0-h))/(2.0*h)
assert abs(fd-K) < 1e-7

for delta in (1e-2, 1e-3, 1e-4):
    p = p0 + delta
    # Dense half-interval grid; symmetry supplies the other half.
    n = 100000
    best = (float('inf'), None)
    for i in range(1, n+1):
        z = 0.5 * i / n
        val = q(p, z)
        if val < best[0]:
            best = (val, z)
    assert abs(best[1]-0.5) <= 0.5/n
    assert abs(best[0]-balanced(p)) < 1e-11

ratio = balanced(p0+1e-5)/1e-5
assert abs(ratio-K) < 2e-4
print('VERIFY_OK')
print('p_sil=%.15f' % p0)
print('K=%.15f' % K)
print('delta_1e-5_ratio=%.15f' % ratio)
