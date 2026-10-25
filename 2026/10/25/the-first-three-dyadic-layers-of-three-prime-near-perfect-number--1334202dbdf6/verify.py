"""Exact finite certificate for the first three dyadic layers of near-perfect 2^a*p*q.
Only Python standard library. The analytic bounds justifying exhaustiveness are in RESULT.md.
"""
from math import isqrt


def is_prime(z):
    if z < 2:
        return False
    if z % 2 == 0:
        return z == 2
    for d in range(3, isqrt(z) + 1, 2):
        if z % d == 0:
            return False
    return True


def certificate():
    expected = [(1, []), (2, []), (3, [(5624, 152), (9112, 136),
                                     (11096, 8), (13736, 68), (17816, 8)])]
    total_tested = 0
    print('CERTIFICATE: analytic bounded prime-pair sieve, no arbitrary search cutoff')
    for a, target in expected:
        h = (1 << (a + 1)) - 1
        p_bound = h + isqrt(h * (h + 1))
        solutions = []
        reduced_candidates = 0
        per_p = []
        for p in range(3, p_bound + 1, 2):
            if not is_prime(p):
                continue
            if p == h:
                per_p.append((p, 0, 0))
                continue  # d=2^(a+1)*p cannot divide n=2^a*p*q
            accepted_q = 0
            reduced = 0
            for q in range(p + 2, h * (p + 1) + 1, 2):
                if not is_prime(q):
                    continue
                total_tested += 1
                if p < h:
                    if (h * (p + 1)) % q:
                        continue  # d>2^a*p, thus q | d and q | h*(p+1)
                else:
                    if (p - h) * q >= h * (p + 1):
                        continue  # positivity
                reduced += 1
                delta = h * (p + q + 1) - p * q
                n = (1 << a) * p * q
                if delta > 0 and delta < n and n % delta == 0:
                    solutions.append((n, delta))
                    accepted_q += 1
            reduced_candidates += reduced
            per_p.append((p, reduced, accepted_q))
        solutions.sort()
        assert solutions == target, (a, solutions, target)
        print(f'a={a}, h={h}, p_bound={p_bound}, reduced_candidates={reduced_candidates}, solutions={solutions}')
        print('per-p (p, candidate_q, solutions):', per_p)
    # Independently validate all 5 witnesses directly by summing divisors.
    for n, d in expected[-1][1]:
        sigma = sum(v + (n // v if v*v != n else 0)
                    for v in range(1, isqrt(n) + 1) if n % v == 0)
        assert sigma == 2*n+d and 0 < d < n and n % d == 0
    print('VERIFY_OK:', total_tested, 'prime-pair tests, five direct divisor-sum witness checks')


if __name__ == '__main__':
    certificate()
