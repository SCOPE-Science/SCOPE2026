from fractions import Fraction
from math import acos, atan, sqrt, pi, floor

def seq(r, nmax):
    r=Fraction(r)
    z=[Fraction(1), Fraction(1,1)/(1+r)]
    d=3+2*r
    for n in range(2,nmax+1):
        z.append((4*z[-1]-z[-2])/d)
    return z

# Critical repeated-root identity.
r=Fraction(1,2)
z=seq(r,40)
for n,zn in enumerate(z):
    target=Fraction(n+3,3)*Fraction(1,2)**n
    assert zn==target, (n,zn,target)
    assert zn>0

# Exact first-negative indices from rational recurrence.
cases={Fraction(51,100):42, Fraction(3,5):12, Fraction(1):5,
       Fraction(2):3, Fraction(3):3, Fraction(10):2}
for r,expected in cases.items():
    z=seq(r,expected+2)
    got=next(n for n,v in enumerate(z) if v<0)
    assert got==expected,(r,got,expected,z)
    assert all(v>=0 for v in z[:got])

# Representative subcritical positivity checks in exact arithmetic.
for den in range(3,31):
    for num in range(1,den):
        r=Fraction(num,den)
        if r<=Fraction(1,2):
            assert all(v>0 for v in seq(r,80)), r

# Phase formula away from exact-zero boundary cases.
def phase_index(r):
    theta=acos(2/sqrt(3+2*r))
    phi=atan(1/((1+r)*sqrt(2*r-1)))
    q=(pi/2+phi)/theta
    return floor(q)+1

for r in [0.501,0.51,0.6,1.0,2.0,10.0]:
    got=next(n for n,v in enumerate(seq(Fraction(str(r)),600)) if v<0)
    assert got==phase_index(r),(r,got,phase_index(r))

# Critical-delay constant: increasingly near-threshold samples approach pi*sqrt(2).
target=pi*sqrt(2)
errs=[]
for eps in [1e-2,1e-3,1e-4,1e-5]:
    r=0.5+eps
    val=phase_index(r)*sqrt(eps)
    errs.append(abs(val-target))
assert errs[-1] < 0.03, errs
assert errs[-1] < errs[0], errs
print('VERIFY_OK')
