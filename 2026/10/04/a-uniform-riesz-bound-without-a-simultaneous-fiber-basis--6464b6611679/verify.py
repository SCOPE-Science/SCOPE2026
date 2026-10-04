from fractions import Fraction

PRIMES = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 43, 59, 101]

def dot2(a, b):
    return (a[0]*b[0] + a[1]*b[1]) & 1

for p in PRIMES:
    S = set(range((p+1)//2))
    T = set(range(p)) - S
    assert len(S) == (p+1)//2
    assert len(T) == (p-1)//2
    assert 3*len(S) <= 2*p
    q2 = Fraction(len(S), p)
    assert q2 <= Fraction(2, 3)

    e1 = (1, 0)
    e2 = (0, 1)
    for t in range(p):
        d = e1 if t in S else e2
        plus_rows = []
        for z in range(p):
            x = e2 if z == 0 else (e1 if z == 1 else (1, 1))
            if dot2(d, x) == 0:
                plus_rows.append(z)
        expected = [0] if t in S else [1]
        assert plus_rows == expected

# Exact arithmetic behind (380 + 152*sqrt(6))/3 < 251:
assert 6 * 152 * 152 < 373 * 373
print('VERIFY_OK primes=%d q2_bound=2/3 inequality=exact' % len(PRIMES))
