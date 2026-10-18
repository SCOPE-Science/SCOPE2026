"""Reproducible checks for unequal planar truncations of a hyperbolic ball.

Requires sympy and mpmath; analytic proof is in RESULT.md.
"""
from math import pi, asinh, sqrt
import sympy as sp
import mpmath as mp

# Exact formal series in sinhr=s>0, alpha=a.
s, a = sp.symbols('s a', positive=True)
c = sp.sqrt(1+s*s)
A = s*s*sp.cos(a) + sp.sqrt(1+s*s*sp.sin(a)**2)-1
B = s*(2*c*sp.cos(a)+sp.sin(a)*sp.atan(c*sp.tan(a)))
A4 = -s*s*c*c/sp.Integer(8)
A6 = s*s*c*c*(3*s*s+1)/sp.Integer(48)
B4 = -s*c*(4*s*s+1)/sp.Integer(12)
B6 = s*c*(36*s**4+22*s*s+1)/sp.Integer(180)
for expr, power, expect in [(A,4,A4),(A,6,A6),(B,4,B4),(B,6,B6)]:
    coef = sp.expand(sp.series(expr,a,0,7).removeO()).coeff(a,power)
    assert sp.simplify(coef-expect)==0, (power,sp.simplify(coef-expect))
N=sp.simplify(B6*A4-B4*A6)
assert sp.simplify(N+s**3*(4*s*s-1)*c**5/960)==0
leading=sp.simplify(sp.Rational(3,4)*N/A4**3/(2*sp.pi))
assert sp.simplify(leading-(4*s*s-1)/(5*sp.pi*s**3*c))==0

# Deep-cut endpoint in the variable u=cos(alpha), for which the
# surface-area derivative does not vanish.
u=sp.symbols('u',positive=True)
q=sp.sqrt(c*c-s*s*u*u)
# arctan(c sqrt(1-u^2)/u) equals pi/2-arctan(u/(c sqrt(1-u^2)))
A_u=s*s*u+q-1
B_u=s*(2*c*u+sp.sqrt(1-u*u)*(sp.pi/2-sp.atan(u/(c*sp.sqrt(1-u*u)))))
As=[sp.simplify(sp.diff(A_u,u,k).subs(u,0)) for k in [1,2]]
Bs=[sp.simplify(sp.diff(B_u,u,k).subs(u,0)) for k in [1,2]]
limit=sp.simplify((Bs[1]*As[0]-Bs[0]*As[1])/As[0]**3/(2*sp.pi))
assert sp.simplify(limit-(4-sp.pi-2/(c*c))/(4*sp.pi*s**3))==0

r0=asinh(.5)
r1=asinh(sqrt((pi-2)/(4-pi)))
assert 0<r0<r1
print('Exact symbolic coefficients and endpoint thresholds: PASS')
print('Critical radii',format(r0,'.12f'),format(r1,'.12f'))

mp.mp.dps=65
for r,alpha in [('0.3','0.035'),('0.6','0.035'),('0.6','1.56'),('1.2','1.56')]:
    radius=mp.mpf(r); angle=mp.mpf(alpha)
    z=mp.sinh(radius);C=mp.cosh(radius)
    area=lambda t: 2*mp.pi*(z*z*mp.cos(t)+mp.sqrt(1+z*z*mp.sin(t)**2)-1)
    curvature=lambda t: 2*mp.pi*z*(2*C*mp.cos(t)+mp.sin(t)*mp.atan(C*mp.tan(t)))
    Ap=mp.diff(area,angle);App=mp.diff(area,angle,2)
    Mp=mp.diff(curvature,angle);Mpp=mp.diff(curvature,angle,2)
    hess=(Mpp*Ap-Mp*App)/Ap**3
    pred=((4*z*z-1)/(5*mp.pi*z**3*C*angle**2)
           if angle<1 else (4-mp.pi-2/C**2)/(4*mp.pi*z**3))
    rel=abs((hess-pred)/pred)
    assert rel < mp.mpf('0.08'), (r,alpha,rel)
    x=area(angle)
    step=mp.mpf('0.0000001')*min(x-area(mp.pi/2),area(mp.mpf('0.000001'))-x)
    if step<=0:step=mp.mpf('1e-12')
    # Invert strictly decreasing area to construct exactly area-balanced cuts.
    ap=mp.findroot(lambda t:area(t)-(x+step),(angle-step/Ap,angle-step/(2*Ap)))
    am=mp.findroot(lambda t:area(t)-(x-step),(angle+step/Ap,angle+step/(2*Ap)))
    assert abs((area(ap)+area(am)-2*x))<mp.mpf('1e-45')
    delta=curvature(ap)+curvature(am)-2*curvature(angle)
    ratio=delta/(step**2)
    assert mp.sign(ratio)==mp.sign(hess)
    assert abs((ratio-hess)/hess)<mp.mpf('0.002')
    print('r=',r,'alpha=',alpha,'Hessian=',mp.nstr(hess,12),'asymptotic rel.err=',mp.nstr(rel,4),'finite fixed-area sign=',int(mp.sign(delta)))
print('Independent differentiation and exactly balanced area perturbations: PASS')
