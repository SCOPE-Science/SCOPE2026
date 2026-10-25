#!/usr/bin/env python3
"""Independent numerical consistency checks for the nearest-neighbor specialization.
Run: python3 check.py   (requires mpmath).  Numerical checks are not proofs.
"""
import mpmath as mp
mp.mp.dps = 85

def g0(kappa):
    k = mp.mpf(kappa)
    modulus_squared = 16 / (4 + k)**2
    return 2 * mp.ellipk(modulus_squared) / (mp.pi * (4 + k))

def g1(kappa):
    return ((4 + kappa)*g0(kappa) - 1) / 4

def secular(kappa):
    return g0(kappa)**2 - g1(kappa)**2

def root(lam):
    # Since the secular function decreases, bisection in log(kappa) is reliable.
    l = mp.mpf(lam)
    left, right = mp.mpf(-260), mp.mpf(25)
    for _ in range(450):
        middle = (left+right)/2
        if l*l*secular(mp.exp(middle)) > 1:
            left = middle
        else:
            right = middle
    return mp.exp((left+right)/2)

print('lambda | kappa | leading asymptotic | ratio')
for coupling in ['1.5','1.2','1.0','0.9']:
    lam = mp.mpf(coupling)
    k = root(lam)
    predicted = 32*mp.exp(-mp.pi/2-8*mp.pi/lam**2)
    assert mp.fabs(lam**2*secular(k)-1) < mp.mpf('1e-45')
    assert mp.fabs((4+k)*g0(k)-4*g1(k)-1) < mp.mpf('1e-45')
    print(coupling, mp.nstr(k,18), mp.nstr(predicted,18), mp.nstr(k/predicted,18))
assert abs(float(root('0.9')/(32*mp.exp(-mp.pi/2-8*mp.pi/mp.mpf('0.9')**2))-1)) < 1e-9
print('checks passed')
