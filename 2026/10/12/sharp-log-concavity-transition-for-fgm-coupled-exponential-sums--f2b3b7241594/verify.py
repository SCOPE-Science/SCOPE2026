#!/usr/bin/env python3
"""Independent numerical and exact-arithmetic diagnostics for an FGM exponential-sum curvature theorem.

The all-parameter theorem relies on the accompanying analytic proof, not on these finite checks.
"""
from fractions import Fraction
import math


def coeff(t):
    v = math.exp(-t)
    B = t - 4 + 4 * (t + 1) * v
    Bp = 1 - 4 * t * v
    Bpp = 4 * (t - 1) * v
    L = 4 * t * (t + 1) * v - 2
    Q = -1 + 4 * (t*t - 3*t + 4) * v - 16 * v*v
    return B, Bp, Bpp, L, Q


def curvature_numerator(t, theta):
    B, Bp, Bpp, L, Q = coeff(t)
    A = t + theta * B
    Ap = 1 + theta * Bp
    App = theta * Bpp
    return A * App - Ap * Ap, -1 + theta * L + theta*theta*Q


def exact_polynomial_checks():
    count = 0
    # z is a formal placeholder for exp(-t); rational evaluation checks
    # the derivatives' polynomial identities at independent rational points.
    for i in range(1, 33):
        t = Fraction(i, 13)
        for j in range(1, 23):
            z = Fraction(j, 30)
            B = t - 4 + 4*(t+1)*z
            Bp = 1-4*t*z
            Bpp = 4*(t-1)*z
            L = 4*t*(t+1)*z-2
            Q = -1 + 4*(t*t-3*t+4)*z-16*z*z
            assert t*Bpp-2*Bp == L
            assert B*Bpp-Bp*Bp == Q
            for theta in (Fraction(-1), Fraction(-1,2), Fraction(0), Fraction(1,2),Fraction(1)):
                A = t+theta*B
                Ap = 1+theta*Bp
                App = theta*Bpp
                assert A*App-Ap*Ap == -1+L*theta+Q*theta*theta
                count += 1
    return count


def integrate_simpson(f, a, b, n=2000):
    h=(b-a)/n
    z=f(a)+f(b)
    for i in range(1,n):
        z += (4 if i%2 else 2)*f(a+i*h)
    return z*h/3


def independently_integrated_densities():
    count=0
    for theta in [-1,-0.5,0,0.5,1]:
        for t in [0.07,0.25,0.9,1.4,1.65,2.1,4.5,9.0]:
            observed=integrate_simpson(
                lambda u: math.exp(-t) * (1+theta*(2*math.exp(-u)-1)*(2*math.exp(-(t-u))-1)),
                0, t)
            B=coeff(t)[0]
            expected=math.exp(-t)*(t+theta*B)
            assert abs(observed-expected) <= 2e-10*max(1,expected), (theta,t,observed,expected)
            x,y=curvature_numerator(t,theta)
            assert abs(x-y)<2e-12*max(1,abs(x),abs(y)), (theta,t,x,y)
            count+=1
    return count


def threshold(t):
    _,_,_,L,Q=coeff(t)
    D=L*L+4*Q
    if L<=0 or D<0:
        return math.inf
    return 2/(L+math.sqrt(D))


def golden_min(f,a,b):
    invphi=(math.sqrt(5)-1)/2
    c=b-(b-a)*invphi;d=a+(b-a)*invphi
    for _ in range(200):
        if f(c)<f(d):
            b,d=d,c;c=b-(b-a)*invphi
        else:
            a,c=c,d;d=a+(b-a)*invphi
    return (a+b)/2


def diagnostics():
    # Exact rational bounds show the violation at t=log 4 and theta=1.
    s=sum((Fraction(1,k*2**k) for k in range(1,7)),Fraction())
    assert s==Fraction(1327,1920) and s>Fraction(11,16)
    assert Fraction(3)<Fraction(7,4)**2
    t4=math.log(4)
    f4=2*t4*t4-2*t4-1
    x,y=curvature_numerator(t4,1)
    assert f4>0 and abs(x-f4)<1e-12 and abs(y-f4)<1e-12
    # The following optimization and grid tests are diagnostics, not certificates
    # for the continuous infimum.
    t0=golden_min(threshold,1.4,1.95)
    r0=threshold(t0)
    assert 1.63<t0<1.66 and .859<r0<.862
    for i in range(1,3001):
        t=.001+i*.006
        _,_,_,L,Q=coeff(t)
        assert L<2
        if t>1:
            assert Q<0
        if t<1:
            for theta in [-1,-.9,-.5,-.1,0,.1,.5,1]:
                assert curvature_numerator(t,theta)[0]<1e-9
        for theta in [-1,-.5,0,.5,.75]:
            assert curvature_numerator(t,theta)[0]<1e-8
    # Both sides of the numerical threshold give the expected local signs.
    assert curvature_numerator(t0, .84)[0]<0
    assert curvature_numerator(t0, .88)[0]>0
    return t0,r0,f4


if __name__=='__main__':
    n=exact_polynomial_checks()
    m=independently_integrated_densities()
    t0,th,f4=diagnostics()
    print('PASS: %d exact-rational polynomial-identity evaluations' % n)
    print('PASS: %d independently integrated density/curvature diagnostics' % m)
    print('PASS: rational logarithm/square-root counterexample inequalities')
    print('NUMERICAL ONLY: threshold ~ %.12f at t ~ %.12f' % (th,t0))
    print('NUMERICAL ONLY: numerator at theta=1, t=log4 ~ %.12f' % f4)
    print('All-parameter validity follows from the written proof, not the finite tests.')
