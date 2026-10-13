"""Reproduce exact identities and illustrative quadrature for a rational copula.

Requires Python 3 with sympy, numpy, scipy. Run: python check.py
The symbolic tests concern identities, not a computer-assisted proof of
positivity or of the global optimum. Those arguments are in RESULT.md.
"""
import numpy as np
import sympy as sp
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq
from scipy.special import spence

u, v, a = sp.symbols('u v a', real=True)
C = u*v*(1-a*u)*(1-a*v)/((1-a)*(1-a*u*v))
N = (a*(1-u)*(1-v) + (1-a*u)*(1-a*v)
     - a*(1-a*u*v)**3)
c = N / ((1-a)*(1-a*u*v)**3)
assert sp.factor(sp.diff(C, u, v) - c) == 0
assert sp.factor(C - u*v - a*u*v*(1-u)*(1-v)
                 / ((1-a)*(1-a*u*v))) == 0
assert sp.factor(C.subs(v, 1)-u) == 0
assert sp.factor(C.subs(u, 1)-v) == 0
print('Symbolic identities: PASS')

def quadrature(degree):
    nodes, weights = leggauss(degree)
    nodes, weights = (nodes+1)/2, weights/2
    x, y = nodes[:, None], nodes[None, :]
    q = x*y
    w = q*(1-x)*(1-y)*weights[:, None]*weights[None, :]
    def ab(t):
        den = (1+t*q)**2
        return np.sum(w/den), np.sum(w*q/den)
    def H(t):
        A, B = ab(t)
        return t*t*B/A
    def rho(t):
        return -12*t/(1+t)*np.sum(w/(1+t*q))
    root = brentq(lambda t: H(t)-1, 2, 3, xtol=1e-13)
    return root, rho(root), rho(2), H(2), H(3)

def published_spearman(alpha):
    # The dilogarithm convention here is Li_2(alpha) = spence(1-alpha).
    return (12*(1+alpha)*spence(1-alpha) - 3*alpha*(12+alpha)
            - 24*(1-alpha)*np.log1p(-alpha)) / (alpha*alpha*(1-alpha))

runs = [quadrature(n) for n in (64, 96, 144)]
for n, z in zip((64, 96, 144), runs):
    print(f'degree {n}: t*={z[0]:.14f}, rho*={z[1]:.14f}, '
          f'rho(-2)={z[2]:.14f}, H(2)={z[3]:.9f}, H(3)={z[4]:.9f}')
    assert 2 < z[0] < 3 and z[1] < z[2] < 0
    assert z[3] < 1 < z[4]
    assert abs(z[1] - published_spearman(-z[0])) < 2e-12
    assert abs(z[2] - published_spearman(-2)) < 2e-12
for lower, upper in zip(runs[:-1], runs[1:]):
    assert np.max(np.abs(np.array(lower) - np.array(upper))) < 1e-10

cv = sp.lambdify((u, v, a), c, 'numpy')
grid = np.linspace(0, 1, 81)
for aa in (-200, -10, -3, -2, -0.1, 0, 0.2, 0.5):
    got = cv(grid[:, None], grid[None, :], aa)
    assert np.min(got) >= -1e-12, (aa, np.min(got))
assert cv(0, 1, sp.Rational(3, 4)) < 0
print('Illustrative density grid and stable numerical root: PASS')
