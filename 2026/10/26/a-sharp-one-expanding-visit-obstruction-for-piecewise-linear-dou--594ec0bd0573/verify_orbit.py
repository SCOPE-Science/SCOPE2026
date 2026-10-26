"""Exact rational certificate for a four-cycle of a piecewise-linear circle map.

Run: python verify_orbit.py
Only Python standard library is required.
"""
from fractions import Fraction as Q

A = Q(203, 5000)
B = Q(17, 25)
PLUS = 2 * (1 + B)
MINUS = 2 * (1 - B)
points = [Q(t, 9312200) for t in (3571863, 9213387, 6460887, 4699287)]

def f(x):
    y = PLUS*x + A - B/2 if x < Q(1,2) else MINUS*x + A + 3*B/2
    return y - (y.numerator // y.denominator)

assert all(0 < x < 1 for x in points)
assert points[0] < Q(1,2)
assert all(x > Q(1,2) for x in points[1:])
assert len(set(points)) == 4
assert all(f(points[i]) == points[(i+1) % 4] for i in range(4))
assert PLUS * MINUS**3 == Q(344064, 390625) < 1

# Rational checks supporting the bounds used in the universal proof.
t = Q(3,4)
assert (4-t)*t**4 == Q(1053,1024) > 1
assert sum(t**(-j) for j in (1,2,3)) == Q(148,27) > 5
for k in range(5,75):
    for denom in (2,3,5,7,11,37):
        for numer in range(1,denom):
            t=Q(numer,denom)
            H=sum(t**j for j in range(k-1))
            assert H>(5-t)*t**(k-1)
print('PASS: four exact orbit steps, primitive period, itinerary, multiplier, and rational inequality stress tests')
