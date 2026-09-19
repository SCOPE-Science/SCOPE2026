from math import gcd, log2


def bits(x, n):
    return tuple((x >> i) & 1 for i in range(n))


def asint(z):
    return sum(b << i for i, b in enumerate(z))


def chi(z):
    n = len(z)
    return tuple(z[i] ^ (z[(i + 1) % n] & z[(i + 2) % n]) ^ z[(i + 2) % n] for i in range(n))


def f_map(z, v):
    n = len(z)
    return tuple(z[i] ^ (z[(i + v) % n] & z[(i + 2 * v) % n]) ^ z[(i + 2 * v) % n] for i in range(n))


def g_map(z, v):
    n = len(z)
    return tuple(z[i] ^ (z[(i - 2 * v) % n] & z[(i - v) % n]) ^ z[(i - v) % n] for i in range(n))


def affine_a(z):
    n = len(z)
    return tuple(1 ^ z[(-i) % n] for i in range(n))


def blocks(z, v):
    n = len(z)
    d = gcd(n, v)
    ell = n // d
    return [tuple(z[(r + t * v) % n] for t in range(ell)) for r in range(d)]


def anf_degree(table, n):
    a = list(table)
    for j in range(n):
        bit = 1 << j
        for mask in range(1 << n):
            if mask & bit:
                a[mask] ^= a[mask ^ bit]
    return max((mask.bit_count() for mask, c in enumerate(a) if c), default=0)


def inverse_degree(mapfun, n):
    inv = [None] * (1 << n)
    for x in range(1 << n):
        y = asint(mapfun(bits(x, n)))
        assert inv[y] is None
        inv[y] = x
    degree = 0
    for j in range(n):
        table = [(inv[y] >> j) & 1 for y in range(1 << n)]
        degree = max(degree, anf_degree(table, n))
    return degree


def permutation_order(mapfun, n, cap=1024):
    perm = [asint(mapfun(bits(x, n))) for x in range(1 << n)]
    current = list(range(1 << n))
    for exponent in range(1, cap + 1):
        current = [perm[x] for x in current]
        if all(current[x] == x for x in range(1 << n)):
            return exponent
    raise AssertionError("order exceeds cap")


block_checks = 0
for n in range(3, 14):
    for v in range(1, n):
        ell = n // gcd(n, v)
        if ell % 2 == 0:
            continue
        for x in range(1 << n):
            z = bits(x, n)
            assert blocks(f_map(z, v), v) == [chi(b) for b in blocks(z, v)]
            assert blocks(g_map(z, v), v) == [affine_a(chi(affine_a(b))) for b in blocks(z, v)]
            block_checks += 2

inverse_cases = []
for n, v in [(6, 2), (10, 2), (12, 4), (14, 2), (15, 3), (15, 5)]:
    ell = n // gcd(n, v)
    degree = inverse_degree(lambda z, v=v: f_map(z, v), n)
    assert degree == (ell + 1) // 2
    inverse_cases.append((n, v, ell, degree))

order_cases = []
for n, v in [(6, 2), (10, 2), (12, 4), (15, 3), (15, 5)]:
    ell = n // gcd(n, v)
    expected = 1 << int(log2(ell))
    f_order = permutation_order(lambda z, v=v: f_map(z, v), n)
    g_order = permutation_order(lambda z, v=v: g_map(z, v), n)
    assert f_order == expected == g_order
    order_cases.append((n, v, ell, f_order))

print("PASS")
print("block_checks =", block_checks)
print("inverse_degree_cases =", inverse_cases)
print("order_cases =", order_cases)
