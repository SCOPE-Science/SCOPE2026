#!/usr/bin/env python3
from math import isqrt


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def tau(n):
    if n < 1:
        raise ValueError("tau expects a positive integer")
    ans = 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            ans *= e + 1
        d += 1 if d == 2 else 2
    if n > 1:
        ans *= 2
    return ans


def legendre_nonresidue(a, p):
    a %= p
    return a != 0 and pow(a, (p - 1) // 2, p) == p - 1


def theorem_member(beta, r, p):
    c = 8 * beta + r
    if c % p != 0 or c % (p * p) == 0:
        return False
    t = c // p
    return t % 8 != 1 or legendre_nonresidue(t, p)


def square_modulus_solution(t, p):
    mod = 8 * p
    return next((x for x in range(mod) if (x * x - t) % mod == 0), None)


assertions = 0
members = 0
square_witnesses = 0
direct_tau_checks = 0

for p in range(3, 200, 2):
    if not is_prime(p):
        continue
    for r in (3, 5, 7):
        predicted = []
        exact_p_candidates = 0
        candidate_residues = set()
        for beta in range(p * p):
            c = 8 * beta + r
            member = theorem_member(beta, r, p)
            if c % p == 0 and c % (p * p) != 0:
                exact_p_candidates += 1
                t = c // p
                candidate_residues.add(t % p)
                x0 = square_modulus_solution(t, p)
                congruence_has_square = x0 is not None
                expected_has_square = (t % 8 == 1 and not legendre_nonresidue(t, p))
                assert congruence_has_square == expected_has_square
                assertions += 1
                assert member == (not congruence_has_square)
                assertions += 1
                if congruence_has_square:
                    x = x0
                    while x * x < t:
                        x += 8 * p
                    n = (x * x - t) // (8 * p)
                    N = 8 * (p * p * n + beta) + r
                    assert N == p * x * x
                    assert tau(N) % 4 == 2
                    square_witnesses += 1
                    assertions += 2
            if member:
                predicted.append(beta)
                members += 1
                for n in range(40):
                    N = 8 * (p * p * n + beta) + r
                    assert tau(N) % 4 == 0
                    direct_tau_checks += 1
                    assertions += 1
        assert exact_p_candidates == p - 1
        assertions += 1
        assert candidate_residues == set(range(1, p))
        assertions += 1
        expected_count = (p - 1) // 2 if p % 8 == r % 8 else p - 1
        assert len(predicted) == expected_count
        assertions += 1

print(
    "VERIFY_OK",
    f"assertions={assertions}",
    f"members={members}",
    f"square_witnesses={square_witnesses}",
    f"direct_tau_checks={direct_tau_checks}",
)
