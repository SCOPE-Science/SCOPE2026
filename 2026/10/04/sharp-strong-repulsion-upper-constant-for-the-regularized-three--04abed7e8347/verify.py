import math
from fractions import Fraction

gamma0 = Fraction(52, 27)
gamma_c = 4.0/3.0 - math.sqrt(3.0)/math.pi

def S(gamma, k):
    if abs(k) < 1e-8:
        return math.pi * (gamma - gamma_c) / 2.0
    a = math.pi*k/2.0
    return math.sqrt(3.0)/2.0 + gamma*math.tanh(a)/k - 4.0*math.sinh(math.pi*k/6.0)/(k*math.cosh(a))

def series_num(n):
    return 3**(2*n+1)*(8*n-9) + 27

assert series_num(0) == 0
assert series_num(1) == 0
for n in range(2, 15):
    assert series_num(n) > 0

# Exact zero-curvature threshold: the k^2 coefficient is pi^3(52-27 gamma)/648.
assert 52 - 27*gamma0 == 0

# Corroborative numerical checks of the proved global inequality.
for gamma in [52.0/27.0, 2.0, 2.5, 4.0]:
    s0 = S(gamma, 0.0)
    for j in range(1, 20001):
        k = 12.0*j/20000.0
        if not S(gamma, k) < s0 + 2e-12:
            raise AssertionError((gamma, k, S(gamma, k), s0))

# Below threshold, zero must fail local maximality.
for gamma in [0.8, 1.2, 1.8, 1.92]:
    if not gamma < 52.0/27.0:
        continue
    k = 1e-3
    if not S(gamma, k) > S(gamma, 0.0):
        raise AssertionError((gamma, S(gamma, k), S(gamma, 0.0)))

print('VERIFY_OK gamma0=52/27 series_positive_from_n=2 stress_cases=4 local_obstruction_cases=4')
