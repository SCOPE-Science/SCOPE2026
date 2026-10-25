#!/usr/bin/env python3
"""Numerical and exact-radical consistency checks for rectangular radial mean bodies.

This is a finite cross-check, not an exhaustive proof over real parameters.
Requires only the Python standard library.
"""
from decimal import Decimal, getcontext
from math import cos, sin, hypot, pi, exp, log, log1p, expm1, sqrt


def phi(s, t, p, q):
    if p == 0:
        factor = exp(-1-q/2)
    else:
        factor = exp((-log1p(p) + log1p(-p*q/(p+2)))/p)
    return 2*hypot(s,t*q)*factor


def radius(a, b, p, theta):
    c, s = abs(cos(theta)), abs(sin(theta))
    h1, h2 = c/(2*a), s/(2*b)
    if h1 >= h2:
        return phi(a,b,p,h2/h1)
    return phi(b,a,p,h1/h2)


def q_in(p, A):
    return (p+2-sqrt((p+2)**2-4*(p+1)/A**2))/(2*(p+1))


def elasticity(p, q):
    w = 1-p*q/(p+2)
    alpha = 2/p
    return alpha*(1-w)/(w*(-expm1(alpha*log(w))))


def q_star(p):
    low, high = 1e-9, 1.0
    assert elasticity(p,low)<2<elasticity(p,high)
    for _ in range(90):
        mid=(low+high)/2
        if elasticity(p,mid)<2: low=mid
        else: high=mid
    return (low+high)/2


def transition(p):
    q=q_star(p)
    w=1-p*q/(p+2)
    return q, sqrt(q*q/expm1(-2/p*log(w)))


def predicted(a,b,p):
    A=a/b
    r_min=phi(b,a,p,q_in(p,A))
    r_axis=phi(a,b,p,0)
    if p<=2:
        return r_min,r_axis,None
    q_c,A_c=transition(p)
    if A>A_c: return r_min,r_axis,None
    if abs(A-A_c)<1e-13: return r_min,r_axis,q_c
    root=(p+2+sqrt((p+2)**2-4*(p+1)*A**2))/(2*(p+1))
    return r_min,phi(a,b,p,root),root


def direct_moment(a,b,p,theta,n=16000):
    """Independent midpoint quadrature of the exit-distance density.

    For p<0 a power substitution regularizes the endpoint.
    """
    h1,h2=abs(cos(theta))/(2*a),abs(sin(theta))/(2*b)
    T=1/max(h1,h2)
    if p < 0:
        # Substitute t=T*v^(1/(p+1)) to eliminate t^p at zero.
        alpha=1/(p+1)
        total=0.0
        for i in range(n):
            v=(i+.5)/n
            t=T*v**alpha
            total+=(h1+h2-2*h1*h2*t)
        moment=T**(p+1)*total/((p+1)*n)
        return moment**(1/p)
    if p == 0:
        # Substitute t=T*v^2 to smooth the integrable logarithm.
        total=0.0
        for i in range(n):
            v=(i+.5)/n
            t=T*v*v
            total+=2*T*v*(h1+h2-2*h1*h2*t)*log(t)
        return exp(total/n)
    total=0.0
    for i in range(n):
        t=T*(i+.5)/n
        total+=t**p*(h1+h2-2*h1*h2*t)
    return (T*total/n)**(1/p)


# Verify the quartic transition using 60-digit radical arithmetic.
getcontext().prec=60
z=(1+Decimal(17).sqrt())/8
q4=(69-3*Decimal(17).sqrt())/64
A2=(Decimal(963)+459*Decimal(17).sqrt())/2048
assert abs(z*z-(1-Decimal(2)*q4/3)) < Decimal('1e-55')
assert abs(Decimal(9)/4*z*(1-z)*(1+z)**2-A2) < Decimal('1e-55')
assert abs(float(A2.sqrt())-transition(4)[1]) < 1e-12

# Explore a wide range of moment parameters and rectangle eccentricities.
for p in [-0.8,-0.2,0.0,0.4,1.0,2.0,2.1,3.0,4.0,8.0,20.0]:
    if p>2:
        qc,Ac=transition(p)
        assert 0<qc<1<Ac
        eccentricities=[1.0001,1.02,Ac*.98,Ac,Ac*1.02,3.2]
    else:
        eccentricities=[1.0001,1.02,1.2,2.0,3.2]
    for A in eccentricities:
        if A<=1:continue
        low,high,max_q=predicted(A,1,p)
        values=[radius(A,1,p,pi*i/(2*8000)) for i in range(8001)]
        assert abs(low-min(values))<4e-6,(p,A,'min',low,min(values))
        assert abs(high-max(values))<4e-6,(p,A,'max',high,max(values))
        for theta in [0.18,0.46,0.91,1.33]:
            check=direct_moment(A,1,p,theta,8000)
            expected=radius(A,1,p,theta)
            assert abs(check-expected)/expected < 3e-4,(p,A,theta,check,expected)

print('RADIAL_RECTANGLE_CHECKS_OK')
