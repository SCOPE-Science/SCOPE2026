"""Exact rational checks for stationary fourth-cumulant formulas.

No stochastic simulation or external data is used. The proof is analytic;
these independent fraction calculations test the moment and determinant formulas.
"""
from fractions import Fraction as F
from itertools import combinations
from math import prod


def determinant(M):
    n = len(M)
    a = [row.copy() for row in M]
    val = F(1)
    for j in range(n):
        p = next((k for k in range(j, n) if a[k][j]), None)
        if p is None:
            return F(0)
        if p != j:
            a[j], a[p] = a[p], a[j]
            val = -val
        pivot = a[j][j]
        val *= pivot
        for i in range(j + 1, n):
            factor = a[i][j] / pivot
            for k in range(j, n):
                a[i][k] -= factor * a[j][k]
    return val


def check(rate, drift, noise):
    m = len(drift)
    a = [2*x for x in drift]
    c = [noise[i]/drift[i] for i in range(m)]
    mean = [c[i]*(1-rate/(rate+a[i])) for i in range(m)]
    energy2 = [c[i]**2*(1-2*rate/(rate+a[i])+rate/(rate+2*a[i])) for i in range(m)]
    measured = []
    for i in range(m):
        row=[]
        for j in range(m):
            if i == j:
                z = (energy2[i] - mean[i]**2)/mean[i]**2
            else:
                cross = c[i]*c[j]*(1-rate/(rate+a[i])-rate/(rate+a[j])+rate/(rate+a[i]+a[j]))
                z = (cross - mean[i]*mean[j])/(mean[i]*mean[j])
            row.append(z)
        measured.append(row)
    b = [x/rate for x in a]
    predicted = [[1/(1+b[i]+b[j]) for j in range(m)] for i in range(m)]
    assert measured == predicted, (measured, predicted)
    for i,j in combinations(range(m),2):
        assert measured[i][j] == 2*measured[i][i]*measured[j][j]/(measured[i][i]+measured[j][j])
    expected_det = prod((b[j]-b[i])**2 for i,j in combinations(range(m),2))/prod(1+b[i]+b[j] for i in range(m) for j in range(m))
    assert determinant(predicted) == expected_det
    for k in range(1,m+1):
        for rows in combinations(range(m),k):
            for cols in combinations(range(m),k):
                minor = determinant([[predicted[i][j] for j in cols] for i in rows])
                distinct_row = len({b[i] for i in rows}) == k
                distinct_col = len({b[j] for j in cols}) == k
                assert minor > 0 if distinct_row and distinct_col else minor == 0
    recovered = [(1/row[i]-1)/2 for i,row in enumerate(measured)]
    assert recovered == b
    return str(determinant(predicted)), m


cases = [
    (F(3), [F(1,2),F(2),F(9,2)], [F(2),F(3),F(5)]),
    (F(3), [F(1,2),F(1,2),F(9,2)], [F(2),F(3),F(5)]),
    (F(5), [F(1),F(4),F(9),F(16)], [F(3),F(3),F(3),F(3)]),
]
for n, case in enumerate(cases,1):
    d, m = check(*case)
    print(f"case {n}: modes={m} normalized-Cauchy-det={d} PASS")
print("EXACT_RATIONAL_CHECKS_PASS")
