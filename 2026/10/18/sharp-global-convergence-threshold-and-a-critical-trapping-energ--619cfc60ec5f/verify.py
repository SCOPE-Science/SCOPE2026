"""Reproducible symbolic and finite checks of a sinusoidal-jerk Lyapunov identity.

Requires Python 3, SymPy, SciPy and NumPy. Finite tests are diagnostics;
infinite-time assertions follow from the written proof.
"""
from sympy import symbols, sin, cos, diff, simplify, expand, factor
from scipy.integrate import solve_ivp
import numpy as np

x,y,z,a,b,c,d,h=symbols('x y z a b c d h', real=True)
vec=(y,a*z,-y-b*z+c*sin(d*x))
V=((1+h*b/a)*y*y+a*z*z)/2+h*y*z-c*y*sin(d*x)+(h*c/d)*cos(d*x)
def deriv(expr):
    return sum(diff(expr,v)*f for v,f in zip((x,y,z),vec))
assert simplify(deriv(V)+a*(b-h)*z*z+(h+c*d*cos(d*x))*y*y)==0
crit=V.subs(h,b).subs(b,c*d)
E=a*(z+(c*d/a)*y)**2/2+(y-c*sin(d*x))**2/2+c*c*(1+cos(d*x))**2/2
assert simplify(crit+c*c-E)==0
assert simplify(deriv(E).subs(b,c*d)+c*d*(1+cos(d*x))*y*y)==0
print('symbolic identities: 3/3')

configs=[(2.,1.2,.7,1.1),(1.5,.8,.6,4/3),(.7,.9,.45,2.),(2.,.6,.8,2.)]
rng=np.random.default_rng(984211)
checks=0
for aa,bb,cc,dd in configs:
    hh=min(bb,(bb+cc*dd)/2) if bb>=cc*dd else bb
    for _ in range(12):
        w0=np.array([rng.uniform(-6,6),rng.uniform(-2,2),rng.uniform(-2,2)])
        def field(t,w):
            X,Y,Z=w
            return [Y,aa*Z,-Y-bb*Z+cc*np.sin(dd*X)]
        sol=solve_ivp(field,(0,30),w0,rtol=2e-11,atol=2e-13,max_step=.05)
        assert sol.success
        X,Y,Z=sol.y
        Q=lambda X,Y,Z: (1+hh*bb/aa)*Y**2/2+aa*Z**2/2+hh*Y*Z-cc*Y*np.sin(dd*X)+hh*cc/dd*np.cos(dd*X)
        values=Q(X,Y,Z)
        if bb>=cc*dd-1e-12:
            assert np.max(np.diff(values))<3e-7, (aa,bb,cc,dd,np.max(np.diff(values)))
        checks+=1
print(f'finite solution traces: {checks}/{checks}')
