from fractions import Fraction
from math import sqrt

def det(a,b,c):
    return Fraction(1) + 2*a*b*c - a*a - b*b - c*c

def deficit(a,b,c):
    s=a*a+b*b+c*c
    return 2*s+8*a*b*c

# Exact checks for the two sharpness families at rational parameters.
for q in range(2,41):
    for p in range(0,q//2+1):
        t=Fraction(p,q)
        a=b=t; c=-t
        assert det(a,b,c) >= 0
        s=a*a+b*b+c*c
        # First-branch identity: because s=3 t^2, (s/3)^(3/2)=t^3.
        assert deficit(a,b,c) == 2*s-8*t**3

for q in range(2,41):
    for p in range((q+1)//2,q+1):
        t=Fraction(p,q)
        a=b=t; c=2*t*t-1
        assert det(a,b,c) == 0
        s=a*a+b*b+c*c
        assert Fraction(3,4) <= s <= 3
        assert deficit(a,b,c) == 6*s-4

# Exact rational grid check of the sharp global linear stability bound.
count=0
for q in range(2,15):
    vals=[Fraction(p,q) for p in range(-q,q+1)]
    for a in vals:
        for b in vals:
            for c in vals:
                if det(a,b,c) >= 0:
                    s=a*a+b*b+c*c
                    d=deficit(a,b,c)
                    assert d >= Fraction(2,3)*s
                    # Supplemental floating check of the full piecewise envelope.
                    sf=float(s)
                    env=(2*sf-8*(sf/3.0)**1.5) if sf <= 0.75 else (6*sf-4)
                    assert float(d) + 1e-11 >= env
                    count += 1

# Exact nontrivial equality pattern for the global 2/3 constant.
a=b=Fraction(1,2); c=Fraction(-1,2)
s=a*a+b*b+c*c
assert s == Fraction(3,4)
assert det(a,b,c) == 0
assert deficit(a,b,c) == Fraction(2,3)*s == Fraction(1,2)

print('VERIFY_OK', count)
