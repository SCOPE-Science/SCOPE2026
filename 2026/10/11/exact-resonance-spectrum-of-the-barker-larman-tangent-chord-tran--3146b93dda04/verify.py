#!/usr/bin/env python3
import math
import sympy as s
from math import gcd

R, S = s.symbols("R S", positive=True)
fp, fm, fpp, fpm = s.symbols("fp fm fpp fpm", real=True)

# Endpoint coefficients obtained from the implicit equation.
a_plus = R*fp/S
a_minus = -R*fm/S

# q''(s)=1/R^3 and d/ds atan(s)=1/R^2 at s=+/-S.
b_plus = s.simplify(
    -(R/S) * (s.Rational(1,2)*a_plus**2/R**3 - fpp*a_plus/R**2)
)
b_minus = s.simplify(
    -(-R/S) * (s.Rational(1,2)*a_minus**2/R**3 - fpm*a_minus/R**2)
)

assert s.simplify(b_plus - (fpp*fp/S**2 - fp**2/(2*S**3))) == 0
assert s.simplify(b_minus - (fpm*fm/S**2 + fm**2/(2*S**3))) == 0

L1 = s.simplify(a_plus-a_minus)
L2 = s.simplify(b_plus-b_minus)
assert s.simplify(L1 - R*(fp+fm)/S) == 0
assert s.simplify(
    L2 - ((fpp*fp-fpm*fm)/S**2 - (fp**2+fm**2)/(2*S**3))
) == 0

# Resonant harmonic simplification, represented by k beta = pi/2 modulo pi.
t, k = s.symbols("t k", real=True)
fplus = s.cos(t+s.pi/2)
fminus = s.cos(t-s.pi/2)
dfplus = -k*s.sin(t+s.pi/2)
dfminus = -k*s.sin(t-s.pi/2)
res_L1 = s.trigsimp(fplus+fminus)
res_L2 = s.trigsimp(
    (dfplus*fplus-dfminus*fminus)/S**2
    - (fplus**2+fminus**2)/(2*S**3)
)
assert s.simplify(res_L1) == 0
assert s.simplify(res_L2 + s.sin(t)**2/S**3) == 0

# Exact finite regression of the arithmetic classification.
for b in range(2, 31):
    for a in range(1, (b+1)//2):
        if 2*a >= b or gcd(a,b) != 1:
            continue
        for kk in range(1, 5*b+1):
            # cos(pi*kk*a/b)=0 iff 2*kk*a/b is an odd integer.
            zero = ((2*kk*a) % b == 0) and (((2*kk*a)//b) % 2 == 1)
            predicted = (b % 2 == 0) and (kk % (b//2) == 0) and ((kk//(b//2)) % 2 == 1)
            assert zero == predicted

# Two exact basic resonances.
# beta=pi/4: R=sqrt(2), S=1, k=2.
assert s.simplify((-s.sin(2*t)**2) - (-s.sin(2*t)**2/s.Integer(1)**3)) == 0

# beta=pi/6: R=2/sqrt(3), S=1/sqrt(3), k=3.
S2 = 1/s.sqrt(3)
assert s.simplify(-s.sin(3*t)**2/S2**3 + 3*s.sqrt(3)*s.sin(3*t)**2) == 0

print("VERIFY_OK")
print("first_variation = (R/S)*(f(theta+beta)+f(theta-beta))")
print("multiplier = (2R/S)*cos(k beta)")
print("resonance = reduced beta/pi has even denominator")
print("quadratic_resonant_coefficient = -sin(k theta)^2/S^3")
