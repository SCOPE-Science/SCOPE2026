"""Reproducible finite checks of an analytic quaternionic numerical-range theorem.

Requires Python 3 and standard library. This program checks algebraic consequences
and numerical quadrature; it is not a substitute for the all-parameter proof.
"""
from fractions import Fraction as Q
from math import sqrt, asin, pi, isclose
from random import Random

def mul(x,y):
    a,b,c,d=x; e,f,g,h=y
    return (a*e-b*f-c*g-d*h,a*f+b*e+c*h-d*g,a*g-b*h+c*e+d*f,a*h+b*g-c*f+d*e)
def conj(z): return (z[0],-z[1],-z[2],-z[3])
I=(0.,1.,0.,0.); J=(0.,0.,1.,0.)

def volume_profile(r):
    q=sqrt(1-r*r)
    return (8*r**3+16*r-(2*r**3+13*r)*q-(12*r*r+3)*asin(r))/8

def integration_midpoint(r,N=20000):
    phi=asin(r);step=phi/N
    return sum(((r-__import__('math').sin((j+.5)*step))**3)*__import__('math').sin((j+.5)*step) for j in range(N))*step

rng=Random(1026)
checks=0
for a,b,c in [(2.,1.,1.),(1.,1.,2.),(6.,.05,.7),(1.002,.998,4.),(3.,.5,1.5)]:
    d=a-b; s=a+b; rr=d/s
    for k in range(10000):
        g=[rng.gauss(0,1) for _ in range(5)]
        norm=sqrt(sum(t*t for t in g)); g=[v/norm for v in g]
        t=g[0]
        rad=sqrt((1+t)/2)
        q=tuple(g[i]/(2*rad) for i in range(1,5))
        re=2*c*rad*mul(J,q)[0]
        sk=mul(mul(conj(q),I),q)
        im=[a*rad*rad*I[i]+b*sk[i] for i in (1,2,3)]
        rho=sqrt(sum(y*y for y in im))
        u=sqrt(max(0,1-(re/c)**2))
        lo=max(0,(d-s*u)/2)
        hi=(d+s*u)/2
        assert lo-1e-9 <=rho<=hi+1e-9,(a,b,c,re,rho,lo,hi)
        checks+=1
    if rr:
        value=volume_profile(rr)
        integ=integration_midpoint(rr)
        assert abs(value-integ)<1e-8, (value,integ)
        checks+=1
for a,b in [(2,1),(5,3),(100,99),(7,1)]:
    d=Q(a-b); s=Q(a+b)
    for k in range(100):
        t=Q(k,101); R2=Q(1)-t*t
        B=Q(a*b)
        # Coefficient identity controlling maximal imaginary radius.
        # x/c=t, z arbitrary with |z| <= sqrt(1-t^2).
        z=Q((k%17)-8,17)
        if z*z>R2: continue
        expr=(d+s*z)**2/4+B*(R2-z*z)
        ans=d*d/4+B*R2+s*d*z/2+d*d*z*z/4
        assert expr==ans
        checks+=1
print('PASS',checks,'finite checks; volume profile and shell bounds')
