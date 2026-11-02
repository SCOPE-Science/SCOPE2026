#!/usr/bin/env python3
"""Deterministic finite checks for athermal integrated-OU extreme-hitting laws.
These checks are not proofs of asymptotic claims.
"""
import math

checks = 0

def close(a, b, tol=1e-8):
    global checks
    checks += 1
    assert abs(a-b) <= tol * max(1.0, abs(a), abs(b)), (a, b, tol)

def yes(x):
    global checks
    checks += 1
    assert x

def a_fn(g, t):
    return -math.expm1(-g*t)/g

def q(g, d, u, t):
    # stable positive quadrature formula also for small t
    K = 300
    h = t/K
    s = a_fn(g, 0.0)**2 + a_fn(g, t)**2
    for k in range(1, K):
        s += (4 if k % 2 else 2) * a_fn(g, k*h)**2
    return u*a_fn(g,t)**2 + (2*d)*h*s/3

def q_closed(g, d, u, t):
    z = -math.expm1(-g*t)
    return u*(z/g)**2 +(2*d/g**2)*(t-2*z/g +(1-math.exp(-2*g*t))/(2*g))

def q_simpson(g,d,u,t,K=3000):
    h=t/K
    s=0.0
    for k in range(K+1):
        a=a_fn(g,k*h)
        s += (1 if k in (0,K) else (4 if k%2 else 2))*a*a
    return u*a_fn(g,t)**2+2*d*h*s/3

def find_t(g,d,u,N):
    target=1/(2*math.log(N)) # ell=1
    lo,hi=0.0,1.0
    while q(g,d,u,hi)<target:
        hi*=2
    for _ in range(70):
        md=(lo+hi)/2
        if q(g,d,u,md)<target:lo=md
        else:hi=md
    return (lo+hi)/2

# Closed-form variance and independent Simpson quadrature cross-check
for g in (0.2,1.0,2.5):
    for d in (0.15,1.0,3.0):
        for u in (0.,0.01,0.5,7.0):
            for t in (0.12,0.3,1.0,2.0,4.0):
                close(q(g,d,u,t),q_simpson(g,d,u,t),2e-8)
                close(q_closed(g,d,u,t),q_simpson(g,d,u,t),2e-8)
                yes(q(g,d,u,t)>0)

# Short-time variance expansion and a uniform upper bound on the expected supremum
for g in (0.3,1.,3.):
    for d in (0.1,1.,5.):
        for u in (0.,0.001,0.02,1.,100.):
            for t in (0.001/g,0.02/g,0.1/g,0.4/g,1./g):
                v=q(g,d,u,t)
                m_bound=math.sqrt(2/math.pi)*(t*math.sqrt(u)+(2./3.)*math.sqrt(2*d)*t**1.5)
                yes(m_bound<=2*math.sqrt(v)*(1+1e-8))
                approx=u*t*t+(2*d/3)*t**3
                yes(v<=approx*(1+1e-8))
                yes(v>0)

# For ever-decreasing velocity variances, verify limiting critical interpolation.
# Numerical finite-N tests use moderate 1/log N asymptotics, so tolerance is moderate.
for Dv in (0.2,1.0,3.0):
    for b in (0.,0.2,1.,4.):
        # Solve unique b*s^2 + (2Dv/3)s^3 = 1/2
        lo,hi=0.,10.
        for _ in range(90):
            s=(lo+hi)/2
            if b*s*s+(2*Dv/3)*s**3<0.5:lo=s
            else:hi=s
        s=(lo+hi)/2
        for lam in (80.,500.,5000.):
            # create synthetic logarithm via direct Gaussian threshold rather than huge N
            velocity=b*lam**(-1/3)
            # q_N(t)=1/(2*lam), bisection directly
            lo,hi=0.,2.
            for _ in range(70):
                mid=(lo+hi)/2
                if q(1.,Dv,velocity,mid)<1/(2*lam):lo=mid
                else:hi=mid
            root=(lo+hi)/2
            yes(abs(root*lam**(1/3)-s)<0.2*s)

yes(math.sqrt(14/(3*math.pi))/(1-math.exp(-1)) < 2)
print('PASS: '+str(checks)+' deterministic checks')
