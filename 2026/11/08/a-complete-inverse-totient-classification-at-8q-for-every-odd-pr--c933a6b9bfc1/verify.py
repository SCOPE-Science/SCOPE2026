"""Exact arithmetic checks of the inverse-totient classification at 8q.

Usage: python verify.py
Only Python's standard library is needed.
Finite checks support, but do not establish, the unrestricted theorem.
"""
from itertools import product
from math import isqrt


def prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for p in range(3, isqrt(n) + 1, 2):
        if n % p == 0:
            return False
    return True


def candidates(q):
    if q == 3:
        return [35, 39, 45, 52, 56, 70, 72, 78, 84, 90]
    if q == 5:
        return [41, 55, 75, 82, 88, 100, 110, 132, 150]
    A, B, C = 2*q + 1, 4*q + 1, 8*q + 1
    result = []
    if prime(A):
        result += [5*A, 8*A, 10*A, 12*A]
    if prime(B):
        result += [3*B, 4*B, 6*B]
    if prime(C):
        result += [C, 2*C]
    return sorted(result)


def inverse_by_prime_powers(m):
    """Independent exact finite inverse: enumerate allowed prime-power factors."""
    ps = [d + 1 for d in range(1, m + 1) if m % d == 0 and prime(d + 1)]
    branches = []
    for p in ps:
        choices = [(1, 1)]
        e = 1
        while m % (p**(e - 1) * (p - 1)) == 0:
            choices.append((p**e, p**(e - 1) * (p - 1)))
            e += 1
        branches.append(choices)
    found = []
    for combo in product(*branches):
        n, tot = 1, 1
        for term, phi_term in combo:
            n *= term
            tot *= phi_term
        if tot == m:
            found.append(n)
    assert len(found) == len(set(found))
    return sorted(found)


def totient_sieve(n):
    phi = list(range(n + 1))
    for p in range(2, n + 1):
        if phi[p] == p:
            for j in range(p, n + 1, p):
                phi[j] -= phi[j] // p
    return phi


def main():
    qlimit = 997
    qlist = [q for q in range(3, qlimit + 1, 2) if prime(q)]
    nlimit = 24*qlimit + 12
    phi = totient_sieve(nlimit)
    by_value = {}
    for n in range(1, nlimit + 1):
        by_value.setdefault(phi[n], []).append(n)
    checked = 0
    for q in qlist:
        formula = candidates(q)
        sieve = by_value.get(8*q, [])
        independent = inverse_by_prime_powers(8*q)
        assert formula == sieve == independent, (q, formula, sieve, independent)
        assert len(formula) != 1
        if q >= 7:
            A, B, C = 2*q + 1, 4*q + 1, 8*q + 1
            assert len(formula) == 4*prime(A) + 3*prime(B) + 2*prime(C)
            if q % 3 == 1:
                assert len(formula) in (0, 3)
            else:
                assert len(formula) in (0, 2, 4, 6)
        checked += 1
    for q in [3, 5, 7, 11, 13, 17, 23, 29, 37]:
        print(f'FIBER q={q} size={len(candidates(q))} members={candidates(q)}')
    print(f'VERIFY_OK primes_checked={checked} q_max={qlimit} n_bound={nlimit} exact_phi_sieve=yes independent_prime_power_inverse=yes equality_and_disjointness=yes')


if __name__ == '__main__':
    main()
