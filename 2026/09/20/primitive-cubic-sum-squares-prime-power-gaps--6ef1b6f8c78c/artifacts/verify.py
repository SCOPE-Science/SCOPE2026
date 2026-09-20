from math import gcd

LIMIT = 500


def is_prime_power(n):
    """Return (p,e) when n=p**e for a prime p and e>=1, else None."""
    if n < 2:
        return None
    if n % 2 == 0:
        p = 2
    else:
        p = None
        d = 3
        while d * d <= n:
            if n % d == 0:
                p = d
                break
            d += 2
        if p is None:
            return (n, 1)

    m = n
    e = 0
    while m % p == 0:
        m //= p
        e += 1
    return (p, e) if m == 1 else None


def predicted_branch(a, b, prime_power):
    if prime_power is None:
        return None
    ell, exponent = prime_power
    A = a * (a * a - 3 * b * b)

    if A < 0:
        if ell != 3 and a == b + 1:
            return "star"
        return None

    Q = a * a - 4 * a * b + b * b
    if ell != 3 and Q == 1:
        return "pell"
    if ell == 3 and (a, b) in {(2, 1), (7, 2)}:
        return "three"
    return None


checked = 0
prime_power_hits = 0
branch_counts = {"star": 0, "pell": 0, "three": 0}
mismatches = []
examples = []

for a in range(2, LIMIT + 1):
    for b in range(1, a):
        if gcd(a, b) != 1 or (a - b) % 2 == 0:
            continue

        checked += 1
        A = a * (a * a - 3 * b * b)
        B = b * (3 * a * a - b * b)
        x, y, z = abs(A), B, a * a + b * b
        assert x * x + y * y == z ** 3

        delta = abs(x - y)
        prime_power = is_prime_power(delta)
        branch = predicted_branch(a, b, prime_power)

        if (prime_power is not None) != (branch is not None):
            mismatches.append((a, b, delta, prime_power, branch))

        if prime_power is not None:
            prime_power_hits += 1
            branch_counts[branch] += 1
            if len(examples) < 12:
                examples.append(
                    (a, b, x, y, z, delta, prime_power, branch)
                )

print(f"normalized parameter pairs checked: {checked}")
print(f"prime-power gaps found: {prime_power_hits}")
print(
    "branch counts: "
    + ", ".join(
        f"{name}={branch_counts[name]}"
        for name in ("star", "pell", "three")
    )
)
print(f"classification mismatches: {len(mismatches)}")
print("first examples:")
for row in examples:
    print(row)
