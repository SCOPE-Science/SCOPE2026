import math
from fractions import Fraction

# Exact prey-direction check at the predator-free state.
r = Fraction(2, 1)
a = Fraction(1, 1)
xbar_q = r / a
assert r - 2 * a * xbar_q == -r

# One admissible finite-lifespan instance of the source functional forms.
xbar = float(xbar_q)
tau_star = 1.0
nu = 4.0
L = 30.0
k = 2.0
bp = 0.5
bep = 0.2
zeta = 0.3
dp = 0.3
dep = 0.05
muM = 0.2
rho = 0.2


def phi_ge(t):
    return 1.0 / (1.0 + math.exp(-nu * (t - tau_star)))


def A(t):
    # Integral from 0 to t of 1/(1+exp(nu*(s-tau_star))) ds.
    return t - (math.log1p(math.exp(nu * (t - tau_star)))
                - math.log1p(math.exp(-nu * tau_star))) / nu


def B(t):
    tilde = 0.0 if t < tau_star else bp * (math.exp(-bep * (t - tau_star)) + 1.0)
    return k * xbar * phi_ge(t) + tilde * (1.0 - math.exp(-zeta * xbar))


hunger = muM * math.exp(-rho * xbar)


def M0(t):
    return dp * math.exp(-dep * L) * (math.exp(dep * t) - 1.0) / dep + hunger * t


def trap_integral(func, n=24000):
    h = L / n
    s = 0.5 * (func(0.0) + func(L))
    for i in range(1, n):
        s += func(i * h)
    return s * h


def R(g):
    return trap_integral(lambda t: B(t) * math.exp(-M0(t) - g * xbar * A(t)))


def minus_Rprime(g):
    return xbar * trap_integral(lambda t: A(t) * B(t) * math.exp(-M0(t) - g * xbar * A(t)))

# A(t) is positive away from zero for the smooth source indicator.
for t in (0.01, 0.1, 1.0, 5.0, L):
    assert A(t) > 0.0

# Strict monotonicity on a broad test grid.
grid = [0.0, 0.2, 0.5, 1.0, 2.0, 4.0]
rv = [R(g) for g in grid]
assert all(rv[i] > rv[i + 1] for i in range(len(rv) - 1))

# Numerical derivative agrees with the differentiated integral.
g0 = 0.8
eps = 1e-4
fd = -(R(g0 + eps) - R(g0 - eps)) / (2.0 * eps)
analytic = minus_Rprime(g0)
assert abs(fd - analytic) / analytic < 2e-5

# This instance starts above one and falls below one, so bisection finds one crossing.
assert R(0.0) > 1.0 and R(4.0) < 1.0
lo, hi = 0.0, 4.0
for _ in range(60):
    mid = 0.5 * (lo + hi)
    if R(mid) > 1.0:
        lo = mid
    else:
        hi = mid
gc = 0.5 * (lo + hi)
assert abs(R(gc) - 1.0) < 2e-8

# The real Euler-Lotka root has the same sign as R(g)-1.
def F(lam, g):
    return trap_integral(lambda t: B(t) * math.exp(-M0(t) - g * xbar * A(t) - lam * t))


def root_lambda(g):
    # Finite lifespan guarantees a continuous strictly decreasing transform in lambda.
    lo, hi = -4.0, 4.0
    assert F(lo, g) > 1.0 and F(hi, g) < 1.0
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        if F(mid, g) > 1.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)

assert root_lambda(max(0.0, gc - 0.2)) > 0.0
assert root_lambda(gc + 0.2) < 0.0
print('VERIFY_OK')
