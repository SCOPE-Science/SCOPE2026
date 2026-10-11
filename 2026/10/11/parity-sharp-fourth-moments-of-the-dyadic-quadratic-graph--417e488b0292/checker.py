"""Exact finite checks for the dyadic quadratic-graph fourth-moment identity.

Run: python3 checker.py
This finite checker corroborates the algebraic argument; it does not prove the infinite theorem.
"""
from collections import defaultdict
from random import Random


def constant(m):
    return 2 ** ((m + 1) // 2) if m % 2 else 3 * 2 ** (m // 2 - 1)


def root_count(m, d):
    n = 1 << m
    return sum((2 * h * (d - h)) % n == 0 for h in range(n))


def root_formula(m, d):
    l = m - 1
    if l == 0:
        return 2
    n = 1 << m
    d %= n
    r = m if d == 0 else (d & -d).bit_length() - 1
    q = (l + 1) // 2
    return 2 ** (r + 2) if 2 * r < l else 2 ** (m - q)


def energy(m, coefficients):
    n = 1 << m
    fiber = defaultdict(complex)
    support = [(t, z) for t, z in enumerate(coefficients) if z != 0]
    for a, ca in support:
        for b, cb in support:
            fiber[((a + b) % n, (a*a + b*b) % n)] += ca * cb
    return sum(int(z.real)**2 + int(z.imag)**2 for z in fiber.values())


def verify():
    counts = 0
    for m in range(1, 11):
        n = 1 << m
        for d in range(n):
            assert root_count(m, d) == root_formula(m, d), (m,d)
            counts += 1
        k = m // 2
        if m % 2:
            assert max(root_formula(m,d) for d in range(n)) == constant(m)
            period = 1 << k
        else:
            assert max(root_formula(m,d) for d in range(n)) == (1 << (k+1))
            period = 1 << (k-1)
        f = [int(t % period == 0) for t in range(n)]
        total = sum(z*z for z in f)
        assert energy(m, f) == constant(m) * total * total, (m,energy(m,f))
        counts += 2
    # Raw congruence-fiber energy is compared directly against the claimed
    # fourth moment, with complex Gaussian-integer inputs and no floating point.
    rng = Random(202610)
    for m in range(1,8):
        n=1<<m
        for _ in range(8):
            f=[complex(rng.randrange(-2,3),rng.randrange(-2,3)) for t in range(n)]
            total=sum(int(z.real)**2+int(z.imag)**2 for z in f)
            assert energy(m,f) <= constant(m)*total*total
            counts += 1
    print('CHECK_PASS', counts)

if __name__ == '__main__':
    verify()
