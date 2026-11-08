"""Reproduce algebraic and finite-sample consequences of the three-ring theorem.
Analytical classification in RESULT.md is required for the universal assertion.
"""
import math
import cmath
import random
import sympy as sp

x,y,z = sp.symbols('x y z', positive=True)
s1=x+y+z
s2=x*y+x*z+y*z
s3=x*y*z
assert sp.expand(s3*s1-y*y*s2 - y*(x+z)*(x*z-y*y)) == 0
T=sp.symbols('T')
assert sp.expand((x-T)*(y-T)*(z-T) - (s3-s2*T+s1*T*T-T**3)) == 0

rng=random.Random(1592)
checks=0

def polynomials(radii, sign=1, C=1):
    t0,t1,t2=[r*r for r in radii]
    S1=t0+t1+t2
    S2=t0*t1+t0*t2+t1*t2
    S3=t0*t1*t2
    amp=math.sqrt(C)
    return (lambda w: amp*(1j*sign*math.sqrt(S3)+math.sqrt(S1)*w*w),
            lambda w: amp*(1j*sign*math.sqrt(S2)*w+w**3))

def grid(radii,delta):
    for j,r in enumerate(radii):
        ph=delta if j==1 else 0.0
        for k in range(4):
            yield r*cmath.exp(1j*(ph+k*math.pi/2))

for radii in [(1,2,4),(1.5,3,6),(0.5,2,8),(2,3,4.5)]:
    t0,t1,t2=[r*r for r in radii]
    S1=t0+t1+t2
    S2=t0*t1+t0*t2+t1*t2
    S3=t0*t1*t2
    for angle in [0.1,math.pi/8,math.pi/6,0.413,math.pi/4,-.257]:
        f,g=polynomials(radii)
        measurements=[abs(f(w))**2-abs(g(w))**2 for w in grid(radii,angle)]
        pred=16*t1*t1*math.sin(2*angle)**2*(math.sqrt(S3*S1)-t1*math.sqrt(S2))**2
        actual=sum(u*u for u in measurements)
        assert abs(actual-pred) <= 1e-8*(1+abs(pred)), (radii,angle,actual,pred)
        checks+=1
        for j in [0,2]:
            assert max(abs(u) for u in measurements[4*j:4*j+4])<=1e-9
            checks+=1
        if math.isclose(radii[1]*radii[1], radii[0]*radii[2],rel_tol=1e-12):
            assert max(abs(u) for u in measurements)<1e-8
            checks+=1
        else:
            assert actual>1e-8
            checks+=1

for _ in range(80):
    r0=math.exp(rng.uniform(-2,1))
    r2=r0*math.exp(rng.uniform(.2,3))
    r1=math.sqrt(r0*r2)
    angle=rng.uniform(-1.2,1.2)
    s=rng.choice([-1,1])
    C=math.exp(rng.uniform(-2,2))
    f,g=polynomials((r0,r1,r2),s,C)
    for w in grid((r0,r1,r2),angle):
        a=abs(f(w))**2
        b=abs(g(w))**2
        assert abs(a-b)<=5e-11*(1+a+b)
        checks+=1

print('THREE_RING_RESONANCE_CHECKS_PASSED',checks)
