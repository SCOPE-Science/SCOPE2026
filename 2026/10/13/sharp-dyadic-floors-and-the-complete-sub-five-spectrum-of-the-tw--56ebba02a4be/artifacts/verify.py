from math import isqrt

def divisors(n):
    out = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return out

def sigma(n):
    return sum(divisors(n))

def chi4(d):
    if d % 2 == 0:
        return 0
    return 1 if d % 4 == 1 else -1

def lam(n):
    return sum(chi4(d) for d in divisors(n))

def a_formula(n):
    numerator = sigma(n) - lam(n)
    if n % 2 == 0:
        numerator -= 2 * sigma(n // 2)
    if n % 4 == 0:
        numerator += 4 * sigma(n // 4)
    assert numerator % 4 == 0
    return numerator // 4

def a_direct(n):
    total = 0
    for x in range(1, n + 1):
        for y in range(x + 1, n + 1):
            ux = 1
            r = 0
            while ux * x + y <= n:
                rem = n - ux * x
                if rem > 0 and rem % y == 0:
                    uy = rem // y
                    if uy % 2 == 1:
                        s = (uy - 1) // 2
                        total += -1 if (r + s) % 2 else 1
                r += 1
                ux += 2
    return total

expected = {
    0: {1, 2},
    1: {3, 4, 5, 6, 10},
    2: {7, 14},
    3: {8, 9, 11, 13, 18, 22, 26},
    4: {17, 34},
}

for n in range(1, 121):
    assert a_formula(n) == a_direct(n), (n, a_formula(n), a_direct(n))

seen = {j: set() for j in range(5)}
for n in range(1, 20001):
    value = a_formula(n)
    if value <= 4:
        seen[value].add(n)
assert seen == expected, (seen, expected)

for k in range(2, 13):
    floor_value = (1 << (k - 1)) - 1
    second_floor = (1 << (k + 1)) - 3
    assert a_formula(1 << k) == floor_value
    for m in range(3, 1000, 2):
        value = a_formula((1 << k) * m)
        assert value >= second_floor, (k, m, value, second_floor)
        if value == second_floor:
            assert m == 3
    assert a_formula((1 << k) * 3) == second_floor

print("VERIFY_OK direct_n=120 low_spectrum_n=20000 dyadic_k=2..12 odd_m<1000")
