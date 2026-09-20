"""Exact rational checks for the Bernoulli weak-limit constructions."""
from fractions import Fraction


def moments(law):
    mean = sum(Fraction(k) * p for k, p in law.items())
    factorial2 = sum(Fraction(k * (k - 1)) * p for k, p in law.items())
    total = sum(law.values(), Fraction(0))
    return total, mean, factorial2


def strict_variance_construction(law, lam, n):
    total, mean, f2 = moments(law)
    assert total == 1 and mean == lam
    var = f2 + lam - lam * lam
    d = lam - var
    assert d > 0
    delta = d - lam * lam / n
    assert delta > 0
    j = next(k for k, p in law.items() if k >= 1 and p > 0)
    eps = delta / (j * (n - j))
    assert eps <= law[j]
    out = dict(law)
    out[j] -= eps
    out[0] = out.get(0, Fraction(0)) + eps * (1 - Fraction(j, n))
    out[n] = out.get(n, Fraction(0)) + eps * Fraction(j, n)
    return {k: p for k, p in out.items() if p}


def boundary_construction(law, lam, n):
    total, mean, f2 = moments(law)
    assert total == 1 and mean == lam
    var = f2 + lam - lam * lam
    assert var == lam
    a = lam.numerator // lam.denominator
    theta = lam - a
    z = {a: 1 - theta}
    z[a + 1] = z.get(a + 1, Fraction(0)) + theta
    _, _, zf2 = moments(z)
    dz = lam * lam - zf2
    assert dz > 0
    eta = lam * lam / (n * dz)
    assert 0 <= eta <= 1
    keys = set(law) | set(z)
    return {k: (1 - eta) * law.get(k, 0) + eta * z.get(k, 0) for k in keys}


def check_pairwise_count(law, lam, n):
    total, mean, f2 = moments(law)
    assert total == 1
    assert mean == lam
    assert f2 == (1 - Fraction(1, n)) * lam * lam
    p = lam / n
    pair = f2 / (n * (n - 1))
    assert pair == p * p


# Deterministic target Y=1: explicit closed form.
for n in range(2, 101):
    law = {
        0: Fraction(n - 1, n * n),
        1: Fraction(n - 1, n),
        n: Fraction(1, n * n),
    }
    check_pairwise_count(law, Fraction(1), n)

# Several strict-underdispersion finite targets.
examples = [
    ({1: Fraction(1)}, Fraction(1)),
    ({2: Fraction(7, 10), 3: Fraction(3, 10)}, Fraction(23, 10)),
    ({0: Fraction(1, 4), 1: Fraction(1, 2), 2: Fraction(1, 4)}, Fraction(1)),
]
for law, lam in examples:
    for n in (100, 257, 1000):
        built = strict_variance_construction(law, lam, n)
        check_pairwise_count(built, lam, n)

# Variance-equals-mean boundary: target {0,2}/2 for lambda=1.
boundary = {0: Fraction(1, 2), 2: Fraction(1, 2)}
for n in (10, 101, 1000):
    built = boundary_construction(boundary, Fraction(1), n)
    check_pairwise_count(built, Fraction(1), n)

print("all exact rational checks passed")
