#!/usr/bin/env python3
"""Independent numerical checks of Brownian span/local-time mixed moments.

Use only the Python standard library. Execute `python verify.py`.
The analytic proof, not numerical quadrature, establishes the theorem.
"""
import math

SQRT2 = math.sqrt(2.0)
PI = math.pi

def phi(x):
    return math.exp(-0.5*x*x) / math.sqrt(2.0*PI)

def Q(x):
    return 0.5 * math.erfc(x/SQRT2)

def f(t, a):
    x = a/math.sqrt(t)
    return 2.0*math.sqrt(t)*(phi(x)-x*Q(x))

def h(t, a):
    x = a/math.sqrt(t)
    return 2.0*t*((1.0+x*x)*Q(x)-x*phi(x))

def mixed(t, a):
    return a*f(t,a) + (5.0/6.0)*h(t,a) + (1.0/3.0)*h(t,2.0*a)

def cov(t, a):
    return mixed(t,a)-math.sqrt(8.0*t/PI)*f(t,a)

def simpson(fun, a, b, steps=4000):
    if steps%2: raise ValueError('steps must be even')
    width=(b-a)/steps
    val=fun(a)+fun(b)
    for j in range(1,steps): val += (4 if j%2 else 2)*fun(a+j*width)
    return val*width/3

# Independently compute the Brownian expected local time using its
# occupation-density heat kernel, and h by integrated first-passage tail.
count=0
for t in (0.4,1.0,1.75):
    for a in (0.0,0.15,0.7,1.6):
        # Transform s=u^2 to remove the s^-1/2 singularity at zero.
        quadf=simpson(lambda u:(2.0/math.sqrt(2*PI))*
                       (math.exp(-(a*a)/(2*u*u)) if u else (1.0 if a==0 else 0.0)),
                       0.0,math.sqrt(t),6000)
        assert abs(quadf-f(t,a))<1e-9,(t,a,'f',quadf,f(t,a))
        quadh=simpson(lambda u:4.0*u*Q(a/u) if u else 0.0,
                      0.0,math.sqrt(t),6000)
        assert abs(quadh-h(t,a))<1e-9,(t,a,'h',quadh,h(t,a))
        count+=2

# Independent time-Laplace quadrature of the explicit mixed moment, using
# exponentially weighted t integrals. Analytically this must be
# a exp(-k a)/(lambda k)+[5 exp(-k a)+2 exp(-2ka)]/(3 lambda k^2).
for lam in (0.7,1.5,3.0):
    k=math.sqrt(2.0*lam)
    for a in (0.0,0.3,1.0):
        # s=u^2 removes finite-time square-root onset. Tail beyond t=80/lam
        # is bounded far below double precision.
        Tmax=80.0/lam
        calc=simpson(lambda u: 2.0*u*math.exp(-lam*u*u)*mixed(u*u,a) if u else 0.0,
                     0.0,math.sqrt(Tmax),12000)
        expected=a*math.exp(-k*a)/(lam*k) + (5*math.exp(-k*a)+2*math.exp(-2*k*a))/(3*lam*k*k)
        assert abs(calc-expected)<5e-8, (lam,a,calc,expected)
        count+=1

# Covariance identities, Brownian scaling, spatial symmetry, and sign regimes.
assert abs(cov(1,0)-(7.0/6.0-4.0/PI))<1e-12; count+=1
for t in (0.4,1.0,1.75):
    assert cov(t,0)<0; count+=1
    for a in (math.sqrt(8*t/PI),2*math.sqrt(8*t/PI),3*math.sqrt(8*t/PI)):
        assert cov(t,a)>0; count+=1
    for z in (0.2,0.5,1.0,2.0):
        assert abs(cov(t,z*math.sqrt(t))/t-cov(1,z))<2e-14; count+=1
assert cov(1,0.5)<0 and cov(1,1)>0; count+=1

# Occupation conservation: integral of covariance over all levels is zero.
whole=2.0*simpson(lambda a:cov(1,a),0.0,9.0,18000)
assert abs(whole)<2e-7, whole
count+=1
print('PASS:',count,'independent quadrature / Laplace / scaling / sign / conservation checks')
