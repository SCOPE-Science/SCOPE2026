from math import isqrt

B = 100_000


def square_terms(limit, weight=1):
    out = []
    for x in range(isqrt(limit) + 1):
        out.append((weight * x * x, 1 if x == 0 else 2))
    return out


def ternary_counts(a, b, c):
    out = [0] * (B + 1)
    xs = square_terms(B, a)
    ys = square_terms(B, b)
    zs = square_terms(B, c)
    for xv, xm in xs:
        for yv, ym in ys:
            s = xv + yv
            if s > B:
                break
            mult = xm * ym
            for zv, zm in zs:
                n = s + zv
                if n > B:
                    break
                out[n] += mult * zm
    return out


def smallest_prime_factors(limit):
    spf = list(range(limit + 1))
    if limit >= 1:
        spf[1] = 1
    for p in range(2, isqrt(limit) + 1):
        if spf[p] == p:
            for n in range(p * p, limit + 1, p):
                if spf[n] == n:
                    spf[n] = p
    return spf


def factor_data(n, spf):
    k = 0
    squarefree = True
    while n > 1:
        p = spf[n]
        exponent = 0
        while n % p == 0:
            n //= p
            exponent += 1
        if exponent > 1:
            squarefree = False
        k += 1
    return squarefree, k


r3 = ternary_counts(1, 1, 1)
r135 = ternary_counts(1, 3, 5)
spf = smallest_prime_factors(B)

# (modulus, residues, comparator, normalization denominator)
rows = [
    (40, {11, 19}, r3, 8),
    (40, {21, 29}, r3, 8),
    (40, {3, 27}, r3, 8),
    (40, {7, 23}, r135, 4),
    (120, {53, 77}, r3, 8),
    (120, {43, 67}, r3, 8),
    (120, {11, 59}, r3, 8),
    (120, {31, 79}, r135, 4),
    (120, {23, 47}, r135, 4),
    (120, {19, 91}, r3, 8),
    (120, {83, 107}, r3, 8),
    (120, {7, 103}, r135, 4),
]

checks = 0
for modulus, residues, counts, denominator in rows:
    for n in range(2, B + 1):
        if n % modulus not in residues:
            continue
        squarefree, omega = factor_data(n, spf)
        if not squarefree:
            continue
        assert counts[n] % denominator == 0
        normalized_parity = (counts[n] // denominator) & 1
        is_prime = omega == 1
        assert normalized_parity == int(is_prime), (modulus, residues, n, counts[n])
        checks += 1

# The comparison-row hypothesis is essential: outside it, the r_135 parity
# need not vanish on squarefree composites.
assert r135[39] // 4 == 3
assert r135[111] // 4 == 7

print(f"bound={B}")
print(f"row-membership checks={checks}")
print("all normalized comparator parities equal the prime indicator")
print("outside-row checks: r135(39)/4=3, r135(111)/4=7")
