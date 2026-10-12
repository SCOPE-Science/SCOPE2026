from fractions import Fraction
from math import log

lam = Fraction(1, 1)
delta = Fraction(1, 10_000_000_000)
beta = 2
r = 10
gamma0 = Fraction(1, 4)
tau = lam / (lam + delta)

def jcount(gamma):
    j = 0
    while (beta ** j) * gamma < tau:
        j += 1
    return j

def rho(gamma):
    j = jcount(gamma)
    return Fraction(1, 1) - tau / ((beta ** j) * gamma)

assert jcount(gamma0) == 2
assert rho(gamma0) == 1 - tau
assert rho(gamma0) == delta / (1 + delta)

# Checkpoint evolution with the source's multiplicative 1.1 aggressive update.
gamma = gamma0
n = 0
while gamma < tau / 2:
    assert jcount(gamma) == 2
    # Two backtracks per iteration gives 2r > r, hence aggressive scaling.
    assert 2 * r > r
    gamma *= Fraction(11, 10)
    n += 1
assert n == 8
assert gamma == Fraction(214358881, 400000000)
assert tau / 2 < gamma < tau
assert jcount(gamma) == 1
# Exactly one backtrack per iteration gives total r, the balanced unchanged case.
assert 1 * r == r

rho0 = rho(gamma0)
rho8 = rho(gamma)
assert Fraction(0, 1) < rho8 < Fraction(1, 2)

# Exact one-backtrack band samples: j=1 and checkpoint scale is unchanged.
for k in range(1, 100):
    # Convex combinations of the two open endpoints tau/2 and tau.
    q = Fraction(k, 100)
    g = (Fraction(1, 1) - q) * (tau / 2) + q * tau
    assert tau / 2 < g < tau
    assert jcount(g) == 1
    rr = rho(g)
    assert Fraction(0, 1) < rr < Fraction(1, 2)

print('VERIFY_OK')
print('N=', n)
print('gamma8=', format(float(gamma), '.10f'))
print('tau=', format(float(tau), '.12f'))
print('rho0=', format(float(rho0), '.13g'))
print('rho8=', format(float(rho8), '.13f'))
print('objective_factor8=', format(float(rho8 * rho8), '.14f'))
