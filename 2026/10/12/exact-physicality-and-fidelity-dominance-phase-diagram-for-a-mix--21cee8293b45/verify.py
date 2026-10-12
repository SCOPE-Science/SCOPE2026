from fractions import Fraction as Q


def eps_max(q):
    return 2 * (1 - q) / (3 - q)


def eps_all(q):
    return 2 * (1 + q) / (3 * (3 - q))


def g(q, eps):
    return (1 + q) / (3 - q) + eps


def f_nonorth(q, eps):
    return Q(2, 3) + eps * (3 - q) / (6 * (1 + q))


def f_new(p):
    return (7 - 4 * p) / 9


def p_star(q, eps):
    return Q(1, 4) - 3 * eps * (3 - q) / (8 * (1 + q))

# Exact boundary identities.
for q in [Q(0), Q(1, 9), Q(1, 4), Q(1, 2), Q(3, 4), Q(9, 10)]:
    em = eps_max(q)
    assert g(q, em) == 1
    assert g(q, Q(0)) == (1 + q) / (3 - q)
    assert (eps_all(q) <= em) == (q <= Q(1, 2))

# Fixed-epsilon inversion used for the source's epsilon-only statement.
for eps in [Q(1, 10), Q(1, 5), Q(2, 5), Q(1, 2), Q(3, 5)]:
    qmax = (2 - 3 * eps) / (2 - eps)
    if 0 <= qmax <= 1:
        assert eps_max(qmax) == eps

# The two values used in the source figures have exact physical cutoffs.
assert (2 - 3 * Q(1, 5)) / (2 - Q(1, 5)) == Q(7, 9)
assert (2 - 3 * Q(2, 5)) / (2 - Q(2, 5)) == Q(1, 2)

# Exact fidelity comparison against rho_new.
count = 0
for q in [Q(0), Q(1, 9), Q(1, 4), Q(1, 2), Q(3, 4)]:
    em = eps_max(q)
    for frac in [Q(1, 5), Q(1, 2), Q(4, 5), Q(1)]:
        eps = em * frac
        if eps == 0:
            continue
        ps = p_star(q, eps)
        assert f_nonorth(q, eps) == f_new(ps)
        for p in [Q(0), Q(1, 20), Q(1, 8), Q(1, 5), Q(6, 25)]:
            if p >= Q(1, 4):
                continue
            lhs = f_nonorth(q, eps) - f_new(p)
            rhs = p - ps
            assert (lhs > 0) == (rhs > 0)
            assert (lhs == 0) == (rhs == 0)
            count += 1

# Best physically allowed nonorthogonal fidelity versus the best useful rho_new fidelity.
# F_N is increasing in epsilon, hence its physical maximum is attained at g=1.
for q in [Q(0), Q(1, 9), Q(1, 4), Q(1, 2), Q(3, 4)]:
    fmax = f_nonorth(q, eps_max(q))
    assert fmax == (3 + q) / (3 * (1 + q))
    assert (fmax > Q(7, 9)) == (q < Q(1, 2))
    assert (fmax == Q(7, 9)) == (q == Q(1, 2))

print(f"VERIFY_OK comparison_cases={count} figure_cutoffs=7/9,1/2 critical_q=1/2")
