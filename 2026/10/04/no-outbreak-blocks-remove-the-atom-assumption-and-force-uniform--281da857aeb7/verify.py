from fractions import Fraction


def no_outbreak_step(p, iota, delta):
    r = len(p)
    assert len(iota) == r - 1
    p2 = [Fraction(0) for _ in range(r)]
    if r > 2:
        for j in range(1, r - 1):
            p2[j] = p[j - 1]
    p2[r - 1] = p[r - 1] + p[r - 2]
    i2 = [Fraction(1)]
    for j in range(1, r - 1):
        i2.append((Fraction(1) - delta) * iota[j - 1])
    return p2, i2


def expected_iota(deltas, r):
    m = r - 1
    out = [Fraction(1)]
    for j in range(2, r):
        prod = Fraction(1)
        # formula: product over block indices m-j+2,...,m in 1-based indexing
        start0 = m - j + 1
        for idx in range(start0, m):
            prod *= (Fraction(1) - deltas[idx])
        out.append(prod)
    return out


def make_states(r):
    den = r * (r + 1) // 2
    p_a = [Fraction(j + 1, den) for j in range(r)]
    p_b = list(reversed(p_a))
    i_a = [Fraction(1)] + [Fraction(r - j, r) for j in range(1, r - 1)]
    i_b = [Fraction(1)] + [Fraction(1, j + 2) for j in range(1, r - 1)]
    return (p_a, i_a), (p_b, i_b)


for r in range(2, 13):
    m = r - 1
    deltas = [Fraction((2 * s + 1) % 7, 8) for s in range(m)]
    (pa, ia), (pb, ib) = make_states(r)
    for d in deltas:
        pa, ia = no_outbreak_step(pa, ia, d)
        pb, ib = no_outbreak_step(pb, ib, d)
    target_p = [Fraction(0)] * (r - 1) + [Fraction(1)]
    assert pa == target_p == pb
    expected = expected_iota(deltas, r)
    assert ia == expected == ib

# Exact examples of the minorization mass alpha = beta^(r-1).
for r, beta in [(2, Fraction(1, 3)), (3, Fraction(2, 5)), (7, Fraction(3, 4))]:
    alpha = beta ** (r - 1)
    assert Fraction(0) < alpha <= Fraction(1)

print("VERIFY_OK")
