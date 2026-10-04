#!/usr/bin/env python3
import math
from pathlib import Path

LIMIT = 10**38
MR_BASES = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)
SMALL_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)

def is_prime_64(n):
    if n < 2:
        return False
    for p in SMALL_PRIMES:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in MR_BASES:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True

def rho_split(n):
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    for c in range(1, 200):
        x = 2 + c
        y = x
        d = 1
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = math.gcd(abs(x - y), n)
        if d != n:
            return d
    raise RuntimeError("Pollard-Rho failed to split an input")

def factor_64(n, out=None):
    if out is None:
        out = []
    if n == 1:
        return out
    if is_prime_64(n):
        out.append(n)
        return out
    d = rho_split(n)
    factor_64(d, out)
    factor_64(n // d, out)
    return out

def factor_counts_64(n):
    assert 1 <= n < 2**64
    fs = sorted(factor_64(n, []))
    prod = 1
    counts = {}
    for p in fs:
        assert is_prime_64(p)
        prod *= p
        counts[p] = counts.get(p, 0) + 1
    assert prod == n
    return counts

def sigma_square_from_base(a):
    counts = factor_counts_64(a)
    ans = 1
    for p, e in counts.items():
        ans *= (p ** (2 * e + 1) - 1) // (p - 1)
    return ans

def candidates():
    rows = []
    # Family B: N+1 = 2 a^2, N+3 = b^2, b^2 - 2 a^2 = 2.
    b, a, t = 2, 1, 0
    count_b = 0
    while 2 * a * a <= LIMIT:
        m = 2 * a * a
        assert b * b - 2 * a * a == 2
        assert a % 2 == 1 and b % 2 == 0
        rows.append(("B", t, m, a, b))
        count_b += 1
        b, a = 3 * b + 4 * a, 2 * b + 3 * a
        t += 1
    next_b = ("B", t, 2 * a * a, a, b)

    # Family A: N+1 = a^2, N+3 = 2 b^2, a^2 - 2 b^2 = -2.
    a, b, t = 4, 3, 1
    count_a = 0
    while a * a <= LIMIT:
        m = a * a
        assert a * a - 2 * b * b == -2
        assert a % 2 == 0 and b % 2 == 1
        rows.append(("A", t, m, a, b))
        count_a += 1
        a, b = 3 * a + 4 * b, 2 * a + 3 * b
        t += 1
    next_a = ("A", t, a * a, a, b)

    rows.sort(key=lambda z: z[2])
    return rows, count_a, count_b, next_a, next_b

def make_csv(rows):
    out = ["family,t,N,N_plus_1,a,b,identity_left,identity_right,residual\n"]
    for fam, t, m, a, b in rows:
        assert max(a, b) < 2**64
        sa = sigma_square_from_base(a)
        sb = sigma_square_from_base(b)
        if fam == "A":
            left = sa + 2
            right = 3 * sb
        else:
            left = 3 * sa + 2
            right = sb
        residual = left - right
        assert residual != 0
        N = m - 1
        out.append(f"{fam},{t},{N},{m},{a},{b},{left},{right},{residual}\n")
    return "".join(out)

def main():
    rows, count_a, count_b, next_a, next_b = candidates()
    assert count_a == 25
    assert count_b == 25
    assert len(rows) == 50
    assert all(m <= LIMIT for _, _, m, _, _ in rows)
    assert next_a[2] > LIMIT
    assert next_b[2] > LIMIT

    # The largest coordinate below the cutoff is still in the deterministic 64-bit range.
    assert max(max(a, b) for _, _, _, a, b in rows) < 2**64

    generated = make_csv(rows)
    expected = Path("pell_candidates.csv").read_text(encoding="utf-8")
    assert generated == expected

    print("VERIFY_OK")
    print("candidate_count=50")
    print("family_A_count=25")
    print("family_B_count=25")
    print("first_excluded_A_N_plus_1=" + str(next_a[2]))
    print("first_excluded_B_N_plus_1=" + str(next_b[2]))
    print("largest_checked_N_plus_1=" + str(max(r[2] for r in rows)))
    print("largest_coordinate=" + str(max(max(r[3], r[4]) for r in rows)))

if __name__ == "__main__":
    main()
