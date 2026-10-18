#!/usr/bin/env python3
"""Pure-Python finite-field and irreducibility certificate for a genus-six curve."""
from itertools import product


def prime_divisors(n):
    out = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def rem(a, b, p):
    a, b = trim([x % p for x in a]), trim([x % p for x in b])
    assert b != [0]
    inv = pow(b[-1], -1, p)
    while len(a) >= len(b) and a != [0]:
        mult = a[-1] * inv % p
        ofs = len(a) - len(b)
        for i, c in enumerate(b):
            a[ofs+i] = (a[ofs+i] - mult*c) % p
        a = trim(a)
    return a


def mulrem(a, b, f, p):
    z = [0] * (len(a)+len(b)-1)
    for i, c in enumerate(a):
        for j, d in enumerate(b):
            z[i+j] = (z[i+j] + c*d) % p
    return rem(z, f, p)


def power_mod(a, k, f, p):
    acc = [1]
    while k:
        if k & 1:
            acc = mulrem(acc, a, f, p)
        a = mulrem(a, a, f, p)
        k //= 2
    return acc


def gcd_monic(a, b, p):
    while b != [0]:
        a, b = b, rem(a, b, p)
    inv = pow(a[-1], -1, p)
    return trim([v*inv % p for v in a])


def irreducible(f, p):
    assert f[-1] % p != 0
    n = len(f)-1
    f = [v % p for v in f]
    z = [0, 1]
    for r in prime_divisors(n):
        h = power_mod(z, p**(n//r), f, p)
        minus_z = trim([(h[i] if i < len(h) else 0)-(z[i] if i < 2 else 0)
                        for i in range(max(2, len(h)))])
        if gcd_monic(f, trim([v % p for v in minus_z]), p) != [1]:
            return False
    h = power_mod(z, p**n, f, p)
    difference = trim([(h[i] if i < len(h) else 0)-(z[i] if i < 2 else 0)
                       for i in range(max(2, len(h)))])
    return rem([v % p for v in difference], f, p) == [0]


def point_count(n):
    p, q = 5, 5**n
    modulus = None
    for low in product(range(p), repeat=n):
        if low[0] and irreducible(list(low)+[1], p):
            modulus = list(low)+[1]
            break
    assert modulus is not None
    digits = [tuple(k//(p**i) % p for i in range(n)) for k in range(q)]

    def pack(a):
        return sum((v % p)*p**i for i, v in enumerate(a))

    def add(a, b):
        return pack([digits[a][i]+digits[b][i] for i in range(n)])

    def neg(a):
        return pack([-v for v in digits[a]])

    def multiply(a, b):
        v = [0]*(2*n-1)
        for i in range(n):
            for j in range(n):
                v[i+j] += digits[a][i]*digits[b][j]
        for j in range(2*n-2, n-1, -1):
            lead = v[j] % p
            for i in range(n):
                v[j-n+i] -= lead*modulus[i]
        return pack(v[:n])

    def field_power(a, k):
        acc = 1
        while k:
            if k & 1:
                acc = multiply(acc, a)
            a = multiply(a, a)
            k //= 2
        return acc

    generator = next(a for a in range(1, q)
                     if all(field_power(a, (q-1)//r) != 1 for r in prime_divisors(q-1)))
    power_table = [1]*(q-1)
    logs = [-1]*q
    for j in range(q-1):
        if j:
            power_table[j] = multiply(power_table[j-1], generator)
        logs[power_table[j]] = j
    assert len(set(power_table)) == q-1

    def times(a, b):
        return 0 if a == 0 or b == 0 else power_table[(logs[a]+logs[b]) % (q-1)]

    def trace(a):
        ans, b = 0, a
        for _ in range(n):
            ans = add(ans, b)
            b = 0 if b == 0 else power_table[(5*logs[b]) % (q-1)]
        assert ans in range(5)
        return ans

    if n <= 3:
        fibers = [0]*q
        for y in range(q):
            z = add(field_power(y, 5), neg(y))
            fibers[z] += 1
        assert all(fibers[z] == (5 if trace(z) == 0 else 0) for z in range(q))

    zero_trace = 0
    for x in range(1, q):
        f = add(add(times(x, x), x), power_table[(-logs[x]) % (q-1)])
        zero_trace += trace(f) == 0
    return (n, q, modulus, zero_trace, 2 + 5*zero_trace)


def verify():
    rows = [point_count(n) for n in range(1, 7)]
    counts = [row[-1] for row in rows]
    assert counts == [2, 2, 77, 602, 3022, 16337]
    s = [5**n + 1 - counts[n-1] for n in range(1, 7)]
    coeff = [1]
    for n in range(1, 7):
        numerator = -sum(coeff[n-j]*s[j-1] for j in range(1, n+1))
        assert numerator % n == 0
        coeff.append(numerator//n)
    for n in range(7, 13):
        coeff.append(5**(n-6)*coeff[12-n])
    assert coeff == [1, -4, -4, 21, 46, -100, -85, -500, 1150,
                     2625, -2500, -12500, 15625]
    assert sum(coeff) == 3775
    assert irreducible(coeff, 3)  # Rabin's finite-field criterion, degree 12.
    def val5(v):
        count = 0
        while v and v % 5 == 0:
            v //= 5
            count += 1
        return count
    vals = [val5(v) for v in coeff]
    assert vals == [0, 0, 0, 0, 0, 2, 1, 3, 2, 3, 4, 5, 6]
    assert all(vals[k] >= (k-4)/2 for k in range(4, 9))
    assert all(vals[k] >= k-6 for k in range(8, 13))
    assert vals[4] == 0 and vals[8] == 2 and vals[12] == 6
    for row in rows:
        print('extension', row)
    print('zeta_numerator_coefficients:', coeff)
    print('jacobian_points_over_F5:', sum(coeff))
    print('Newton_slopes: 0 x 4, 1/2 x 4, 1 x 4')
    print('irreducible_reduction_mod_3: true')
    print('VERIFY_OK')


if __name__ == '__main__':
    verify()
