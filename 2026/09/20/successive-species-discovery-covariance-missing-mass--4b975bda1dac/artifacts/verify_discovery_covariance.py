from fractions import Fraction
from math import exp


def moments_and_cov(p, n):
    one = Fraction(1, 1)
    m = sum(x * (one - x) ** n for x in p)
    m_next = sum(x * (one - x) ** (n + 1) for x in p)
    eq = sum(x * x * (one - x) ** n for x in p)
    em2 = eq
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            em2 += 2 * p[i] * p[j] * (one - p[i] - p[j]) ** n
    var_m = em2 - m * m
    joint = sum(
        p[i] * p[j] * (one - p[i] - p[j]) ** n
        for i in range(len(p)) for j in range(len(p)) if i != j
    )
    cov_direct = joint - m * m_next
    cov_identity = var_m - (m - m_next) * (one - m)
    return m, m_next, joint, cov_direct, cov_identity


def spike_cov(n, a, K):
    one = Fraction(1, 1)
    m = (one - a) * a ** n + a * (one - a / K) ** n
    m_next = (one - a) * a ** (n + 1) + a * (one - a / K) ** (n + 1)
    joint = (2 * (one - a) * a ** (n + 1) * (one - Fraction(1, K)) ** n
             + a * a * (one - Fraction(1, K)) * (one - 2 * a / K) ** n)
    return joint - m * m_next


# Exact identity checks on several rational species laws.
tests = [
    [Fraction(1,2), Fraction(1,3), Fraction(1,6)],
    [Fraction(2,5), Fraction(1,5), Fraction(1,5), Fraction(1,5)],
    [Fraction(7,10), Fraction(1,10), Fraction(1,10), Fraction(1,10)],
]
checks = 0
for p in tests:
    for n in range(1, 8):
        *_, c1, c2 = moments_and_cov(p, n)
        assert c1 == c2
        checks += 1

# Uniform laws have strictly negative adjacent-discovery covariance.
for n in range(1, 13):
    for K in range(2, 13):
        p = [Fraction(1, K)] * K
        *_, c1, c2 = moments_and_cov(p, n)
        formula = Fraction(K-1, K) * (Fraction(K-2, K) ** n - Fraction(K-1, K) ** (2*n))
        assert c1 == c2 == formula
        assert formula < 0
        checks += 1

# Finite one-heavy-plus-equal-rare families eventually have positive covariance.
rows = []
for n in range(1, 13):
    a = Fraction(n, n + 2)
    first = None
    for K in range(2, 5000):
        c = spike_cov(n, a, K)
        if c > 0:
            first = K
            break
    assert first is not None
    rows.append((n, a, first, spike_cov(n, a, first)))
    checks += 1

# The diffuse-tail limit is positive and is the exact K->infinity limit.
for n in range(1, 13):
    a = Fraction(n, n + 2)
    limit = a ** (n + 1) * (1 - a) ** 2 * (1 - a ** n)
    assert limit > 0
    # Numerical convergence is used only as a sanity check; positivity is analytic.
    err1 = abs(float(spike_cov(n, a, 2000)) - float(limit))
    err2 = abs(float(spike_cov(n, a, 4000)) - float(limit))
    assert err2 < err1
    checks += 1

# Unique large-n scaling constant for the diffuse-tail family.
def g(c):
    return 2.0 / c - 1.0 + 1.0 / (exp(c) - 1.0)

lo, hi = 1e-12, 20.0
for _ in range(200):
    mid = (lo + hi) / 2
    if g(mid) > 0:
        lo = mid
    else:
        hi = mid
c_star = (lo + hi) / 2
h_star = c_star * c_star * exp(-c_star) * (1.0 - exp(-c_star))
assert abs(g(c_star)) < 1e-12

print(f"exact_checks={checks}")
print("n  a  first_positive_K")
for n, a, K, c in rows:
    print(f"{n:2d} {a!s:>5s} {K:4d}")
print(f"c_star={c_star:.15f}")
print(f"h_star={h_star:.15f}")
print("status=PASS")
