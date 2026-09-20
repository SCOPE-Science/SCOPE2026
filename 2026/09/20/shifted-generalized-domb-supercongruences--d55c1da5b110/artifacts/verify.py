from math import comb

def vp(n, p):
    if n == 0:
        return 10**9
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v

def T(n, A, B, C):
    if n == 0:
        return 1
    return sum(
        comb(n + k - 1, k) ** A
        * comb(2 * k, k) ** B
        * comb(2 * (n - k), n - k) ** C
        for k in range(n + 1)
    )

expected_prefix = [1, 4, 76, 2560, 106060, 4864504]
actual_prefix = [T(n, 2, 1, 1) for n in range(6)]
assert actual_prefix == expected_prefix

checks = 0
for p in (5, 7):
    for m in (1, 2):
        for r in (1, 2):
            for A in (0, 1, 2, 3):
                for B, C in ((1, 1), (2, 1), (1, 2)):
                    lhs = T(m * p**r, A, B, C)
                    rhs = T(m * p**(r - 1), A, B, C)
                    exponent = min(A + 1, 3) * r
                    assert (lhs - rhs) % p**exponent == 0
                    checks += 1

sharp = []
for A, B, C in ((0, 1, 1), (1, 2, 1), (2, 1, 1)):
    d = T(5, A, B, C) - T(1, A, B, C)
    sharp.append(vp(d, 5))
assert sharp == [1, 2, 3]

print("A364111 prefix:", actual_prefix)
print("supercongruence checks:", checks)
print("sharpness valuations at p=5, r=1:", sharp)
print("all checks passed")
