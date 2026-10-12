from math import gcd


def euclid_quotients(q, p):
    assert 1 < p < q and gcd(p, q) == 1
    out = []
    while p:
        out.append(q // p)
        q, p = p, q % p
    return out


def least_bezout(p, q):
    a = pow(p, -1, q)
    b = (a * p - 1) // q
    assert 0 < a < q and 0 < b < p and a * p - b * q == 1
    return a, b


def T_direct(n):
    return sum(
        1
        for m in range(1, n + 1, 2)
        if gcd(m, n) == 1 and gcd((m - 1) // 2, n) == 1
    )


def primes_upto(n):
    ps = []
    for x in range(2, n + 1):
        if all(x % p for p in ps if p * p <= x):
            ps.append(x)
    return ps


# The parity theorem for all coprime odd pairs in a substantial exact box.
pair_cases = 0
for p in range(3, 302, 2):
    for q in range(p + 2, 402, 2):
        if gcd(p, q) != 1:
            continue
        a, b = least_bezout(p, q)
        qs = euclid_quotients(q, p)
        assert qs[-1] >= 2
        assert (a & 1) == (sum(qs) & 1)
        assert (a ^ b) & 1 == 1
        pair_cases += 1

# The two-prime-power branch, checked by direct enumeration wherever n is modest.
ps = [p for p in primes_upto(43) if p % 2]
branch_cases = 0
examples = []
for i, p in enumerate(ps):
    for q in ps[i + 1:]:
        parity = sum(euclid_quotients(q, p)) & 1
        for e in range(1, 4):
            for f in range(1, 4):
                n = (p ** e) * (q ** f)
                if n > 30000:
                    continue
                S = (p ** (e - 1)) * (q ** (f - 1)) * (p - 2) * (q - 2)
                expected = (S + 1) // 2 if parity else (S - 3) // 2
                got = T_direct(n)
                assert got == expected, (p, q, e, f, got, expected)
                branch_cases += 1
                if e == f == 1 and len(examples) < 8:
                    examples.append((p, q, sum(euclid_quotients(q, p)), got))

print(
    "VERIFY_OK",
    f"bezout_parity_pairs={pair_cases}",
    f"two_prime_power_cases={branch_cases}",
    "examples=" + ";".join(f"{p},{q},Q={s},T={t}" for p,q,s,t in examples),
)
