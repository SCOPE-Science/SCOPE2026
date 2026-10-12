from fractions import Fraction


def v3(n):
    c = 0
    while n % 3 == 0 and n:
        c += 1
        n //= 3
    return c


def sigma_prime_power(p, a):
    return (p ** (a + 1) - 1) // (p - 1)


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return n == d
        d += 1 if d == 2 else 2
    return True


def Ipp(p, a):
    return Fraction(p ** (a + 1) - 1, p ** a * (p - 1))


def abundancy_product(parts):
    z = Fraction(1, 1)
    for p, a in parts:
        z *= Ipp(p, a)
    return z

assert abundancy_product([(3, 4), (5, 2)]) == Fraction(3751, 2025) > Fraction(9, 5)
assert abundancy_product([(3, 2), (5, 4)]) == Fraction(10153, 5625) > Fraction(9, 5)
assert abundancy_product([(3, 2), (5, 2), (13, 2), (31, 2)]) == Fraction(20191, 10075) > Fraction(9, 5)

local_checks = 0
for p in range(5, 500):
    if not is_prime(p) or p == 3:
        continue
    for a in range(2, 401, 2):
        got = v3(sigma_prime_power(p, a))
        want = v3(a + 1) if p % 3 == 1 else 0
        assert got == want, (p, a, got, want)
        local_checks += 1

residue_checks = 0
seen1 = set()
seen2 = set()
seen0 = set()
for a in range(2, 5001, 2):
    w = v3(a + 1)
    if w == 1:
        seen1.add(a % 18)
        assert a % 18 in {2, 14}
    elif w == 2:
        seen2.add(a % 54)
        assert a % 54 in {8, 44}
    elif w == 0:
        seen0.add(a % 6)
        assert a % 6 in {0, 4}
    residue_checks += 1
assert seen1 == {2, 14}
assert seen2 == {8, 44}
assert seen0 == {0, 4}

print(f"VERIFY_OK abundancy=3 local_checks={local_checks} residue_checks={residue_checks} v1={sorted(seen1)} v2={sorted(seen2)}")
