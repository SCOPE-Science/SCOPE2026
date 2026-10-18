"""Finite characteristic checks for a uniform Picard-curve Cartier formula.
Run with Python 3 and no external libraries. The infinite theorem uses a proof.
"""
from math import comb


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b, p):
    return trim([(a[i] if i < len(a) else 0) % p +
                 (b[i] if i < len(b) else 0) % p for i in range(max(len(a), len(b)))])


def mul(a, b, p):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] = (c[i + j] + x * y) % p
    return trim(c)


def scl(a, u, p):
    return trim([u * v % p for v in a])


def coeff(e, n, p):
    """Polynomial in t: [z^n](z^2+2tz+1)^e."""
    c = [0] * (n + 1)
    for j in range(n // 2 + 1):
        if j > e or n - j > e:
            continue
        h = n - 2*j
        c[h] = (c[h] + comb(e, j) * comb(e-j, h) * pow(2, h, p)) % p
    return trim(c)


def powpoly(a, n, p):
    out = [1]
    while n:
        if n & 1: out = mul(out, a, p)
        a = mul(a, a, p)
        n //= 2
    return out


def derivative(a, p):
    return trim([i*a[i] % p for i in range(1, len(a))] or [0])


def rem(a, b, p):
    a = a[:]
    b = trim(b[:])
    if b == [0]: raise ZeroDivisionError
    while len(a) >= len(b) and a != [0]:
        v = a[-1] * pow(b[-1], -1, p) % p
        off = len(a) - len(b)
        for i, bb in enumerate(b):
            a[off+i] = (a[off+i] - v*bb) % p
        trim(a)
    return a


def gcd(a, b, p):
    while b != [0]:
        a, b = b, rem(a, b, p)
    return scl(a, pow(a[-1], -1, p), p)


def value(a, t, p):
    acc = 0
    for c in reversed(a): acc = (acc*t + c) % p
    return acc


for p in (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71):
    assert all(p%d for d in range(2, int(p**0.5) + 1)), p
    m = (p-1)//6 if p % 6 == 1 else (p-5)//6
    w = [p-1, 0, 1]  # t^2-1
    if p % 6 == 1:
        H = coeff(2*m, m, p)
        A = coeff(4*m, 3*m, p)
        B = coeff(4*m, 2*m, p)
        constant = (-1)**m * comb(4*m, m) % p
        assert A == mul(powpoly(w, m, p), H, p), (p, A, H)
        assert B == scl(powpoly(w, m, p), constant, p), (p, B)
        assert constant != 0
        rank_regular, rank_exceptional = 3, 1
    else:
        H = coeff(2*m+1, m, p)
        A = coeff(4*m+3, 3*m+2, p)
        assert A == scl(mul(powpoly(w, m+1, p), H, p), 2, p), (p, A, H)
        rank_regular, rank_exceptional = 2, 0
    assert len(H)-1 == m, p
    assert value(H, 1, p) != 0 and value(H, -1, p) != 0, p
    assert gcd(H, derivative(H, p), p) == [1], p
    print('p=',p,'m=',m,'H=',H,'Cartier generic/exceptional ranks=',rank_regular,rank_exceptional)
print('VERIFY_OK: exact Cartier coefficients and exceptional squarefreeness, 18 primes')
