"""Numerical and exact-arithmetic checks of entropy identities for a symmetric intermittent map.

Run: python verify.py
This test is finite numerical corroboration, not a substitute for the proof.
"""
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 55

def F(z):
    return (1 + z) * mp.log1p(z) - z * mp.log(z) if z else mp.mpf('0')

def entropy(B):
    B = mp.mpf(str(B))
    if B == 1:
        return mp.log(2)
    q = B - 1
    a = B / (B + 1)
    return a / q * mp.quad(lambda z: F(z) * z**(1 / q - 1), [0, 1])

def entropy_direct(B):
    B = mp.mpf(str(B))
    q = B - 1
    a = B / (B + 1)
    if B == 1:
        return mp.log(2)
    # Integral of log |T'| over half the interval, two branches.
    return a * mp.quad(lambda t: mp.log1p(t**q) + t**q * mp.log1p(t**(-q)), [0, 1])

for B in range(1, 9):
    for t in [Fraction(1, 6), Fraction(1, 3), Fraction(2, 5), Fraction(3, 4)]:
        z = t**(B - 1)
        outer_slope = 1 + z
        inner_slope = 1 + 1/z
        assert Fraction(1, outer_slope) + Fraction(1, inner_slope) == 1
    assert abs(entropy(B) - entropy_direct(B)) < mp.mpf('1e-48'), B

values = [entropy(B) for B in [1, 1.1, 1.5, 2, 3, 5, 10, 30]]
assert all(u > v > 0 for u, v in zip(values, values[1:])), values
assert abs(entropy(2) - mp.mpf('0.59086290741326041')) < mp.mpf('1e-16')
for q in ['0.01','0.001']:
    deficit = (mp.log(2) - entropy(1 + mp.mpf(q))) / mp.mpf(q)**2
    assert abs(deficit - mp.mpf('0.25')) < mp.mpf('3') * mp.mpf(q)
C = mp.pi**2 / 12 + 2 * mp.log(2)
J = -C - mp.mpf(3) * mp.zeta(3) / 4
for B in [100, 200, 400]:
    calculated = entropy(B)
    two_term = C / B + J / B**2
    assert abs(calculated - two_term) < mp.mpf('7') / B**3
print('VERIFY_OK', len(values), 'entropy(2)=', mp.nstr(entropy(2), 18), 'C=', mp.nstr(C,18), 'J=', mp.nstr(J,18))
