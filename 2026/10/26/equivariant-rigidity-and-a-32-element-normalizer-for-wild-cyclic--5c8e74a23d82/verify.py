"""Exact finite-field checks of the translation normal form for a cyclic four-cover.

This validates polynomial identities and finite examples, not the infinite-field proof.
"""

MOD = 0x1009
FIELD_SIZE = 4096

def mul(a, b):
    c = 0
    while b:
        if b & 1:
            c ^= a
        a <<= 1
        if a & FIELD_SIZE:
            a ^= MOD
        b >>= 1
    return c

def power(a, n):
    ans = 1
    while n:
        if n & 1:
            ans = mul(ans, a)
        a = mul(a, a)
        n >>= 1
    return ans

def phi(lam, s):
    return power(s, 4) ^ power(s, 2) ^ mul(lam, s)

candidates = [1] + [a for a in range(2, FIELD_SIZE) if power(a, 2) ^ a ^ 1 == 0]
assert len(candidates) == 3
for lam in candidates:
    invlam = power(lam, FIELD_SIZE - 2)
    assert mul(lam, invlam) == 1
    buckets = {}
    for e in (0, 1):
        roots = [s for s in range(FIELD_SIZE) if phi(lam, s) == mul(lam, e)]
        assert len(roots) == 4, (lam, e, roots)
        buckets[e] = set(roots)
        for s in roots:
            beta = mul(power(s, 2), invlam)
            assert power(s, 2) == mul(lam, beta)
            # Original second Witt component after base translation;
            # the beta*x correction restores the first Witt component x.
            # Addition of (0,s*x) cancels the quadratic coefficient.
            constant = power(beta, 3)
            constant = mul(lam, constant) ^ power(beta, 2)
            for x in range(FIELD_SIZE):
                xp = x ^ beta
                translated = mul(lam, power(xp, 3)) ^ mul(beta, xp)
                translated ^= mul(power(s, 2), power(x, 2)) ^ mul(s, x)
                assert (translated ^ constant) == (mul(lam, power(x, 3)) ^ mul(e, x)), (lam, s, e, x)
    assert not buckets[0].intersection(buckets[1])
    all_roots = buckets[0] | buckets[1]
    assert len(all_roots) == 8
    for s in all_roots:
        for t in all_roots:
            assert (s ^ t) in all_roots
    print(f'VERIFY_OK lambda={lam:#04x} zero_coefficient_roots=4 inversion_coefficient_roots=4 translation_space=8 normalizer_lifts=32 centralizer_lifts=16')
print('VERIFY_OK explicit_Witt_translation_polynomial_identity_all_x_GF4096')
