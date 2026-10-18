"""Reproduce symbolic identities and independent area quadratures for a genus-zero rational map."""
import math
import sympy as sp
import mpmath as mp
x,y,a,h=sp.symbols('x y a h', real=True, positive=True)
V=(x*x+y*y-x-y+a)/(x*y)
z=(a-y+y*y)/x
F=(y,z)
assert sp.cancel(V.subs({x:y,y:z}, simultaneous=True)-V)==0
DX=sp.Matrix(F).jacobian((x,y))
assert sp.simplify(DX.det()/(F[0]*F[1])-1/(x*y))==0
X=sp.Matrix([(x*x-y*y+a-x)/y,(x*x-y*y-a+y)/x])
assert all(sp.simplify(c)==0 for c in X-sp.Matrix([-x*y*sp.diff(V,y),x*y*sp.diff(V,x)]))
mp.mp.dps=50
samples=[('1','1.2'),('1','1.7'),('0.5','0.5'),('2','1.8')]
for aa_s,hh_s in samples:
    aa=mp.mpf(aa_s);hh=mp.mpf(hh_s)
    disc0=(hh+2)**2+(4-hh**2)*(1-4*aa)
    xl=(hh+2-mp.sqrt(disc0))/(4-hh**2)
    xr=(hh+2+mp.sqrt(disc0))/(4-hh**2)
    def integrand(t):
        xx=(xl+xr)/2+(xr-xl)/2*mp.cos(t)
        D=(1+hh*xx)**2-4*(xx*xx-xx+aa)
        D=max(D,mp.mpf(0))
        yyplus=(1+hh*xx+mp.sqrt(D))/2
        yyminus=(1+hh*xx-mp.sqrt(D))/2
        if yyminus<=0:
            raise ArithmeticError('elliptic oval failed positive quadrant check')
        return mp.log(yyplus/yyminus)*(xr-xl)/2*mp.sin(t)/xx
    area=mp.quad(integrand,[0,mp.pi/3,2*mp.pi/3,mp.pi])
    hc=2-1/aa
    expected=2*mp.pi*(mp.acos(hc/2)-mp.acos(hh/2))
    assert abs(area-expected)<mp.mpf('1e-27'),(aa,hh,area,expected)
for hh in [mp.mpf(s) for s in ['-0.5','0','0.5','1','1.5','1.9']]:
    tau=mp.quad(lambda t:1/(1-hh*t+t*t),[0,-1])
    ph=mp.acos(hh/2)
    assert abs(tau+ph/mp.sqrt(4-hh*hh)) < mp.mpf('1e-40')
    T=2*mp.pi/mp.sqrt(4-hh*hh)
    assert abs((tau/T)*2*mp.pi+ph)<mp.mpf('1e-40')
print('VERIFY_OK 4 area quadratures, 6 independent shift integrals, 3 symbolic identities')
