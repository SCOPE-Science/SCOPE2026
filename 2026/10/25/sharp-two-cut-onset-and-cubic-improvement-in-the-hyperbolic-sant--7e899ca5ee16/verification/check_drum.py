#!/usr/bin/env python3
"""Independent symbolic and high-precision checks of the two-cut drum expansion."""
import sympy as sp
import mpmath as mp

u, a = sp.symbols('u a', positive=True, real=True)
s = sp.sqrt(u)
c = sp.sqrt(1 + u)
z = (u * sp.cos(a) + sp.sqrt(1 + u * sp.sin(a)**2) - 1).series(a, 0, 8).removeO().expand()
m = (2*s*c*sp.cos(a) + s*sp.sin(a)*sp.atan(c*sp.tan(a))).series(a, 0, 8).removeO().expand()
assert sp.simplify(z.coeff(a,2)) == 0
assert sp.simplify(m.coeff(a,2)) == 0
z4 = -u*(1+u)/8
z6 = u*(1+u)*(1+3*u)/48
m4 = -s*c*(1+4*u)/12
m6 = s*c*(36*u*u+22*u+1)/180
for computed, exact in [(z.coeff(a,4),z4),(z.coeff(a,6),z6),
                        (m.coeff(a,4),m4),(m.coeff(a,6),m6)]:
    assert sp.simplify(computed - exact) == 0
sphere_derivative=(1+2*u)/(s*c)
A=sp.simplify(m4 - sphere_derivative*z4)
B=sp.simplify(m6 - sphere_derivative*z6)
assert sp.simplify(A-s*c*(1-2*u)/24) == 0
assert sp.simplify(B-s*c*(54*u*u+13*u-11)/720) == 0
assert sp.simplify(B.subs(u,sp.Rational(1,2))-sp.sqrt(3)/160) == 0
D=sp.symbols('D',real=True)
ymin=sp.simplify(-2*A/(3*B))
assert sp.simplify(sp.limit(ymin.subs(u,sp.Rational(1,2)+D)/D,D,0)-sp.Rational(40,9)) == 0
# The leading optimized improvement in units (S-2pi)^3.
gain=sp.simplify(-4*sp.pi*(A*ymin*ymin+B*ymin**3))
lead=sp.limit(gain.subs(u,sp.Rational(1,2)+D)/(4*sp.pi*D)**3,D,0)
assert sp.simplify(lead-25*sp.sqrt(3)/(1458*sp.pi**2)) == 0

mp.mp.dps=75
pi=mp.pi

def exact_measures(r,alpha):
    q=mp.sinh(r);v=mp.cosh(r)
    area=4*pi*(q*q*mp.cos(alpha)+mp.sqrt(1+q*q*mp.sin(alpha)**2)-1)
    curvature=4*pi*(2*q*v*mp.cos(alpha)+q*mp.sin(alpha)*mp.atan(v*mp.tan(alpha)))
    return area,curvature

def fixed_area_deficit(area,alpha):
    base=mp.asinh(mp.sqrt(area/(4*pi)))
    rr=mp.findroot(lambda radius: exact_measures(radius,alpha)[0]-area,base)
    actual=exact_measures(rr,alpha)[1]
    sphere=mp.sqrt(16*pi*area+4*area*area)
    return actual-sphere

def coeffs(area):
    t=area/(4*pi)
    return (4*pi*mp.sqrt(t*(1+t))*(1-2*t)/24,
            4*pi*mp.sqrt(t*(1+t))*(54*t*t+13*t-11)/720)

# Expansion and sign independently checked from the unexpanded formulas.
for area in [mp.mpf('4'),2*pi,mp.mpf('6.4'),mp.mpf('7.2')]:
    aa,bb=coeffs(area)
    alpha=mp.mpf('0.006')
    observed=fixed_area_deficit(area,alpha)
    prediction=aa*alpha**4+bb*alpha**6
    assert abs(observed-prediction) < mp.mpf('3e-13')
    if area<2*pi:
        assert observed>0
    elif area>2*pi:
        assert observed<0
    else:
        assert observed>0

# The exact source formulas produce smaller M than both classical competitors.
for area in [mp.mpf('6.30'),mp.mpf('6.50'),mp.mpf('7.00'),mp.mpf('7.65')]:
    d=fixed_area_deficit(area,mp.mpf('0.08'))
    sphere=mp.sqrt(16*pi*area+4*area*area)
    flat=mp.sqrt(2*pi**3*area+(pi*pi/4)*area*area)
    assert d < 0
    assert sphere < flat

coeff=25*mp.sqrt(3)/(1458*pi*pi)
for excess in ['0.04','0.02','0.01','0.005']:
    ee=mp.mpf(excess); area=2*pi+ee
    alpha=mp.sqrt(mp.mpf(10)*ee/(9*pi))
    gain=-fixed_area_deficit(area,alpha)
    ratio=gain/(coeff*ee**3)
    assert abs(ratio-1)<mp.mpf('0.005')
print('PASS: exact symbolic coefficients, sharp critical expansion, stationary branch,')
print('      numerical fixed-area signs, subcrossover improvements, cubic onset.')
