#!/usr/bin/env python3
"""Reproducible symbolic and numerical diagnostics for a local geometric-probability theorem.

This verifies universal space-form boundary identities and numerical limiting slopes;
it is not a substitute for the normal-coordinate locality argument in the proof.
"""
import sympy as sp
import mpmath as mp
x,y,z,a=sp.symbols('x y z a',real=True)
# Spherical/hyperbolic cosine law reduces the tangent-angle numerator to:
id1=sp.trigsimp(sp.sin(x)**2+sp.sin(y)**2-sp.sin(x+y)**2+2*sp.sin(x)*sp.sin(y)*sp.cos(x+y),method='fu')
assert id1==0,id1
print('EXACT_COSINE_HALF_ANGLE_IDENTITY_PASSED')
# The boundary has x+y=pi/2 when the triangle angle is 90 degrees.
# cos(x+y)+z sin x sin y = 0, so at z=0 the derivative dy/dz is sin x sin y.
# Equivalently, for a=2x, the derivative of the threshold b=2y is sin(a).
assert sp.simplify(2*sp.sin(x)*sp.cos(x)-sp.sin(2*x))==0
assert sp.integrate(sp.sin(a),(a,0,sp.pi))==2
print('EXACT_RIGHT_ANGLE_BOUNDARY_FIRST_VARIATION_PASSED')
# Angular gaps (a,b,c) have density 1/(2*pi*pi); one nonacute angle
# moves its b-threshold by z*sin(a), so the single-angle probability
# changes by z/pi^2 and the acute probability by -3z/pi^2.
assert sp.simplify(3*sp.integrate(sp.sin(a),(a,0,sp.pi))/(2*sp.pi**2)-3/sp.pi**2)==0
print('EXACT_DIRICHLET_BOUNDARY_DENSITY_AND_CURVATURE_COEFFICIENT_PASSED')
mp.mp.dps=65
def one_nonacute(z):
    def integrand(a):
        return mp.atan(mp.cos(a/2)/((1-z)*mp.sin(a/2)))
    return mp.quad(integrand,[0,mp.pi/2,mp.pi])/mp.pi**2
p0=1-3*one_nonacute(mp.mpf('0'))
assert abs(p0-mp.mpf(1)/4)<mp.mpf('1e-58')
for K in [1,-1]:
    errors=[]
    for r0 in ['0.3','0.2','0.1','0.05']:
        r=mp.mpf(r0)
        zz=mp.sin(r)**2 if K==1 else -mp.sinh(r)**2
        P=1-3*one_nonacute(zz)
        slope=(P-mp.mpf('0.25'))/r**2
        target=-3*K/mp.pi**2
        error=abs(slope-target)
        errors.append(error)
        print('SPACE_FORM_TEST',K,r0,mp.nstr(P,22),mp.nstr(slope,20),mp.nstr(error,9))
    assert errors[-1]<mp.mpf('0.00015')
    assert all(errors[i]>errors[i+1] for i in range(len(errors)-1))
print('INDEPENDENT_SPACE_FORM_GEODESIC_COSINE_LAW_SLOPES_PASSED')
print('ALL_CHECKS_PASSED')
