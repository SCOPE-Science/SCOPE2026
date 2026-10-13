from fractions import Fraction
from math import floor, log


def frac(x):
    return x - floor(x)


def length_float(Q, m):
    v0 = 1.5 - m / Q
    fv = frac(v0)
    if m % 2:
        return min(fv / (1 + 1 / Q), (1 - fv) / (1.5 - 1 / Q))
    w0 = -m / Q
    fw = frac(w0)
    if fw <= 0.5:
        return 0.0
    return min((fw - 0.5) / (1 + 1 / Q), (1 - fw) / (1.5 - 1 / Q))


def exact_checks(Q):
    q = Fraction(Q, 1)
    a = 1 / (Fraction(3, 2) - 1 / q)
    N = Q // 20
    checked = 0
    for m in range(1, N + 1):
        t = Fraction(m, Q)
        A = (Fraction(1, 2) - t) / (1 + 1 / q)
        if m % 2:
            B = (Fraction(1, 2) + t) / (Fraction(3, 2) - 1 / q)
            assert B <= A
            L = B
            L0 = Fraction(1, 3)
        else:
            B = t / (Fraction(3, 2) - 1 / q)
            assert B <= A
            L = B
            L0 = Fraction(0, 1)
        F = lambda X: Fraction(1, m) - 1 / (Fraction(m, 1) + X)
        lhs = F(L) - F(L0)
        rhs = a / (q * (Fraction(m, 1) + L))
        assert lhs == rhs
        checked += 1
    return checked


def truncated_J(Q, M):
    s = 0.0
    si = 0.0
    for m in range(1, M + 1):
        L = length_float(Q, m)
        s += 1.0 / m - 1.0 / (m + L)
        L0 = 1.0 / 3.0 if m % 2 else 0.0
        si += 1.0 / m - 1.0 / (m + L0)
    return s - si


count = 0
for Q in (40, 100, 500, 2000):
    count += exact_checks(Q)
rows = []
for Q in (200, 1000, 5000):
    M = 200 * Q
    d = truncated_J(Q, M)
    scaled = Q * d - (2.0 / 3.0) * log(Q)
    rows.append((Q, M, scaled))
assert all(-1.25 < s < -1.10 for _, _, s in rows)
print('VERIFY_OK exact_low_branch_cases=%d' % count)
for Q, M, s in rows:
    print('Q=%d cutoff=%d scaled_remainder=%.12f' % (Q, M, s))
