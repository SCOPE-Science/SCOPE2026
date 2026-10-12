#!/usr/bin/env python3
"""Exact finite-instance checks for a finite-state theta-method positivity theorem.
Run: python3 check_theta.py. Uses Python's standard library only.
"""
from fractions import Fraction as F


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def solve(a, b):
    n = len(a)
    aug = [[F(x) for x in a[i]] + [F(b[i])] for i in range(n)]
    for c in range(n):
        p = next((r for r in range(c, n) if aug[r][c]), None)
        assert p is not None
        aug[c], aug[p] = aug[p], aug[c]
        z = aug[c][c]
        aug[c] = [x / z for x in aug[c]]
        for r in range(n):
            if r == c:
                continue
            z = aug[r][c]
            aug[r] = [aug[r][j] - z * aug[c][j] for j in range(n + 1)]
    return [aug[i][-1] for i in range(n)]


def inverse(a):
    n = len(a)
    columns = [solve(a, [F(int(j == k)) for j in range(n)]) for k in range(n)]
    return [[columns[j][i] for j in range(n)] for i in range(n)]


def random_graph(n, seed):
    q = [[F(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and (j == (i + 1) % n or (3 * i + 5 * j + seed) % 5 < 2):
                q[i][j] = F(1 + (11 * i + 7 * j + 3 * seed) % 4)
        q[i][i] = -sum(q[i], F(0))
    return q


def stationary(q):
    n = len(q)
    a = [[q[j][i] for j in range(n)] for i in range(n)]
    a[-1] = [F(1)] * n
    return solve(a, [F(0)] * (n - 1) + [F(1)])


def diag_deviation(q, pi):
    n = len(q)
    a = [[-q[i][j] + pi[j] for j in range(n)] for i in range(n)]
    ainv = inverse(a)
    return [ainv[i][i] - pi[i] * sum(ainv[i]) for i in range(n)]


def return_moment(q, i):
    n = len(q)
    others = [j for j in range(n) if j != i]
    b = [[-q[j][k] for k in others] for j in others]
    m = solve(b, [F(1)] * (n - 1))
    v = solve(b, [2 * x for x in m])
    rate = -q[i][i]
    weights = [q[i][j] / rate for j in others]
    return sum((weights[k] * m[k] for k in range(n - 1)), F(0)), sum((weights[k] * v[k] for k in range(n - 1)), F(0))


def resolvent(q, h):
    n = len(q)
    return inverse([[F(int(i == j)) - h * q[i][j] for j in range(n)] for i in range(n)])


def theta(q, h, th):
    r = resolvent(q, th * h)
    return [[(r[i][j] - (1 - th) * F(int(i == j))) / th for j in range(len(q))] for i in range(len(q))]


def main():
    cases = diag_checks = step_checks = 0
    for n in range(2, 9):
        for seed in range(9):
            q = random_graph(n, seed)
            pi = stationary(q)
            assert min(pi) > 0 and sum(pi) == 1
            for i in range(n):
                rate = -q[i][i]
                mean, second = return_moment(q, i)
                assert mean > 0 and second > 0
                assert pi[i] == 1 / (1 + rate * mean)
                d = diag_deviation(q, pi)[i]
                assert d == pi[i] ** 2 * rate * second / 2 and d > 0
                diag_checks += 1
            hs = [F(1, 10), F(1, 3), F(1), F(3), F(10), F(100)]
            old = [F(1)] * n
            for h in hs:
                r = resolvent(q, h)
                assert all(sum(row) == 1 for row in r)
                assert all(x > 0 for row in r for x in row)
                for i in range(n):
                    assert pi[i] < r[i][i] < old[i]
                old = [r[i][i] for i in range(n)]
                diag_checks += n
            critical = 1 - min(pi)
            for th in [F(1, 8), F(1, 3), F(1, 2), F(2, 3), F(3, 4), critical, F(1)]:
                for h in [F(1, 3), F(1), F(3), F(10), F(100)]:
                    t = theta(q, h, th)
                    r = resolvent(q, th * h)
                    assert all(sum(row) == 1 for row in t)
                    assert all(t[i][j] > 0 for i in range(n) for j in range(n) if i != j)
                    assert (all(x >= 0 for row in t for x in row) == (min(r[i][i] for i in range(n)) >= 1 - th))
                    if th >= critical:
                        assert all(x > 0 for row in t for x in row)
                    step_checks += 1
            cases += 1
    # An exact comparison of finite cutoffs at the same stationary distribution:
    q_cyc = [[F(-1), F(1), F(0)], [F(0), F(-1), F(1)], [F(1), F(0), F(-1)]]
    q_complete = [[F(-2) if i == j else F(1) for j in range(3)] for i in range(3)]
    for q in (q_cyc, q_complete):
        assert stationary(q) == [F(1, 3)] * 3
    assert min(theta(q_cyc, F(3), F(1, 2))[i][i] for i in range(3)) > 0
    assert min(theta(q_cyc, F(4), F(1, 2))[i][i] for i in range(3)) < 0
    assert min(theta(q_complete, F(2), F(1, 2))[i][i] for i in range(3)) == 0
    assert min(theta(q_complete, F(3), F(1, 2))[i][i] for i in range(3)) < 0
    print('VERIFY_OK', cases, 'irreducible generators;', diag_checks,
          'stationarity/return-moment/diagonal checks;', step_checks,
          'exact-rational theta matrices; two distinct cutoffs at common stationary law')

if __name__ == '__main__':
    main()
