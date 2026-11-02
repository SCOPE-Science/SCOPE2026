#!/usr/bin/env python3
"""Independent exact-algebra and high-precision quadrature checks for a two-direction descent identity."""
import math
import sympy as sp
import mpmath as mp

r,t=sp.symbols('r t', positive=True)
C11=(r*r-1)**2*t**4/((1+t*t)*(r*r+t*t)**2*(1+r*r*t*t))
# Rational partial fractions lead to elementary half-line integrals.
parts=(r**4/((r*r+1)*(r*r+t*t)**2)
      +r*r*(r*r+2)/((r*r-1)*(r*r+1)**2*(r*r+t*t))
      +r*r/((r*r-1)*(r*r+1)**2*(r*r*t*t+1))
      -1/((r*r-1)*(t*t+1)))
assert sp.cancel(C11-parts)==0
I11= (r/(2*(r*r+1)) + r*(r*r+2)/((r*r-1)*(r*r+1)**2)
        +r/((r*r-1)*(r*r+1)**2)-1/(r*r-1))
D11=(r*r+r+2)/(2*(r+1)**3)
D22=r*(2*r*r+r+1)/(2*(r+1)**3)
trace_C=(r-1)**2/(r*r+1)
fac=((r*r-1)/(r*r+1))**2
assert sp.cancel(I11-fac*D11)==0
assert sp.cancel(trace_C-I11-fac*D22)==0
assert sp.cancel(D11+D22-(r*r+1)/(r+1)**2)==0

mp.mp.dps=50
numeric_checks=0
for rv in [mp.mpf(1), mp.mpf('1.1'), mp.sqrt(2), mp.mpf(2), mp.mpf(7), mp.mpf(25)]:
    def b(theta):
        c,s=mp.cos(theta),mp.sin(theta)
        den=rv*rv*c*c+s*s
        v1,v2=-s/mp.sqrt(den),rv*c/mp.sqrt(den)
        return v1*v1, v2*v2, v1*v2
    def Bcorr(theta):
        c,s=mp.cos(theta),mp.sin(theta)
        den=(rv*rv*c*c+s*s)*(rv*rv*s*s+c*c)
        rho2=(rv*rv-1)**2*c*c*s*s/den
        return rho2
    t1,t2=1/(rv+1),rv/(rv+1)
    # One-angle exact conditional expectations: orthogonal partner, iid second partner.
    def quad(j,kind):
        def integrand(theta):
            q=b(theta)
            weight = Bcorr(theta) if kind=='orth' else t1*q[0]+t2*q[1]
            return q[j]*weight
        return mp.quad(integrand,[0,mp.pi/2,mp.pi])/mp.pi
    num_C=[quad(0,'orth'),quad(1,'orth')]
    num_D=[quad(0,'iid'),quad(1,'iid')]
    pred_D=[(rv**2+rv+2)/(2*(rv+1)**3), rv*(2*rv**2+rv+1)/(2*(rv+1)**3)]
    fact=((rv**2-1)/(rv**2+1))**2
    for actual,pred in zip(num_D,pred_D):
        assert abs(actual-pred)<mp.mpf('1e-32'),(rv,actual,pred)
        numeric_checks+=1
    for actual,pred in zip(num_C,[fact*k for k in pred_D]):
        assert abs(actual-pred)<mp.mpf('1e-32'),(rv,actual,pred)
        numeric_checks+=1
    # The mixed (offdiagonal) moment is odd under theta -> -theta.
    off=mp.quad(lambda theta: b(theta)[2]*(Bcorr(theta)),[-mp.pi/2,0,mp.pi/2])/mp.pi
    assert abs(off)<mp.mpf('1e-32')
    numeric_checks+=1
print('CHECK_OK symbolic-rational=4 high-precision-angular=',numeric_checks)
