"""Exact-rational checks for coordinatewise stability of weighted two-row supermodular least squares.
Run with Python 3 standard library, no data files required.
"""
from fractions import Fraction as F
from itertools import product
from random import Random


def isotonic_pava(y, w):
    blocks = []
    for i, (x, wt) in enumerate(zip(y, w)):
        blocks.append([i, i + 1, wt, wt * x])
        while len(blocks) > 1 and blocks[-2][3] * blocks[-1][2] > blocks[-1][3] * blocks[-2][2]:
            right = blocks.pop()
            left = blocks.pop()
            blocks.append([left[0], right[1], left[2] + right[2], left[3] + right[3]])
    z = list(y)
    for lo, hi, wt, tot in blocks:
        z[lo:hi] = [tot / wt] * (hi - lo)
    return z


def isotonic_enumerate(y, w):
    m = len(y)
    best = None
    best_score = None
    for mask in range(1 << (m - 1)):
        cuts = [0] + [j + 1 for j in range(m - 1) if mask & (1 << j)] + [m]
        means = []
        for lo, hi in zip(cuts[:-1], cuts[1:]):
            cw = sum(w[lo:hi]); av = sum(w[j] * y[j] for j in range(lo, hi)) / cw
            means.append(av)
        if any(means[k] > means[k + 1] for k in range(len(means) - 1)):
            continue
        z = [v for v, (lo, hi) in zip(means, zip(cuts[:-1], cuts[1:])) for _ in range(lo, hi)]
        score = sum(w[i] * (y[i] - z[i]) ** 2 for i in range(m))
        if best_score is None or score < best_score:
            best_score, best = score, z
    assert best is not None
    return best


def project(top, bottom, a, b):
    m = len(top)
    c = [a[i] * b[i] / (a[i] + b[i]) for i in range(m)]
    s = [(a[i] * top[i] + b[i] * bottom[i]) / (a[i] + b[i]) for i in range(m)]
    d = [bottom[i] - top[i] for i in range(m)]
    dh = isotonic_pava(d, c)
    return ([s[i] - b[i] / (a[i] + b[i]) * dh[i] for i in range(m)],
            [s[i] + a[i] / (a[i] + b[i]) * dh[i] for i in range(m)])


def predicted(a, b):
    c = [a[i] * b[i] / (a[i] + b[i]) for i in range(len(a))]
    C = sum(c)
    return 1 + 2 * max(max(a[i], b[i]) / (a[i] + b[i]) * (1 - c[i] / C) for i in range(len(a)))


def full_pool_jacobian(a, b):
    m = len(a)
    c = [a[i] * b[i] / (a[i] + b[i]) for i in range(m)]
    C = sum(c)
    J = []
    for row in (0, 1):
        for j in range(m):
            mu = a[j] / (a[j] + b[j]); lam = b[j] / (a[j] + b[j])
            coef = -lam if row == 0 else mu
            line = []
            for inputrow in (0, 1):
                for i in range(m):
                    ds = (mu if inputrow == 0 else lam) if j == i else 0
                    dd = (c[i] / C) * (-1 if inputrow == 0 else 1)
                    line.append(ds + coef * dd)
            J.append(line)
    return J


def run():
    rng = Random(20261018)
    checks = 0
    for m in range(1, 8):
        for _ in range(20):
            a = [F(rng.randint(1, 17), rng.randint(1, 5)) for j in range(m)]
            b = [F(rng.randint(1, 17), rng.randint(1, 5)) for j in range(m)]
            top = [F(rng.randint(-9, 9), 3) for j in range(m)]
            bot = [F(rng.randint(-9, 9), 3) for j in range(m)]
            c = [a[i] * b[i] / (a[i] + b[i]) for i in range(m)]
            y = [bot[i] - top[i] for i in range(m)]
            assert isotonic_pava(y, c) == isotonic_enumerate(y, c)
            checks += 1
            ph = project(top, bot, a, b)
            assert all((ph[1][j + 1] - ph[0][j + 1]) >= (ph[1][j] - ph[0][j]) for j in range(m - 1))
            checks += 1
            bound = predicted(a, b)
            J = full_pool_jacobian(a, b)
            norms = [sum(abs(z) for z in r) for r in J]
            assert max(norms) == bound
            checks += len(norms)
            # Strictly decreasing differences force one open pooled block.
            top0 = [F(0) for _ in range(m)]
            bot0 = [F(m - j) for j in range(m)]
            assert len(set(project(top0, bot0, a, b)[1][j] - project(top0, bot0, a, b)[0][j] for j in range(m))) == 1
            checks += 1
            row = max(range(len(norms)), key=norms.__getitem__)
            signs = [F(1) if z >= 0 else F(-1) for z in J[row]]
            eps = F(1, 1000000)
            top1 = [top0[j] + eps * signs[j] for j in range(m)]
            bot1 = [bot0[j] + eps * signs[m + j] for j in range(m)]
            ph0 = project(top0, bot0, a, b)
            ph1 = project(top1, bot1, a, b)
            got = (ph1[0][row] - ph0[0][row]) / eps if row < m else (ph1[1][row - m] - ph0[1][row - m]) / eps
            assert got == bound, (m, row, got, bound)
            checks += 1
            for i in range(2):
                for j in range(m):
                    # Independent Jacobian exact difference through a tiny coordinate step.
                    esign = [F(0)] * (2 * m)
                    esign[i * m + j] = eps
                    t = [top0[k] + esign[k] for k in range(m)]
                    bb = [bot0[k] + esign[m + k] for k in range(m)]
                    pp = project(t, bb, a, b)
                    for outrow in range(2):
                        for k in range(m):
                            assert (pp[outrow][k] - ph0[outrow][k]) / eps == J[outrow * m + k][i * m + j]
                            checks += 1
    # A bounded sequence approaching amplification three in the smallest genuine grid.
    for k in (10, 100, 1000):
        a = [F(k), F(1)]
        b = [F(1, k), F(1)]
        assert predicted(a, b) > F(29, 10) if k >= 100 else predicted(a, b) > F(2)
        checks += 1
    print(f'EXACT_RATIONAL_CHECKS_PASSED={checks}')

if __name__ == '__main__':
    run()
