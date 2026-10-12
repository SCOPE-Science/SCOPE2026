from pathlib import Path
import sympy as sp

# Exact verification for the sextic parametrization in Fomin--Shustin Example 8.4.
t, s, u, v = sp.symbols('t s u v')
P = -8*t**6 + 24*t**4 + 4*t**3 - 18*t**2 - 6*t + 1
Q = -2*t**4 + 4*t**2 - 1
X = -8*u**6 + 24*u**4*v**2 + 4*u**3*v**3 - 18*u**2*v**4 - 6*u*v**5 + v**6
Y = -2*u**4*v**2 + 4*u**2*v**4 - v**6
Z = v**6

assert sp.Poly(X, u, v).total_degree() == 6
assert sp.Poly(Y, u, v).total_degree() == 6
assert sp.Poly(Z, u, v).total_degree() == 6
assert sp.expand(X.subs({u:t, v:1}) - P) == 0
assert sp.expand(Y.subs({u:t, v:1}) - Q) == 0
assert X.subs({u:1, v:0}) == -8 and Y.subs({u:1, v:0}) == 0 and Z.subs({u:1, v:0}) == 0

# Reproduce the source's difference-resultant factorization.
r = sp.symbols('r')
Pr = sp.cancel((P - P.subs(t, r))/(t-r))
Qr = sp.cancel((Q - Q.subs(t, r))/(t-r))
res = sp.factor(sp.resultant(Pr, Qr, t))
expected = 256*(2*r**2-3)*(2*r**2-2*r-1)*(2*r**2+2*r-1)*(8*r**6-24*r**4-4*r**3+18*r**2+6*r-1)
assert sp.expand(res-expected) == 0
assert sp.gcd(sp.Poly(expected, r), sp.Poly(sp.diff(expected, r), r)).degree() == 0
assert sp.Poly(expected, r).degree() == 12

# Local chart X != 0 at the unique point at infinity, with s=v/u.
Xs = sp.expand(X.subs({u:1, v:s}))
Ys = sp.expand(Y.subs({u:1, v:s}))
Zs = s**6
assert Xs.subs(s,0) == -8
assert sp.factor(Ys/s**2).subs(s,0) == -2
N = sp.factor(Zs*Xs**2 + 8*Ys**3)
expected_N = -s**9*(s**2+2*s-2)*(7*s**7-2*s**6-78*s**5-72*s**4+96*s**3+96*s**2-32*s-32)
assert sp.expand(N-expected_N) == 0
assert sp.expand(expected_N/s**9).subs(s,0) == -64
# Therefore ord_s(Y/X)=2 and ord_s(Z/X+8(Y/X)^3)=9.

puiseux_m, puiseux_n = 2, 9
delta_infty = (puiseux_m-1)*(puiseux_n-1)//2
mu_infty = 2*delta_infty
intersection_Linf = 6
polar = mu_infty + intersection_Linf - 1
pa = (6-1)*(6-2)//2
assert delta_infty == 4
assert mu_infty == 8
assert pa == 10
assert 6 + delta_infty == pa
assert polar == 13

print('VERIFY_OK basket=6A1+A8 puiseux=(2,9) delta_infty=4 mu_infty=8 Linf_intersection=6 polar=13 genus_defect=10')
