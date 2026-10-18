"""Numerical checks for a sinusoidally forced piecewise scalar cycle.
Run: python3 quadrature_verify.py. Uses only the Python standard library.
Analytic statements in RESULT.md are not replaced by these finite checks.
"""
import math

def simpson(f, left, right, n=2000):
    h=(right-left)/n
    value=f(left)+f(right)
    for j in range(1,n):
        value+=(4 if j%2 else 2)*f(left+j*h)
    return h*value/3

def H(a,t):
    return simpson(lambda s: math.sin(s)*math.exp(-a*math.sin(s)), t,math.pi)-simpson(lambda s: math.sin(s)*math.exp(a*math.sin(s)), 0,t)

def theta(a):
    low,high=0.,math.pi
    for _ in range(51):
        mid=(low+high)/2
        if H(a,mid)>0:
            low=mid
        else:
            high=mid
    return (low+high)/2

def positive_arc(a,t,th):
    return math.exp(a*math.sin(t))*simpson(lambda s:math.sin(s)*math.exp(-a*math.sin(s)),th,t)

def c_root():
    lo,hi=1.,2.
    for _ in range(55):
        c=(lo+hi)/2
        if c*math.tanh(c)<1: lo=c
        else:hi=c
    return (lo+hi)/2

c=c_root()
assert abs(c-1.1996786402577338)<1e-14
assert abs(H(4.,.31)-.01167831680615195)<2e-9
for a in (.1,1.,4.,12.,40.):
    th=theta(a)
    assert abs(H(a,th)) < 1e-9
    assert positive_arc(a,(th+math.pi)/2,th)>0
    assert abs(positive_arc(a,th+math.pi,th))<2e-8
    multiplier=math.exp(-4*a*math.sin(th))
    assert 0 < multiplier < 1
    print('a=',a,' crossing=',f'{th:.14f}',' multiplier=',f'{multiplier:.14f}')
for a in (.05,.025):
    th=theta(a)
    assert abs(th-(math.pi/2-math.pi*a/4)) < a**3
for a in (20.,40.,80.):
    th=theta(a)
    assert abs(a*th-c)<2/a**2
assert math.exp(-16*math.sin(theta(4.)))<math.exp(-4*c)
print('CHECK_OK: finite evaluations passed; the global theorem relies on proof, not sampling')
