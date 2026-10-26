"""Exact finite checks for a low-Omega unitary/exponential divisor-sum classification.

The universal mathematical proof is in RESULT.md; these computations are
corroborative, not a replacement for the quantifier-unbounded argument.
Only Python's standard library is used.
"""
from math import isqrt


def sieve_spf(limit):
    spf = list(range(limit + 1))
    for p in range(2, isqrt(limit) + 1):
        if spf[p] == p:
            for n in range(p*p, limit + 1, p):
                if spf[n] == n:
                    spf[n] = p
    return spf


def factor(n, spf):
    out = []
    while n > 1:
        p = spf[n]
        a = 0
        while n % p == 0:
            n //= p
            a += 1
        out.append((p, a))
    return out


def sums(factors):
    star = exp = 1
    for p, a in factors:
        star *= 1 + p**a
        exp *= sum(p**d for d in range(1, a + 1) if a % d == 0)
    return star, exp


def check_bounded(limit=1000000):
    spf = sieve_spf(limit)
    solutions = []
    checked = 0
    for n in range(2, limit + 1):
        fs = factor(n, spf)
        if sum(a for _, a in fs) <= 4:
            checked += 1
            s, e = sums(fs)
            if s == e:
                solutions.append(n)
    assert solutions == [20, 45], solutions
    assert sums([(2, 2), (5, 1)]) == (30, 30)
    assert sums([(3, 2), (5, 1)]) == (60, 60)
    return checked


def check_symbolic_elimination(limit=20000):
    """Check the proof's necessary divisibility reduction for all prime r."""
    spf = sieve_spf(limit)
    primes = [p for p in range(2, limit + 1) if spf[p] == p]
    for r in primes:
        a = r*r + 1
        g = r - 1
        # Every hypothetical equality would force t | gcd(a,g) and
        # t(k+1)=g with k>=2; also t = a/q with prime q>r.
        admissible = []
        for t in range(1, min(2, g) + 1):
            if a % t == 0 and g % t == 0 and g//t >= 3 and (r == 2 or t % 2 == 0):
                k = g//t - 1
                q, rem = divmod(a, t)
                if rem == 0 and q > r and (q+1) % k == 0:
                    p = (q+1)//k
                    if r < p < q:
                        admissible.append((r,p,q,k,t))
        # The sole algebraic candidate is (7,13,25); 25 is not prime.
        assert all((r,p,q,k,t) == (7,13,25,2,2)
                   for r,p,q,k,t in admissible), admissible
    return len(primes)


if __name__ == '__main__':
    tested = check_bounded()
    primetested = check_symbolic_elimination()
    print(f'VERIFY_OK: {tested} integers with Omega<=4 through 1000000; '
          f'prime-root reduction through {primetested} primes; '
          'unique positive equality values 20,45')
