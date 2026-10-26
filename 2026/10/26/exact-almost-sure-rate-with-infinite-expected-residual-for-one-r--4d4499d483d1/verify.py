"""Reproducible symbolic and numerical checks for a redrawn one-row residual sketch."""
import math
import random
import sympy as sp

checks = 0

def ok(test):
    global checks
    assert bool(test)
    checks += 1

# Symbolic residual identity for a diagonal matrix.
a,b,u,v,X,Y=sp.symbols('a b u v X Y',real=True)
d=a*X*u+b*Y*v
alpha=(X*u+Y*v)/d
r1=sp.cancel(u*(1-a*alpha))
r2=sp.cancel(v*(1-b*alpha))
ok(sp.simplify(r1-(b-a)*u*v*Y/d)==0)
ok(sp.simplify(r2+(b-a)*u*v*X/d)==0)
ok(sp.cancel(X*r1+Y*r2)==0)
ok(sp.cancel(r1/r2+Y/X)==0)

# Numerical check of the logarithmic angular integral, including indefinite cases.
def step_angle_rate(l1,l2,nsamples,seed):
    rng=random.Random(seed)
    theta=0.37
    sum_log=0.0
    for j in range(nsamples):
        phi=2*math.pi*rng.random()
        den=l1*math.cos(phi)*math.cos(theta)+l2*math.sin(phi)*math.sin(theta)
        fac=abs((l2-l1)*math.cos(theta)*math.sin(theta)/den)
        assert fac>0 and math.isfinite(fac)
        sum_log+=math.log(fac)
        theta=phi-math.pi/2
    return sum_log/nsamples

for l1,l2,seed in ((1.0,3.0,101),(-2.0,-5.0,102),(-1.0,3.0,103),(0.5,12.0,104)):
    measured=step_angle_rate(l1,l2,150000,seed)
    target=math.log(abs(l2-l1)/(abs(l1)+abs(l2)))
    print('spectra',l1,l2,'measured',measured,'target',target)
    ok(abs(measured-target)<0.025)

# Deterministic angular quadrature of the elementary logarithmic integrals.
for l1,l2 in ((1.0,3.0),(-2.0,5.0)):
    m=65536
    mean_cos_sin=0.0
    mean_anorm=0.0
    mean_projection=0.0
    for j in range(m):
        t=(j+0.3712)*2*math.pi/m
        mean_cos_sin+=math.log(abs(math.cos(t)*math.sin(t)))
        mean_anorm+=.5*math.log(l1*l1*math.cos(t)**2+l2*l2*math.sin(t)**2)
        mean_projection+=math.log(abs(l1*math.cos(t)*math.cos(.23)+l2*math.sin(t)*math.sin(.23)))
    mean_cos_sin/=m
    mean_anorm/=m
    mean_projection/=m
    ok(abs(mean_cos_sin+2*math.log(2))<0.001)
    ok(abs(mean_anorm-math.log((abs(l1)+abs(l2))/2))<0.001)
    ok(abs(mean_projection-(.5*math.log(l1*l1*math.cos(.23)**2+l2*l2*math.sin(.23)**2)-math.log(2)))<0.001)

# Exact heavy-tail witnesses: sketches approach orthogonality to A r.
for l1,l2 in ((sp.Rational(1),sp.Rational(3)),(sp.Rational(-1),sp.Rational(3))):
    rr=sp.Matrix([sp.Rational(2),sp.Rational(1)])
    Ar=sp.diag(l1,l2)*rr
    sperp=sp.Matrix([-Ar[1],Ar[0]])
    for k in (3,4,5):
        h=sp.Rational(1,10**k)
        s=sperp+h*Ar
        al=(s.dot(rr))/(s.dot(Ar))
        rn=rr-al*Ar
        ok(s.dot(rn)==0)
        # A nonzero orthogonal limit has nonzero numerator and amplitude grows as 1/h.
        ok(abs(rn[0])>sp.Rational(10**k,100))

print('PASS: checks=',checks)
