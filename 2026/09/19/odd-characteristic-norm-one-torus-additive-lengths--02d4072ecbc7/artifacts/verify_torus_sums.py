#!/usr/bin/env python3
"""Finite-field sanity checks for the norm-one torus sumset formulas.

The prime-field cases are exhaustive.  The q=p^2 cases use a nested quadratic
representation and check non-prime prime powers as well.  These computations
support, but do not replace, the general algebraic proof in RESULT.md.
"""

def legendre_prime(a, p):
    a %= p
    if a == 0:
        return 0
    return -1 if pow(a, (p - 1) // 2, p) == p - 1 else 1


def check_prime(p):
    d = next(a for a in range(2, p) if legendre_prime(a, p) == -1)
    elements = [(a, b) for a in range(p) for b in range(p)]

    def add(x, y):
        return ((x[0] + y[0]) % p, (x[1] + y[1]) % p)

    def norm(x):
        return (x[0] * x[0] - d * x[1] * x[1]) % p

    T = {x for x in elements if norm(x) == 1}
    T2 = {add(x, y) for x in T for y in T}
    T3 = {add(x, y) for x in T2 for y in T}
    chi_m3 = legendre_prime(-3, p)
    epsilon = int(chi_m3 != 1)

    assert len(T) == p + 1
    assert len(T2) == (p * p + 2 * p + 3) // 2
    assert len(T3) == (p * p if epsilon else p * p - 1)
    if not epsilon:
        assert (0, 0) not in T3

    counts = [0, 0, 0, 0]
    for s in elements:
        if s == (0, 0):
            ell = 0
        elif s in T:
            ell = 1
        elif s in T2:
            ell = 2
        elif s in T3:
            ell = 3
        else:
            raise AssertionError("length exceeds three")
        counts[ell] += 1

        if s != (0, 0) and norm(s) != 1:
            a = norm(s)
            Delta = (1 - 4 * pow(a, -1, p)) % p
            predicted = 2 if legendre_prime(Delta, p) in (0, -1) else 3
            assert ell == predicted

    expected = [
        1,
        p + 1,
        (p + 1) * ((p + 1) // 2 - epsilon),
        (p + 1) * (p - 5 + 2 * epsilon) // 2,
    ]
    assert counts == expected
    return counts, len(T2), len(T3), chi_m3


def check_square_prime_power(p):
    # E = F_{p^2} = F_p[a]/(a^2-d0), then K = E[b]/(b^2-D).
    d0 = next(a for a in range(2, p) if legendre_prime(a, p) == -1)
    E = [(x, y) for x in range(p) for y in range(p)]
    zero, one = (0, 0), (1, 0)

    def eadd(x, y):
        return ((x[0] + y[0]) % p, (x[1] + y[1]) % p)

    def eneg(x):
        return ((-x[0]) % p, (-x[1]) % p)

    def esub(x, y):
        return eadd(x, eneg(y))

    def emul(x, y):
        return ((x[0] * y[0] + d0 * x[1] * y[1]) % p,
                (x[0] * y[1] + x[1] * y[0]) % p)

    def epow(x, n):
        r = one
        while n:
            if n & 1:
                r = emul(r, x)
            x = emul(x, x)
            n //= 2
        return r

    q = p * p

    def echar(x):
        if x == zero:
            return 0
        return 1 if epow(x, (q - 1) // 2) == one else -1

    D = next(x for x in E if x != zero and echar(x) == -1)
    K = [(a, b) for a in E for b in E]

    def kadd(x, y):
        return (eadd(x[0], y[0]), eadd(x[1], y[1]))

    def knorm(x):
        return esub(emul(x[0], x[0]), emul(D, emul(x[1], x[1])))

    T = {x for x in K if knorm(x) == one}
    T2 = {kadd(x, y) for x in T for y in T}
    T3 = {kadd(x, y) for x in T2 for y in T}
    chi_m3 = echar(((-3) % p, 0))
    epsilon = int(chi_m3 != 1)

    assert len(T) == q + 1
    assert len(T2) == (q * q + 2 * q + 3) // 2
    assert len(T3) == (q * q if epsilon else q * q - 1)
    return len(T2), len(T3), chi_m3


if __name__ == "__main__":
    for p in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]:
        counts, s2, s3, chi = check_prime(p)
        print(f"q={p:2d}: chi(-3)={chi:2d}, lengths={counts}, |2T|={s2}, |3T|={s3}")
    for p in [3, 5, 7]:
        q = p * p
        s2, s3, chi = check_square_prime_power(p)
        print(f"q={q:2d}: chi(-3)={chi:2d}, |2T|={s2}, |3T|={s3}")
    print("PASS")
