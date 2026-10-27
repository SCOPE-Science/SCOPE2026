"""Checks for the Bessel fourth-moment cutoff and critical gap formulas.

Requires sympy, scipy, and numpy. Numerical tests illustrate formulas; the
analytic argument is given in RESULT.md.
"""
import math
import sympy as sp
import numpy as np
from scipy.special import jv
from scipy.integrate import quad, simpson

r, nu, a, b = sp.symbols('r nu a b', positive=True, real=True)
s = a*a+b*b
sprime = 2*nu*a*a/r-2*(nu+1)*b*b/r
assert sp.simplify(2*r*s*s+r*r*2*s*sprime-2*r*(2*nu+1)*(a**4-b**4)) == 0
print('PASS symbolic recurrence identity')

for k in (0, 1, 2, 5):
    for R in (0.7, 2., 7., 30.):
        lhs = quad(lambda t: t*(jv(k,t)**4-jv(k+1,t)**4), 0, R, epsabs=1e-11)[0]
        rhs = R**2*(jv(k,R)**2+jv(k+1,R)**2)**2/(2*(2*k+1))
        assert abs(lhs-rhs) < 1e-8, (k,R,lhs,rhs)
print('PASS positive cutoff identities at 16 parameter points')

for k in (0, 1, 3):
    R=1e5
    exact=R*R*(jv(k,R)**2+jv(k+1,R)**2)**2/(2*(2*k+1))
    limit=2/(math.pi**2*(2*k+1))
    assert abs(exact-limit)<1e-5, (k,exact,limit)
print('PASS large-aperture odd-reciprocal limits')

R = 700.
radius=np.linspace(0,R,140001)
radius[0]=1e-30
for q in (4.2, 4.05, 4.01):
    mean=math.gamma((q+1)/2)/(math.sqrt(math.pi)*math.gamma((q+2)/2))
    common_tail=(2/math.pi)**(q/2)*mean*2/(q-4)*R**(-(q-4)/2)
    values=[]
    for k in (0, 1, 2):
        values.append(float(simpson(radius*np.abs(jv(k,radius))**q,x=radius))+common_tail)
    gap=(values[0]**(2/q)-values[1]**(2/q))/math.sqrt(q-4)
    if q==4.01:
        assert abs(gap-1/(math.pi*math.sqrt(3)))<.003,(gap,q)
print('PASS mean-tail-subtracted gap diagnostics')
