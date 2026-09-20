#!/usr/bin/env python3
"""Exact finite verification for the k=7 divisor-sum theorem."""

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def vp(n, p):
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e

def S(alpha):
    return (2 ** (7 * alpha) - 1) // 127

def common_inequality(v, beta, lam):
    lhs = (2**lam - 1) ** (beta - 1)
    rhs = sum(2 ** (i * (lam + v)) for i in range(7))
    return lhs <= rhs

# The next beta after 12 when v=2 is already impossible at lambda=2.
assert not common_inequality(2, 20, 2)
# The next beta after 8 when v=3 is already impossible at lambda=2.
assert not common_inequality(3, 24, 2)

# Constants used in the beta=4 elimination.
expected_constants = {
    1: 5461,   # 43 * 127
    2: 8128,   # 2^6 * 127
    3: 14197,  # prime
    4: 28672,  # 2^12 * 7
    5: 61741,  # 29 * 2129
}
for t, expected in expected_constants.items():
    got = sum(4**i * t**(6-i) for i in range(7))
    assert got == expected
assert 5461 == 43 * 127
assert 8128 == 2**6 * 127
assert is_prime(14197)
assert 28672 == 2**12 * 7
assert 61741 == 29 * 2129
assert is_prime(29) and is_prime(2129)

def finite_rows(v, beta, lambda_values):
    rows = []
    q_bound = 3 * 2 ** (v - 1)
    for lam in lambda_values:
        for q in range(1, q_bound, 2):
            p = q * 2**lam - 1
            if not is_prime(p) or p == 7:
                continue
            for alpha in range(2, lam + v + 1):
                if p >= 3 * 2**(alpha - 1) - 1:
                    continue
                rows.append((alpha, p, lam, q, vp(S(alpha), p)))
    return rows

# The elementary exponent bound
#   (lambda-1)(beta-1) < 6(lambda+v)+1
# gives lambda <= 4, 25, 4 in the three remaining cases.
cases = [
    (2, 12, range(2, 5), 11, 8, 1),
    (3, 8, range(2, 26), 7, 62, 1),
    (4, 16, range(2, 5), 15, 33, 2),
]

for v, beta, lambdas, required, expected_count, expected_max in cases:
    rows = finite_rows(v, beta, lambdas)
    maximum = max(row[-1] for row in rows)
    assert len(rows) == expected_count
    assert maximum == expected_max
    assert maximum < required
    print(
        f"v={v}, beta={beta}: "
        f"{len(rows)} admissible tuples; "
        f"max v_p(S_alpha)={maximum} < {required}"
    )

# Independent small-box sanity check of the original divisibility.
solutions = []
for alpha in range(2, 15):
    bound = 3 * 2**(alpha - 1) - 1
    for p in range(3, bound, 2):
        if not is_prime(p):
            continue
        for beta in range(2, 21):
            sig2 = S(alpha)
            sigp = (p ** (7 * beta) - 1) // (p**7 - 1)
            n = 2**(alpha - 1) * p**(beta - 1)
            if (sig2 * sigp) % n == 0:
                solutions.append((alpha, p, beta))

assert solutions == [
    (2, 3, 2),
    (3, 7, 2),
    (5, 31, 2),
    (13, 8191, 2),
]
print("small-box sanity check:", solutions)
