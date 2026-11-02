"""Exact checks for dyadic triangular divisibility and an incidence Möbius value.
Run using Python 3 standard library: python3 verify.py.
All tests are finite checks supplementing the proofs in RESULT.md.
"""
from math import isqrt, lcm

EXPECTED = {
    1: (), 3: (2, 3), 5: (2, 3, 11), 7: (2, 3),
    9: (2, 3, 8, 18), 11: (2, 3), 13: (2, 3),
    15: (2, 3, 8, 11, 32), 17: (2, 3), 19: (2, 3),
    21: (2, 3, 8, 128), 23: (2, 3), 25: (2, 3, 11, 32),
    27: (2, 3, 8, 18, 512), 29: (2, 3), 31: (2, 3),
    33: (2, 3, 8, 2048), 35: (2, 3, 11, 32, 43, 128)
}

def triangular(n):
    return n * (n + 1) // 2

def factor(n):
    if n < 1:
        raise ValueError(n)
    ans = {}
    d = 2
    while d * d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            ans[d] = e
        d = 3 if d == 2 else d + 2
    if n > 1:
        ans[n] = ans.get(n, 0) + 1
    assert all(p >= 2 for p in ans)
    assert all(not any(p % c == 0 for c in range(2, isqrt(p) + 1)) for p in ans)
    return ans

def divisors(factors):
    vals = [1]
    for p, e in factors.items():
        old = vals
        vals = [d * p**v for v in range(e + 1) for d in old]
    return sorted(vals)

def triangular_divisors(k):
    n = 1 << k
    f = factor((1 << k) + 1)
    f[2] = k - 1
    target = triangular(n)
    assert target == (1 << (k - 1)) * ((1 << k) + 1)
    values = []
    for v in divisors(f):
        root = isqrt(8 * v + 1)
        if root * root == 8 * v + 1:
            j = (root - 1) // 2
            assert triangular(j) == v
            values.append(j)
    return values

def mobius_of_interval(k):
    indices = sorted(triangular_divisors(k))
    mu = {}
    for j in indices:
        if j == 1:
            mu[j] = 1
        else:
            mu[j] = -sum(mu[i] for i in indices if i < j and triangular(j) % triangular(i) == 0)
    return indices, mu

def order_2(d):
    assert d > 1 and d % 2
    x = 2 % d
    r = 1
    while x != 1:
        x = x * 2 % d
        r += 1
    return r

def permitted_k(j, k):
    value = triangular(j)
    alpha = 0
    while value % 2 == 0:
        value //= 2
        alpha += 1
    if k < alpha + 1:
        return False
    if value == 1:
        return True
    factorization = factor(value)
    orders = [order_2(p**e) for p, e in factorization.items()]
    if any(ord_ % 2 for ord_ in orders):
        return False
    s_set = set()
    odd_lcm = 1
    for ord_ in orders:
        s = 0
        while ord_ % 2 == 0:
            ord_ //= 2
            s += 1
        s_set.add(s)
        odd_lcm = lcm(odd_lcm, ord_)
    if len(s_set) != 1:
        return False
    s, = s_set
    return k % (2**s * odd_lcm) == 2**(s - 1) * odd_lcm

for k, expected in EXPECTED.items():
    vals = triangular_divisors(k)
    assert vals[0] == 1 and vals[-1] == 1 << k
    assert tuple(vals[1:-1]) == expected, (k, vals[1:-1], expected)
    if k < 35 and k >= 3:
        assert all(triangular(j) % 3 == 0 for j in vals[1:-1])
indices, mu = mobius_of_interval(35)
assert indices == [1, 2, 3, 11, 32, 43, 128, 2**35]
assert [mu[j] for j in indices] == [1, -1, 0, 0, 0, -1, 0, 1]
for k in range(3, 35, 2):
    assert mobius_of_interval(k)[1][1 << k] == 0
assert triangular(43) == 946
assert (order_2(11), order_2(43)) == (10, 14)
assert (1 << 35) + 1 == 3*11*43*281*86171
for k in range(1, 180):
    if k >= 2:
        assert (triangular(1 << k) % triangular(43) == 0) == (k % 70 == 35)
checks = 0
for j in range(2, 100):
    for k in range(1, 40):
        assert permitted_k(j, k) == (triangular(1 << k) % triangular(j) == 0), (j, k)
        checks += 1
print('VERIFY_OK: 18 complete dyadic divisor intervals; first odd-power escape at 35;')
print('eight-element interval with Möbius value 1; 70-residue criterion;')
print(f'{checks} independent order-versus-integer divisibility comparisons.')
