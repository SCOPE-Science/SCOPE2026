import math
import sympy as sp

theta, a, b = sp.symbols("theta a b", real=True)
F = 1/(sp.cos(theta)+a*sp.sin(theta))**2 + 1/(sp.cos(theta)-b*sp.sin(theta))**2
assert sp.simplify(sp.diff(F, theta).subs(theta, 0) - 2*(b-a)) == 0

u, q = sp.symbols("u q", real=True)
G = 2*(1+u)*(1+q**2*u)/(1-q**2*u)**2
target = -2*(q**4*u + 3*q**2*u + 3*q**2 + 1)/(q**2*u - 1)**3
assert sp.simplify(sp.diff(G, u) - target) == 0

def ftheta(a, b, theta):
    c, s = math.cos(theta), math.sin(theta)
    d1, d2 = c+a*s, c-b*s
    if abs(d1) < 1e-12 or abs(d2) < 1e-12:
        return float("inf")
    return 1/d1**2 + 1/d2**2

def grid_min(a, b, N=200000):
    return min(ftheta(a,b,2*math.pi*j/N) for j in range(N))

for qv in [0.0, 0.5, 1.0, 1.5, -1.5]:
    expected = 2/max(1, qv*qv)
    assert abs(grid_min(qv,qv)-expected) < 2e-5

for av,bv in [(0.5,0.4),(-0.2,0.7),(2.0,-2.0)]:
    assert grid_min(av,bv) < 2-1e-5

print("VERIFY_OK")
