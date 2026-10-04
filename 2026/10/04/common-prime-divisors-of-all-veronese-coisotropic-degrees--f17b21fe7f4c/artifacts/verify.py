from math import comb, gcd

def polar_closed(n, e):
    return [comb(n + 1, i + 1) * (e ** i) * ((e - 1) ** (n - i)) for i in range(n + 1)]

def polar_chern(n, e):
    out = []
    for i in range(n + 1):
        s = 0
        for j in range(n - i + 1):
            s += ((-1) ** j) * comb(n - j + 1, i + 1) * comb(n + 1, j) * (e ** (n - j))
        out.append(s)
    return out

def factor_support_part(N, e):
    x = e
    p = 2
    primes = []
    while p * p <= x:
        if x % p == 0:
            primes.append(p)
            while x % p == 0:
                x //= p
        p += 1 if p == 2 else 2
    if x > 1:
        primes.append(x)

    ans = 1
    for p in primes:
        y = N
        while y % p == 0:
            ans *= p
            y //= p
    return ans

gcd_checks = 0
for n in range(1, 80):
    for e in range(2, 31):
        vals = polar_closed(n, e)
        g = 0
        for v in vals:
            g = gcd(g, v)
        assert g == factor_support_part(n + 1, e), (n, e, g, factor_support_part(n + 1, e))
        gcd_checks += 1

chern_checks = 0
for n in range(1, 15):
    for e in range(2, 11):
        assert polar_closed(n, e) == polar_chern(n, e)
        chern_checks += 1

ed_checks = 0
for n in range(1, 50):
    for e in range(2, 20):
        vals = polar_closed(n, e)
        lhs = sum(vals)
        rhs_num = (2 * e - 1) ** (n + 1) - (e - 1) ** (n + 1)
        assert rhs_num % e == 0
        assert lhs == rhs_num // e
        ed_checks += 1

# Quadratic calibration.
for n in range(1, 50):
    vals = polar_closed(n, 2)
    assert vals == [comb(n + 1, i + 1) * (2 ** i) for i in range(n + 1)]

print("VERIFY_OK", gcd_checks, chern_checks, ed_checks)
