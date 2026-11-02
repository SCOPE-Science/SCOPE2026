"""Exact finite-n algebraic checks for stratified power quadrature.

The mathematical proof in RESULT.md supplies the general assertions and limits.
No external packages, downloads, or certification services are needed.
"""
from fractions import Fraction as F


def variance_one_third_cubic(j):
    j = F(j)
    a = j**3 - (j-1)**3
    return 3*a - F(9, 4)*(j**2-(j-1)**2)**2


def variance_one_quarter_quartic(j):
    j = F(j)
    a = j**4 - (j-1)**4
    return 2*a*(j**2-(j-1)**2) - F(16, 9)*(j**3-(j-1)**3)**2


def closed_quartic(j):
    j = F(j)
    return F(2, 9)*(6*j*j-6*j+1)


for j in range(1, 201):
    assert variance_one_third_cubic(j) == F(3, 4)
    assert variance_one_quarter_quartic(j) == closed_quartic(j)

for n in (1, 2, 3, 5, 12, 100, 200):
    v_cubic = sum((variance_one_third_cubic(j) for j in range(1,n+1)), F()) / n**4
    assert v_cubic == F(3,4*n**3)
    v_quartic = sum((variance_one_quarter_quartic(j) for j in range(1,n+1)), F()) / n**6
    assert v_quartic == F(4,9*n**3)-F(2,9*n**5)

# Verify parameter-specific asymptotic constants and strict improvement
# over two admissible, but nonoptimal, supercritical power grades.
alpha = F(1, 4)
p_opt = F(2)/(1-alpha)

def asymptotic_constant(p):
    q = p*(1-alpha)
    assert q > F(3, 2)
    return alpha**2*p**4/(12*(2*q-3))

assert p_opt == F(8,3)
assert asymptotic_constant(p_opt) == F(64,243)
assert asymptotic_constant(F(7, 3)) > asymptotic_constant(p_opt)
assert asymptotic_constant(F(4)) > asymptotic_constant(p_opt)

print('VERIFY_OK exact cell variances; exact finite-n laws; optimal-grade benchmark')
