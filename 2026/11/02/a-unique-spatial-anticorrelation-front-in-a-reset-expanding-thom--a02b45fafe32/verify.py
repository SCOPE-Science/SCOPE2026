#!/usr/bin/env python3
"""Independent quadrature tests of reset-age density covariance and its unique sign boundary.

Uses only the stated self-similar hydrodynamic expansion and the resetting law.
These finite checks support, but do not prove, the unbounded-domain statements.
"""
import math
from scipy.integrate import quad
from scipy.optimize import brentq

CHECKS = 0

def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)

def F(u):
    # F(lambda) for lambda=1+u*u in dimensionless units.
    return u * math.sqrt(1.0 + u*u) + math.asinh(u)

def moments(alpha, z):
    """Moments of U=1/lambda and B_z=U*(1-z*z*U*U)_+.

    Substitute lambda=1+u^2 to remove the square-root density singularity.
    """
    def kernel(u):
        lam = 1.0 + u*u
        return 2.0*alpha*math.sqrt(lam)*math.exp(-alpha*F(u))
    def integrate(fn, lo=0):
        return quad(lambda u: kernel(u)*fn(1.0+u*u), lo, math.inf,
                    epsabs=8e-12, epsrel=8e-11, limit=400)[0]
    m1 = integrate(lambda x: 1/x)
    m2 = integrate(lambda x: 1/x**2)
    m3 = integrate(lambda x: 1/x**3)
    m4 = integrate(lambda x: 1/x**4)
    lo = math.sqrt(max(0.0, z-1.0))
    b = integrate(lambda x: 1/x-z*z/x**3, lo)
    ab = integrate(lambda x: 1/x**2-z*z/x**4, lo)
    return m1, m2, m3, m4, b, ab

def contrast(alpha, z):
    m1,_,_,_,b,ab = moments(alpha,z)
    return ab/b-m1

def root(alpha):
    return brentq(lambda z: contrast(alpha,z), 0.0, max(4.0, 2.0/alpha), xtol=1e-8)

def dimensionless_lambda_at(s):
    # Independent inversion of the deterministic expansion clock F(lambda)=s.
    if s == 0: return 1.0
    u=brentq(lambda u:F(u)-s, 0, max(2.0, math.sqrt(s)+3))
    return 1+u*u

def moment_from_age(alpha,k):
    # Reset age density alpha * exp(-alpha*s), s= sqrt(2) omega t.
    def integrate(w):
        s=w/alpha
        lam=dimensionless_lambda_at(s)
        return math.exp(-w)/lam**k
    return quad(integrate,0,32,epsabs=1e-9,epsrel=1e-9,limit=150)[0]

for alpha in [0.08,0.2,0.5,1.0,3.0,10.0]:
    m1,m2,m3,m4,_,_=moments(alpha,0)
    # The u-variable density has total integral one.
    norm=quad(lambda u:2*alpha*math.sqrt(1+u*u)*math.exp(-alpha*F(u)),
              0,math.inf,epsabs=1e-11,epsrel=1e-10)[0]
    check(abs(norm-1)<2e-9,('normalization',alpha,norm))
    for k,mi in enumerate([m1,m2,m3,m4],start=1):
        other=moment_from_age(alpha,k)
        check(abs(mi-other)<1.2e-7,('independent clock',alpha,k,mi,other))
    check(m2>m1*m1,('nonzero variance',alpha))
    check(m4>m1*m3,('positive covariance',alpha))
    y=root(alpha)
    check(abs(contrast(alpha,y))<5e-8,('root residual',alpha,y))
    check(contrast(alpha,0)>0,('positive center',alpha))
    check(contrast(alpha,y*1.05)<0,('negative exterior',alpha))
    check(contrast(alpha,y*.95)>0,('positive interior',alpha))
    zs=[i*y/25 for i in range(1,64)]
    cs=[contrast(alpha,z) for z in zs]
    for v,w in zip(cs,cs[1:]):
        check(w<v,('strict monotonicity',alpha))
    if y<1:
        yc=math.sqrt((m2-m1*m1)/(m4-m1*m3))
        check(abs(y-yc)<1e-7,('core closed formula',alpha,y,yc))

for alpha in [5,10,30]:
    y=root(alpha)
    check(abs(y-1/math.sqrt(3))<1.0/alpha,('fast clock asymptotic',alpha,y))
for alpha in [0.01,0.001,0.0001]:
    y=root(alpha)
    check(y>1,('weak clock outside initial support',alpha,y))
    check(y>root(alpha*10),('weak clock outward trend',alpha,y))
    L=math.log(1/alpha)
    approx=2/(3*alpha*L*math.log(L))
    check(.3<y/approx<1.1,('weak clock double log scale',alpha,y,approx))

print('PASS',CHECKS,'deterministic quadrature and sign-boundary checks')
