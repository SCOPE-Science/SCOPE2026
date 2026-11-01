"""Finite supplemental checks for the sharp quadratic Hankel kernel-test inequality.

Run: python3 verify.py
The analytical theorem is proved separately; sampling does not certify all inputs.
"""
from fractions import Fraction
import cmath
import math
import random

checks = 0

def assert_close(x, y, tolerance=3e-10):
    global checks
    assert abs(x-y) <= tolerance * max(1.0, abs(x), abs(y)), (x, y)
    checks += 1


def f(b, r):
    return (1-r*r) * ((1-b*b+b*r)**2 + b*b)


def golden_max(fun, lo=0., hi=1., iterations=130):
    invphi=(math.sqrt(5)-1)/2
    x=hi-invphi*(hi-lo)
    y=lo+invphi*(hi-lo)
    fx,fy=fun(x),fun(y)
    for _ in range(iterations):
        if fx < fy:
            lo,x,fx=x,y,fy
            y=lo+invphi*(hi-lo)
            fy=fun(y)
        else:
            hi,y,fy=y,x,fx
            x=hi-invphi*(hi-lo)
            fx=fun(x)
    return max(fun(0.),fun(1.),fx,fy)

# Exact polynomial identity for the extremizing symbol, in t=sqrt(6) r.
# (t-1)^2(t^2+4t+8) = 50-(6-t^2)((1+t)^2+6).
def conv(a,b):
    z=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): z[i+j]+=x*y
    return z
lhs=conv(conv([Fraction(-1),Fraction(1)],[Fraction(-1),Fraction(1)]),
         [Fraction(8),Fraction(4),Fraction(1)])
rhs=conv([Fraction(6),Fraction(0),Fraction(-1)],
         [Fraction(7),Fraction(2),Fraction(1)])
rhs=[Fraction(50)-rhs[0]]+[-x for x in rhs[1:]]
assert lhs==rhs
checks+=1

r0=1/math.sqrt(6)
b0=math.sqrt(2/3)
assert_close(f(b0,r0),25/27)
assert_close(golden_max(lambda r:f(b0,r)),25/27)
assert_close((1/(5/math.sqrt(27))),3*math.sqrt(3)/5)
assert_close(b0/r0,2)

for k in range(2001):
    b=k/2000
    rr=b if b<=.5 else r0
    lower=f(b,rr)
    assert lower+2e-14>=25/27, (b, lower)
    checks+=1
    best=golden_max(lambda r:f(b,r))
    assert best+2e-13>=25/27,(b,best)
    checks+=1
    if abs(b-b0)>.03:
        assert best>25/27+1e-5
        checks+=1

rng=random.Random(260933242)
for k in range(10000):
    a=rng.random()*2*math.pi
    b=rng.random()*2*math.pi
    A=rng.random()*4
    B=rng.random()*4
    c=A*complex(math.cos(a),math.sin(a))
    d=B*complex(math.cos(b),math.sin(b))
    op=(A+math.sqrt(A*A+4*B*B))/2
    sample_radius=rng.random()*.999999
    # The complex phase-optimized kernel value equals the real positive profile.
    sampled=(1-sample_radius**2)*((A+B*sample_radius)**2+B**2)
    angle=cmath.phase(c)-cmath.phase(d)
    z=sample_radius*complex(math.cos(angle),math.sin(angle))
    measured=(1-sample_radius**2)*(abs(c+d*z)**2+B**2)
    assert_close(sampled,measured)
    tests=golden_max(lambda r:(1-r*r)*((A+B*r)**2+B*B))
    assert math.sqrt(tests)*3*math.sqrt(3)/5+1e-9>=op
    checks+=1

# Extremizing complex rotations have the same ratio.
for _ in range(1000):
    theta,phi=(rng.random()*2*math.pi for _ in range(2))
    c=complex(math.cos(theta),math.sin(theta))/3
    d=math.sqrt(2/3)*complex(math.cos(phi),math.sin(phi))
    radius=r0
    z=radius*cmath.exp(1j*(theta-phi))
    G2=(1-radius*radius)*(abs(c+d*z)**2+abs(d)**2)
    assert_close(G2,25/27)

print(f'PASS: {checks} finite checks (not a substitute for the proof)')
