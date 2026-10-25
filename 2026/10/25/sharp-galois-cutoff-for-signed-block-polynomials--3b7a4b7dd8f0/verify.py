"""Exact certificate for the signed-block polynomial Galois cutoff.

Only Python standard library is required. The finite-field irreducibility
checks use the Rabin criterion; integer discriminants use Bareiss elimination.
The large-degree theorem invoked in the accompanying proof is external.
"""
from math import gcd, isqrt


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def pmul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            out[i + j] = (out[i + j] + u * v) % p
    return trim(out)


def divmodp(a, b, p):
    a = trim([x % p for x in a])
    b = trim([x % p for x in b])
    assert b != [0]
    quot = [0] * max(1, len(a) - len(b) + 1)
    inv = pow(b[-1], -1, p)
    while a != [0] and len(a) >= len(b):
        degree = len(a) - len(b)
        mult = a[-1] * inv % p
        quot[degree] = mult
        for j, bj in enumerate(b):
            a[degree + j] = (a[degree + j] - mult * bj) % p
        a = trim(a)
    return trim(quot), a


def modp(a, f, p):
    return divmodp(a, f, p)[1]


def pgcd(a, b, p):
    a, b = trim([x % p for x in a]), trim([x % p for x in b])
    while b != [0]:
        a, b = b, modp(a, b, p)
    return trim([z * pow(a[-1], -1, p) % p for z in a])


def ppow(a, e, f, p):
    out = [1]
    a = modp(a, f, p)
    while e:
        if e & 1:
            out = modp(pmul(out, a, p), f, p)
        e //= 2
        if e:
            a = modp(pmul(a, a, p), f, p)
    return out


def prime_divs(d):
    return [p for p in range(2, d + 1) if d % p == 0 and all(p % q for q in range(2, isqrt(p) + 1))]


def irreducible(f, p):
    f = trim([c % p for c in f])
    d = len(f) - 1
    assert f[-1] == 1
    if d == 1:
        return True
    x = [0, 1]
    xp = [x]
    for i in range(1, d + 1):
        xp.append(ppow(xp[-1], p, f, p))
    if xp[d] != x:
        return False
    for r in prime_divs(d):
        t = xp[d // r].copy()
        t[1] = (t[1] - 1) % p
        if pgcd(f, t, p) != [1]:
            return False
    return True


def split_one_and_d_minus_one(f, p):
    d = len(f) - 1
    xp = ppow([0, 1], p, f, p)
    xp += [0] * max(0, 2 - len(xp))
    xp[1] = (xp[1] - 1) % p
    lin = pgcd(f, xp, p)
    if len(lin) != 2:
        return False
    q, rem = divmodp(f, lin, p)
    return rem == [0] and len(q) - 1 == d - 1 and irreducible(q, p)


def bareiss(A):
    A = [row.copy() for row in A]
    n = len(A)
    sign = 1
    old = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            i = next((i for i in range(k + 1, n) if A[i][k] != 0), None)
            if i is None:
                return 0
            A[k], A[i] = A[i], A[k]
            sign *= -1
        t = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                v = A[i][j] * t - A[i][k] * A[k][j]
                assert v % old == 0
                A[i][j] = v // old
            A[i][k] = 0
        old = t
    return sign * A[-1][-1]


def discriminant(f):
    d = len(f) - 1
    if d <= 1:
        return 1
    g = [i * f[i] for i in range(1, len(f))]
    m, n = len(f) - 1, len(g) - 1
    F, G = f[::-1], g[::-1]
    A = [[0] * (m + n) for _ in range(m + n)]
    for i in range(n):
        A[i][i:i + m + 1] = F
    for i in range(m):
        A[n + i][i:i + n + 1] = G
    return (-1) ** (d * (d - 1) // 2) * bareiss(A)


def isprime(n):
    if n < 2:
        return False
    return all(n % d for d in range(2, isqrt(n) + 1))


def block(n, k):
    return [-1] * k + [1] * (n - k)


def int_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            out[i + j] += v * w
    return out


def main():
    # n,k,integer discriminant, modular irreducibility prime,
    # modular (1,d-1) factorization prime, squarefree discriminant prime.
    rows = [
        (2, 1, 1, 2, None, None),
        (3, 1, 5, 2, None, 5),
        (4, 1, -44, 3, None, 11),
        (5, 1, -563, 2, 3, 563),
        (5, 2, -331, 2, 5, 331),
        (6, 1, 9584, 5, None, 599),
        (7, 1, 205937, 3, 17, 205937),
        (7, 3, 61193, 3, 41, 11),
        (8, 1, -5390272, 7, None, 84223),
        (8, 3, -1205696, 3, None, 18839),
    ]
    count = 0
    for n, k, d, irr_p, cycle_p, ram_p in rows:
        f = block(n, k)
        assert discriminant(f) == d, (n, k, discriminant(f), d)
        assert irreducible(f, irr_p), (n, k, irr_p)
        if cycle_p is not None:
            assert split_one_and_d_minus_one(f, cycle_p), (n, k, cycle_p)
        if ram_p is not None:
            assert isprime(ram_p)
            assert d % ram_p == 0 and d % (ram_p * ram_p) != 0
        count += 1
    a = [1, 1, 0, 1]   # X^3 + X + 1
    b = [-1, 0, 1, 1]  # X^3 + X^2 - 1
    assert int_mul(a, b) == block(7, 2)
    assert discriminant(a) == -31 and discriminant(b) == -23
    assert irreducible(a, 2) and irreducible(b, 2)
    assert gcd(31, 23) == 1
    # Confirm every reciprocal pair and all coprime k up through n=8.
    for n in range(2, 9):
        for k in range(1, n):
            if gcd(n, k) == 1:
                assert block(n, n - k) == [-v for v in block(n, k)[::-1]]
    print('CERTIFICATE_OK representative_pairs=', count,
          ' n8_modular_cases=2', ' cubic_discriminants=-31,-23',
          ' lower_degree_exception=(7,2),(7,5)')


if __name__ == '__main__':
    main()
