"""Independent deterministic numerical checks for a two-Gaussian concentration phase boundary.
The proof of the theorem is analytic; finite tests do not certify all parameters.
Standard Python 3 only.
"""
from math import pi, exp, sqrt, log, tanh, cosh, gamma, factorial, isclose


def logcosh(t):
    u = abs(t)
    return u - log(2.0) + log(1.0 + exp(-2.0 * u))


def g(a, x):
    return logcosh(2 * a * x) - x*x


def mode_x(a):
    assert 2*a*a > 1
    lo, hi = 1.e-8, a
    for j in range(80):
        md = (lo+hi)/2
        if a*tanh(2*a*md)-md > 0: lo=md
        else: hi=md
    return (lo+hi)/2


def endpoint(a):
    xstar = mode_x(a)
    lo, hi = xstar, 2*a+2
    assert g(a,lo)>0 and g(a,hi)<0
    for j in range(95):
        md=(lo+hi)/2
        if g(a,md)>0: lo=md
        else: hi=md
    return (lo+hi)/2


def simpson(f, end, n=16000):
    assert n%2==0
    h=end/n
    s=f(0)+f(end)
    for j in range(1,n):
        s+=(4 if j%2 else 2)*f(j*h)
    return s*h/3


def normalized_critical_volume(q, a):
    if 2*a*a<=1: return 0.0
    r=endpoint(a)
    m=2*q
    vol_ball_transverse=pi**((m-1)/2)/gamma((m+1)/2)
    integral=simpson(lambda x: max(g(a,x),0.0)**((m-1)/2),r)
    return 2*vol_ball_transverse*integral/pi**q


def prefactor(q):
    return 3**q*gamma(q)/(sqrt(pi)*gamma(2*q+.5))

checks=0
for q in (1,2,3):
    assert normalized_critical_volume(q, .5)==0; checks+=1
    prev=0
    for a in (0.75,0.82,1.0,1.4,2.0,4.0):
        volume=normalized_critical_volume(q,a)
        assert volume > prev; checks+=1
        prev=volume
    for mu in (0.003,0.0015):
        a=sqrt((1+mu)/2)
        ratio=normalized_critical_volume(q,a)/(prefactor(q)*mu**(2*q-.5))
        assert abs(ratio-1)<.02, (q,mu,ratio)
        checks+=1
    large=normalized_critical_volume(q,8.0)/(2*8.0**(2*q)/factorial(q))
    assert abs(large-1)<.035,(q,large);checks+=1
for a in (.75,1.0,2.0,4.0):
    x=mode_x(a)
    end=endpoint(a)
    assert 0<x<end<2*a+2;checks+=1
    assert abs(a*tanh(2*a*x)-x)<1e-10;checks+=1
    assert abs(g(a,end))<1e-10;checks+=1
assert isclose(prefactor(1),4/pi,rel_tol=1e-12);checks+=1
assert isclose(prefactor(2),48/(35*pi),rel_tol=1e-12);checks+=1
print(f'PASS {checks} deterministic checks; analytic arguments are required for continuum claims')
