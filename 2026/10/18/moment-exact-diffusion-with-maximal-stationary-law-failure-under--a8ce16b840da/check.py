"""Exact rational checks for common-reset affine processes and their moment-equivalent diffusion.
Uses Python standard library only; it supplements, rather than replaces, analytic proofs.
"""
from fractions import Fraction as F
from itertools import combinations
from random import Random


def determinant(matrix):
    a = [list(map(F, row)) for row in matrix]
    n = len(a)
    value = F(1)
    for k in range(n):
        row = next((j for j in range(k, n) if a[j][k] != 0), None)
        if row is None:
            return F(0)
        if row != k:
            a[k], a[row] = a[row], a[k]
            value = -value
        v = a[k][k]
        value *= v
        for j in range(k+1, n):
            t = a[j][k] / v
            for h in range(k+1, n):
                a[j][h] -= t * a[k][h]
            a[j][k] = F(0)
    return value


def check(a, b, rate, marks):
    # marks is a list of (probability, remaining fraction) pairs.
    d = len(a)
    assert d == len(b) and len(set(a)) == d and all(v > 0 for v in a+b)
    assert sum(p for p, _ in marks) == 1
    assert all(0 <= mark <= 1 for _, mark in marks)
    delta = rate * sum(p * (1-mark) for p,mark in marks)
    kappa = rate * sum(p * (1-mark)**2 for p,mark in marks)
    zeta = rate * sum(p * (1-mark**2) for p,mark in marks)
    assert 2 * delta - kappa == zeta
    assert kappa > 0
    c = [u + delta for u in a]
    m = [b[i] / c[i] for i in range(d)]
    covariance = [[kappa*m[i]*m[j] / (a[i] + a[j] + zeta)
                   for j in range(d)] for i in range(d)]
    for i in range(d):
        assert b[i] - c[i]*m[i] == 0
        for j in range(d):
            raw = covariance[i][j] + m[i]*m[j]
            # Stationary moment equations for jump and diffusion generators coincide.
            assert b[i]*m[j] + b[j]*m[i] -(a[i]+a[j]+zeta)*raw == 0
            assert b[i]*m[j] + b[j]*m[i] -(c[i]+c[j]-kappa)*raw == 0
    pred = (kappa**d)
    for t in m: pred *= t*t
    for i,j in combinations(range(d),2): pred *= (a[j]-a[i])**2
    for i in range(d):
        for j in range(d): pred /= (a[i]+a[j]+zeta)
    assert determinant(covariance) == pred and pred > 0
    # Cubic jump-minus-diffusion generator discrepancy.
    x = F(3,5)
    i = 0
    J3 = 3*b[i]*x*x - 3*a[i]*x**3 + rate * sum(p*(mark**3-1)*x**3 for p, mark in marks)
    D3 = 3*b[i]*x*x - 3*c[i]*x**3 + 3*kappa*x**3
    assert J3 - D3 == -rate*sum(p*(1-mark)**3 for p, mark in marks)*x**3
    assert J3 != D3
    # If A=0 exactly, the exponentially distributed age gives the covariance.
    if marks == [(F(1), F(0))]:
        for i in range(d):
            for j in range(d):
                ex_i_j = (b[i]*b[j] / (a[i]*a[j]))*(
                    1-rate/(rate+a[i])-rate/(rate+a[j])+rate/(rate+a[i]+a[j]))
                assert ex_i_j - m[i]*m[j] == covariance[i][j]
    return 8 + d + 2*d*d + (d*d if marks == [(F(1),F(0))] else 0)

rng = Random(720314)
number = 0
for d in range(2,6):
    for _ in range(60):
        rates = rng.sample(range(1, 45), d)
        a = [F(k, rng.randint(2,11)) for k in rates]
        if len(set(a))<d:
            continue
        b = [F(rng.randint(1,14), rng.randint(1,11)) for _ in range(d)]
        rho = F(rng.randint(1,10), rng.randint(1,10))
        mark = F(rng.randint(0,9), 10)
        p = F(rng.randint(1,9),10)
        for marks in [[(F(1),F(0))], [(p,F(0)), (1-p,mark)]]:
            number += check(a,b,rho,marks)
print(f"PASS: {number} exact rational assertions in affine common-reset systems")
