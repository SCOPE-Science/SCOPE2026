from collections import Counter

# Small exact finite-field anchors for the theorem.  Elements are represented
# in the polynomial basis modulo the listed irreducible polynomial over F_2.
IRRED = {5: 0x25, 7: 0x83, 9: 0x203}

def mul(a, b, m, poly):
    mask = (1 << m) - 1
    mod = poly & mask
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & (1 << m):
            a ^= mod
    return out & mask

def power(a, e, m, poly):
    out = 1
    while e:
        if e & 1:
            out = mul(out, a, m, poly)
        a = mul(a, a, m, poly)
        e >>= 1
    return out

def trace(a, m, poly):
    s = 0
    z = a
    for _ in range(m):
        s ^= z
        z = mul(z, z, m, poly)
    assert s in (0, 1)
    return s

def f1(a, m, poly):
    if a == 0:
        return 0
    q = 1 << m
    return power(a, q - 17, m, poly) ^ power(a, (q + 19) // 3, m, poly) ^ a

def f2(a, m, poly):
    if a == 0:
        return 0
    q = 1 << m
    e1 = q - (1 << (m - 4)) - 1
    e2 = q - ((1 << (m - 2)) + 4) // 3
    return power(a, e1, m, poly) ^ power(a, e2, m, poly) ^ a

def g4(b, m, poly):
    q = 1 << m
    total = 0
    for y in range(q):
        value = power(y, 17, m, poly) ^ mul(b, power(y, 3, m, poly), m, poly)
        total += 1 if trace(value, m, poly) == 0 else -1
    return total

def check(m):
    poly = IRRED[m]
    q = 1 << m
    d1 = {f1(a, m, poly) for a in range(q)}
    d2 = {f2(a, m, poly) for a in range(q)}
    d1.discard(0)
    d2.discard(0)
    assert d1 == d2
    D = d1
    assert len(D) == q // 2

    degree = {}
    for d in D:
        ordered = sum(1 for y in D if (y ^ d) in D)
        assert ordered % 2 == 0
        rho = ordered // 2
        g = g4(d, m, poly)
        assert rho == (q - g) // 8
        assert 8 * rho == q - g
        if g:
            # Nonzero quadratic-form values must have one of the four
            # radical dimensions r=1,3,5,7 allowed by the theorem.
            ok = any(abs(g) == (1 << ((m + r) // 2)) for r in (1, 3, 5, 7) if r <= m)
            assert ok
        degree[d] = rho

    n = len(D)
    a3 = sum(degree.values()) // 3
    assert 3 * a3 == sum(degree.values())
    assert a3 == q * (q - 2) // 48
    assert a3 == n * (n - 1) // 12
    assert len(set(degree.values())) > 1
    print(f"m={m} n={n} A3={a3} repair={dict(sorted(Counter(degree.values()).items()))}")

for m in (5, 7, 9):
    check(m)
print("VERIFY_OK")
