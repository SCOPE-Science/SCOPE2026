"""Exact-rational checks for directed circular two-kernel transfer formulas.

Run: python3 verify.py. The analytic proof covers arbitrary real parameters;
this finite script checks sampled matrix identities, not the full theorem.
"""
from fractions import Fraction as F
from itertools import combinations
from math import sqrt


def determinant(mat):
    n = len(mat)
    a = [[F(v) for v in row] for row in mat]
    sign = 1
    product = F(1)
    for j in range(n):
        k = next((i for i in range(j, n) if a[i][j]), None)
        if k is None:
            return F(0)
        if k != j:
            a[k], a[j] = a[j], a[k]
            sign = -sign
        pivot = a[j][j]
        product *= pivot
        for i in range(j + 1, n):
            coeff = a[i][j] / pivot
            for t in range(j + 1, n):
                a[i][t] -= coeff * a[j][t]
            a[i][j] = F(0)
    return product * sign


def elementary(weights, order):
    return sum((__import__('math').prod(weights[i] for i in z)
                for z in combinations(range(len(weights)), order)), F(0))


def principal_sum(mat, order):
    return sum((determinant([[mat[i][j] for j in ids] for i in ids])
                for ids in combinations(range(len(mat)), order)), F(0))

q = F(1, 256)
w = [F(1), F(2, 3), F(3, 2), F(5, 4), F(7, 5), F(11, 6)]
layouts = ([0, 1, 2, 3, 4, 5], [0, 1, 3, 4, 6, 7])
checks = 0
for n in range(2, 7):
    for layout in layouts:
        x = layout[:n]
        # With L=1, alpha=8 log(2), the normalized wrapped
        # exponential kernel at forward distance m/8 equals 2**(-m).
        M = []
        for i in range(n):
            row = []
            for j in range(n):
                m = (x[i] - x[j]) % 8
                row.append(w[i] * F(1, 2**m))
            M.append(row)
        for k in range(1, n + 1):
            got = principal_sum(M, k)
            predicted = (1 - q)**(k - 1) * elementary(w[:n], k)
            assert got == predicted, (n, layout, k, got, predicted)
            checks += 1

# Wrapped Erlang-2 kernel after cancelling the global prefactor
# alpha**2/(1-q). With L=1, the residual kernel is
# e**(-alpha*d)*(d+a), a=q/(1-q).
a = q/(1 - q)
w1, w2 = F(2, 3), F(7, 5)
radii = []
for m in range(1, 8):
    d = F(m, 8)
    def kval(t):
        assert (8*t).denominator == 1
        return F(1, 2**int(8*t)) * (t + a)
    matrix = [[w1 * kval(F(0)), w1 * kval(1 - d)],
              [w2 * kval(d), w2 * kval(F(0))]]
    det = determinant(matrix)
    assert det == -q*w1*w2*d*(1-d)
    trace = a*(w1 + w2)
    disc = trace*trace + 4*q*w1*w2*d*(1-d)
    rho_direct = (float(trace) + sqrt(float(trace*trace - 4*det)))/2
    rho_formula = (float(trace) + sqrt(float(disc)))/2
    assert abs(rho_direct - rho_formula) < 1e-13
    radii.append(rho_formula)
    checks += 2
assert radii[0] < radii[1] < radii[2] < radii[3]
assert radii[3] > radii[4] > radii[5] > radii[6]
assert max(radii) == radii[3]
print('PASS: %d exact-rational principal-minor/determinant checks' % checks)
print('PASS: wrapped Erlang-2 Perron root uniquely maximal at antipodal separation on tested grid')
print('Normalised Erlang-2 Perron roots: %s' % ', '.join('%.12g'%z for z in radii))
