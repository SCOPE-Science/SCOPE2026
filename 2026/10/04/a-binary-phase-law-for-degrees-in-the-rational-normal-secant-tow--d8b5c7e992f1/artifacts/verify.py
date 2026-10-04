from math import comb

PRIMES = (2, 3, 5, 7, 11, 13)

def vp(n, p):
    out = 0
    while n and n % p == 0:
        n //= p
        out += 1
    return out

def vp_int(n, p):
    out = 0
    while n % p == 0 and n:
        n //= p
        out += 1
    return out

def digit_sum(n, p):
    s = 0
    while n:
        s += n % p
        n //= p
    return s

def carry_count(a, b, p):
    carries = 0
    carry = 0
    while a or b or carry:
        z = (a % p) + (b % p) + carry
        if z >= p:
            carries += 1
            carry = 1
        else:
            carry = 0
        a //= p
        b //= p
    return carries

def first_odd(d):
    for k in range((d - 2) // 2 + 1):
        if comb(d - k, k + 1) % 2:
            return k
    return None

checks = 0
for d in range(2, 501):
    ks = range((d - 2) // 2 + 1)
    vals = [comb(d - k, k + 1) for k in ks]
    all_even = all(v % 2 == 0 for v in vals)
    exceptional = ((d + 2) & (d + 1)) == 0
    assert all_even == exceptional, (d, vals)

    if exceptional:
        assert first_odd(d) is None
    else:
        t = vp_int(d + 2, 2)
        assert first_odd(d) == (1 << t) - 1, (d, first_odd(d), t)

    for k, D in zip(ks, vals):
        a = k + 1
        b = d - 2 * k - 1
        for p in PRIMES:
            predicted = (digit_sum(a, p) + digit_sum(b, p) - digit_sum(a + b, p)) // (p - 1)
            assert predicted == carry_count(a, b, p)
            assert predicted == vp_int(D, p), (d, k, p, D, predicted, vp_int(D, p))
            checks += 1

assert [d for d in range(2, 64) if first_odd(d) is None] == [2, 6, 14, 30, 62]
assert comb(10 - 3, 3 + 1) == 35
print('VERIFY_OK', checks)
