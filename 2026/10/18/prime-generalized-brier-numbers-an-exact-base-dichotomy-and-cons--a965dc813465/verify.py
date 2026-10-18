"""Finite checks for the elementary local obstruction and CRT unit patch.

This does NOT certify the external two-sided covering systems, infinitude,
or the use of prime-distribution theorems.
"""
from math import gcd


def crt_pair(r, m, s, n):
    assert gcd(m, n) == 1
    t = ((s - r) * pow(m, -1, n)) % n
    return (r + m * t) % (m * n), m * n


def prime_list(hi):
    ans = []
    for x in range(2, hi + 1):
        if all(x % p for p in ans if p * p <= x):
            ans.append(x)
    return ans


def main():
    tested_exact = 0
    for b in range(2, 513):
        m = b - 1
        good = b % 2 == 0 and m % 3 != 0
        candidates = [c for c in range(m) if
                      gcd(c, m) == gcd(c - 1, m) == gcd(c + 1, m) == 1]
        assert bool(candidates) == good, (b, candidates)
        if good:
            assert gcd(2, m) == gcd(1, m) == gcd(3, m) == 1
        tested_exact += 1
    # Independently check the simple formula beyond the brute-force range.
    for b in range(513, 200001):
        m = b - 1
        good = b % 2 == 0 and m % 3 != 0
        assert (gcd(1, m) == gcd(2, m) == gcd(3, m) == 1) == good

    primes = prime_list(300)
    checked_crt = 0
    for b in range(2, 301):
        if b % 2 or (b - 1) % 3 == 0:
            continue
        # Toy unit congruences only: these are NOT a complete covering.
        ps = [p for p in primes if p >= 5 and gcd(p, b * (b - 1)) == 1][:4]
        assert len(ps) == 4
        residues = [(-pow(b, -1, ps[0])) % ps[0],
                    (+pow(b, -2, ps[1])) % ps[1],
                    (-pow(b, -3, ps[2])) % ps[2],
                    (+pow(b, -4, ps[3])) % ps[3]]
        r, Q = 0, 1
        for rr, p in zip(residues, ps):
            r, Q = crt_pair(r, Q, rr, p)
        r, Q = crt_pair(r, Q, 1 + b * b, b ** 3)
        r, Q = crt_pair(r, Q, 2 % (b - 1), b - 1)
        assert gcd(r, Q) == 1
        assert gcd(r - 1, b - 1) == gcd(r + 1, b - 1) == 1
        assert all(r % p == residue for p, residue in zip(ps, residues))
        checked_crt += 1

    print(f"VERIFY_OK exact_local_bases={tested_exact} "
          f"analytic_condition_bases=199488 crt_unit_instances={checked_crt}")


if __name__ == '__main__':
    main()
