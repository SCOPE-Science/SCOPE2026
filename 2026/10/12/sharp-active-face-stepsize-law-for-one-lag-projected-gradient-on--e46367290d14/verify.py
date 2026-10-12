"""Exact rational corroboration of the scalar phase diagram; not a proof by enumeration."""
from fractions import Fraction as F

def step(x,y,a,s):
    return max(F(0), y - s*(x-a))

def E(u,v,s):
    c=s/(1+s)
    return u*u - 2*c*u*v + s*v*v

# Six-cycle at the exact interior threshold.
a=s=F(1)
y=[F(3,2),F(1)]
for _ in range(10):
    y.append(step(y[-2],y[-1],a,s))
assert y[:7] == [F(3,2),F(1),F(1,2),F(1,2),F(1),F(3,2),F(3,2)]
assert all(y[k]==y[k+6] for k in range(6))

# Active but non-strict: every s>=1 has exact absorption by indices 3 and 4.
for s in [F(1),F(3,2),F(5,2),F(10)]:
    for x0 in [F(0),F(1,3),F(3)]:
        for x1 in [F(0),F(2,3),F(5)]:
            y=[x0,x1]
            for _ in range(4):y.append(step(y[-2],y[-1],F(0),s))
            assert y[3]==0 and y[4]==0

# Strict activity gives a decreasing staircase regardless of the stale value.
for s in [F(1,20),F(1,2),F(3),F(20)]:
    for x0,x1 in [(F(10),F(5)), (F(0),F(0)), (F(100),F(1))]:
        y=[x0,x1]
        bound=1+(x1.numerator*(s.denominator) + (s.numerator*x1.denominator) - 1)//(s.numerator*x1.denominator)
        # a=-1 and x1/(s|a|) = x1/s.
        for _ in range(bound+2):y.append(step(y[-2],y[-1],F(-1),s))
        assert y[bound]==0 and all(z==0 for z in y[bound:])

# The exact quadratic identity and clipping monotonicity on rational parameters.
for s in [F(1,20),F(1,4),F(2,3),F(9,10)]:
    assert s-s*s/(1+s)**2>0
    for a in [F(0),F(1),F(4,3)]:
        for x0 in [F(0),F(1,3),F(2),F(4)]:
            for x1 in [F(0),F(2,3),F(3)]:
                v=x0-a;u=x1-a
                w=u-s*v
                z=max(-a,w)
                identity=E(w,u,s)-E(u,v,s)
                target=-s*(1-s)/(1+s)*u*u-s*(1-s)*v*v
                assert identity==target
                assert E(z,u,s)<=E(w,u,s)
                assert E(z,u,s)<=E(u,v,s)
print('VERIFY_OK')
