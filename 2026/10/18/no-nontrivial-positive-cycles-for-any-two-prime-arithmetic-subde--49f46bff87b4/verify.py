"""Exact finite regression for a universal theorem on two-prime arithmetic subderivatives."""
P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def valuation(n, p):
    a = 0
    while n and n % p == 0:
        n //= p
        a += 1
    return a

def deriv(n, p, q):
    a, b = valuation(n, p), valuation(n, q)
    numerator = n * (q*a + p*b)
    assert numerator % (p*q) == 0
    return numerator // (p*q)

for i, p in enumerate(P):
    for q in P[i+1:]:
        for a in range(24):
            for b in range(24):
                if a == b == 0:
                    continue
                c = q*a + p*b
                u, v = valuation(c, p), valuation(c, q)
                if c != p**u * q**v:
                    continue
                aa, bb = a+u-1, b+v-1
                assert aa >= 0 and bb >= 0
                nxt = q*aa + p*bb
                assert nxt == c + q*(u-1) + p*(v-1)
                if c >= p*q:
                    assert nxt >= p*q
                elif nxt > 0:
                    assert nxt > c
        for n in range(1, 3000):
            t, seen = n, set()
            for step in range(28):
                if t == 0 or t > 10**8 or t in seen:
                    break
                seen.add(t)
                t = deriv(t, p, q)
            if t in seen:
                assert deriv(t, p, q) == t
            fixed = (valuation(n, p) == p and valuation(n, q) == 0) or (valuation(n, q) == q and valuation(n, p) == 0)
            assert (deriv(n, p, q) == n) == fixed
print('PASS: 45 prime pairs; smooth-state transitions, invariant threshold, bounded orbit and fixed-point tests')
