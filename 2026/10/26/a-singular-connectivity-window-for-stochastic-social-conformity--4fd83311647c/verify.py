"""Exact finite-state checks for the grouped stochastic meme imitation model.

The finite computations independently corroborate selected finite examples;
the asymptotic theorem rests on the accompanying analytical proof.
Requires only the Python standard library.
"""
from fractions import Fraction as F
from itertools import product


def solve(a, b):
    n = len(b)
    a = [list(row) + [b[i]] for i, row in enumerate(a)]
    for j in range(n):
        pivot = next(k for k in range(j, n) if a[k][j])
        a[j], a[pivot] = a[pivot], a[j]
        z = a[j][j]
        a[j] = [u / z for u in a[j]]
        for i in range(n):
            if i == j:
                continue
            z = a[i][j]
            if z:
                a[i] = [a[i][k] - z * a[j][k] for k in range(n + 1)]
    return [row[-1] for row in a]


def extinction_time(n, m, pressure, coupling, intrinsic=F(1, 3), forget=F(1, 5)):
    s, mu, a, g = map(F, (pressure, coupling, intrinsic, forget))
    assert n >= 2 and m >= 1 and s > 0 and 0 <= mu <= 1 and a > 0 and g > 0
    N = n * m
    eta = 1 + (n - 1) * mu
    states = [u for u in product(range(m + 1), repeat=n) if sum(u)]
    ix = {u: j for j, u in enumerate(states)}
    mat = [[F(0) for _ in states] for _ in states]
    for row, st in enumerate(states):
        fa = [a + s * F(k, m) for k in st]
        fb = [1 + s * (1 - F(k, m)) for k in st]
        z = eta / n * sum((F(k, N) * fa[j] + F(m-k, N) * fb[j]) for j, k in enumerate(st)) + g * F(sum(st), N)
        assert z > 0
        for j, k in enumerate(st):
            up = F(m-k, N) * sum((1 if j == h else mu) * F(st[h], N) * fa[h] for h in range(n)) / z
            down = F(k, N) * (g + sum((1 if j == h else mu) * F(m-st[h], N) * fb[h] for h in range(n))) / z
            assert 0 <= up <= 1 and 0 <= down <= 1 and up + down <= 1
            mat[row][row] += up + down
            if k < m:
                v = list(st); v[j] += 1
                mat[row][ix[tuple(v)]] -= up
            if k > 0:
                v = list(st); v[j] -= 1
                if sum(v):
                    mat[row][ix[tuple(v)]] -= down
    t = solve(mat, [F(1)] * len(states))
    return t[ix[(1,) + (0,) * (n - 1)]]


def group_chain_limit(n, c, gamma):
    c, gamma = F(c), F(gamma)
    prod, ans = F(1), F(0)
    for i in range(1, n + 1):
        death = i * (gamma + c * F(n-i, n))
        birth = c * F(i*(n-i), n)
        ans += prod / death
        if i < n:
            prod *= birth / death
    return ans


def check():
    count = 0
    a, g = F(1, 3), F(1, 5)
    for n, m in [(2, 1), (2, 2), (3, 1)]:
        # Nontrivial inequality at high pressure, both endpoint couplings.
        s = F(200)
        t0 = extinction_time(n, m, s, 0)
        tm = extinction_time(n, m, s, F(1, 2))
        t1 = extinction_time(n, m, s, 1)
        assert tm < min(t0, t1), (n, m, t0, tm, t1)
        count += 1
        # Direct exact resolvent computation against asymptotic coefficients.
        for mu in (F(0), F(1, 5), F(1)):
            predicted = F(1, 1) / g if mu == 0 else (1 + (n-1)*mu) / (n*g)
            observed = extinction_time(n, m, F(100000), mu) / 100000
            assert abs(observed - predicted) < F(1, 100), (n, m, mu, observed, predicted)
            count += 1
    for n, m in [(2, 1), (2, 2), (3, 1)]:
        for c in (F(0), F(1, 10), F(1), F(10)):
            s = F(100000)
            observed = extinction_time(n, m, s, c / s) / s
            expected = group_chain_limit(n, c, g)
            assert abs(observed - expected) < F(1, 100), (n, m, c, observed, expected)
            count += 1
    for c in [F(0), F(1, 10), F(1), F(10), F(100)]:
        lhs = group_chain_limit(2, c, g)
        rhs = (4*g+c) / (2*g*(2*g+c))
        assert lhs == rhs
        count += 1
    print('exact finite-state and limiting-generator assertions passed:', count)
    print('example (n=2,m=2,s=200):',
          'isolated=', float(extinction_time(2, 2, 200, 0)),
          'half-mixed=', float(extinction_time(2, 2, 200, F(1, 2))),
          'fully-mixed=', float(extinction_time(2, 2, 200, 1)))


if __name__ == '__main__':
    check()
