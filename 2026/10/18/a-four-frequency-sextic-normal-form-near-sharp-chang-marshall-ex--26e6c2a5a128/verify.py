"""Exact Laurent-constant Taylor verification of a Chang--Marshall local normal form.

Requires Python 3 and sympy. Computes a finite formal power series, not
an external proof or independent validation.
"""
import sympy as sp
from collections import defaultdict
m, t, k, lam = sp.symbols('m t k lam', positive=True, real=True)
u, v, w = sp.symbols('u v w', real=True)
# Constant Fourier coefficient of exp(2u cos theta+2v cos 2theta+2w cos 3theta),
# retaining only terms through total weighted degree 6.
characters = {(1, 1): u, (1, -1): u,
              (2, 2): v, (2, -2): v,
              (3, 3): w, (3, -3): w}
P = {(0, 0): sp.S.One}
F = {0: sp.S.One}
for j in range(1, 7):
    Q = defaultdict(lambda: sp.S.Zero)
    for (degree, mode), coefficient in P.items():
        for (step, frequency), amplitude in characters.items():
            if degree + step <= 6:
                Q[(degree + step, mode + frequency)] += coefficient*amplitude/j
    P = Q
    for (degree, mode), coefficient in P.items():
        if mode == 0:
            F[degree] = F.get(degree, sp.S.Zero) + coefficient
F2, F4, F6 = [sp.expand(F[n]) for n in (2, 4, 6)]
L2 = F2
L4 = sp.expand(F4 - F2**2/2)
L6 = sp.expand(F6 - F2*F4 + F2**3/3)
assert sp.simplify(L2-u**2) == 0
assert sp.simplify(L4 - (v**2 + u**2*v - u**4/4)) == 0
assert sp.simplify(L6 - (u**6/9 - 2*u**4*v/3 + u**3*w/3 + 2*u*v*w + w**2)) == 0
# The polynomial a z^m+t z^(m+1)+k t^2 z^(m+2)+lam t^3 z^(m+3)
# is normalized to Dirichlet energy 1 by a positive a(t).
a = (1/sp.sqrt(m)) * (1-(m+1)*t**2/2
      - ((m+2)*k**2/2+(m+1)**2/8)*t**4)
U = a*t+k*t**3+k*lam*t**5
V = a*k*t**2+lam*t**4
W = a*lam*t**3
S = 1/m - t**2/m-2*k**2*t**4/m-3*lam**2*t**6/m
Z = L2.subs({u:U,v:V,w:W})+L4.subs({u:U,v:V,w:W})+L6.subs({u:U,v:V,w:W})
D = sp.series(1/m-S-Z,t,0,7).removeO().expand()
kstar = (2*m+1)/(2*sp.sqrt(m))
lamstar = (12*m**2+15*m+4)/(12*m)
assert sp.simplify(D.coeff(t,2)) == 0
assert sp.simplify(D.coeff(t,4)-(k-kstar)**2/m) == 0
C6 = sp.factor(D.coeff(t,6).subs(k,kstar))
assert sp.simplify(C6 - (2*(lam-lamstar)**2/m+1/(24*m))) == 0
print('VERIFY_OK exact Fourier expansion; unique quartic cancellation; sharp four-mode sextic coefficient 1/(24m)')
