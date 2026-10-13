from math import comb, factorial, gcd

def chow_degree(a, b):
    return comb(a + b, a)

def hurwitz_degree(a, b):
    d = a + b
    return 2 * factorial(d - 1) // (factorial(a - 1) * factorial(b - 1))

def sectional_genus_twice_minus_two(a, b):
    d = a + b
    C = comb(d, a)
    A = comb(d - 1, a - 1)
    B = comb(d - 1, a)
    return -(a + 1) * A - (b + 1) * B + (d - 1) * C

pairs = 0
primitive = 0
for a in range(1, 201):
    for b in range(1, 201):
        d = a + b
        C = chow_degree(a, b)
        H = hurwitz_degree(a, b)

        assert H * d == 2 * a * b * C
        assert H == 2 * C + sectional_genus_twice_minus_two(a, b)

        expected_gcd = C * gcd(d, 2 * a * b) // d
        assert gcd(C, H) == expected_gcd

        is_primitive = gcd(C, H) == 1
        expected_primitive = min(a, b) == 1 and max(a, b) % 2 == 0
        assert is_primitive == expected_primitive

        pairs += 1
        primitive += int(is_primitive)

print("VERIFY_OK", pairs, primitive)
