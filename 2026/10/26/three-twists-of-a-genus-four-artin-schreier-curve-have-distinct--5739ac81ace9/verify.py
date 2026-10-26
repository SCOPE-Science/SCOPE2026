"""Independent standard-library exact verification of three genus-four zeta functions.

Run: python3 verify.py
"""
MODULI = {1: [1, 1], 2: [1, 0, 1], 3: [1, 0, 2, 1], 4: [1, 0, 1, 1, 1]}
CLAIMED_COUNTS = {0: [5, 5, 44, 113], 1: [2, 8, 44, 44], 2: [5, 17, 44, 89]}
CLAIMED_L = {0: [1, 1, -2, 3, 15, 9, -18, 27, 81],
             1: [1, -2, 1, 6, -21, 18, 9, -54, 81],
             2: [1, 1, 4, 9, 15, 27, 36, 27, 81]}


def trim(v):
    v = list(v)
    while len(v) > 1 and not v[-1]:
        v.pop()
    return v


def add_poly(a, b, p):
    return trim([((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p
                 for i in range(max(len(a), len(b)))])


def sub_poly(a, b, p):
    return trim([((a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)) % p
                 for i in range(max(len(a), len(b)))])


def mul_poly(a, b, p):
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] = (result[i + j] + x * y) % p
    return trim(result)


def div_rem(a, b, p):
    a, b = trim([v % p for v in a]), trim([v % p for v in b])
    assert b != [0]
    q = [0] * max(1, len(a) - len(b) + 1)
    while a != [0] and len(a) >= len(b):
        k = len(a) - len(b)
        u = a[-1] * pow(b[-1], -1, p) % p
        q[k] = u
        a = sub_poly(a, [0] * k + [(u * v) % p for v in b], p)
    return trim(q), a


def rem(a, b, p):
    return div_rem(a, b, p)[1]


def gcd_poly(a, b, p):
    while b != [0]:
        a, b = b, rem(a, b, p)
    return trim([(t * pow(a[-1], -1, p)) % p for t in a])


def power_mod(a, exponent, modulus, p):
    output = [1]
    while exponent:
        if exponent & 1:
            output = rem(mul_poly(output, a, p), modulus, p)
        a = rem(mul_poly(a, a, p), modulus, p)
        exponent //= 2
    return output


def irreducible(poly, p):
    """Rabin criterion, valid for monic polynomials over F_p."""
    poly = trim([t % p for t in poly])
    assert poly[-1] == 1
    n = len(poly) - 1
    if n == 1:
        return True
    x = [0, 1]
    for divisor in range(2, n + 1):
        if n % divisor == 0 and all(divisor % t for t in range(2, int(divisor ** 0.5) + 1)):
            if gcd_poly(sub_poly(power_mod(x, p ** (n // divisor), poly, p), x, p), poly, p) != [1]:
                return False
    return sub_poly(power_mod(x, p ** n, poly, p), x, p) == [0]


def ff(m):
    mod = MODULI[m]
    assert irreducible(mod, 3), (m, mod)
    q = 3 ** m

    def digits(x):
        return [(x // 3 ** k) % 3 for k in range(m)]

    def code(v):
        return sum((v[i] % 3) * 3 ** i for i in range(m))

    def plus(a, b):
        return code([(a + b) % 3 for a, b in zip(digits(a), digits(b))])

    def times(a, b):
        a, b = digits(a), digits(b)
        return code((rem(mul_poly(a, b, 3), mod, 3) + [0] * m)[:m])

    def power(a, n):
        v = 1
        while n:
            if n & 1:
                v = times(v, a)
            a = times(a, a)
            n //= 2
        return v

    return q, plus, times, power


def counts():
    out = {c: [] for c in range(3)}
    trace_histograms = []
    for m in range(1, 5):
        q, plus, times, power = ff(m)
        hist = [0, 0, 0]
        for x in range(1, q):
            inverse_square = power(x, q - 3)
            rhs = plus(plus(times(x, x), x), inverse_square)
            trace, cur = 0, rhs
            for _ in range(m):
                trace = plus(trace, cur)
                cur = power(cur, 3)
            assert trace in (0, 1, 2)
            hist[trace] += 1
        trace_histograms.append(hist)
        for c in range(3):
            # 2 rational points lie over poles 0 and infinity, each totally ramified.
            n = 2 + 3 * hist[(-m * c) % 3]
            brute = 2
            for x in range(1, q):
                f = plus(plus(times(x, x), x), power(x, q - 3))
                for y in range(q):
                    if plus(plus(power(y, 3), times(2, y)), (-c) % 3) == f:
                        brute += 1
            assert n == brute, (c, m, n, brute)
            out[c].append(n)
    assert trace_histograms == [[1, 1, 0], [1, 2, 5], [14, 9, 3], [37, 29, 14]]
    assert out == CLAIMED_COUNTS, out
    return out


def l_from_counts(nvalues):
    q = 3
    genus = 4
    s = {k: q ** k + 1 - nvalues[k - 1] for k in range(1, genus + 1)}
    co = [1]
    for k in range(1, genus + 1):
        numerator = -sum(co[k-j] * s[j] for j in range(1, k + 1))
        assert numerator % k == 0
        co.append(numerator // k)
    for i in range(genus + 1, 2 * genus + 1):
        co.append(q ** (i - genus) * co[2 * genus - i])
    return co


def polynomial_modular_certificates():
    # Each mod-2 factor has degree four (including multiplicity),
    # each mod-5 factor has degree 2 or 6: disjoint possible proper degrees.
    factors2 = {
        0: [[1,1,0,0,1],[1,0,0,1,1]],
        1: [[1,1,1,1,1],[1,1,1,1,1]],
        2: [[1,1,0,0,1],[1,0,0,1,1]]}
    factors5 = {
        0: [[2,0,1],[-2,-2,0,0,0,2,1]],
        1: [[2,1,1],[-2,0,-1,1,2,0,1]],
        2: [[2,-1,1],[-2,2,-1,-2,2,-2,1]]}
    for c in range(3):
        for p, parts in [(2, factors2[c]), (5, factors5[c])]:
            total = [1]
            for f in parts:
                f = [v % p for v in f]
                assert irreducible(f, p), (c, p, f)
                total = mul_poly(total, f, p)
            assert total == [v % p for v in CLAIMED_L[c]], (c, p, total)
        assert {len(f)-1 for f in factors2[c]} == {4}
        assert {len(f)-1 for f in factors5[c]} == {2, 6}


def main():
    counts_table = counts()
    for c, n in counts_table.items():
        assert l_from_counts(n) == CLAIMED_L[c], (c, l_from_counts(n))
        # Functional-equation coefficient symmetry is checked by l_from_counts.
        assert sum((CLAIMED_L[c][i] % 3 != 0) for i in range(9)) == 3
        # No integral factor can exist, by incompatible factor-degree partitions
        # modulo 2 and 5. Thus the Weil polynomial is Q-irreducible.
    polynomial_modular_certificates()
    assert len({tuple(row) for row in CLAIMED_L.values()}) == 3
    print('VERIFY_OK')
    for c in range(3):
        print('c=', c, 'N1..N4=', counts_table[c], 'L=', CLAIMED_L[c])


if __name__ == '__main__':
    main()
