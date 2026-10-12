#!/usr/bin/env python3
from fractions import Fraction

# Curve E: y^2 = x^3 + 13x^2 - 32x.
def rhs(x):
    return x**3 + 13*x**2 - 32*x

pts = [(0,0),(4,12),(4,-12),(-8,24),(-8,-24)]
assert all(y*y == rhs(x) for x,y in pts)

# The birational reduction from the two square conditions.
# q = u-(t-2), X=-2q, Y=2qv, t=(X^2+8X-32)/(4X).
for X in (4,-8):
    t = Fraction(X*X + 8*X - 32, 4*X)
    assert t == 1
    a = (t-2)**2 + 8
    b = 4*t + 5
    assert a == 9 and b == 9

# 2-isogeny descent local exclusions for E_{a,b}: y^2=x^3+a x^2+b x.
# A square-class d is represented only if N^2=d M^4+a M^2 e^2+(b/d)e^4
# has a primitive solution.  For E, d=-1 and d=2 are impossible mod 3.
def squares(m): return {i*i % m for i in range(m)}
for d in (-1,2):
    b = -32
    a = 13
    b2 = b//d
    ok=False
    for M in range(3):
        for e in range(3):
            if M%3==0 and e%3==0: continue
            z=(d*M**4 + a*M*M*e*e + b2*e**4)%3
            if z in squares(3): ok=True
    assert not ok, (d,'unexpected mod-3 solution')

# Isogenous curve E': y^2=x^3-26x^2+297x.
# Negative d classes are impossible over R. Positive d=3,11 are impossible mod 16.
for d in (3,11):
    b = 297
    a = -26
    b2 = b//d
    ok=False
    for M in range(16):
        for e in range(16):
            if M%2==0 and e%2==0: continue
            z=(d*M**4 + a*M*M*e*e + b2*e**4)%16
            if z in squares(16): ok=True
    assert not ok, (d,'unexpected mod-16 solution')
for d in (-1,-3,-11,-33):
    b2 = 297//d
    assert d < 0 and b2 < 0 and -26 < 0

# Good-reduction point counts; discriminant has prime divisors only 2,3,11.
def count_points(p):
    n=1
    for x in range(p):
        r=rhs(x)%p
        n += sum(1 for y in range(p) if y*y%p==r)
    return n
assert count_points(5)==6
assert count_points(7)==6

# Six rational points are therefore all torsion once the 2-descent rank is zero.
assert len({('O',),*[(x,y) for x,y in pts]}) == 6
print('E_points_mod_5=6')
print('E_points_mod_7=6')
print('alpha_E_classes={1,-2}')
print('alpha_Eprime_classes={1,33}')
print('rank_from_2_isogeny_descent=0')
print('rational_points=O,(0,0),(4,+-12),(-8,+-24)')
print('parameter_t=1')
print('CHECK_OK')
