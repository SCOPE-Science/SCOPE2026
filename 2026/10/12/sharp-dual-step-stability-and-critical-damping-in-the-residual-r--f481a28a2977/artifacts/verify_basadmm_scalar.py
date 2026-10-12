import math
import numpy as np
import sympy as sp

a, beta, sigma = sp.symbols("a beta sigma", positive=True)
d = a + beta
r = (a + beta/sp.Integer(2))/d
u = 1/(sigma*d)

T = sp.simplify(1 + r - 2*u)
D = sp.simplify(r - u)

assert sp.simplify(1 - T + D - 1/(sigma*d)) == 0
assert sp.factor(1 + T + D) == (3*beta*sigma + 4*a*sigma - 3)/(sigma*d)
assert sp.factor(1 - D) == (beta*sigma + 2)/(2*sigma*d)

Delta = sp.factor(T**2 - 4*D)
assert sp.simplify(
    Delta - (4*u**2 - 4*r*u + (1-r)**2)
) == 0
assert sp.simplify(2*r - 1 - a/d) == 0

sigma_star = 2/(a + beta/sp.Integer(2) + sp.sqrt(a*d))
rho_star = (1 - sp.sqrt(a/d))/2
u_plus = (r + sp.sqrt(2*r-1))/2
assert sp.simplify(1/(d*u_plus) - sigma_star) == 0

# At critical damping the polynomial has the double root rho_star.
Ts = sp.simplify(T.subs(sigma, sigma_star))
Ds = sp.simplify(D.subs(sigma, sigma_star))
assert sp.simplify(Ts - 2*rho_star) == 0
assert sp.simplify(Ds - rho_star**2) == 0

# Source proof coupling sigma = 2/beta.
T0 = sp.factor(T.subs(sigma, 2/beta))
D0 = sp.factor(D.subs(sigma, 2/beta))
Delta0 = sp.factor(T0**2 - 4*D0)
assert sp.simplify(T0 - (beta + 4*a)/(2*(a+beta))) == 0
assert sp.simplify(D0 - a/(a+beta)) == 0
assert sp.simplify(Delta0 - beta*(beta-8*a)/(4*(a+beta)**2)) == 0

# The source coupling matches sigma_star exactly at a/beta = 1/8.
assert sp.simplify(sigma_star.subs(a, beta/8) - 2/beta) == 0

def radius(a0, b0, s0):
    d0 = a0+b0
    r0 = (a0+b0/2)/d0
    u0 = 1/(s0*d0)
    T0 = 1+r0-2*u0
    D0 = r0-u0
    roots = np.roots([1.0, -T0, D0])
    return max(abs(z) for z in roots)

for ratio in (0.01, 0.125, 1.0, 10.0):
    a0 = ratio
    b0 = 1.0
    threshold = 3/(4*a0+3*b0)
    sstar = 2/(a0+b0/2+math.sqrt(a0*(a0+b0)))
    qstar = 0.5*(1-math.sqrt(a0/(a0+b0)))

    assert sstar > threshold
    assert abs(radius(a0,b0,sstar)-qstar) < 1e-7
    assert radius(a0,b0,threshold*1.001) < 1
    assert radius(a0,b0,threshold*0.999) > 1

    lo = threshold*1.0005
    hi = max(8.0, 8*sstar)
    grid = np.geomspace(lo, hi, 20000)
    vals = np.array([radius(a0,b0,s) for s in grid])
    assert vals.min() >= qstar - 2e-5
    assert abs(vals.min()-qstar) < 2e-3

print("VERIFY_OK")
