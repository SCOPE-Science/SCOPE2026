"""Finite exact and deterministic checks for the skewness of circular number variance."""
from fractions import Fraction as F
from math import comb, isclose
import sympy as sp

u,v,s=sp.symbols('u v s', real=True, nonnegative=True)
# Two same-sign quadrants and two opposite-sign quadrants, after scaling by s.
same = 4*sp.integrate(sp.integrate((1-u)*(1-v)*(1-u+v),(v,0,u)),(u,0,1))
opposite=2*sp.integrate(sp.integrate((1-u)*(1-v)*(1-u-v),(v,0,1-u)),(u,0,1))
assert (same,opposite,same+opposite)==(sp.Rational(11,30),sp.Rational(11,60),sp.Rational(11,20))

# Independent discrete mesh quadrature of the full three-point expectation;
# rotation invariance fixes the first of three circle points at zero.
for mesh in (80,160,320):
    scale=F(1,mesh)
    windows=(F(1,10),F(1,5),F(1,4))
    for h in windows:
        q=[max(h-min(F(k,mesh),F(mesh-k,mesh)), F(0)) for k in range(mesh)]
        m=h*h
        triangle_sum=F(0)
        for i in range(mesh):
            if not q[i]: continue
            for j in range(mesh):
                if q[j]: triangle_sum+=q[i]*q[j]*q[(i-j)%mesh]
        triangle_mean=triangle_sum/mesh**2
        target=F(11,20)*h**5
        assert abs(float(triangle_mean-target))<3e-5,(mesh,h,triangle_mean,target)

# Exact central moment for 2 iid circle points; h is two-point triangular score.
for hh in (F(1,11),F(1,5),F(1,3)):
    EY=hh**2; EY2=F(2,3)*hh**3; EY3=hh**4/F(2)
    mu3=EY3-3*EY*EY2+2*EY**3
    assert 8*mu3==4*hh**4*(1-2*hh)**2
    for n in range(2,100):
        exact=8*(F(n*(n-1),2)*mu3+n*(n-1)*(n-2)*(F(11,20)*hh**5-hh**6))
        closed=2*n*(n-1)*hh**4*((1-2*hh)**2+(n-2)*(F(11,5)*hh-4*hh**2))
        assert exact==closed and exact>0

# Verified large-n, small-window asymptotic regimes, avoiding assuming a CLT.
for n in (5000,30000,150000):
    for alpha in (F(3,2),F(1),F(1,2)):
        hh=float(n)**(-float(alpha))
        var=F(4,3)*n*(n-1)*hh**3*(1-F(3,2)*hh)
        k3=2*n*(n-1)*hh**4*((1-2*hh)**2+(n-2)*(F(11,5)*hh-4*hh**2))
        skew=float(k3)/float(var)**1.5
        if alpha>1:
            ref=3*3**.5/(4*n*hh**.5)
        elif alpha<1:
            ref=33*3**.5/20*hh**.5
        else:
            ref=(3*3**.5/4)*(1+11/5)/(n*hh**.5)
        assert abs(skew/ref-1)<.08,(n,alpha,skew,ref)
print('All exact symbolic and deterministic quadrature checks passed.')
