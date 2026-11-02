#!/usr/bin/env python3
"""Exact integer certificate for the first odd ample number with three prime supports.

No external modules, datasets, or probabilistic tests are needed.
Run: python3 verify.py
"""
import hashlib
from math import comb

if not __debug__:
    raise RuntimeError("Run without Python -O: assertions are essential to the certificate")

PRIMES = (3, 5, 7)
CANDIDATE_EXPONENTS = (20, 9, 6)
CANDIDATE = 3**20 * 5**9 * 7**6
CANDIDATE_RECURSIVE_DIVISORS = 841632661765951062016


def powers_up_to(base, limit):
    values = [1]
    while values[-1] * base <= limit:
        values.append(values[-1] * base)
    return values


def get(table, a, b, c):
    if a < 0 or b < 0 or c < 0:
        return 0
    return table[(a, b, c)]


def evaluate():
    powers = [powers_up_to(p, CANDIDATE) for p in PRIMES]
    kappa = {}
    prefix = {}
    cases = 0
    smaller_cases = 0
    violations = []
    digest = hashlib.sha256()

    # The mixed-neighbor recurrence comes from
    # K(x,y,z) = 1 / (2(1-x)(1-y)(1-z) - 1).
    # The second recurrence is independent: direct proper-divisor summation
    # using three-dimensional inclusion-exclusion of prefix boxes.
    for a in range(len(powers[0])):
        for b in range(len(powers[1])):
            for c in range(len(powers[2])):
                if a == b == c == 0:
                    value = 1
                else:
                    value = (
                        2 * (get(kappa, a - 1, b, c) +
                             get(kappa, a, b - 1, c) +
                             get(kappa, a, b, c - 1))
                        - 2 * (get(kappa, a - 1, b - 1, c) +
                               get(kappa, a - 1, b, c - 1) +
                               get(kappa, a, b - 1, c - 1))
                        + 2 * get(kappa, a - 1, b - 1, c - 1)
                    )
                proper = (
                    get(prefix, a - 1, b, c) +
                    get(prefix, a, b - 1, c) +
                    get(prefix, a, b, c - 1) -
                    get(prefix, a - 1, b - 1, c) -
                    get(prefix, a - 1, b, c - 1) -
                    get(prefix, a, b - 1, c - 1) +
                    get(prefix, a - 1, b - 1, c - 1)
                )
                assert value == 1 + proper, (a, b, c, value, proper)
                assert value > 0
                kappa[(a, b, c)] = value
                prefix[(a, b, c)] = value + proper

                # Exhaust all positive exponent triples whose smallest
                # odd-prime realization is at most the candidate.
                n = powers[0][a] * powers[1][b] * powers[2][c]
                if a and b and c and n <= CANDIDATE:
                    cases += 1
                    digest.update(f'{a},{b},{c},{n},{value}\n'.encode())
                    if n < CANDIDATE:
                        smaller_cases += 1
                        assert value <= n, (a, b, c, value, n)
                    else:
                        if value > n:
                            violations.append((a, b, c, n, value))
    assert CANDIDATE == 801204488268064453125
    assert CANDIDATE_RECURSIVE_DIVISORS > CANDIDATE
    assert kappa[CANDIDATE_EXPONENTS] == CANDIDATE_RECURSIVE_DIVISORS
    assert len(violations) == 1
    assert violations[0] == (*CANDIDATE_EXPONENTS, CANDIDATE, CANDIDATE_RECURSIVE_DIVISORS)
    assert cases == 4650 and smaller_cases == 4649

    # A genuinely separate direct divisor-lattice recursion on small cases.
    # No generating function and no inclusion-exclusion are used here.
    independent = {}
    for a in range(7):
        for b in range(7):
            for c in range(7):
                smaller = sum(
                    independent[(i, j, h)]
                    for i in range(a + 1)
                    for j in range(b + 1)
                    for h in range(c + 1)
                    if (i, j, h) != (a, b, c)
                )
                independent[(a, b, c)] = 1 + smaller
                assert independent[(a, b, c)] == kappa[(a, b, c)]

    # Independently evaluate the triple-prime formula in Fink's 2020 paper.
    # This calculation is based on binomial sums rather than divisor recursion.
    def two_prime_formula(a, c):
        return (2 ** a) * sum(comb(c, i) * comb(a + i, i)
                              for i in range(c + 1))

    def three_prime_formula(a, b, c):
        return sum((-1) ** j * comb(b, j) * comb(a + b - j, b)
                   * two_prime_formula(a + b - j, c)
                   for j in range(b + 1))

    for a, b, c in ((20, 9, 6), (1, 1, 1), (3, 5, 2), (7, 4, 3),
                    (20, 9, 5), (19, 9, 6), (20, 8, 6)):
        assert three_prime_formula(a, b, c) == kappa[(a, b, c)]

    return {
        'max_exponents': tuple(len(v)-1 for v in powers),
        'all_triples_checked': cases,
        'strictly_smaller_triples_checked': smaller_cases,
        'independent_direct_divisor_cases': len(independent),
        'independent_closed_formula_cases': 7,
        'first_exponents': CANDIDATE_EXPONENTS,
        'first_integer': CANDIDATE,
        'recursive_divisor_count': CANDIDATE_RECURSIVE_DIVISORS,
        'census_sha256': digest.hexdigest(),
    }


if __name__ == '__main__':
    r = evaluate()
    for key, val in r.items():
        print(f'{key}={val}')
    print('VERIFY_OK')
