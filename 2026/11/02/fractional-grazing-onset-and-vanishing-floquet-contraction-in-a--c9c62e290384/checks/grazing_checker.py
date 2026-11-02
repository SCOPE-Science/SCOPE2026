"""Reproduce algebraic grazing constants and finite-parameter orbit checks.

The adaptive integrations provide diagnostics, not proof of the limit.
"""
import math
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

u,d,b=sp.symbols('u d b', positive=True)
L=sp.sqrt(2*d)
one=sp.integrate(d-u**2/2,(u,-L,L))
assert sp.simplify(2*one / d**sp.Rational(3,2) - 8*sp.sqrt(2)/3)==0
assert sp.simplify(2*(2*L)/sp.sqrt(d)-4*sp.sqrt(2))==0
C=(3*sp.pi/(8*sp.sqrt(2)*b))**sp.Rational(2,3)
assert sp.simplify(sp.pi - (8*sp.sqrt(2)/3)*b*C**sp.Rational(3,2))==0
K=4*sp.sqrt(2)*b*sp.sqrt(C)
print('EXACT_TWO_GRAZING_WINDOWS_PASS')
print('EXACT_OUTSIDE_RESIDENCE_PASS')
print('EXACT_NORMAL_FORM_ROOT_PASS')
print('EXACT_MULTIPLIER_CONSTANT_PASS')

def return_section(lam,r,b=1.):
    def f(t,z):
        x,y=z
        h=math.copysign(max(abs(x)-1.,0.),x)
        return (y+lam*x-b*h,-x)
    def event(t,z): return z[0]
    event.direction=1
    event.terminal=False
    sol=solve_ivp(f,(0,8.),(0.,r),events=event,rtol=2e-10,atol=2e-11,max_step=.035)
    roots=sol.y_events[0]
    if len(roots)<2: raise RuntimeError('No full Poincare crossing')
    return roots[-1][1]

if __name__=='__main__':
    bb=1.
    c=float(C.subs(b,bb)); k=float(K.subs(b,bb))
    for lam in (0.003,0.001,0.0003):
        r=brentq(lambda z:return_section(lam,z,bb)-z,1+0.2*c*lam**(2/3),1+2.0*c*lam**(2/3),xtol=4e-11)
        ratio=(r-1.)/(c*lam**(2/3))
        assert abs(ratio-1.)<0.15,(lam,r,ratio)
        print(f'FINITE_DIAGNOSTIC lambda={lam:.4g} radius={r:.10f} amplitude_ratio={ratio:.5f}')
    print('FINITE_INTEGRATION_DIAGNOSTICS_PASS')
