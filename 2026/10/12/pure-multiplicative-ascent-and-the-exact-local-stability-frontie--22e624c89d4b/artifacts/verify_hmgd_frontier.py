import math
import sympy as sp

theta, a, c, h, etaA, etaM = sp.symbols(
    "theta a c h etaA etaM", positive=True
)

L = c + sp.Rational(1, 2) * h * (theta - a) ** 2
g = sp.diff(L, theta)
m = sp.simplify(theta * g / L)
mp = sp.simplify(sp.diff(m, theta).subs(theta, a))
assert sp.simplify(mp - a*h/c) == 0

q = sp.simplify(1 - etaA*h/sp.Integer(2) + etaM*mp)
assert sp.simplify(q - (1 - etaA*h/2 + etaM*a*h/c)) == 0

def sigmoid(z):
    return 1.0 / (1.0 + math.exp(-z))

def slog(z):
    if z > 0.0:
        return math.log1p(z)
    if z < 0.0:
        return -math.log1p(-z)
    return 0.0

def step(x, aa, cc, hh, eA, eM):
    LL = cc + 0.5*hh*(x-aa)**2
    gg = hh*(x-aa)
    mm = x*gg/LL
    return x - eA*gg*sigmoid(mm) + eM*slog(mm)

aa, cc, hh = 2.0, 4.0, 1.0
eA, eM = 1.0, 0.2
qq = 1.0 - eA*hh/2.0 + eM*aa*hh/cc
assert abs(qq) < 1.0
x = aa + 1e-6
ratio = abs(step(x, aa, cc, hh, eA, eM)-aa)/abs(x-aa)
assert abs(ratio-abs(qq)) < 1e-5

eA, eM = 0.0, 0.3
qq = 1.0 + eM*aa*hh/cc
assert qq > 1.0
x = aa + 0.25
last_inc = None
for _ in range(20000):
    xn = step(x, aa, cc, hh, eA, eM)
    assert xn > x
    last_inc = xn - x
    x = xn
assert x > 100.0
assert abs(last_inc - eM*math.log(3.0)) < 1e-3

for X in (1e3, 1e4, 1e5):
    LL = cc + 0.5*hh*(X-aa)**2
    mm = X*hh*(X-aa)/LL
    assert abs(mm-2.0) < 0.02

print("VERIFY_OK")
