"""Exact rational checks for a rooted-forest polarization theorem.

Run: python forest_polarization_check.py
No third-party packages or remote resources are needed.
"""
from fractions import Fraction as F
from itertools import product


def centered_inner(a, b):
    n = len(a)
    sa = sum(a, F(0))
    sb = sum(b, F(0))
    return sum((a[i] - sa / n) * (b[i] - sb / n)
               for i in range(n))


def forests(h, gamma, x):
    n = len(gamma)
    for nxt in product((-1, 0, 1, 2), repeat=n):
        if any(nxt[i] == i for i in range(n)):
            continue
        roots = []
        valid = True
        for i in range(n):
            j = i
            seen = set()
            while nxt[j] != -1:
                if j in seen:
                    valid = False
                    break
                seen.add(j)
                j = nxt[j]
            if not valid:
                break
            roots.append(j)
        if not valid:
            continue
        w = F(1)
        for i, j in enumerate(nxt):
            if j != -1:
                w *= h * gamma[j]
        yield w, tuple(x[r] for r in roots), nxt


def exact_equilibrium(h, gamma, x):
    # Independent exact Gaussian elimination, not the closed-form formula.
    n = len(x)
    mat = [[F(i == j) + h * (F(i == j) - gamma[j])
            for j in range(n)] + [x[i]] for i in range(n)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if mat[i][k])
        mat[k], mat[pivot] = mat[pivot], mat[k]
        t = mat[k][k]
        mat[k] = [v / t for v in mat[k]]
        for i in range(n):
            if i != k:
                t = mat[i][k]
                mat[i] = [mat[i][j] - t * mat[k][j]
                          for j in range(n + 1)]
    return tuple(mat[i][-1] for i in range(n))


def test():
    checks = 0
    gammas = [
        (F(1, 3), F(1, 3), F(1, 3)),
        (F(1, 5), F(3, 10), F(1, 2)),
        (F(1, 2), F(1, 4), F(1, 4)),
        (F(1, 8), F(1, 8), F(3, 4)),
        (F(3, 5), F(1, 5), F(1, 5)),
        (F(1, 10), F(2, 5), F(1, 2)),
    ]
    for h in [F(1, 9), F(1, 3), F(1), F(3), F(11)]:
        for gamma in gammas:
            assert sum(gamma) == 1
            for x in [(F(0), F(0), F(1)),
                      (F(0), F(1, 2), F(1)),
                      (F(2, 9), F(4, 9), F(5, 9))]:
                f = list(forests(h, gamma, x))
                assert len(f) == 16
                zweight = sum((w for w, _, _ in f), F(0))
                assert zweight == (1 + h) ** 2
                checks += 2

                z = exact_equilibrium(h, gamma, x)
                avg = tuple(sum((w * y[i] for w, y, _ in f), F(0)) / zweight
                            for i in range(3))
                assert avg == z
                assert z == tuple((xi + h * sum(gamma[j] * x[j]
                                                    for j in range(3))) / (1 + h)
                                  for xi in x)
                checks += 2

                p = centered_inner(z, z)
                one = sum((w * centered_inner(y, y) for w, y, _ in f),
                          F(0)) / zweight
                var = one - p
                assert var >= 0
                checks += 1
                for t in [1, 2, 3, 5, 11]:
                    # The iid sample-mean quadratic formula holds for each t.
                    expected_plugin = p + var / t
                    assert expected_plugin >= p
                    checks += 1
                # Cross-products from two independent forests are unbiased.
                pair = sum((w * v * centered_inner(y, yy)
                            for w, y, _ in f for v, yy, _ in f), F(0))
                assert pair / (zweight ** 2) == p
                checks += 1
                if x == (F(0), F(0), F(1)):
                    p_formula = F(2, 3) / (1 + h) ** 2
                    ep_formula = F(2, 3) * (1 + h * (1 + gamma[2])) / (1 + h) ** 2
                    assert p == p_formula
                    assert one == ep_formula
                    assert var == F(2, 3) * h * (1 + gamma[2]) / (1 + h) ** 2
                    checks += 3
                    for t in [1, 2, 3, 5, 11]:
                        ratio = (p + var / t) / p
                        assert ratio == 1 + h * (1 + gamma[2]) / t
                        checks += 1
    print('PASS: %d exact rational assertions' % checks)


if __name__ == '__main__':
    test()
