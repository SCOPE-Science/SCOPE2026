"""Exact finite certificate for least three-prime reciprocal-gcd integrality.

Run using Python 3 standard library; no external mathematical library.
The factorization procedure is complete because its sieve always reaches
at least the square root of every polynomial value it factors.
"""
from math import isqrt

LIMIT = 411612748708891
EXPECTED = (LIMIT, 349, 121453, 9710803)


def F(n):
    return n * n - n + 1


def primes_through(bound):
    mask = bytearray(b"\x01") * (bound + 1)
    mask[0:2] = b"\x00\x00"
    for p in range(2, isqrt(bound) + 1):
        if mask[p]:
            mask[p * p : bound + 1 : p] = b"\x00" * (((bound - p * p) // p) + 1)
    return [p for p in range(2, bound + 1) if mask[p]]


def distinct_factors(n, primes):
    """Exact prime factors; require primes through floor(sqrt(n_initial))."""
    assert primes and primes[-1] >= isqrt(n)
    answer = []
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            answer.append(p)
            while n % p == 0:
                n //= p
    if n > 1:
        answer.append(n)
    return answer


def main():
    # 75000^3 exceeds LIMIT, so it contains all potential least primes.
    # For p <= floor(cuberoot(LIMIT)), sqrt(F(p)) < p < 75000.
    assert 75000 ** 3 > LIMIT
    small_primes = primes_through(75000)
    candidate_p_count = 0
    candidate_edges = []
    for p in small_primes:
        if p ** 3 > LIMIT:
            break
        candidate_p_count += 1
        for u in distinct_factors(F(p), small_primes):
            if u > p and p * u * (p + 1) <= LIMIT:
                candidate_edges.append((p, u, LIMIT // (p * u)))

    # Every F(u) has floor(sqrt(F(u))) < u. The second sieve therefore
    # contains every possible trial divisor for every tested F(u).
    largest_u = max(u for p, u, cap in candidate_edges)
    medium_primes = primes_through(largest_u)
    answers = set()
    for p, u, cap in candidate_edges:
        for v in distinct_factors(F(u), medium_primes):
            if p < v <= cap and v != u and F(v) % p == 0:
                answers.add((p * u * v, p, u, v))

    assert candidate_p_count == 7339, candidate_p_count
    assert len(candidate_edges) == 1948, len(candidate_edges)
    assert largest_u == 19771363, largest_u
    assert sorted(answers) == [EXPECTED], sorted(answers)

    _, p, u, v = EXPECTED
    assert F(p) % u == F(u) % v == F(v) % p == 0
    numer = F(p) * F(u) * F(v)
    assert numer % LIMIT == 0
    assert numer // LIMIT == 410433300314317
    for q in (p, u, v):
        assert distinct_factors(q, medium_primes) == [q]

    print("candidate_least_primes=", candidate_p_count, sep="")
    print("candidate_first_edges=", len(candidate_edges), sep="")
    print("maximum_intermediate_prime=", largest_u, sep="")
    print("completing_three_cycles=", len(answers), sep="")
    print("unique_product=", EXPECTED[0], sep="")
    print("prime_cycle=", f"{p}->{u}->{v}->{p}", sep="")
    print("reciprocal_gcd_sum=", numer // LIMIT, sep="")
    print("CERTIFICATE_OK")


if __name__ == "__main__":
    main()
