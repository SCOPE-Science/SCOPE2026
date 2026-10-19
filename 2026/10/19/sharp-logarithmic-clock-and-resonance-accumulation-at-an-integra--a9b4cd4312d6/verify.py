"""Reproducible algebraic and quadrature diagnostics for a Hopf–Langford period law.

Requires sympy and scipy; no data files or network requests.
Finite checks corroborate but do not replace the asymptotic proof.
"""
import math
import sympy as s
from scipy.integrate import quad
from scipy.optimize import brentq

g, d, t = s.symbols('g d t', positive=True)
p = s.symbols('p', positive=True)
r = d * s.sqrt((g + 1) / g) * s.sech(d * t)
w = -d * s.tanh(d * t)
assert s.simplify(s.diff(r, t) - r*w) == 0
assert s.simplify(s.diff(w, t) + g*(r*r - d*d + w*w)) == 0
assert s.simplify(g/(g+1)*r*r + w*w - d*d) == 0
assert s.simplify(3*(p*(p-2)/6)/8 - 5*(p/2)**2/12 + p*(p+3)/24) == 0
for gamma in (0.5, 1.0, 2.0, 4.0):
    c = gamma
    nu = 2/gamma
    Y = ((gamma + 1)/gamma)**(gamma/2)
    C = 2**(1 + 2*gamma)*c*c*Y*Y
    E_star = -c*c/(2*(gamma+1))
    eps = 1e-8 if gamma == 4.0 else 1e-6
    E = -eps*c*c*Y*Y/2
    assert E_star < E < 0
    peak = (2/(nu+2))**(1/nu)
    root1 = brentq(lambda u:u*u*(1-u**nu)-eps,math.sqrt(eps)*0.99,peak)
    root2 = brentq(lambda u:u*u*(1-u**nu)-eps,peak,1.0)
    # Sine-square parametrization removes both integrable square-root endpoint singularities.
    def integrand(theta):
        z=math.sin(theta)**2
        u=root1+(root2-root1)*z
        den=u*u*(1-u**nu)-eps
        if not den > 0: # endpoint evaluation via a nearby interior point
            theta = max(1e-7,min(math.pi/2-1e-7,theta))
            z=math.sin(theta)**2
            u=root1+(root2-root1)*z
            den=u*u*(1-u**nu)-eps
        return 2*(root2-root1)*math.sin(theta)*math.cos(theta)/math.sqrt(den)
    # endpoints only are sampled directly in diagnostic quadrature; robustly skip their singular forms.
    I=quad(integrand,1e-7,math.pi/2-1e-7,epsabs=1e-8,limit=300)[0]
    T=2*I/c
    predicted=math.log(C/(-E))/c
    assert abs(T-predicted)*c < 0.05,(gamma,T,predicted)
    print(f'gamma={gamma:g}: cT={c*T:.9f}, log(C/-E)={c*predicted:.9f}')
print('All symbolic identities and four near-separatrix quadrature comparisons passed.')
