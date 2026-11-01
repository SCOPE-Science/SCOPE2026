"""Supplementary exact and floating-point checks for discrete q-Hermite kernel asymptotics.

The analytic uniform convergence and exact limiting constant are proved in RESULT.md.
No external Python packages are required.
"""
from fractions import Fraction
from math import e, isclose

checks = 0

def check(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1


def poch(q, j, step=1):
    out = Fraction(1)
    for k in range(1, j + 1):
        out *= (1 - q ** (step * k))
    return out


def coeff_formula(n, q):
    result = [Fraction(0) for _ in range(n + 1)]
    for k in range(n // 2 + 1):
        ratio = Fraction(1)
        for j in range(n - 2 * k + 1, n + 1):
            ratio *= (1 - q ** j)
        result[n - 2 * k] = ((-1) ** k * q ** (k * (k - 1))
                              * ratio / poch(q, k, 2))
    return result


def rec_polys(q, highest):
    poly = [[Fraction(1)], [Fraction(0), Fraction(1)]]
    for n in range(1, highest):
        nxt = [Fraction(0)] * (n + 2)
        gamma = q ** (n - 1) * (1 - q ** n)
        for j, a in enumerate(poly[n]):
            nxt[j + 1] += a
        for j, a in enumerate(poly[n - 1]):
            nxt[j] -= gamma * a
        poly.append(nxt)
    return poly[:highest + 1]


for q in (Fraction(1, 2), Fraction(2, 3), Fraction(3, 4)):
    polys = rec_polys(q, 20)
    for n, p in enumerate(polys):
        check(p == coeff_formula(n, q), f"recurrence/coefficients n={n}, q={q}")
        endpoint = sum(p)
        check(endpoint == q ** (n * (n - 1) // 2),
              f"endpoint n={n}, q={q}")
    for x in (Fraction(0), Fraction(1, 3), Fraction(1), Fraction(-1)):
        for j in (1, 2, 4, 7):
            left = Fraction(1)
            right = Fraction(1)
            for m in range(1, j + 1):
                left *= 1 - q ** (2 * m) * x * x
                right *= (1 - q ** m * x) * (1 + q ** m * x)
            check(left == right, f"weight product q={q}, x={x}")


def c_q(q):
    product = 1.0
    j = 1
    while q ** (2 * j) > 1e-16:
        product *= 1.0 - q ** (2 * j)
        j += 1
    return product


def w_q(q, x):
    product = 1.0
    j = 1
    while q ** (2 * j) > 1e-16:
        product *= 1.0 - (q ** (2 * j)) * x * x
        j += 1
    return product


def diagonal_tail(q, n_cutoff, x):
    # Long finite tail: for x=1-O(1/N), a 35N cutoff makes the
    # omitted purely geometric tail exponentially small in 35.
    h0 = 1.0
    h1 = x
    total = 0.0
    limit = 35 * n_cutoff
    for n in range(1, limit):
        if n > n_cutoff:
            total += h1 * h1
        h_next = x * h1 - q ** (n - 1) * (1.0 - q ** n) * h0
        h0, h1 = h1, h_next
    if limit > n_cutoff:
        total += h1 * h1
    return w_q(q, x) ** 2 * total


def maximize_tail(q, N):
    # Golden section on the predicted boundary layer, solely as a check.
    lo, hi = 0.12, 1.2
    golden = (5 ** 0.5 - 1) / 2
    c = hi - golden * (hi - lo)
    d = lo + golden * (hi - lo)
    for _ in range(53):
        if diagonal_tail(q, N, 1 - c / N) > diagonal_tail(q, N, 1 - d / N):
            hi = d
        else:
            lo = c
        c = hi - golden * (hi - lo)
        d = lo + golden * (hi - lo)
    s = (lo + hi) / 2
    return s, diagonal_tail(q, N, 1 - s / N)


for q in (0.2, 0.5, 0.8, 0.9):
    C = c_q(q)
    limit = C ** 4 / e
    for N in (75, 150, 300):
        s, observed = maximize_tail(q, N)
        check(0.44 < s < 0.56, f"boundary layer q={q}, N={N}: {s}")
        rel = N * observed / limit
        check(0.96 < rel < 1.04, f"leading constant q={q}, N={N}: {rel}")

# These are finite checks only; they do not establish the infinite limit.
print(f"CHECK_OK {checks}")
