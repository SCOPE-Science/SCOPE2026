"""Exact Markov-generator identities and independent finite checks for a two-reserve comparison.

Requires Python 3 and SymPy. This script is a reproducibility check, not a substitute
for the complete all-parameter analytical proof in RESULT.md.
"""
import math
from fractions import Fraction
from random import Random
import sympy as S

m,h,c,s = S.symbols('m h c s', positive=True)
Q = S.Matrix([[-2*h,2*h],[c,-(h+c)]])
absorption = S.Matrix([0,h])
transform = (S.Matrix([[1,0]])*(s*S.eye(2)-Q).inv()*absorption)[0]
assert S.factor(transform - 2*h**2/(s**2+(3*h+c)*s+2*h**2)) == 0
assert S.factor(-S.diff(transform,s).subs(s,0) - (3*h+c)/(2*h**2)) == 0
mean = ((-Q).inv()*S.ones(2,1))[0]
assert S.factor(mean-(3*h+c)/(2*h**2)) == 0
c_mean = 2*h*h/m-3*h
c_tail = (h-m)*(2*h-m)/m
assert S.factor(c_tail-c_mean-m) == 0
assert S.factor((m*m-(3*h+c)*m+2*h*h).subs(c,c_tail)) == 0
assert S.factor((2*h*h/m-m) * (m*m/(2*h*h-m*m))-m) == 0

rng = Random(410203)
for _ in range(256):
    mm = Fraction(rng.randint(1,13),rng.randint(1,11))
    hh = mm * Fraction(rng.randint(12,31),10)
    cc = Fraction(rng.randint(0,65),rng.randint(1,11))
    q = S.Matrix([[-2*S.Rational(hh.numerator,hh.denominator), 2*S.Rational(hh.numerator,hh.denominator)],
                  [S.Rational(cc.numerator,cc.denominator),-S.Rational(hh.numerator,hh.denominator)-S.Rational(cc.numerator,cc.denominator)]])
    exact_m = ((-q).inv()*S.ones(2,1))[0]
    target = S.Rational(3*hh+cc)/S.Rational(2*hh*hh)
    assert exact_m == target
    assert S.det(-q) == 2*S.Rational(hh*hh)

mm=1.0;hh=2.0;cc=2.5
slow=(3*hh+cc-math.sqrt((3*hh+cc)**2-8*hh**2))/2
fast=(3*hh+cc+math.sqrt((3*hh+cc)**2-8*hh**2))/2
assert slow>mm
surv=lambda t: (fast*math.exp(-slow*t)-slow*math.exp(-fast*t))/(fast-slow)
f=lambda t:surv(t)-math.exp(-mm*t)
lo,hi=0.1,10.0
assert f(lo)>0>f(hi)
for _ in range(100):
    mid=(lo+hi)/2
    if f(mid)>0: lo=mid
    else: hi=mid
cross=(lo+hi)/2
assert abs(cross-2.01543084627562)<1.e-10

# The computed critical-rescue scaling is checked at successively smaller gaps.
limit_constant=7*math.log(8/7)
for gap in (0.01,0.005):
    cc=3-gap
    slow=(6+cc-math.sqrt((6+cc)**2-32))/2
    fast=(6+cc+math.sqrt((6+cc)**2-32))/2
    d=fast-slow
    # Asymptotic comparison is exponentially accurate here.
    approx=math.log(fast/d)/(slow-1)
    assert abs(gap*approx-limit_constant)<0.02
print('PASS: exact generator, Laplace and moment identities; 256 independent rational parameter cases; example crossover and critical asymptotics')
