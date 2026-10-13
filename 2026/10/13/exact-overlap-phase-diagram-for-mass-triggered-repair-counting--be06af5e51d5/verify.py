from fractions import Fraction as F


def mass(h, a, b):
    if a > b:
        return F(0)
    return sum(h[i] for i in range(a, b + 1))


def check_repairs(h, repairs, L, U):
    last_v = None
    last_p = None
    for u, p, v in repairs:
        assert 1 <= u <= p <= v < len(h)
        if last_v is not None:
            assert v > last_v
            assert u >= last_p + 1
        assert mass(h, u, v) >= L
        assert mass(h, p + 1, v) <= U
        last_v, last_p = v, p


def multiplicity(repairs):
    lo = min(u for u, _, _ in repairs)
    hi = max(v for _, _, v in repairs)
    return max(sum(u <= t <= v for u, _, v in repairs) for t in range(lo, hi + 1))


def sharp(L, U):
    assert L > U
    d = L - U
    q = U // d
    if q == 0:
        h = [F(0), L, F(0), L]
        r = [(1, 1, 2), (2, 3, 3)]
        check_repairs(h, r, L, U)
        assert multiplicity(r) == 2
        return
    R = U - q * d
    N = 2 * q + 3
    h = [F(0)] * (N + 1)
    for i in range(1, q + 2):
        h[i] = d
    h[q + 2] = R
    for i in range(q + 3, 2 * q + 3):
        h[i] = d
    h[2 * q + 3] = R + d
    repairs = [(j, j, q + j + 1) for j in range(1, q + 2)]
    repairs.append((q + 2, q + 3, 2 * q + 3))
    check_repairs(h, repairs, L, U)
    assert multiplicity(repairs) == q + 2


def unbounded_example(K):
    L = U = F(1)
    h = [F(0)] * (2 * K + 1)
    h[K + 1] = L
    repairs = [(j, j, K + j) for j in range(1, K + 1)]
    check_repairs(h, repairs, L, U)
    assert multiplicity(repairs) == K


# Source specialization.
L, U = F(4), F(1)
assert L > 2 * U
assert 2 + U // (L - U) == 2
sharp(L, U)

# Two nontrivial sharp finite-overlap regimes.
sharp(F(7, 4), F(1))
sharp(F(3, 2), F(1))

# No finite universal bound when L <= U.
unbounded_example(9)

# Sharpness of the strict L > 2U separation threshold.
L, U = F(2), F(1)
d = L - U
h = [F(0), U, d, F(0), U]
repairs = [(1, 1, 3), (2, 3, 4)]
check_repairs(h, repairs, L, U)
assert repairs[1][1] == repairs[0][2]

print('VERIFY_OK')
