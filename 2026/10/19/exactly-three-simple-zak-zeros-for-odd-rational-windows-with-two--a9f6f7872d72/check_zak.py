"""Standalone numerical checks for a two-pole rational-window Zak-zero theorem.

Requires Python 3 standard library only. Analytical proof establishes universal statements;
these finite tests verify formula conventions and local transversality.
"""
import cmath
import math

PI=math.pi

def g(t,a,b):
    return t/((t*t+a*a)*(t*t+b*b))

def k_lam(lam,theta,xi):
    den=math.cosh(lam)-math.cos(theta)
    return (math.cosh(lam*(1-xi))-cmath.exp(-1j*theta)*math.cosh(lam*xi))/den

def dk_lam(lam,theta,xi):
    c=math.cos(theta)
    em=cmath.exp(-1j*theta)
    den=math.cosh(lam)-c
    numerator=math.cosh(lam*(1-xi))-em*math.cosh(lam*xi)
    numerator_deriv=(1-xi)*math.sinh(lam*(1-xi))-em*xi*math.sinh(lam*xi)
    return numerator_deriv/den-numerator*math.sinh(lam)/(den*den)

def closed_z(a,b,x,xi):
    theta=2*PI*x
    phase=cmath.exp(1j*theta*xi)
    if a==b:
        return 1j*PI*PI/a*phase*dk_lam(2*PI*a,theta,xi)
    return -1j*PI/(b*b-a*a)*phase*(k_lam(2*PI*a,theta,xi)-k_lam(2*PI*b,theta,xi))

def direct_z(a,b,x,xi,cutoff=3600):
    return sum(g(x-k,a,b)*cmath.exp(2j*PI*k*xi) for k in range(-cutoff,cutoff+1))

def detjac(a,b,x,xi):
    h=1e-5
    zx=(closed_z(a,b,x+h,xi)-closed_z(a,b,x-h,xi))/(2*h)
    zy=(closed_z(a,b,x,xi+h)-closed_z(a,b,x,xi-h))/(2*h)
    return (zx.conjugate()*zy).imag

pairs=((0.17,0.35),(0.35,0.35),(0.45,1.2),(0.8,1.5),(1.0,2.0),(1.3,1.3),(2.0,3.0))
points=((0.08,0.13),(0.37,0.23),(0.61,0.44),(0.82,0.71),
        (0,0),(0,0.5),(0.5,0),(0.31,0.5),(0.50,0.50))
comparisons=0
for a,b in pairs:
    for x,xi in points:
        got=direct_z(a,b,x,xi)
        expected=closed_z(a,b,x,xi)
        assert abs(got-expected)<8e-8, ('Zak equality',a,b,x,xi,got,expected)
        comparisons+=1
    for x,xi in ((0,0),(0,.5),(.5,0)):
        assert abs(closed_z(a,b,x,xi))<1e-10
        j=detjac(a,b,x,xi)
        assert abs(j)>1e-12, ('degenerate',a,b,x,xi,j)
        comparisons+=2
    for ti in range(21):
        for wi in range(21):
            x=ti/21
            xi=wi/21
            if x==0 and xi==0:continue
            z=closed_z(a,b,x,xi)
            assert abs(z)>1e-12, ('grid zero',a,b,x,xi,z)
            comparisons+=1
print('VERIFY_OK',comparisons,'formula, nondegenerate-zero, and grid checks; standard library only')
