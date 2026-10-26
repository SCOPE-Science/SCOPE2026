"""Exact-rational checks for stationary-observation semi-Markov hitting times.

No external libraries are required. The probabilistic theorem is proved in RESULT.md;
these finite linear-system checks validate its algebra and the explicit witness.
"""
from fractions import Fraction as F
from itertools import product


def solve(a, b):
    n = len(b)
    r = [[F(z) for z in row] + [F(rhs)] for row, rhs in zip(a, b)]
    for c in range(n):
        k = next(k for k in range(c, n) if r[k][c])
        r[c], r[k] = r[k], r[c]
        q = r[c][c]
        r[c] = [z / q for z in r[c]]
        for k in range(n):
            if k != c:
                q = r[k][c]
                r[k] = [x - q * y for x, y in zip(r[k], r[c])]
    return [row[-1] for row in r]


def stationary(p):
    n = len(p)
    a = [[(F(1) if i == j else F(0)) - p[j][i] for j in range(n)] for i in range(n)]
    a[-1] = [F(1) for _ in range(n)]
    b = [F(0)] * (n - 1) + [F(1)]
    return solve(a, b)


def hit(p, means):
    n = len(p)
    result = [[F(0) for _ in range(n)] for _ in range(n)]
    for target in range(n):
        others = [i for i in range(n) if i != target]
        a = [[(F(1) if i == k else F(0)) - p[i][k] for k in others] for i in others]
        h = solve(a, [means[i] for i in others])
        for i, x in zip(others, h):
            result[i][target] = x
    return result


def eval_model(p, means, second, marked_means):
    n = len(p)
    nu = stationary(p)
    total = sum((nu[i] * means[i] for i in range(n)), F(0))
    pi = [nu[i] * means[i] / total for i in range(n)]
    h = hit(p, means)
    k0 = [sum((pi[j] * h[i][j] for j in range(n)), F(0)) for i in range(n)]
    assert len(set(k0)) == 1
    eq_p = [[marked_means[i][j] / means[i] for j in range(n)] for i in range(n)]
    assert all(sum(row, F(0)) == 1 for row in eq_p)
    eq_h = [[F(0) if i == j else second[i] / (2 * means[i]) +
             sum((eq_p[i][k] * h[k][j] for k in range(n)), F(0))
             for j in range(n)] for i in range(n)]
    eq_k = [sum((pi[j] * eq_h[i][j] for j in range(n)), F(0)) for i in range(n)]
    predicted = []
    for i in range(n):
        defect = (1 - pi[i]) * (second[i] / (2 * means[i]) - means[i])
        defect -= pi[i] * sum(((eq_p[i][j] - p[i][j]) * h[j][i] for j in range(n)), F(0))
        predicted.append(k0[i] + defect)
    assert predicted == eq_k
    return nu, pi, h, k0, eq_h, eq_k


def star_checks():
    z = F(0)
    one = F(1)
    half = F(1, 2)
    p = [[z, half, half], [one, z, z], [one, z, z]]
    means = [F(2), one, F(2)]
    second = [F(8), F(2), F(8)]
    marks_a = [[z, half, F(3, 2)], [one, z, z], [F(2), z, z]]
    marks_b = [[z, F(3, 2), half], [one, z, z], [F(2), z, z]]
    ra = eval_model(p, means, second, marks_a)
    rb = eval_model(p, means, second, marks_b)
    nu, pi, h, k, ea, ka = ra
    _, _, _, _, eb, kb = rb
    assert nu == [half, F(1, 4), F(1, 4)]
    assert pi == [F(4, 7), F(1, 7), F(2, 7)]
    assert h == [[z, F(6), F(5)], [one, z, F(6)], [F(2), F(8), z]]
    assert k == [F(16, 7)] * 3
    assert (ea[0][1], ea[0][2], ka) == (F(8), F(7, 2), [F(15, 7), F(16, 7), F(16, 7)])
    assert (eb[0][1], eb[0][2], kb) == (F(4), F(13, 2), [F(17, 7), F(16, 7), F(16, 7)])
    # A Gamma(shape 5/3, scale 3/5) mean is 1; scale 9/5 mean is 3.
    shape = F(5, 3)
    for mean, scale in [(F(1), F(3, 5)), (F(3), F(9, 5))]:
        assert shape * scale == mean
        assert mean**2 * (1 + 1/shape) == F(8, 5) * mean**2
    assert (F(1, 2) * F(8, 5) + F(1, 2) * F(72, 5)) == F(8)
    assert all(second[i] - means[i]**2 == means[i]**2 for i in range(3))
    print('Three-state witnesses: exact rational moments, means, Kemeny values, defects and reversed marks checked.')


def generic_checks():
    # Vary the irreducible transition matrix, holding means and second moments,
    # and joint duration/destination means. All arithmetic is exact.
    checks = 0
    for a, b, c in product(range(1, 5), repeat=3):
        p = [
            [F(0), F(a, a + b), F(b, a + b)],
            [F(c, c + 1), F(0), F(1, c + 1)],
            [F(2, 3), F(1, 3), F(0)],
        ]
        means = [F(a + 1, 2), F(b + 1, 2), F(c + 1, 2)]
        # An independent mark model has E[W 1_{Y=k}]=p_ik m_i.
        indep = [[p[i][j] * means[i] for j in range(3)] for i in range(3)]
        second = [means[i]**2 * F(a + b + c + i + 3, 4) for i in range(3)]
        # Increase second moment if needed to satisfy Jensen's inequality.
        second = [max(second[i], means[i]**2) for i in range(3)]
        _, _, _, k, _, ke = eval_model(p, means, second, indep)
        assert len(set(k)) == 1
        for i in range(3):
            nu = stationary(p)
            pi = [nu[j]*means[j]/sum(nu[t]*means[t] for t in range(3)) for j in range(3)]
            assert ke[i] - k[i] == (1-pi[i])*(second[i]/(2*means[i])-means[i])
        checks += 1
    print(f'{checks} distinct three-state rational renewal-kernel models: exact independent-mark correction checked.')


if __name__ == '__main__':
    star_checks()
    generic_checks()
    print('All assertions passed.')
