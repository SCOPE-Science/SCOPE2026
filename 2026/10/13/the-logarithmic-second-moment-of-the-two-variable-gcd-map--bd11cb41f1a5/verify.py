"""Independent finite identities for the squared two-variable gcd-map moment.

The asymptotic limit is proved analytically and is not certified by this script.
Run: python3 verify.py
"""
from fractions import Fraction
from math import gcd, pi, log


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n):
    k, count = n, 0
    p = 2
    while p * p <= k:
        if k % p == 0:
            count += 1
            k //= p
            if k % p == 0:
                return 0
            while k % p == 0:
                k //= p
        p += 1
    if k > 1:
        count += 1
    return -1 if count % 2 else 1


def jordan2(n):
    return sum(mobius(d) * (n // d) ** 2 for d in divisors(n))


def phi(n):
    return sum(mobius(d) * (n // d) for d in divisors(n))


def prime_factors(n):
    return [p for p in range(2, n + 1) if n % p == 0 and all(p % v for v in range(2, int(p**0.5) + 1))]


def square_sum_direct(x):
    s = 0
    for a in range(1, x + 1):
        for b in range(1, x + 1):
            f = gcd(a*b, a+b) // gcd(a,b)
            g = gcd(a,b)
            assert f == gcd(g, (a+b)//g)
            s += f*f
    return s


def count_primitive_pairs(y, d):
    return sum(gcd(i,j) == 1 and (i+j)%d == 0
               for i in range(1, y+1) for j in range(1, y+1))


def square_sum_divisor_reconstruction(x):
    total = 0
    for d in range(1, int((2*x)**0.5) + 1):
        jd = jordan2(d)
        for k in range(1, 2*x//(d*d) + 1):
            y = x//(d*k)
            if y:
                total += jd * count_primitive_pairs(y, d)
    return total


for n in range(1, 301):
    assert jordan2(n) == n*n - sum(jordan2(d) for d in divisors(n) if d < n)
    prod = Fraction(jordan2(n), 1)
    for p in prime_factors(n):
        prod *= Fraction(p, p+1)
    assert prod == n*phi(n)

exact = {}
for x in (12, 24, 40, 75, 120):
    d = square_sum_direct(x)
    r = square_sum_divisor_reconstruction(x)
    assert d == r, (x,d,r)
    exact[x] = d

# A larger direct sweep checks the trend, not the theorem.
for x in (200, 400, 800):
    exact[x] = square_sum_direct(x)

print('VERIFY_OK jordan_identity_n=300 exact_pair_divisor_reconstructions=5 gcd_forms=yes')
for x in sorted(exact):
    s = exact[x]
    ratio = s/(x*x)
    residual = ratio - 3/(pi*pi)*log(x)
    print(f'x={x} exact_sum={s} normalized={ratio:.9f} residual={residual:.9f}')
print('analytic_asymptotic=proof_not_finite_check')
