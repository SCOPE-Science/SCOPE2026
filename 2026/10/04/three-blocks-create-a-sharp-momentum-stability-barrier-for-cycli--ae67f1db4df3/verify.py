import math, cmath
from fractions import Fraction


def P(c,a):
    return (1+c+c*c + a*c**3*(c*c-2*c-2)
            + 3*a*a*c**3*(c*c-c-1) + 3*a**3*c**5)

def Q(c):
    return 7*c**4 + 2*c**3 - 3*c*c - 2*c - 1

def modal_roots(c,a):
    tr=c*c*(3-c)
    disc=tr*tr-4*c**3
    lam=(tr+cmath.sqrt(disc))/2
    d=((1+a)*lam)**2-4*a*lam
    s=cmath.sqrt(d)
    return ((1+a)*lam+s)/2, ((1+a)*lam-s)/2

# Exact-rational factorization checks on a grid.
for ci in range(1,20):
    c=Fraction(ci,20)
    for ai in range(0,21):
        a=Fraction(ai,20)
        left=(1-a*a*c**3)**2-(1+a)**2*c**3*(1-a*c*c*(3-c)+a*a*c**3)
        right=(1-c)*P(c,a)
        assert left == right

# P is decreasing on [0,1]: endpoint values of the convex derivative bracket are negative.
for ci in range(1,100):
    c=Fraction(ci,100)
    d0=c*c-2*c-2
    d1=8*(2*c+1)*(c-1)
    assert d0 < 0 and d1 < 0

# Isolate the unique quartic threshold.
lo,hi=0.0,1.0
for _ in range(100):
    mid=(lo+hi)/2
    if Q(mid) < 0:
        lo=mid
    else:
        hi=mid
cstar=(lo+hi)/2
mustar=1/cstar-1
assert abs(cstar-0.8489724556331144671) < 2e-15
assert abs(mustar-0.1778945163235689914) < 3e-15

# Unit extrapolation: one unstable and one stable example, plus the boundary.
for m, expected in [(0.1,'unstable'),(0.2,'stable')]:
    c=1/(1+m)
    rr=max(abs(z) for z in modal_roots(c,1.0))
    if expected=='unstable':
        assert rr > 1+1e-6
    else:
        assert rr < 1-1e-6
rr=max(abs(z) for z in modal_roots(cstar,1.0))
assert abs(rr-1) < 2e-13

# For a supercritical c, the unique alpha root splits stable and unstable regimes.
c=0.9
lo,hi=0.0,1.0
for _ in range(100):
    mid=(lo+hi)/2
    if P(c,mid)>0:
        lo=mid
    else:
        hi=mid
acrit=(lo+hi)/2
assert 0<acrit<1
assert max(abs(z) for z in modal_roots(c,acrit-1e-5)) < 1
assert max(abs(z) for z in modal_roots(c,acrit+1e-5)) > 1

# Two-block Jury inequalities for a dense grid.
for ci in range(1,100):
    c=ci/100
    lam=c*c
    for ai in range(0,101):
        a=ai/100
        assert 1-lam > 0
        assert 1+(1+2*a)*lam > 0
        assert 1-a*lam > 0

print('VERIFY_OK')
