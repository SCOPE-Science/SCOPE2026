#!/usr/bin/env python3
import math
import sympy as sp

s = sp.symbols("s", positive=True)
rt2 = sp.sqrt(2)
D = 1 + 4*s - 4*s**2
u = (3 - 2*s - 2*rt2*(1-s))/D
poly = D*u**2 + (4*s - 6)*u + 1
assert sp.simplify(poly) == 0

disc = sp.factor((4*s-6)**2 - 4*D)
assert sp.simplify(disc - 32*(1-s)**2) == 0
assert sp.simplify(sp.limit(u, s, 0, dir="+") - (3-2*rt2)) == 0

def cert(N):
    a = math.pi/N
    ss = math.sin(a)**2
    uu = (3-2*ss-2*math.sqrt(2)*(1-ss))/(1+4*ss-4*ss*ss)
    lam = 1-uu
    A = (1-lam)*ss
    B = 0.5*(1-math.sqrt(1-lam*lam*math.tan(a)**2))
    fourth_lower = 0.5*math.tan(a)**2
    return ss, uu, lam, A, B, fourth_lower

worst_eq = 0.0
for N in range(6, 402, 2):
    ss, uu, lam, A, B, F4 = cert(N)
    assert 0 < uu < 0.5
    assert 0 < lam < 1
    worst_eq = max(worst_eq, abs(A-B))
    assert abs(A-B) < 5e-14
    assert A < F4

    best_grid = 0.0
    for k in range(1, 10000):
        x = k/10000
        aa = (1-x)*ss
        bb = 0.5*(1-math.sqrt(1-x*x*math.tan(math.pi/N)**2))
        best_grid = max(best_grid, min(aa,bb))
    assert best_grid <= A + 2e-8

vals = {N: cert(N)[3] for N in (6,8,10,12)}
assert abs(vals[6]-0.05409709377719387) < 1e-15
assert abs(vals[8]-0.028595479208968322) < 1e-15
assert abs(vals[10]-0.017791171246851263) < 1e-15
assert abs(vals[12]-0.012168482248915034) < 1e-15

print("VERIFY_OK")
print("symbolic_quadratic_identity = passed")
print("symbolic_discriminant = passed")
print("symbolic_asymptotic = passed")
print("even_N_sweep = 6..400")
print("max_active_bound_error = %.3e" % worst_eq)
