from fractions import Fraction
import sympy as sp

u, v, k = sp.symbols("u v k", real=True)
z = sp.symbols("z", real=True)
Pz = 125*z**3 - 81*z**2 + 39*z - 11
Pu = 125*u**6 - 81*u**4 + 39*u**2 - 11
vexpr = (153 - 250*u**5 + 1125*u**4 - 88*u**3 - 354*u**2 - 166*u) / 120
kexpr = 5*(125*u**4 - 31*u**2 + 20) / 18
Pk = 27*k**3 - 108*k**2 - 720*k - 800

# Unique z-root: derivative has negative discriminant and positive leading coefficient.
dPz = sp.diff(Pz, z)
assert sp.discriminant(dPz, z) < 0
assert sp.LC(sp.Poly(dPz, z)) > 0
assert Pz.subs(z, 0) < 0 and Pz.subs(z, 1) > 0

# Exact u bracket and uniqueness of the positive u-root.
a = sp.Rational(1281, 2000)       # 0.6405
b = sp.Rational(3203, 5000)       # 0.6406
assert Pu.subs(u, a) < 0 < Pu.subs(u, b)
# Pz has one real root, hence Pu has exactly one positive real root.

# The induced v is strictly between 0 and u on this bracket.
dv = sp.diff(vexpr, u)
assert sp.count_roots(sp.Poly(dv, u), a, b) == 0
assert dv.subs(u, a) > 0
assert vexpr.subs(u, a) > 0
assert vexpr.subs(u, b) < a

h = 2*u/(1-u**2)
y = 2*v/(1-v**2)
s = (1+u**2)/(1-u**2)
t = (1+v**2)/(1-v**2)
R = sp.factor((1+h**2)/(2*h))
r = sp.factor(h/(s+1))
rp = sp.factor(h*(h-y)*(1+h*y)/((1+h**2)*(s*t+h-y)))
assert sp.simplify(r-u) == 0

# Exact equality after imposing v(u) and k(u).
defect = sp.together(R + k*r - 2*(k+2)*rp)
defect_sub = sp.together(defect.subs({v: vexpr, k: kexpr}))
num = sp.Poly(sp.fraction(defect_sub)[0], u)
assert sp.rem(num, sp.Poly(Pu, u)).as_expr() == 0

# Exact parameter cubic.
param_num = sp.Poly(sp.together(Pk.subs(k, kexpr)).as_numer_denom()[0], u)
assert sp.rem(param_num, sp.Poly(Pu, u)).as_expr() == 0
assert sp.discriminant(Pk, k) < 0
assert Pk.subs(k, 7) < 0 < Pk.subs(k, 8)

# Strict Euler gap for the witness: u^2 != 1/3.
assert sp.rem(sp.Poly(3*u**2-1, u), sp.Poly(Pu, u)).as_expr() != 0
Euler_gap = sp.factor(R - 2*r)
assert sp.simplify(Euler_gap - (3*u**2-1)**2/(4*u*(1-u**2))) == 0

# High-precision diagnostic values from the unique positive root.
uroot = [rr for rr in sp.nroots(Pu, n=60, maxsteps=100) if abs(sp.im(rr)) < sp.Rational(1,10)**40 and sp.re(rr) > 0][0]
uv = sp.N(sp.re(uroot), 30)
vv = sp.N(vexpr.subs(u, uv), 30)
kv = sp.N(kexpr.subs(u, uv), 30)
hv = sp.N(h.subs(u, uv), 30)
yv = sp.N(y.subs({u: uv, v: vv}), 30)
assert 0 < float(vv) < float(uv) < 1
assert 7 < float(kv) < 8
print("u*=", uv)
print("v*=", vv)
print("kappa=", kv)
print("h*=", hv)
print("y*=", yv)
print("VERIFY_OK")
