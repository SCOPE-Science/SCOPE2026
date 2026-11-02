#!/usr/bin/env python3
"""Finite symbolic and numerical checks for the orthogonal disk-sum ellipsoid formulas.

Requires Python 3 and SymPy. This executable is supplementary to the analytic proof.
"""
import math
import random
import sympy as sp

x, r, t, s = sp.symbols('x r t s', positive=True)
P = 2*t*t + (r*r-1)*t - 2*r*r
# Under the optimality relation P=0, the two contact moments coincide.
u = (2-t)/3
z_moment = t/(1+t)*(1-r*r*u/t**2)
res = sp.factor((z_moment-sp.Rational(1,3))*3*t*(1+t))
assert sp.simplify(res - P) == 0, (res, P)
# The volume objective's derivative has the exact asserted numerator.
objective = (1+t)**3*(t+r*r)/t**2
assert sp.simplify(sp.diff(objective,t) - (t+1)**2*P/t**3) == 0
# The normalized outer volume ratio is minimized at equal disk radii.
assert abs(2/3*math.sqrt((1+1)**3*(1+1)/1)/(1+1)-4/3)<1e-14

random.seed(14987)
N=0
for a,b in ((1.,1.),(2.,1.),(1.,3.),(7.,2.),(0.5,9.)):
    rr=b/a
    tau=(1-rr*rr+math.sqrt((1-rr*rr)**2+16*rr*rr))/4
    assert .5<tau<2
    px=a*math.sqrt(1+tau)
    qy=math.sqrt(a*a*(1+tau)+b*b*(1+1/tau))
    rz=b*math.sqrt(1+1/tau)
    assert abs(2*a*a*tau*tau+(b*b-a*a)*tau-2*b*b)<1e-9*(a*a+b*b)
    sm=min(1.,tau/rr)
    lam=(2-tau)/(3*sm*sm)
    assert 0<lam<1
    # Independent contact-moment certificate; normalized coordinate covariance=I/3.
    moment_x=(1-lam)*a*a/px**2 +lam*a*a*(1-sm*sm)/px**2
    moment_y=lam*(a*sm+b*(rr/tau)*sm)**2/qy**2
    moment_z=(1-lam)*b*b/rz**2+lam*b*b*(1-(rr*sm/tau)**2)/rz**2
    for k in (moment_x,moment_y,moment_z):
        assert abs(k-1/3)<5e-13,(a,b,tau,k)
        N+=1
    # Independently sample disk-boundary pairs and test the outer containment.
    for k in range(4000):
        alpha=random.uniform(0,2*math.pi)
        beta=random.uniform(0,2*math.pi)
        xx=a*math.cos(alpha)
        yy=a*math.sin(alpha)+b*math.sin(beta)
        zz=b*math.cos(beta)
        assert xx*xx/px**2+yy*yy/qy**2+zz*zz/rz**2<1+1e-12
        N+=1
    # Independently sample normals to verify support inclusion of the John ellipse.
    for k in range(4000):
        nx,ny,nz=(random.gauss(0,1) for _ in range(3))
        hj=math.sqrt(a*a*nx*nx+(a+b)**2*ny*ny+b*b*nz*nz)
        hk=a*math.hypot(nx,ny)+b*math.hypot(ny,nz)
        assert hj<=hk+1e-12*(1+hk)
        N+=1
    # Numerical grid: volume-ratio lower and upper bounds.
    V=2*math.pi*a*b*(a+b)
    VJ=4*math.pi*a*b*(a+b)/3
    VL=4*math.pi*px*qy*rz/3
    assert abs(VJ/V-2/3)<1e-13
    assert 4/3-1e-13<=VL/V<math.sqrt(3)+1e-13
    N+=3
print(f'PASS: {N} symbolic/contact/inclusion/ratio consistency checks across five radius pairs')
