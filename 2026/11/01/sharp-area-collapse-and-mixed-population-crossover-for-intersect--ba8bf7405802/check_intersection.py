"""Numerical reproduction of Brownian-hull intersection coverage asymptotics.

Requires SciPy and NumPy; analytic infinite-parameter proofs are in RESULT.md.
"""
import math
from scipy.integrate import quad
from scipy.special import k0, digamma

GAMMA = -float(digamma(1))
C = 2 * math.sqrt(2) / math.pi**1.5
DK = 1 + 1.5*math.log(2) - GAMMA/2
DB = 1 + math.log(2) - GAMMA


def f_open_derivative(r):
    return C/2 * math.exp(-r*r/4) * k0(r*r/4)


def f_bridge_derivative(r):
    return 2*r * math.exp(-r*r) * k0(r*r)


def F_open_bessel(r):
    return r * quad(lambda t: f_open_derivative(r*t), 0, 1, epsabs=5e-11)[0]


def F_bridge_bessel(r):
    return r*r * quad(lambda t: 2*t*math.exp(-r*r*t*t)*k0(r*r*t*t), 0, 1, epsabs=5e-11)[0]


def F_open_original(r):
    # arcsine radial mixture: rho = |N(0,1)| |cos(theta)|.
    return 2/math.pi * quad(lambda theta: math.erf(r/(math.sqrt(2)*math.cos(theta))), 0, math.pi/2)[0]


def F_bridge_original(r):
    # bridge radial mixture: rho = sqrt(V(1-V))*Rayleigh(1).
    return quad(lambda v: -math.expm1(-r*r/(2*v*(1-v))), 0, 1)[0]


checks = 0
for r in (0.02,0.1,0.4,0.9):
    for bessel, original in ((F_open_bessel, F_open_original),
                             (F_bridge_bessel, F_bridge_original)):
        a,b=bessel(r), original(r)
        assert abs(a-b) < 2e-9, (r,a,b)
        checks += 1
for r in (1e-3,1e-4):
    f=F_open_bessel(r)
    g=F_bridge_bessel(r)
    assert abs(f/(C*r) - (math.log(1/r)+DK)) < 1e-4
    assert abs(g/(r*r) - (2*math.log(1/r)+DB)) < 1e-4
    checks += 2
assert abs((2*math.log(C)+2*DK-3+2*GAMMA) - (3*math.log(4/math.pi)-1+GAMMA)) < 1e-12
assert abs((DB-1+GAMMA)-math.log(2))<1e-12
checks+=2

# The unique joint critical scaling is n ~ lambda*m^2 log(m).
m=10**60
L=math.log(m)
lam=0.65
n=int(lam*m*m*L)
a=1/(C*m*L)
eta=math.pi**3*lam/4
for x in (0.3,1,1.7):
    p=math.exp(m*math.log1p(-F_open_bessel(a*x)) + n*math.log1p(-F_bridge_bessel(a*x)))
    target=math.exp(-x-eta*x*x)
    assert abs(p-target)<0.025, (x,p,target)
    checks+=1

# Compare exact one-dimensional mean-area integrals with first and second asymptotic orders.
for m in (10**6,10**8):
    L=math.log(m)
    a=1/(C*m*L)
    y=2*math.pi*a*a*quad(lambda x: x*math.exp(m*math.log1p(-F_open_bessel(a*x))), 0, 45, epsabs=1e-9)[0]
    base=math.pi**4/(4*m*m*L*L)
    correction=1-(2*math.log(L)+3*math.log(4/math.pi)-1+GAMMA)/L
    assert 0 < y/base < 1
    assert abs(y/base-correction)<0.2
    checks+=1

for n in (10**6,10**8):
    L=math.log(n)
    b=1/math.sqrt(n*L)
    y=2*math.pi*b*b*quad(lambda x: x*math.exp(n*math.log1p(-F_bridge_bessel(b*x))), 0, 20, epsabs=1e-9)[0]
    base=math.pi/(n*L)
    correction=1-(math.log(L)+math.log(2))/L
    assert 0 < y/base < 1
    assert abs(y/base-correction)<0.15
    checks+=1

for lam in (0,0.1,1,10):
    y=quad(lambda x:x*math.exp(-x-(math.pi**3*lam/4)*x*x),0,math.inf)[0]
    assert 0<y<=1+1e-12
    checks+=1
print(f'INTERSECTION_CHECK_OK: {checks} independent numerical/algebraic checks; mixed crossover and two pure second-order expansions')
