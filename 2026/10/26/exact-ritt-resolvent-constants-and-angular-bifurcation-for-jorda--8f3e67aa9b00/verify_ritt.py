"""Supplementary reproducibility checks for an exact two-dimensional Ritt resolvent formula.
The published proof is analytical; sampling here is not a substitute for it.
Requires only Python's standard library.
"""
import math
import cmath

SQRT = math.sqrt
QSTAR = (7 - 2 * SQRT(6)) / 5

def triangular_norm(x):
    return (SQRT(4 + x * x) + x) / 2

def closed(q):
    assert 0 <= q < 1
    if q <= QSTAR:
        return (SQRT(5 + 6 * q + 5 * q * q) + 1 - q) / ((1 + q)**2)
    return SQRT(5) / (2 * SQRT(q))

def matrix_norm_formula(q,z):
    # Direct singular-value formula for the triangular matrix (z-1)(zI-T_q)^(-1).
    a = abs(z - q)
    return abs(z-1) / a * triangular_norm((1-q)/a)

def centered_optimal_angle(q):
    if q <= QSTAR:
        return math.pi
    return math.acos(1 - 5*(1-q)**2/(2*q))

# Algebraic stationarity and bifurcation identities.
assert abs((1-QSTAR)/(1+QSTAR) - 1/SQRT(6)) < 2e-15
assert abs(triangular_norm(1/SQRT(6)) * SQRT(5/6) - SQRT(5)/2) < 2e-15
assert abs((SQRT(5+6*QSTAR+5*QSTAR**2)+1-QSTAR)/(1+QSTAR)**2 - SQRT(5)/(2*SQRT(QSTAR))) < 2e-14

count = 0
for k in range(1,1001):
    q = k / 1002
    optimum = closed(q)
    theta = centered_optimal_angle(q)
    target = matrix_norm_formula(q, cmath.exp(1j*theta))
    assert abs(target - optimum) < 2e-11 * max(1,optimum), (q, optimum,target)
    # Independent angular samples: every prescribed angle obeys proposed global bound.
    for j in range(181):
        th=math.pi*j/180
        z=cmath.exp(1j*th)
        assert matrix_norm_formula(q,z) <= optimum + 1e-11, (q,th)
        count +=1

for q in [0, 0.1, QSTAR, 0.5, 0.9, 0.999]:
    for rho in [1.001,1.01,1.1,1.6,2,4,12,50]:
        for j in range(41):
            theta=2*math.pi*j/41
            assert matrix_norm_formula(q,rho*cmath.exp(1j*theta)) <= closed(q) + 1e-10
            count+=1
assert abs(closed(0) - (1+SQRT(5))) < 1e-14
assert abs(closed(.99999999) - SQRT(5)/2) < 1e-7
print('RITT_FORMULA_SUPPLEMENTARY_CHECKS_OK',count)
