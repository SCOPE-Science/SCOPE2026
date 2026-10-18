#!/usr/bin/env python3
"""Exact rational cross-checks for Erlang-run confined telegraph dynamics.

This finite checker validates two independently derived moment constructions:
a cyclic phase-state generator and a renewal-epoch affine recursion.
It does not establish the boundary asymptotic, which is proved analytically.
"""
from fractions import Fraction as F
from math import comb


def solve(a, b):
    n = len(b)
    z = [list(map(F, a[i])) + [F(b[i])] for i in range(n)]
    for k in range(n):
        p = next(i for i in range(k, n) if z[i][k])
        z[k], z[p] = z[p], z[k]
        c = z[k][k]
        z[k] = [v / c for v in z[k]]
        for i in range(n):
            if i != k:
                c = z[i][k]
                if c:
                    z[i] = [z[i][j] - c*z[k][j] for j in range(n+1)]
    return [row[-1] for row in z]


def generator_moments(m, r, max_n):
    size = 2*m
    previous = [F(1, size)]*size
    moments = [F(1)]
    for n in range(1, max_n+1):
        a = [[F(0)]*size for _ in range(size)]
        b = []
        for i in range(size):
            a[i][i] += n+r
            a[i][(i-1) % size] -= r
            b.append(n*(1 if i < m else -1)*previous[i])
        previous = solve(a, b)
        moments.append(sum(previous))
    return moments


def embedded_moments(m, r, max_n):
    def expB(j):
        return (r/(r+j))**m
    Y = [F(1)]
    for n in range(1, max_n+1):
        coeff = []
        for j in range(n+1):
            q = n-j
            e = F(2)**q*expB(j)*sum(
                (-1)**k * comb(q,k)*expB(j+k) for k in range(q+1))
            coeff.append(comb(n,j)*e)
        numerator = sum(coeff[j]*Y[j] for j in range(n))
        Y.append(numerator/(1-coeff[n]))
    age_laplace = lambda j: F(1) if j == 0 else r/(m*j)*(1-expB(j))
    moments = []
    for n in range(max_n+1):
        plus = sum(F(comb(n,j))*(-1)**j*Y[j]*age_laplace(j)
                   for j in range(n+1))
        moments.append(plus if n % 2 == 0 else F(0))
    return moments


def main():
    tests = 0
    for m in (1,2,3,4):
        for r in (F(1,2),F(1),F(2),F(3)):
            u = generator_moments(m,r,6)
            v = embedded_moments(m,r,6)
            for n in range(7):
                assert u[n] == v[n], (m,r,n,u[n],v[n])
                tests += 1
            assert all(F(0) < u[n] < F(1) for n in (2,4,6))
            tests += 3
    for m, value2, value4 in [
        (1,F(1,3),F(1,5)),
        (2,F(2,5),F(9,34)),
        (3,F(13,27),F(883,2535)),
        (4,F(19,34),F(891,2056)),
    ]:
        u = generator_moments(m,F(1),4)
        assert (u[2],u[4]) == (value2,value4)
        tests += 2
    # Exact Eulerian age-density Laplace transform for Erlang(m,r).
    for m in (1,2,3,4):
        for r in (F(1,2),F(1),F(2),F(3)):
            for j in (1,2,3):
                # Sum the m+1 rational Erlang phase terms explicitly.
                direct = r/F(m)*sum(r**k/(r+j)**(k+1) for k in range(m))
                renewal = r/(m*j)*(1-(r/(r+j))**m)
                assert direct == renewal
                tests += 1
    print('PASS:', tests, 'exact rational assertions')
    print('The logarithmic edge asymptotics are analytic, not certified by finite tests.')

if __name__ == '__main__':
    main()
