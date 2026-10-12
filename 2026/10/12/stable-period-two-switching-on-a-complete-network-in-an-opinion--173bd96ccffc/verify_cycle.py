"""Exact-arithmetic verification of a four-player public-goods opinion/action cycle.

Reproduction: python3 verify_cycle.py (Python 3 standard library only).
The proof for the open parameter family and local attraction is in RESULT.md.
"""
from fractions import Fraction as F

ONE = F(1)
ZERO = F(0)
alpha, beta, lam, r, n = F(1, 20), F(1, 5), F(3, 4), F(3), 4
assert alpha + beta + lam == ONE and ONE < r < n
rho = beta / (beta + lam)
eta = lam / (beta + lam)
kappa = beta * lam / (beta + lam)
theta = F(1, 2) + alpha * (ONE - r / n) / kappa
W = (
    (ZERO, F(1, 10), F(9, 20), F(9, 20)),
    (F(1, 10), ZERO, F(9, 20), F(9, 20)),
    (F(9, 20), F(9, 20), ZERO, F(1, 10)),
    (F(9, 20), F(9, 20), F(1, 10), ZERO),
)
assert all(sum(row) == ONE for row in W)
assert all(W[i][j] == W[j][i] for i in range(n) for j in range(n))
assert all(W[i][j] > ZERO for i in range(n) for j in range(n) if i != j)
assert all(W[i][i] == ZERO for i in range(n))

def update(y):
    means = tuple(sum(W[i][j] * y[j] for j in range(n)) for i in range(n))
    delta = tuple(alpha * (r / n - ONE) + kappa * (m - F(1, 2)) for m in means)
    action = tuple(int(d > ZERO) for d in delta)  # specified defection on equality
    nxt = tuple(rho * means[i] + eta * action[i] for i in range(n))
    assert all(ZERO <= q <= ONE for q in nxt)
    return means, delta, action, nxt

H, L = F(77, 79), F(2, 79)
a = (H, H, L, L)
b = (L, L, H, H)
means_a, delta_a, xa, next_a = update(a)
means_b, delta_b, xb, next_b = update(b)
assert means_a == (F(19, 158),) * 2 + (F(139, 158),) * 2
assert delta_a == (F(-8701, 120080),) * 2 + (F(5699, 120080),) * 2
assert xa == (0, 0, 1, 1) and next_a == b
assert xb == (1, 1, 0, 0) and next_b == a
assert all(delta_a[i] == delta_b[(i + 2) % n] for i in range(n))
assert rho == F(4, 19) and eta == F(15, 19) and theta == F(139, 240)
assert F(19, 158) < theta < F(139, 158)
# Bound for the action sign under perturbations: |(Wy)_i-(Wz)_i| <= ||y-z||_inf.
# Every infinity ball of radius 1/10 around each point is mapped into the
# appropriate opposite sign cell because the minimal input margin is >1/10.
input_margin = min(theta - means_a[0], means_a[2] - theta)
assert input_margin > F(1, 10)
# ||F(y)-F(a)||_inf <= rho ||y-a||_inf within an action cell.
assert ZERO < rho < ONE
assert update((ZERO,) * n)[3] == (ZERO,) * n
assert update((ONE,) * n)[3] == (ONE,) * n

# Three disjoint symmetry eigenspaces of W, exactly:
eigenpairs = (
    ((1, 1, 1, 1), ONE),
    ((1, 1, -1, -1), F(-4, 5)),
    ((1, -1, 0, 0), F(-1, 10)),
    ((0, 0, 1, -1), F(-1, 10)),
)
for vec, ev in eigenpairs:
    assert all(sum(W[i][j] * vec[j] for j in range(n)) == ev * vec[i] for i in range(n))
    assert (rho * ev) ** 2 < ONE
assert sorted((rho * ev) ** 2 for _, ev in eigenpairs) == sorted((F(16, 361), F(256, 9025), F(4, 9025), F(4, 9025)))

# Symbolic family identity at three independent exact interior parameter choices.
for eps, p in ((F(1, 10), F(4, 19)), (F(1, 20), F(1, 3)), (F(1, 4), F(1, 2))):
    q = ONE - p
    D = q + 2 * p * eps
    h = (q + p * eps) / D
    ell = p * eps / D
    low_mean = eps * h + (ONE - eps) * ell
    high_mean = eps * ell + (ONE - eps) * h
    assert h + ell == ONE
    assert low_mean == eps / D and high_mean == ONE - eps / D
    assert p * low_mean == ell and p * high_mean + q == h
print('VERIFY_OK')
