#!/usr/bin/env python3
from fractions import Fraction

projection_cases = 0
for m in range(2, 10):
    for n in range(2, 10):
        for i in (0, m - 1):
            for j in (0, n - 1):
                Q = []
                for a in range(m):
                    row = []
                    for b in range(n):
                        u = Fraction(int(a == i), 1) - Fraction(1, m)
                        v = Fraction(int(b == j), 1) - Fraction(1, n)
                        row.append(u * v)
                    Q.append(row)
                assert all(sum(Q[a][b] for b in range(n)) == 0 for a in range(m))
                assert all(sum(Q[a][b] for a in range(m)) == 0 for b in range(n))
                norm2 = sum(x * x for row in Q for x in row)
                assert norm2 == Fraction((m - 1) * (n - 1), m * n)
                projection_cases += 1

def make_margins(m, n, seed):
    total = m * n + seed + m + n
    r = [1 + ((seed + 3*i) % 4) for i in range(m)]
    sr = sum(r)
    r[-1] += total - sr
    if r[-1] <= 0:
        total += 4*m
        r[-1] += 4*m
    c = [1 + ((2*seed + 5*j) % 3) for j in range(n)]
    sc = sum(c)
    c[-1] += total - sc
    if c[-1] <= 0:
        bump = 3*n
        total += bump
        r[-1] += bump
        c[-1] += bump
    assert sum(r) == sum(c)
    assert min(r) > 0 and min(c) > 0
    return list(map(Fraction, r)), list(map(Fraction, c))

margin_cases = 0
for m in range(2, 7):
    for n in range(2, 7):
        for seed in range(1, 7):
            r, c = make_margins(m, n, seed)
            t = min(min(r) / n, min(c) / m)
            rp = [x - n*t for x in r]
            cp = [x - m*t for x in c]
            assert min(rp) >= 0 and min(cp) >= 0
            S = sum(rp)
            assert S == sum(cp)
            if S == 0:
                Y = [[Fraction(0) for _ in range(n)] for _ in range(m)]
            else:
                Y = [[rp[i] * cp[j] / S for j in range(n)] for i in range(m)]
            X = [[t + Y[i][j] for j in range(n)] for i in range(m)]
            assert all(sum(X[i][j] for j in range(n)) == r[i] for i in range(m))
            assert all(sum(X[i][j] for i in range(m)) == c[j] for j in range(n))
            assert min(x for row in X for x in row) >= t
            assert all(n*t <= x for x in r)
            assert all(m*t <= x for x in c)
            margin_cases += 1

birkhoff_cases = 0
for d in range(2, 51):
    t = Fraction(1, d)
    kappa = Fraction(d - 1, d)
    rho = t / kappa
    assert rho == Fraction(1, d - 1)
    birkhoff_cases += 1

print(
    "VERIFY_OK transportation-inradius "
    f"projection_cases={projection_cases} "
    f"margin_cases={margin_cases} "
    f"birkhoff_cases={birkhoff_cases}"
)
