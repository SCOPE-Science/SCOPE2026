"""Exact-rational and finite-regression checks for partial-derivative image density.
Run: python3 verify.py. Standard library only.
"""
from fractions import Fraction
from itertools import combinations
from math import gcd, lcm, log


def local_divisors(p, a):
    ans = set()
    for b in range(a + 1):
        k = a + 1 - b
        if k % (p ** b) == 0:
            d = k // (p ** b)
            if d >= 1 and d % p:
                ans.add(d)
    return tuple(sorted(ans))


def local_coverage(p, a):
    ds = local_divisors(p, a)
    ans = Fraction()
    for size in range(1, len(ds) + 1):
        for sub in combinations(ds, size):
            ans += Fraction((-1) ** (size + 1), lcm(*sub))
    return ans


def density_interval(p, A):
    low = sum((Fraction(p - 1, p ** (a + 1)) * local_coverage(p, a)
               for a in range(A)), Fraction())
    return low, low + Fraction(1, p ** A)


def source_image_members(p, X):
    # D_p(y)= (y//p)*v_p(y) for all positive y divisible by p.
    # Any preimage y of x<=X must satisfy y<=p*x, since v_p(y)>=1.
    seen = bytearray(X + 1)
    for y in range(p, p * X + 1, p):
        t = y
        v = 0
        while t % p == 0:
            t //= p
            v += 1
        x = (y // p) * v
        if x <= X:
            seen[x] = 1
    return seen


def inverse_count(p, x):
    t = x
    a = 0
    while t % p == 0:
        t //= p
        a += 1
    return sum(t % d == 0 for d in local_divisors(p, a))


def run():
    for p, A in ((2, 48), (3, 32), (5, 22), (7, 18), (11, 15)):
        lo, hi = density_interval(p, A)
        assert 0 < lo < hi < 1
        assert hi - lo == Fraction(1, p ** A)
        # All valuations below p-1 have precisely the singleton divisor a+1.
        for a in range(p-1):
            assert local_divisors(p, a) == (a + 1,)
            assert local_coverage(p, a) == Fraction(1, a + 1)
        assert local_divisors(p, p - 1) == ()
        # Analytic baseline with certified exponential error.
        ref = -(p - 1) * log(1 - 1 / p)
        assert abs(float(lo) - ref) <= float(Fraction(1, p ** (p - 1))) + float(hi - lo) + 1e-13
        print('CERTIFIED_INTERVAL', 'p='+str(p), 'A='+str(A),
              'lower='+format(float(lo), '.16f'),
              'upper='+format(float(hi), '.16f'),
              'absolute_error<='+str(Fraction(1,p**A)))
    X = 60000
    for p in (2, 3, 5):
        image = source_image_members(p, X)
        for x in range(1, X + 1):
            assert bool(image[x]) == (inverse_count(p, x) >= 1), (p, x)
        num = sum(image)
        print('BRUTE_IMAGE_AGREEMENT', 'p='+str(p), 'x_max='+str(X),
              'membership_checks='+str(X), 'image_count='+str(num))
    for p in (2, 3, 5):
        for a in range(30):
            D = local_divisors(p, a)
            # Independently reconstruct preimages using the exact k equation.
            for m in range(1, 301):
                if m % p == 0:
                    continue
                x = p ** a * m
                explicit = set()
                for k in range(1, a + 2):
                    b = 0
                    z = k
                    while z % p == 0:
                        z //= p
                        b += 1
                    if k-1+b == a and m % z == 0:
                        explicit.add((m//z) * p ** k)
                assert len(explicit) == sum(m % d == 0 for d in D)
        print('INVERSE_MULTIPLICITY_AGREEMENT', 'p='+str(p), 'a=0..29', 'm=1..300')
    for p in (2, 3, 5):
        for a in range(30):
            ds = local_divisors(p, a)
            L = lcm(*ds) if ds else 1
            counts = [sum(r % d == 0 for d in ds) for r in range(1, L + 1)]
            nonempty_fraction = Fraction(sum(j >= 1 for j in counts), L)
            assert nonempty_fraction == local_coverage(p, a)
            for r in range(1, L + 1):
                assert counts[r - 1] == sum((r + 5 * p * L) % d == 0 for d in ds)
        print('LOCAL_MULTIPLICITY_DISTRIBUTION', 'p='+str(p), 'a=0..29', 'exact_periodic=PASS')
    print('VERIFY_OK exact_local_rational=PASS inverse_fiber_identity=PASS asymptotic_tail=PASS local_multiplicity=PASS')

if __name__ == '__main__':
    run()
