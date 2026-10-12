from math import isqrt, gcd


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


def prime_factors(n):
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        out.append(n)
    return out


def obstruction(p):
    n = p - 1
    m = n // 2
    return [q for q in prime_factors(m) if n % (q - 1) == 0]


def form(x, y):
    return -x * x + 2 * x * y + 2 * y * y

p = 1871
assert is_prime(p)
assert form(27, 25) == p
assert (p - 1) // 2 == 935
assert 935 % 11 == 0
assert 1870 % 10 == 0
assert 11 in obstruction(p)
assert 551 == 19 * 29 and not is_prime(551)
assert 1211 == 7 * 173 and not is_prime(1211)

# For primes > 3 represented by the discriminant-12 form, the proof shows
# equivalence with p == 11 (mod 12).  Independently verify that none of those
# primes below 1871 has the prime-divisor obstruction.
checked = 0
for r in range(5, p):
    if is_prime(r) and r % 12 == 11:
        checked += 1
        assert obstruction(r) == [], (r, obstruction(r))

# The infinite family bookkeeping: p == 551 (mod 660) implies p == 11
# (mod 12), 11 | (p-1)/2 and 10 | p-1.  Also the progression is reduced.
assert 551 % 12 == 11
assert (551 - 1) % 110 == 0
assert gcd(551, 660) == 1
for t in range(8):
    r = 551 + 660 * t
    assert r % 12 == 11
    assert ((r - 1) // 2) % 11 == 0
    assert (r - 1) % 10 == 0

# Reproduce the minimality congruence argument for possible obstruction q.
# Any q must be 11 mod 12.  For q=11 the only k == 5 mod 6 with
# q(q-1)k < 1870 are 5 and 11, producing the two composites above.
ks = [k for k in range(1, 17) if k % 6 == 5]
assert ks == [5, 11]
assert [11 * 10 * k + 1 for k in ks] == [551, 1211]
assert 5 * 23 * 22 > 1870

print(f"VERIFY_OK least_counterexample={p} smaller_form_primes_checked={checked} progression_modulus=660 progression_residue=551")
