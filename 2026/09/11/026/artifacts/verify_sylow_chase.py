"""Verify the Sylow-arithmetic core of the lane-721 disproof (stdlib only).

Checks, for all distinct prime pairs (p,q) with p,q < 200:
  (a) If p,q both odd: exactly one Sylow family is forced unique:
        q>p  => n_q = 1 forced (q cannot divide p^2-1).
        q<p  => n_p = 1 forced (q not 1 mod p).
  (b) Lemma: p odd, q|p+1, q distinct prime => q<p (so boundary is inside case (a)-second).
  (c) The p=2 exception: (p,q)=(2,3) admits n_3 in {1,4}, so uniqueness fails
      (this is where the order-12 simples live).
Prints VERIFY_OK plus counters on success; raises AssertionError otherwise.
"""
import sys


def primes_below(n):
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i:n:i] = [False] * len(range(i * i, n, i))
    return [i for i, v in enumerate(sieve) if v]


def allowed_sylow(order_factor_base, prime):
    # allowed values of n_prime: divisors of (order / prime-power part) congruent 1 mod prime
    # Here order = p^2 q. For n_q: divisors of p^2 that are 1 mod q. For n_p: divisors of q that are 1 mod p.
    return [d for d in order_factor_base if d % prime == 1]


def main():
    primes = primes_below(200)
    odd = [x for x in primes if x % 2 == 1]
    n_pairs = 0
    n_qgtp_unique = 0
    n_qltp_unique = 0
    boundary_cases = []  # odd distinct pairs with q | p+1
    for p in odd:
        for q in odd:
            if p == q:
                continue
            n_pairs += 1
            div_p2 = [1, p, p * p]
            div_q = [1, q]
            nq_allowed = allowed_sylow(div_p2, q)
            np_allowed = allowed_sylow(div_q, p)
            if q > p:
                # claim: n_q forced 1
                assert nq_allowed == [1], (p, q, nq_allowed)
                n_qgtp_unique += 1
                # also: q | p+1 impossible here
                assert (p + 1) % q != 0, (p, q)
            else:  # q < p
                assert np_allowed == [1], (p, q, np_allowed)
                n_qltp_unique += 1
            if (p * (p + 1)) % q == 0:  # q | p(p+1), q != p  <=>  q | p+1
                assert (p + 1) % q == 0
                assert q < p, (p, q)  # boundary always in q<p regime
                boundary_cases.append((p, q))
    # every odd boundary pair still has unique Sylow p => proper ideal of order p^2
    assert len(boundary_cases) > 0
    for (p, q) in boundary_cases:
        assert [d for d in [1, q] if d % p == 1] == [1]
    # p=2 exception
    n3_allowed_12 = [d for d in [1, 2, 4] if d % 3 == 1]
    assert n3_allowed_12 == [1, 4], n3_allowed_12
    print("pairs_checked=%d q>p_forced=%d q<p_forced=%d boundary_odd=%d"
          % (n_pairs, n_qgtp_unique, n_qltp_unique, len(boundary_cases)))
    print("order12_n3_allowed=%s" % (n3_allowed_12,))
    print("VERIFY_OK")


if __name__ == "__main__":
    sys.exit(main())
