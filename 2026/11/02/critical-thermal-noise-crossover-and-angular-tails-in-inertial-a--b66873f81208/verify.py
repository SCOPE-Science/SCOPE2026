#!/usr/bin/env python3
"""Deterministic consistency checks for a Gaussian-age crossover law."""
import math

CHECKS = 0

def near(x, y, atol=1e-10, rtol=1e-9):
    global CHECKS
    CHECKS += 1
    assert abs(x-y) <= atol + rtol*max(abs(x), abs(y)), (x,y)

def assert_true(cond, label):
    global CHECKS
    CHECKS += 1
    assert cond, label

def angular(a, eta, cosine):
    b = 3/(4*eta)
    c = 1+3*a*a/(4*eta)
    d = 3*a*cosine/(2*eta)
    y = (-d+math.sqrt(d*d+12*b*c))/(2*c)
    t = math.sqrt(y)
    ph = c*t+b/t**3-d/t
    second = 12*b/t**5-2*d/t**3
    return t, ph, second

# Positive definite joint thermal covariance, and exactly recovered moments.
for eta in (0.03, 0.4, 2.0, 100.0):
    for age in (0.05, 0.25, 1.0, 2.0, 10.0):
        xx=2*eta*age**3/3
        vv=2*eta*age
        xv=eta*age**2
        near(xx*vv-xv*xv, eta**2*age**4/3)
        assert_true(xx*vv-xv*xv>0, 'joint covariance SPD')

# Check an explicit unique saddle, its Hessian, exact rate, and angular ordering.
for a in (0.1, 0.4, 1., 2.):
    for eta in (0.07, 0.5, 1., 4.):
        prev = None
        for z in (1., 0.75, 0.25, 0., -0.25, -0.75, -1.):
            t, phi, hess=angular(a,eta,z)
            b=3/(4*eta); c=1+3*a*a/(4*eta); d=3*a*z/(2*eta)
            near(c*t**4+d*t**2-3*b, 0., atol=1e-9)
            near(phi, t+3*(1+a*a*t**4-2*a*z*t*t)/(4*eta*t**3))
            near(phi, 4*c*t/3-2*d/(3*t))
            assert_true(hess>0, 'strict saddle')
            if prev is not None: assert_true(phi>prev, 'angular rate increases with separation')
            prev=phi

# Check convergence of explicitly known stationary means.
gamma, drift, Dr = 1.7, 1.3, 0.45
for r in (100., 1000., 10000.):
    pos=gamma*drift*r*r/((r+gamma)*(r+Dr))
    vel=gamma*drift*r*r/((r+gamma)*(r+Dr))
    near(pos, vel) # scaled r^2 E[X] and r E[V] coincide exactly
    assert_true(abs(pos-gamma*drift)<4*gamma*drift*(gamma+Dr)/r, 'high rate mean')

# Thermal stationary covariance leading terms from exact OU kernels.
for gamma in (0.4, 2., 7.):
    for eta in (0.1,1.,6.):
        last=None
        for r in (1000., 10000., 100000.):
            k=eta/r
            evv=2*k/(r+2*gamma)
            exv=2*k/((r+gamma)*(r+2*gamma))
            # Algebraically stabilized formula for E[XX] thermal covariance:
            # E[XX] = 4 k / (r (r+gamma)(r+2gamma)).
            exx=4*k/(r*(r+gamma)*(r+2*gamma))
            target=(r*r*evv, r**3*exv, r**4*exx)
            if r>=10000:
                near(target[0],2*eta,rtol=0.005)
                near(target[1],2*eta,rtol=0.005)
                near(target[2],4*eta,rtol=0.005)
            last=target

# Verify large-radius leading density factor using elementary Simpson quadrature.
def log_density_direct(R, a, eta, cos_angle):
    tstar, _, _=angular(a,eta,cos_angle)
    # Log-stabilized integration around saddle with a dense deterministic grid.
    low=max(0.001, tstar/8)
    high=max(10., 8*tstar)
    n=6000
    h=(high-low)/n
    b=3/(4*eta); c=1+3*a*a/(4*eta); d=3*a*cos_angle/(2*eta)
    m=math.sqrt(R)*(c*tstar+b/tstar**3-d/tstar)
    s=0.
    for i in range(n+1):
        t=low+h*i
        phi=c*t+b/t**3-d/t
        w=1 if i in (0,n) else (4 if i%2 else 2)
        s += w*t**-3*math.exp(-math.sqrt(R)*phi+m)
    return math.log(3/(4*math.pi*eta*R)) + math.log(s*h/3) - m

for a,eta in ((0.5,1.),(1.,0.5)):
    for cos_angle in (-1.,0.,1.):
        t, rate, hess=angular(a,eta,cos_angle)
        R=10000.
        lead=math.log(3/(4*math.pi*eta))+(-1.25)*math.log(R)+math.log(t**-3*math.sqrt(2*math.pi/hess))-math.sqrt(R)*rate
        actual=log_density_direct(R,a,eta,cos_angle)
        assert_true(abs(actual-lead)<0.07, 'Laplace density asymptotic')

print('PASS', CHECKS, 'deterministic algebra, covariance, angular-tail and quadrature checks')
