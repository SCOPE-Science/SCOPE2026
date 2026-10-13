#!/usr/bin/env python3
"""Algebraic consistency checks for the rank-two qutrit KCBS optimum."""
import math
import sympy as s

z = s.symbols('z', real=True)
w = s.symbols('w')
D = (z - 1) * (5 - z*z) / (3 - z)
N = z**3 - 5*z*z + 3*z + 5
assert s.simplify(s.diff(D, z) - 2*N/(z - 3)**2) == 0
assert s.simplify(s.diff(D, z, 2) - 2*(z - 1)*(z*z - 8*z + 19)/(z - 3)**3) == 0
r = (z - 1)*(z - 2)**2/(3-z)
char = (w-1)*(w-2)**2+r*(w-3)
assert s.simplify(char.subs(w,z))==0
assert s.simplify((5-z)**2-4*(4+3*r)/z-D)==0

phi=(1+s.sqrt(5))/2
x=s.symbols('x', nonnegative=True)
r_x=x*x/((1+x)**2*(1+2*x))
assert s.simplify(s.diff(r_x,x)-2*x*(1+x-x*x)/((1+x)**3*(1+2*x)**2))==0
assert s.simplify(r_x.subs(x,phi)-(5*s.sqrt(5)-11)/2)==0

for xx in [s.Rational(0),s.Rational(1,8),s.Rational(1,2),s.Rational(1),phi]:
    t=s.sqrt(xx)
    rays=[s.Matrix([1,0,0]),s.Matrix([0,1,0]),
          s.Matrix([1,0,t])/s.sqrt(1+xx),
          s.Matrix([-t,-t,1])/s.sqrt(1+2*xx),
          s.Matrix([0,1,t])/s.sqrt(1+xx)]
    for j in range(5):
        assert s.simplify((rays[j].T*rays[(j+1)%5])[0])==0
        assert s.simplify((rays[j].T*rays[j])[0])==1
    M=s.zeros(3)
    for v in rays:
        M+=v*v.T
    assert s.simplify(s.trace(M)-5)==0
    det=s.simplify(M.det())
    assert s.simplify(det-(4+3*r_x.subs(x,xx)))==0
    assert s.simplify(M.charpoly(w).as_expr()-((w-1)*(w-2)**2+r_x.subs(x,xx)*(w-3)))==0

for aa,bb in [(0.5,0.5),(.51,.49),(.6,.4),(.75,.25),(.9,.1),(.99,.01),(1.,0.)]:
    if aa==bb:
        zz=2.
    elif bb==0:
        zz=math.sqrt(5)
    else:
        import scipy.optimize as so
        q=bb/(2*aa-bb)
        # Stationary equation with unsquared, signed radicals.
        def derivative(t):
            dd=(t-1)*(5-t*t)/(3-t)
            nn=t**3-5*t*t+3*t+5
            return aa-bb/2+bb*nn/(2*(t-3)**2*math.sqrt(dd))
        zz=so.brentq(derivative,2.,math.sqrt(5)-1e-11,xtol=1e-14)
        assert abs(q*q*float(N.subs(z,zz))**2-(zz-1)*(5-zz*zz)*(3-zz)**3)<1e-9
    rr=(zz-1)*(zz-2)**2/(3-zz)
    # Reconstruct spectral operator at an independent symmetric pentagon.
    if aa==bb:
        xi=0.
    elif bb==0:
        xi=(1+math.sqrt(5))/2
    else:
        xi=so.brentq(lambda y:y*y/((1+y)**2*(1+2*y))-rr,
                      0.,(1+math.sqrt(5))/2,xtol=1e-14)
    import numpy as np
    t=math.sqrt(xi)
    vectors=[np.array([1.,0.,0.]),np.array([0.,1.,0.]),
             np.array([1.,0.,t])/math.sqrt(1+xi),
             np.array([-t,-t,1.])/math.sqrt(1+2*xi),
             np.array([0.,1.,t])/math.sqrt(1+xi)]
    M=sum(np.outer(v,v) for v in vectors)
    eig=np.linalg.eigvalsh(M)[::-1]
    assert abs(eig[0]-zz)<1e-8
    if bb>0:
        exact=aa*zz+bb*(5-zz+math.sqrt(float(D.subs(z,zz))))/2
    else:
        exact=math.sqrt(5)
    assert abs(aa*eig[0]+bb*eig[1]-exact)<1e-8
print('VERIFY_OK symbolic_spectral=passed exact_projectors=5 optimizer_cases=7')
