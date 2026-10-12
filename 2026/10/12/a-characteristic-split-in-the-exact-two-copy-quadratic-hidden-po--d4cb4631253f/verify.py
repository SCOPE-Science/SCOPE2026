from collections import Counter
from math import sqrt


def odd_prime(p):
    total = 0.0
    good = 0
    for x in range(p):
        for y in range(p):
            if x and y and (x + y) % p:
                good += 1
                fibers = Counter()
                for b in range(p):
                    for c in range(p):
                        v = (x * b + y * c) % p
                        w = (x * b * b + y * c * c) % p
                        fibers[(v, w)] += 1
                sizes = Counter(fibers.values())
                assert sizes[1] == p
                assert sizes[2] == p * (p - 1) // 2
                assert len(fibers) == p * (p + 1) // 2
                total += sum(sqrt(n) for n in fibers.values()) ** 2
    assert good == (p - 1) * (p - 2)
    direct = total / p**6
    formula = (p - 1) * (p - 2) / p**4 * (1 + (p - 1) / sqrt(2)) ** 2
    assert abs(direct - formula) < 1e-12


def gf2_mul(a, b, m, polynomial):
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & (1 << m):
            a ^= polynomial
    return out & ((1 << m) - 1)


def even_field(m, polynomial):
    q = 1 << m
    total = 0
    good = 0
    for x in range(q):
        for y in range(q):
            if x and y and (x ^ y):
                good += 1
                fibers = Counter()
                for b in range(q):
                    for c in range(q):
                        v = gf2_mul(x, b, m, polynomial) ^ gf2_mul(y, c, m, polynomial)
                        b2 = gf2_mul(b, b, m, polynomial)
                        c2 = gf2_mul(c, c, m, polynomial)
                        w = gf2_mul(x, b2, m, polynomial) ^ gf2_mul(y, c2, m, polynomial)
                        fibers[(v, w)] += 1
                assert len(fibers) == q * q
                assert set(fibers.values()) == {1}
                total += q**4
    assert good == (q - 1) * (q - 2)
    assert total / q**6 == (q - 1) * (q - 2) / q**2


# GF(9) = GF(3)[t]/(t^2+1), represented by a+b*t as a+3*b.
def gf9_add(u, v):
    return ((u % 3 + v % 3) % 3) + 3 * (((u // 3) + (v // 3)) % 3)


def gf9_mul(u, v):
    a, b = u % 3, u // 3
    c, d = v % 3, v // 3
    # t^2 = -1 = 2 in GF(3)
    return ((a * c + 2 * b * d) % 3) + 3 * ((a * d + b * c) % 3)


def gf9_neg(u):
    return ((-u) % 3) + 3 * ((-(u // 3)) % 3)


def odd_extension_9():
    q = 9
    total = 0.0
    good = 0
    for x in range(q):
        for y in range(q):
            s = gf9_add(x, y)
            if x and y and s:
                good += 1
                fibers = Counter()
                for b in range(q):
                    for c in range(q):
                        v = gf9_add(gf9_mul(x, b), gf9_mul(y, c))
                        w = gf9_add(gf9_mul(x, gf9_mul(b, b)), gf9_mul(y, gf9_mul(c, c)))
                        fibers[(v, w)] += 1
                sizes = Counter(fibers.values())
                assert sizes[1] == q
                assert sizes[2] == q * (q - 1) // 2
                total += sum(sqrt(n) for n in fibers.values()) ** 2
    assert good == (q - 1) * (q - 2)
    direct = total / q**6
    formula = (q - 1) * (q - 2) / q**4 * (1 + (q - 1) / sqrt(2)) ** 2
    assert abs(direct - formula) < 1e-12


for prime in (3, 5, 7, 11, 13):
    odd_prime(prime)
odd_extension_9()
for degree, polynomial in ((2, 0b111), (3, 0b1011), (4, 0b10011)):
    even_field(degree, polynomial)
print("VERIFY_OK odd_fields=3,5,7,9,11,13 even_fields=4,8,16 exact_success characteristic_limits=1/2,1")
