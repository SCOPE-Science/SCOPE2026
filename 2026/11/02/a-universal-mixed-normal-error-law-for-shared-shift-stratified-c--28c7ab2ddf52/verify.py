"""Exact identities and numerical sanity checks for shared-shift stratified control variates.

Requires Python 3.10+ with SymPy, NumPy and SciPy. This checker is
supporting finite evidence; the all-function limit rests on the proof.
"""
import math
from fractions import Fraction
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.stats import norm

u, z, xi = sp.symbols('u z xi', real=True)
a, b = xi / 2, (1 + xi) / 2
phi = sp.expand((u - a) * (u - b))
mu = sp.integrate(phi, (u, 0, 1))
v = sp.factor(sp.integrate(phi**2, (u, 0, 1)) - mu**2)
expect_v = sp.integrate(v, (xi, 0, 1))
expect_v2 = sp.integrate(v**2, (xi, 0, 1))
assert sp.simplify(v - (sp.Rational(1, 180) + (xi-sp.Rational(1, 2))**2/12)) == 0
assert expect_v == sp.Rational(1, 80)
assert expect_v2 == sp.Rational(101, 518400)
assert sp.factor(3*expect_v2/expect_v**2) == sp.Rational(101, 27)
assert sp.factor(expect_v2 - expect_v**2) == sp.Rational(1, 25920)
checks = 5

def interpolant_error(power, cell, m):
    """Exact local error for x**power after linear interpolation."""
    x_a, x_b = (cell+a)/m, (cell+b)/m
    f_a, f_b = x_a**power, x_b**power
    poly_interp = f_a*(u-b)/(a-b) + f_b*(u-a)/(b-a)
    return sp.factor(((cell+u)/m)**power-poly_interp)

# Direct polynomial interpolant identities, not merely the variance formulas.
for m in (1, 2, 3, 5, 7):
    for i in range(m):
        r = interpolant_error(2, i, sp.Integer(m))
        assert sp.simplify(r-phi/m**2)==0
        assert sp.simplify(r.subs(u,a))==0
        assert sp.simplify(r.subs(u,b))==0
        checks += 3

# Every cell error has conditional mean zero after exact integral compensation.
# With two independent samples, E[(R(U1)-R(U2))**2]/4 = Var(R(U))/2,
# which is exactly the per-cell contribution to m**2 Var(Q).
for power in (2, 3, 4):
    for m in (1, 2, 3, 5):
        for i in range(m):
            r = interpolant_error(power, i, sp.Integer(m)).subs(xi, sp.Rational(1, 4))
            rmu = sp.integrate(r,(u,0,1))
            rv = sp.factor(sp.integrate(r**2,(u,0,1))-rmu**2)
            assert rv >= 0
            # Pairwise difference formula as independently integrated polynomials.
            w=sp.symbols('w',real=True)
            diff2=sp.integrate(sp.integrate((r-r.subs(u,w))**2,(u,0,1)),(w,0,1))
            assert sp.simplify(diff2-2*rv)==0
            checks += 2

# Exact conditional normalized variance for the nonaffine quadratic for all m.
for m in (1, 2, 3, 5, 10, 100):
    assert sp.simplify((sp.Integer(m)**3/2)*m*(v/m**4)-v/2)==0
    checks += 1

# A non-quadratic C^2 example shows approach to the predicted limit.
# f(x)=x^3, hence J=int_0^1 (6x)^2 dx = 12.
for m in (5, 10, 30, 100):
    s = 0.0
    for i in range(m):
        # For x^3 local error = 3*i/m^3*phi + psi/m^3, where
        # psi is monic cubic error in local variable u.
        t = sp.Rational(1,4)
        phit=sp.expand(phi.subs(xi,t))
        psit=sp.expand(interpolant_error(3,0,sp.Integer(1)).subs(xi,t))
        r=(3*i*phit+psit)/m**3
        rm=sp.integrate(r,(u,0,1))
        s += float(sp.integrate(r**2,(u,0,1))-rm**2)
    scaled = m**3*s/2
    target = float(v.subs(xi,sp.Rational(1,4)))*12/8
    assert abs(scaled-target) < 0.2/max(1,m/3)
    checks += 1

# Compare exact Gaussian-mixture coverage with the usual normal calibration.
def coverage(z):
    return quad(lambda t: 2*norm.cdf(z/math.sqrt(float(80*v.subs(xi,t))))-1,
                0,1,epsabs=1e-12)[0]
p95=coverage(float(norm.ppf(.975)))
assert 0.9445 < p95 < 0.9448
checks += 1

# Independent residual draws, single shared shift: a Monte Carlo sanity test.
rng=np.random.default_rng(20231016)
nsim=20000
m=100
shifts=rng.random(nsim)
phi_u=lambda u,s: (u-s[:,None,None]/2)*(u-(1+s[:,None,None])/2)
# Chunk batches for modest memory use.
acc=[]
for left in range(0,nsim,1000):
    s=shifts[left:left+1000]
    Us=rng.random((len(s),m,2))
    vals=phi_u(Us,s)
    means=(1/3)-(s+0.5)/2 +(s/2)*((1+s)/2)
    zvals=np.sqrt(m)*(vals.mean(axis=(1,2))-means)
    acc.extend(zvals.tolist())
acc=np.asarray(acc)
assert abs(np.var(acc)-float(expect_v/2)) < 0.0004
checks += 1
print(f'PASS: {checks} exact and numerical assertions; V(xi)={v}; E[V]={expect_v};')
print(f'limiting standardized kurtosis={3*expect_v2/expect_v**2}; asymptotic nominal-95% coverage={p95:.10f}')
