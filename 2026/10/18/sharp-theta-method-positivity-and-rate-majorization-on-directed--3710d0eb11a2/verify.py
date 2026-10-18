"""Exact finite tests for positivity of theta steps on a one-way cyclic generator.

Requires Python 3.9+ standard library only. The all-size theorem is mathematical,
not inferred from these tests.
"""
from fractions import Fraction as F
from itertools import product


def inverse(a):
    n = len(a)
    z = [[F(a[i][j]) for j in range(n)] + [F(i == j) for j in range(n)] for i in range(n)]
    for k in range(n):
        v = next(i for i in range(k, n) if z[i][k])
        z[k], z[v] = z[v], z[k]
        pivot = z[k][k]
        z[k] = [c / pivot for c in z[k]]
        for i in range(n):
            if i != k:
                coeff = z[i][k]
                z[i] = [z[i][j] - coeff * z[k][j] for j in range(2*n)]
    return [row[n:] for row in z]


def mm(a, b):
    n = len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def generator(r):
    n = len(r)
    q = [[F(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        q[i][i] -= r[i]
        q[i][(i+1) % n] += r[i]
    return q


def theta_matrix(r, theta, h):
    q = generator(r)
    n = len(r)
    a = [[F(i == j) - theta*h*q[i][j] for j in range(n)] for i in range(n)]
    b = [[F(i == j) + (1-theta)*h*q[i][j] for j in range(n)] for i in range(n)]
    return mm(inverse(a), b)


def resolvent_diag(r, s):
    ts = [s*x/(1+s*x) for x in r]
    pp = F(1)
    for t in ts: pp *= t
    return [(1-t)/(1-pp) for t in ts], ts, pp


def test():
    checks = 0
    for n in range(2, 8):
        patterns = [
            [F(1)]*n,
            [F(1+i%3, 2) for i in range(n)],
            [F(2*n-1)]+[F(1)]*(n-1),
        ]
        for r, theta, h in product(patterns,
                (F(0), F(1,5), F(1,3), F(1,2), F(3,4), F(9,10), F(1)),
                (F(0), F(1,5), F(1,2), F(1), F(2), F(3), F(5), F(20))):
            z = theta_matrix(r, theta, h)
            assert all(sum(row) == 1 for row in z)
            assert all(z[i][j] >= 0 for i in range(n) for j in range(n) if j!=i)
            if theta == 0:
                good = h*max(r) <= 1
            elif theta == 1:
                good = True
            else:
                diag, ts, pp = resolvent_diag(r, theta*h)
                assert [z[i][i] for i in range(n)] == [(x-(1-theta))/theta for x in diag]
                good = max(ts) <= theta + (1-theta)*pp
                assert min(diag) == diag[r.index(max(r))]
            assert good == all(z[i][j] >= 0 for i in range(n) for j in range(n))
            checks += 1
    # Exact strict majorization barrier inequality at several step sizes.
    for n in range(2, 13):
        r = [F(2*n-1)] + [F(1)]*(n-1)
        same_average = [sum(r)/n]*n
        for s in [F(1,7), F(1,2), F(1), F(3), F(10)]:
            _, x, px = resolvent_diag(r, s)
            _, y, py = resolvent_diag(same_average, s)
            assert max(x) >= max(y)
            assert px < py
            checks += 1
    # Direct boundary checks: n=3 with rates (4,1,1) at theta=1/2.
    r = [F(4), F(1), F(1)]
    for h, expected in [(F(1,2), True), (F(3,5), False)]:
        mat = theta_matrix(r,F(1,2),h)
        assert all(a>=0 for row in mat for a in row)==expected
        checks += 1
    assert checks == 3*6*7*8 + 11*5 + 2
    print('VERIFY_OK exact_checks=', checks)

if __name__ == '__main__':
    test()
