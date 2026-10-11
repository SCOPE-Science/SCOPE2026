#!/usr/bin/env python3
from fractions import Fraction
import math

# Exact algebra: P stands for the independent constant 4*pi.
for lam in [Fraction(1,2), Fraction(2,3), Fraction(3,2), Fraction(5,2)]:
    for c in [Fraction(-2), Fraction(-1,4), Fraction(0), Fraction(3,2)]:
        D = lam*lam + c
        if D == 0:
            continue
        for J in [Fraction(1,3), Fraction(5,7)]:
            P = Fraction(13,5)
            A = (P - 2*J*lam) / D
            assert D*A + 2*lam*J == P
            dA_dlam = ((-2*J)*D - (P-2*J*lam)*(2*lam)) / (D*D)
            assert dA_dlam*D == -2*lam*A - 2*J

# Elementary antiderivatives I_c'(lambda)=(lambda^2+c)^(-2).
def I(c, lam):
    if c > 0:
        a = math.sqrt(c)
        return lam/(2*c*(lam*lam+c)) + math.atan(lam/a)/(2*a**3)
    if c == 0:
        return -1/(3*lam**3)
    k = math.sqrt(-c)
    return -lam/(2*k*k*(lam*lam-k*k)) + math.log(abs((lam+k)/(lam-k)))/(4*k**3)

for c, vals in [(2.0,[0.4,1.3,2.1]), (0.0,[0.7,1.4,2.4]), (-1.0,[0.35,0.7,1.4,2.2])]:
    for lam in vals:
        if abs(lam*lam+c) < 0.1:
            continue
        h = 1e-6
        num = (I(c,lam+h)-I(c,lam-h))/(2*h)
        target = 1/(lam*lam+c)**2
        assert abs(num-target) <= 2e-6*max(1.0,abs(target))

# Euclidean direct lens check: radius R-t and fixed center distance d.
for R,d,t in [(3.0,2.0,0.4),(5.0,1.5,1.2),(2.0,1.0,0.3)]:
    Rp=R-t
    lam=1/Rp
    J=math.pi*d
    A_general=(4*math.pi-2*J*lam)/(lam*lam)
    A_caps=4*math.pi*Rp*(Rp-d/2)
    assert abs(A_general-A_caps) < 1e-10

# Critical hyperbolic profile checks.
for k,A0,t in [(1.0,20.0,0.2),(0.7,30.0,0.15),(1.5,12.0,0.1)]:
    B=A0+2*math.pi/(k*k)
    A=B*math.exp(-2*k*t)-2*math.pi/(k*k)
    Aprime=-2*k*B*math.exp(-2*k*t)
    J=2*math.pi/k
    assert abs(Aprime-(-2*k*A-2*J)) < 1e-10
    loss=B*(1-math.exp(-2*k*t))/(2*k)-2*math.pi*t/(k*k)
    h=1e-6
    def lossf(s):
        return B*(1-math.exp(-2*k*s))/(2*k)-2*math.pi*s/(k*k)
    dloss=(lossf(t+h)-lossf(t-h))/(2*h)
    assert abs(dloss-A) < 1e-7
    assert loss > 0

print('VERIFY_OK')
