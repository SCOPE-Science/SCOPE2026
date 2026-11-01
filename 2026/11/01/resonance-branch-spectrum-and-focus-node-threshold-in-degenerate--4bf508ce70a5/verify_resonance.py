"""Standalone exact-rational checks for the rank-one collapse spectral theorem.
Requires Python 3.9+ and no third-party packages.
This verifies finite identities and Sturm counts; the all-n proof is analytic.
"""
from fractions import Fraction as F


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def matpow(a, n):
    out = [[F(1), F(0)], [F(0), F(1)]]
    for _ in range(n):
        out = matmul(out, a)
    return out


def f_recur(t, d, n):
    vals = [F(1), t]
    while len(vals) <= n:
        vals.append(t * vals[-1] - d * vals[-2])
    return vals


def u_recur(u, n):
    vals = [F(1), u]
    while len(vals) <= n:
        vals.append(u * vals[-1] - vals[-2])
    return vals


def det_tridiagonal(u, c, n):
    # det(u I - J_n(c)), with a boundary diagonal c, other diagonals 0.
    d0, d1 = F(1), u - c
    if n == 1:
        return d1
    for k in range(2, n + 1):
        d0, d1 = d1, u * d1 - d0
    return d1


def sturm_greater(x, c, n):
    # Sturm sequence of leading principal minors of x I - J_n(c).
    vals = [F(1), x - c]
    for k in range(2, n + 1):
        vals.append(x * vals[-1] - vals[-2])
    signs = [1 if v > 0 else -1 for v in vals if v != 0]
    return sum(signs[i] != signs[i-1] for i in range(1, len(signs)))


def run():
    tests = 0
    aa = [F(1, 2), F(3, 4), F(6, 5), F(2)]
    dd = [F(1, 4), F(1), F(9, 4)]
    tt = [F(-7, 5), F(-1, 2), F(0), F(3, 4), F(2)]
    for a in aa:
        for d in dd:
            for t in tt:
                al = [[a, F(1)], [F(0), F(0)]]
                ar = [[t, F(1)], [-d, F(0)]]
                for n in range(1, 15):
                    power = matmul(al, matpow(ar, n))
                    f = f_recur(t, d, n)
                    assert power[0][0] + power[1][1] == a * f[n] - d * f[n - 1]
                    assert power[1] == [F(0), F(0)]
                    tests += 2
    for c in [F(1, 4), F(1), F(5, 4), F(7, 3)]:
        for u in [F(-3), F(-1, 2), F(0), F(1), F(3)]:
            for n in range(1, 15):
                U = u_recur(u, n)
                assert det_tridiagonal(u, c, n) == U[n] - c * U[n-1]
                tests += 1
    for n in range(1, 25):
        for c in [F(1, 5), F(4, 5), F(1), F(6, 5), F(3, 2), F(5, 2)]:
            # Avoid equality at the focus/node boundary.
            if c != F(n+1, n):
                assert sturm_greater(F(2), c, n) == int(c > F(n+1, n))
                tests += 1
            assert sturm_greater(F(-2), c, n) == n
            assert sturm_greater(F(0), c, n) == (n+1)//2
            tests += 2
    # Exact reconstruction of the previously reported 4-right-step polynomial.
    for a in aa:
        for d in dd:
            for t in tt:
                f = f_recur(t, d, 4)
                formula = (a + 2*t)*d*d - (3*a+t)*t*t*d + a*t*t*t*t
                assert a * f[4] - d * f[3] == formula
                tests += 1
    print('PASS: %d exact-rational identity and Sturm-spectrum checks' % tests)

if __name__ == '__main__':
    run()
