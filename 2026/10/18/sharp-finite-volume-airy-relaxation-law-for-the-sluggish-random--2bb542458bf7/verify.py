"""Reproducibility checks for the spectral gap of a confined sluggish walk.

Requires Python 3, numpy, scipy. The analytic infinite-length proof is in RESULT.md;
finite matrices only corroborate its derived identities and asymptotics.
"""

from fractions import Fraction
from math import sqrt
import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigh_tridiagonal
from scipy.optimize import brentq
from scipy.special import airy

checks = 0

def check(cond, description):
    global checks
    assert cond, description
    checks += 1


def weights(L):
    return [abs(k) + 2 for k in range(-L, L + 1)]


def matrices(L):
    w = np.array(weights(L), dtype=float)
    d = np.full(2 * L + 1, 2.0) / w
    d[0] = 1 / w[0]
    d[-1] = 1 / w[-1]
    e = -1 / np.sqrt(w[:-1] * w[1:])
    return d, e


def gap(L):
    d, e = matrices(L)
    vals = eigh_tridiagonal(d, e, select='i', select_range=(0, 1),
                            eigvals_only=True, check_finite=True)
    return float(vals[1])


def odd_gap(L):
    w = np.arange(3, L+3, dtype=float)
    d = 2 / w
    d[-1] = 1 / w[-1]
    e = -1 / np.sqrt(w[:-1] * w[1:])
    return float(eigh_tridiagonal(d, e, select='i', select_range=(0, 0),
                                  eigvals_only=True)[0])

# Rational detailed balance, transition stochasticity, normalization.
for L in range(1, 31):
    w = weights(L)
    Z = sum(w)
    check(Z == L * L + 5 * L + 2, f'normalization {L}')
    for i in range(2*L+1):
        k = i-L
        p_left = Fraction(1,w[i]) if i else Fraction(0)
        p_right = Fraction(1,w[i]) if i<2*L else Fraction(0)
        p_stay = Fraction(1) - p_left - p_right
        check(p_stay >= 0, f'nonnegative holding {L} {k}')
        check(p_left + p_stay + p_right == 1, f'row sum {L} {k}')
        if i<2*L:
            check(Fraction(w[i], Z)*p_right ==
                  Fraction(w[i+1], Z)*Fraction(1,w[i+1]),
                  f'detailed balance {L} {k}')
    # The first positive eigenvalue belongs to the odd subspace.
    check(abs(gap(L)-odd_gap(L)) < 3e-11, f'odd first mode L={L}')

# Airy Dirichlet-Neumann characteristic equation.
def F(b):
    a, ap, bi, bip = airy(-b)
    return ap - bip / sqrt(3)

b = brentq(F, 1.3, 1.8, xtol=2e-14)
mu = b**3
check(abs(F(b)) < 1e-13, 'Airy root')
check(3.476618 < mu < 3.476620, 'first root location')

def u(x):
    a, ap, bi, bip = airy(-b*x)
    return a - bi/sqrt(3)

check(abs(u(0)) < 1e-14, 'Dirichlet endpoint')
check(abs(-b*F(b)) < 2e-13, 'Neumann endpoint')
J = quad(lambda x: x*u(x)**2, 0, 1, epsabs=1e-13)[0]
K = quad(lambda x: u(x)**2, 0, 1, epsabs=1e-13)[0]
I = quad(lambda x: (-b*(airy(-b*x)[1]-airy(-b*x)[3]/sqrt(3)))**2,
         0, 1, epsabs=1e-13)[0]
check(abs(I/J-mu) < 1e-11, 'Rayleigh identity')
check(abs(u(1)**2-3*J) < 1e-11, 'virial endpoint identity')
c = mu*(u(1)**2/2 + 2*K)/J
check(14.91835 < c < 14.91837, 'finite-size correction coefficient')

for L in (20,30,40,50,75,100,150,200,300,500,800,1200):
    eigen = gap(L)
    check(0 < eigen < 1, f'positive spectral gap L={L}')
    scaled = eigen*L**3
    check(scaled < mu, f'leading limit approach from below L={L}')
    check(abs(scaled-mu+c/L) <= 90/L**2,
          f'two-term asymptotic remainder L={L}')

print('checks_passed:', checks)
print('airy_root_b:', format(b,'.15f'))
print('mu:',format(mu,'.15f'))
print('c:', format(c,'.15f'))
for L in (20, 50, 100, 200, 500, 1000):
    scaled = L**3*gap(L)
    print(f'L={L:4d}, L^3 gap={scaled:.12f}, L^2 residual={L**2*(scaled-mu+c/L):.9f}')
