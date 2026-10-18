"""Independent algebraic and quadrature checks for a noisy two-history AA update.

Requires scipy for deterministic Gaussian quadrature; all coefficient identities
and exact update formulas are checked using rational arithmetic.
"""
from fractions import Fraction as F
from itertools import product
from math import exp, pi, sqrt
from scipy.integrate import quad

CHECKS = 0
for q, sigma, u, v in product([F(1, 4), F(1, 3), F(1, 2), F(2, 3), F(3, 4)],
                               [F(1, 10), F(1, 2), F(3, 4)],
                               [F(-3, 2), F(-1, 3), F(0), F(2, 3), F(5, 4)],
                               [F(-2, 1), F(-1, 5), F(0), F(1, 4), F(4, 3)]):
    e0, e1 = sigma*u, sigma*v
    d = 1-q
    y0 = q+e0
    x1 = y0
    y1 = q*x1+e1
    r0, r1 = y0-1, y1-x1
    D = r0-r1
    assert D == -d*d+(2-q)*e0-e1
    assert r1 == -q*d-d*e0+e1
    assert y1 == 1+D+2*r1
    if D:
        t = -r1/D
        assert t*y0+(1-t)*y1 == y1+r1*r1/D
    for lam in (F(1, 100), F(3, 10)):
        t = -D*r1/(D*D+lam)
        assert (y1-t*r1) == y1+r1*r1*D/(D*D+lam)
        t_sym = (lam-D*r1)/(D*D+2*lam)
        assert (y1-t_sym*r1) == y1+(D*r1*r1-lam*r1)/(D*D+2*lam)
    CHECKS += 1

q, sigma = F(1, 2), F(1, 2)
d, a = 1-q, 2-q
B=a*a+1
C=-a*d-1
m = -q*d+C*d*d/B
v = sigma*sigma/B
assert m == -d*(2+d)/B
# The Gaussian regression variance follows from a determinant-one noise map.
assert (d*d+1)*B-C*C == 1

q, sigma = float(q), float(sigma)
d, B, C, m, v = map(float,(d,B,C,m,v))
h = exp(-d**4/(2*sigma*sigma*B))/sqrt(2*pi*sigma*sigma*B)
M4=m**4+6*m*m*v+3*v*v
K=(pi/2)*h*M4

def gaussian_moments(D):
    mu = -q*d+(C/B)*(D+d*d)
    return mu, mu*mu+v, mu**3+3*mu*v, mu**4+6*mu*mu*v+3*v*v

def integrand(D, lam, symmetric=False):
    mu, mom2, mom3, mom4 = gaussian_moments(D)
    A = 1+D
    if symmetric:
        b = 2-lam/(D*D+2*lam)
        c = D/(D*D+2*lam)
    else:
        b = 2
        c = D/(D*D+lam)
    expected = A*A+2*A*b*mu+(b*b+2*A*c)*mom2+2*b*c*mom3+c*c*mom4
    density = exp(-(D+d*d)**2/(2*sigma*sigma*B))/sqrt(2*pi*sigma*sigma*B)
    return expected*density

for sym in (False, True):
    target = K/(sqrt(2) if sym else 1)
    errors = []
    for lam in (1e-3,1e-4,1e-5,1e-6):
        fn = lambda z:integrand(z,lam,sym)
        val = quad(fn,-8,0,epsabs=1e-8,epsrel=1e-8,limit=150)[0]+quad(fn,0,8,epsabs=1e-8,epsrel=1e-8,limit=150)[0]
        errors.append(abs(sqrt(lam)*val-target))
    assert all(errors[j+1] < errors[j] for j in range(len(errors)-1))
    assert errors[-1] < 5e-4
    print('symmetric',sym,'sharp coefficient',f'{target:.12g}','last absolute deviation',f'{errors[-1]:.8g}')
print('Exact rational update checks:', CHECKS)
