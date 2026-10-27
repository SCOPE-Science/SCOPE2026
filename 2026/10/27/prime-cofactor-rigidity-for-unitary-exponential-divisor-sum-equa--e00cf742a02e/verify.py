"""Reproducible finite checks for an exact divisor-sum equality classification.

The infinite theorem is proved in RESULT.md. These tests do not certify
unexamined integers or replace the proof.
"""
from itertools import product
from math import isqrt


def factor(n):
    out = []
    for p in range(2, isqrt(n) + 1):
        if n % p == 0:
            a = 0
            while n % p == 0:
                n //= p
                a += 1
            out.append((p, a))
    if n > 1:
        out.append((n, 1))
    return out


def primes_upto(bound):
    return [p for p in range(2, bound + 1)
            if p > 1 and len(factor(p)) == 1 and factor(p)[0] == (p, 1)]


def sigma_unitary(factors):
    choices = [(1, p ** a) for p, a in factors]
    return sum(__import__('math').prod(s) for s in product(*choices))


def sigma_exponential(factors):
    choices = [tuple(p ** d for d in range(1, a + 1) if a % d == 0)
               for p, a in factors]
    return sum(__import__('math').prod(s) for s in product(*choices))


def is_squarefree(n):
    return all(a == 1 for _, a in factor(n))


def main():
    sol = []
    checks = 0
    repeated_ge2 = 0
    ps = primes_upto(101)
    for m in range(2, 301):
        if not is_squarefree(m):
            continue
        k = len(factor(m))
        for q in ps:
            if m % q == 0:
                continue
            ff = [(q, 1)] + [(p, 2) for p, _ in factor(m)]
            s = sigma_unitary(ff)
            e = sigma_exponential(ff)
            checks += 1
            if k >= 2:
                repeated_ge2 += 1
            if s == e:
                sol.append((m, q, m * m * q))
    assert sorted(sol) == [(2, 5, 20), (3, 5, 45)], sol
    assert sigma_unitary([(2, 2), (5, 1)]) == 30
    assert sigma_exponential([(3, 2), (5, 1)]) == 60
    print('VERIFY_OK', 'squarefree_m=2..300', 'cofactor_primes<=101',
          'exact_pairs', checks, 'k_ge2_pairs', repeated_ge2,
          'solutions', sol)


if __name__ == '__main__':
    main()
