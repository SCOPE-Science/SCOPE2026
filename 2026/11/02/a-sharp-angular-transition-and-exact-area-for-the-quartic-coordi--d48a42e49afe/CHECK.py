"""Independent numerical checks of explicitly stated finite formulas.

This script does not establish the analytic assertions for a continuum.
"""
from math import sin, cos, sqrt, pi, log
from scipy.optimize import minimize_scalar
from scipy.integrate import quad


def ellipse_axes(s):
    return sqrt(s)/(2-s), sqrt(s*(1-s))/(2-s)


def predicted_support(angle):
    q=sin(angle)**2
    if q <= 0.75:
        return abs(cos(angle))
    return 1/sqrt(8*(2*q-1))


def direct_support(angle):
    q=sin(angle)**2
    f=lambda s: -(sqrt(s*(1-s*q))/(2-s))
    res=minimize_scalar(f,bounds=(0,1),method='bounded',options={'xatol':1e-14})
    return max(-res.fun,abs(cos(angle)))


def boundary(s):
    return sqrt(3*s-2)/(2-s)**1.5, (1-s)*sqrt(s+2)/(2-s)**1.5

count=0
for j in range(421):
    theta=2*pi*j/420
    actual=direct_support(theta)
    target=predicted_support(theta)
    assert abs(actual-target) < 3e-8,(theta,actual,target)
    count+=1

for j in range(1,399):
    s=2/3+j/(399*3)
    x,y=boundary(s)
    a,b=ellipse_axes(s)
    assert abs(x*x/a/a+y*y/b/b-1)<1e-11
    assert 0<=x<=1 and 0<=y<=1
    count+=1

integrand=lambda s: 3*s*(1-s)*sqrt(s+2)/((2-s)**4*sqrt(3*s-2))
A,err=quad(integrand,2/3,1,epsabs=1e-12)
A*=4
exact=3*sqrt(3)/8+3*log(2+sqrt(3))/16
assert abs(A-exact)<1e-9,(A,exact)
count+=1
assert abs(predicted_support(pi/2)-1/(2*sqrt(2)))<1e-12
count+=1
print('PASS',count,'finite checks; area numerical',format(A,'.14g'), 'analytic expression', format(exact,'.14g'))
