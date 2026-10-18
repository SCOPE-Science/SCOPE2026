"""Standalone finite checks for the associated Pell self-coprime-index sieve.

No external packages. Its finite checks supplement, rather than replace,
the symbolic proof in RESULT.md.
"""
from fractions import Fraction
from math import gcd, isqrt, lcm, log, sqrt

LIMIT = 100000
SCALE = 10**12
FIRST = [3, 7, 11, 17, 19, 23, 31, 41, 43, 47, 59]


def smallest_prime_factors(bound):
    s = list(range(bound + 1))
    for p in range(2, isqrt(bound) + 1):
        if s[p] == p:
            for k in range(p * p, bound + 1, p):
                if s[k] == k:
                    s[k] = p
    return s


SPF = smallest_prime_factors(LIMIT + 2)


def prime_factors(n):
    fs = []
    while n > 1:
        p = SPF[n]
        fs.append(p)
        while n % p == 0:
            n //= p
    return fs


def alg_mul(a, b, p):
    return ((a[0] * b[0] + 2 * a[1] * b[1]) % p,
            (a[0] * b[1] + a[1] * b[0]) % p)


def alg_power(n, p):
    a, v = ((-3) % p, (-2) % p), (1, 0)
    while n:
        if n & 1:
            v = alg_mul(v, a, p)
        a = alg_mul(a, a, p)
        n >>= 1
    return v


def entry_index(p):
    if p == 2:
        return None
    legendre = pow(2, (p - 1)//2, p)
    h = p - (1 if legendre == 1 else -1)
    for q in prime_factors(h):
        while h % q == 0 and alg_power(h // q, p) == (1, 0):
            h //= q
    return h // 2 if h % 2 == 0 else None


def finite_sieve_density(primes):
    """Exact inclusion-exclusion over compatible fixed 2-adic layers."""
    # Brute subset enumeration is transparent for the eleven specified primes.
    from itertools import combinations
    events = [(p, entry_index(p)) for p in primes]
    events = [(p, e) for p, e in events if e is not None]
    result = Fraction(1, 1)
    for k in range(1, len(events)+1):
        for subset in combinations(events, k):
            def two_val(n):
                return (n & -n).bit_length() - 1
            if len({two_val(e) for _, e in subset}) > 1:
                continue
            modulus = lcm(*(p * e for p, e in subset))
            result += (-1 if k % 2 else 1) * Fraction(1, 2 * modulus)
    return result


def pell_mod_index(n, modulus):
    """Independent companion-matrix modular evaluation of Q_n."""
    if modulus == 1:
        return 0
    if n == 0 or n == 1:
        return 1 % modulus
    def mm(a, b):
        return ((a[0]*b[0] + a[1]*b[2])%modulus,
                (a[0]*b[1] + a[1]*b[3])%modulus,
                (a[2]*b[0] + a[3]*b[2])%modulus,
                (a[2]*b[1] + a[3]*b[3])%modulus)
    m = (2,1,1,0)
    r = (1,0,0,1)
    power = n-1
    while power:
        if power & 1:
            r = mm(r,m)
        m = mm(m,m)
        power //= 2
    return (r[0]+r[1])%modulus


def expected_gcd(n):
    m = n
    out = 1
    while m>1:
        p = SPF[m]
        pp = 1
        while m%p == 0:
            m //= p
            pp *= p
        e = entry_index(p)
        if e is not None and n%e == 0 and (n//e)%2 == 1:
            out *= pp
    return out


def main():
    first = [(p,entry_index(p)) for p in FIRST]
    assert first == [(3, 2), (7, 3), (11, 6), (17, 4), (19, 10),
                     (23, 11), (31, 15), (41, 5), (43, 22), (47, 23), (59, 10)]
    density = finite_sieve_density(FIRST)
    assert density == Fraction(154703748840589, 176325122256360)
    assert density < Fraction(878,1000)
    # Direct recurrence test for the ranks, independent of quadratic arithmetic.
    rank_checks = 0
    for p in range(3,1000,2):
        if SPF[p] != p:
            continue
        a,b = 1,1
        first_zero = None
        for j in range(2,p+2):
            a,b=b,(2*b+a)%p
            if b == 0:
                first_zero=j
                break
        assert entry_index(p) == first_zero, (p,first_zero,entry_index(p))
        rank_checks += 1
    gcd_checks=0
    for n in range(1,10001):
        actual=gcd(n,pell_mod_index(n,n))
        assert actual==expected_gcd(n),(n,actual,expected_gcd(n))
        gcd_checks+=1
    rounded_ceiling_sum = 0
    prime_count=0
    for p in range(3,LIMIT+1,2):
        if SPF[p] == p:
            prime_count+=1
            e=entry_index(p)
            if e is not None:
                rounded_ceiling_sum += (SCALE+2*p*e-1)//(2*p*e)
    assert rounded_ceiling_sum == 137404000609
    # Conservative outward constant, all x>=100000:
    # C = 1.25506*log(1+sqrt(2))/2 < 0.554,
    # 1/log(100000)+1/(2 log(100000)^2) < 0.0905,
    # so C*... < 0.0502.
    assert 1.25506*log(1+sqrt(2))/2*(1/log(LIMIT)+1/(2*log(LIMIT)**2)) < 0.0502
    assert 1-Fraction(rounded_ceiling_sum,SCALE)-Fraction(502,10000) > Fraction(812,1000)
    print('PASS:',gcd_checks,'matrix/valuation gcd comparisons;',rank_checks,'direct prime-rank comparisons')
    print('PASS:',prime_count,'odd primes up to',LIMIT,'; upward-rounded density sum',rounded_ceiling_sum,'/',SCALE)
    print('PASS: eleven-event exact finite density =',density,'=',float(density))
    print('CERTIFIED: 0.812 < natural density < 0.878')


if __name__=='__main__':
    main()
