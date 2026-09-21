from fractions import Fraction
from itertools import combinations
from math import exp, isfinite


def poly_mul(a, b):
    out = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def pgf_coeffs(ps):
    q = [Fraction(1)]
    for p in ps:
        q = poly_mul(q, [1 - p, p])
    return q


def factorial_moment_from_pgf(q, r):
    # Q^(r)(1)/r! = sum_{k>=r} binom(k,r) q_k.
    from math import comb
    return sum(Fraction(comb(k, r)) * q[k] for k in range(r, len(q)))


def elementary(ps, r):
    if r == 0:
        return Fraction(1)
    return sum((prod(c) for c in combinations(ps, r)), Fraction(0))


def prod(xs):
    out = Fraction(1)
    for x in xs:
        out *= x
    return out


def root_poly_coeffs(ps):
    # Descending coefficients of prod_i (u-p_i), reconstructed from e_r.
    n = len(ps)
    return [Fraction(1)] + [((-1) ** r) * elementary(ps, r) for r in range(1, n + 1)]


def eval_poly_desc(coeffs, x):
    y = Fraction(0)
    for c in coeffs:
        y = y * x + c
    return y


def order_stat_cdfs_from_count_pmf(q):
    # H_r = P(N >= r), r=1,...,n.
    n = len(q) - 1
    return [sum(q[r:], Fraction(0)) for r in range(1, n + 1)]


def recover_count_pmf(H):
    n = len(H)
    q = [Fraction(0)] * (n + 1)
    q[0] = 1 - H[0]
    for k in range(1, n):
        q[k] = H[k - 1] - H[k]
    q[n] = H[n - 1]
    return q


def check_exact_recovery():
    cases = [
        [Fraction(1, 5), Fraction(2, 5), Fraction(4, 5)],
        [Fraction(1, 7), Fraction(1, 3), Fraction(1, 2), Fraction(5, 6)],
        [Fraction(2, 9), Fraction(2, 9), Fraction(7, 10)],
    ]
    checks = 0
    for ps in cases:
        q = pgf_coeffs(ps)
        H = order_stat_cdfs_from_count_pmf(q)
        assert recover_count_pmf(H) == q
        checks += len(q)
        for r in range(len(ps) + 1):
            assert factorial_moment_from_pgf(q, r) == elementary(ps, r)
            checks += 1
        coeffs = root_poly_coeffs(ps)
        for p in ps:
            assert eval_poly_desc(coeffs, p) == 0
            checks += 1
    return checks


def check_n2_closed_form():
    cases = [(Fraction(1, 5), Fraction(4, 5)), (Fraction(2, 7), Fraction(3, 7))]
    checks = 0
    for f1, f2 in cases:
        hmin = f1 + f2 - f1 * f2
        hmax = f1 * f2
        s = hmin + hmax
        disc = s * s - 4 * hmax
        assert disc == (f1 - f2) ** 2
        assert s == f1 + f2
        checks += 2
    return checks


def logistic(x):
    return 1.0 / (1.0 + exp(-x))


def bump(x):
    if abs(x) >= 1.0:
        return 0.0
    return exp(-1.0 / (1.0 - x * x))


def flat_signed(x):
    if x == 0.0 or abs(x) >= 1.0:
        return 0.0
    core = exp(-1.0 / (x * x)) * bump(x)
    return core if x > 0 else -core


def check_smooth_braid_grid():
    eps = 0.02
    xs = [(-1.5 + 3.0 * j / 1200.0) for j in range(1201)]
    F1 = [logistic(x) + eps * flat_signed(x) for x in xs]
    F2 = [logistic(x) - eps * flat_signed(x) for x in xs]
    G1 = [logistic(x) + eps * abs(flat_signed(x)) for x in xs]
    G2 = [logistic(x) - eps * abs(flat_signed(x)) for x in xs]

    for a, b, c, d in zip(F1, F2, G1, G2):
        assert abs(min(a, b) - min(c, d)) < 1e-14
        assert abs(max(a, b) - max(c, d)) < 1e-14
        assert all(isfinite(v) for v in (a, b, c, d))

    # Numerical support for monotonicity; the proof uses a small-epsilon derivative bound.
    for vals in (F1, F2, G1, G2):
        assert all(vals[j + 1] >= vals[j] - 1e-14 for j in range(len(vals) - 1))

    # The relabeling switches at the crossing and therefore is not global.
    i_neg = min(range(len(xs)), key=lambda j: abs(xs[j] + 0.5))
    i_pos = min(range(len(xs)), key=lambda j: abs(xs[j] - 0.5))
    assert abs(G1[i_neg] - F2[i_neg]) < 1e-14
    assert abs(G1[i_pos] - F1[i_pos]) < 1e-14
    assert abs(F1[i_neg] - F2[i_neg]) > 1e-12
    assert abs(F1[i_pos] - F2[i_pos]) > 1e-12
    return 4 * len(xs) + 4


if __name__ == '__main__':
    total = 0
    total += check_exact_recovery()
    total += check_n2_closed_form()
    total += check_smooth_braid_grid()
    print(f'PASS: {total} exact/numerical checks')
