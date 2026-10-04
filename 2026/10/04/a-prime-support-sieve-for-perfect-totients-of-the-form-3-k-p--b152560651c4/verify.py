from math import gcd

LIMIT = 200_000
KMAX = 8
EVEN_LIMIT = 20_000


def phi(n):
    r = n
    d = 2
    x = n
    while d*d <= x:
        if x % d == 0:
            while x % d == 0:
                x //= d
            r -= r // d
        d += 1 if d == 2 else 2
    if x > 1:
        r -= r // x
    return r


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def totient_sum(n):
    s = 0
    x = n
    while x != 1:
        x = phi(x)
        s += x
    return s


def strip_2_3(n):
    while n % 2 == 0:
        n //= 2
    while n % 3 == 0:
        n //= 3
    return n

# Directly check the lemma used in the proof.
even_checked = 0
for m in range(2, EVEN_LIMIT + 1, 2):
    assert totient_sum(m) <= 2 * phi(m) - 1
    even_checked += 1

# Check the theorem on every prime p <= LIMIT and k in [2,KMAX].
target_hits = []
sieve_violations = []
for p in range(5, LIMIT + 1, 2):
    if not is_prime(p):
        continue
    u = strip_2_3(p - 1)
    lhs_num = phi(u)
    lhs_den = u
    # Exact integer form of phi(u)/u > 3(p+2)/(4(p-1)).
    support_ok = 4 * (p - 1) * lhs_num > 3 * (p + 2) * lhs_den
    for k in range(2, KMAX + 1):
        n = (3 ** k) * p
        if totient_sum(n) == n:
            target_hits.append((k, p, n, u))
            if not support_ok:
                sieve_violations.append((k, p, n, u))
            assert u % 35 != 0 and u % 55 != 0 and u % 65 != 0

assert not sieve_violations
print(
    "VERIFY_OK "
    f"limit={LIMIT} kmax={KMAX} even_checked={even_checked} "
    f"target_hits={target_hits} sieve_violations=0"
)
