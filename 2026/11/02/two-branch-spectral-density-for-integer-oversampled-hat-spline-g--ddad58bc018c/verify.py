"""Reproducible finite checks for the hat-spline Gabor spectral formula.

Run with: python3 verify.py
Only standard-library modules are used. Finite checks are not substitutes
for the arguments establishing identities for all integer redundancies.
"""
from fractions import Fraction as F
from math import sqrt, asin, pi, sin, cos, isclose

checks = 0

def check(cond, desc):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(desc)

def hat(x):
    return max(F(0), F(1) - abs(x))

def a0(q, x):
    return sum((hat(x-F(k,q))**2 for k in range(-q-1, q+2)), F(0))

def a1(q, x):
    return sum((hat(x-F(k,q))*hat(x-F(k,q)-1) for k in range(-q-1, q+2)), F(0))

def d0(q):
    return F(q*q-1, 3*q)

def formula_a0(q, x):
    return F(2*q,3) + F(1,3*q)-2*q*x*(F(1,q)-x)

def rho(q, lam):
    A = (q*q-1)/(3*q)
    end = A + 1/q
    if lam <= A or lam >= q:
        return 0.0
    if lam <= end:
        return sqrt(q)/(2*sqrt(q-lam))
    return sqrt(q)/(pi*sqrt(q-lam))*asin(min(1.0,1/sqrt(q*(lam-A))))

def simpson(fun, a, b, n=8000):
    assert n % 2 == 0
    h=(b-a)/n
    total=fun(a)+fun(b)
    for j in range(1,n):
        total += (4 if j&1 else 2)*fun(a+j*h)
    return total*h/3

# All overlaps and their quadratic identity are checked in exact rational arithmetic.
for q in range(1,21):
    A=d0(q)
    for j in range(25):
        x=F(j,24*q)
        p0=a0(q,x); p1=a1(q,x)
        check(p0==formula_a0(q,x), f'A0, q={q}, j={j}')
        check(p0+2*p1==q, f'partition, q={q}, j={j}')
        d=F(q)-p0
        check(d==A+2*q*x*(F(1,q)-x), f'D, q={q}, j={j}')
        for theta in [0.0, pi/3, pi/2, pi, 2*pi/3]:
            direct=float(p0)+2*float(p1)*cos(theta)
            symbol=q-float(d)*(1-cos(theta))
            check(abs(direct-symbol)<1e-11, f'symbol q={q}')
    check(formula_a0(q,F(1,2*q))== F(2*q,3)-F(1,6*q), f'min-A0 q={q}')
    check(q-2*(q-formula_a0(q,F(1,2*q)))==A, f'spectral lower q={q}')

# Integrate the exact density after the square-root endpoint substitution
# lambda=q-t*t.  This cancels the integrable singularity at the upper edge.
for q in [2,3,4,5,8,16,32]:
    A=(q*q-1)/(3*q)
    threshold=A+1/q
    t0=sqrt(q-threshold)
    t1=sqrt(q-A)
    def integral_for_power(power):
        # The substitution t=t0(1-u*u) regularizes the interior
        # square-root shoulder of the two-branch density.
        def high(u):
            t=t0*(1-u*u)
            lam=q-t*t
            f=2*sqrt(q)/pi*asin(min(1.0,1/sqrt(q*(lam-A))))
            return lam**power*f*2*t0*u
        def low(t):
            return (q-t*t)**power*sqrt(q)
        return simpson(high,0,1)+simpson(low,t0,t1)
    check(abs(integral_for_power(0)-1)<2e-9, f'density mass q={q}')
    check(abs(integral_for_power(1)-2*q/3)<2e-9*max(q,1),f'mean q={q}')
    check(abs(integral_for_power(2)-(q*q/2+1/(30*q*q)))<3e-9*q*q,f'second moment q={q}')
    check(abs(rho(q, threshold-1e-8)-rho(q,threshold+1e-8))<1e-3,
          f'continuity at spectral shoulder q={q}')

print(f'PASS: {checks} exact/algebraic and numerical checks')
