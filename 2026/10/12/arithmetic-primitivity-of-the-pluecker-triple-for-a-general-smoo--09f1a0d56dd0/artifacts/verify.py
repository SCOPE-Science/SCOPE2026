from math import gcd

def invariants(d):
    D = d * (d - 1)
    F = 3 * d * (d - 2)
    B = d * (d - 2) * (d - 3) * (d + 3) // 2
    return D, F, B

checks = 0
for d in range(4, 10001):
    D, F, B = invariants(d)
    assert gcd(gcd(D, F), B) == d

    want_DF = d * (3 if d % 3 == 1 else 1)
    want_DB = d * (1 if d % 2 == 0 else (4 if d % 4 == 1 else 2))
    u = (d - 2) // 2 if d % 2 == 0 else d - 2
    want_FB = d * u * (3 if d % 3 == 0 else 1)

    assert gcd(D, F) == want_DF, (d, gcd(D, F), want_DF)
    assert gcd(D, B) == want_DB, (d, gcd(D, B), want_DB)
    assert gcd(F, B) == want_FB, (d, gcd(F, B), want_FB)
    checks += 1

assert invariants(4) == (12, 24, 28)
assert invariants(5) == (20, 45, 120)
print("VERIFY_OK", checks)
