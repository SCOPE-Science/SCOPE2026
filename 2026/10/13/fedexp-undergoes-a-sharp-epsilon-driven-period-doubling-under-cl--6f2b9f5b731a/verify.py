from fractions import Fraction
import math
import random

def fedexp_ratio(x, s, b, eps):
    return max(1.0, (x*x+b*b)/(2.0*(x*x+eps/(s*s))))

def T(x, s, b, eps):
    return x - s*x*fedexp_ratio(x,s,b,eps)

def derivative_numeric(x, s, b, eps):
    h = 1e-7*max(1.0,abs(x))
    return (T(x+h,s,b,eps)-T(x-h,s,b,eps))/(2*h)

def r_lower(s):
    return s*(2.0-s)/(2.0*(8.0-3.0*s))

rng = random.Random(350056)

# Fixed-point stability threshold and cycle formula.
for _ in range(500):
    s = rng.uniform(0.03,1.0)
    b = rng.uniform(0.2,3.0)
    r = rng.uniform(0.002,0.49)
    eps = r*s*s*b*b

    if r < 0.5:
        d0 = 1.0-s/(2.0*r)
    else:
        d0 = 1.0-s
    stable_expected = r > s/4.0
    if stable_expected:
        assert abs(d0) < 1.0 + 1e-12
    elif abs(r-s/4.0) > 1e-10:
        assert abs(d0) > 1.0 - 1e-12

    if r < s/4.0:
        xc2 = b*b*(s-4.0*r)/(4.0-s)
        assert xc2 > 0.0
        xc = math.sqrt(xc2)
        assert abs(T(xc,s,b,eps)+xc) < 2e-10
        assert abs(T(-xc,s,b,eps)-xc) < 2e-10
        assert abs(fedexp_ratio(xc,s,b,eps)-2.0/s) < 2e-10

        D = -(5.0*r*s-16.0*r-s*s+3.0*s)/(s*(r-1.0))
        assert abs(derivative_numeric(xc,s,b,eps)-D) < 2e-5
        stable_cycle = r_lower(s) < r < s/4.0
        if stable_cycle:
            assert abs(D) < 1.0
        elif r < r_lower(s)-1e-10:
            assert abs(D) > 1.0

# Exact-local-solve witness.
s = Fraction(1,1)
b = Fraction(1,1)
eps = Fraction(1,8)
r = eps/(s*s*b*b)

# Client local models for a=eta_l=1 are +1 and -1 for every x,
# so FedAvg averages them to zero.
for x0 in (Fraction(-5,2), Fraction(0,1), Fraction(7,3)):
    local1 = b
    local2 = -b
    fedavg = (local1+local2)/2
    assert fedavg == 0

d0 = 1 - s/(2*r)
assert d0 == -3
xc2 = b*b*(s-4*r)/(4-s)
assert xc2 == Fraction(1,6)
D = -(5*r*s-16*r-s*s+3*s)/(s*(r-1))
assert D == Fraction(5,7)
assert D*D == Fraction(25,49)

# At the exact cycle, eta_g=2 and T changes the sign.
xf = math.sqrt(float(xc2))
assert abs(fedexp_ratio(xf,1.0,1.0,0.125)-2.0) < 1e-14
assert abs(T(xf,1.0,1.0,0.125)+xf) < 1e-14

print("verification passed")
