#!/usr/bin/env python3
"""Independent finite-state verification for the capacitated sharing game on K_{n,n}.

This is a finite test, not a substitute for the all-size proof.
Run: python3 verify_capacitated_biclique_spectrum.py
"""
from itertools import combinations


def covers_by_nominations(donors, recipients, capacity):
    """Enumerate every possible individual exact-capacity recipient set."""
    if donors == 0:
        return recipients == 0
    if recipients < capacity:
        return False
    offers = [sum(1 << i for i in choice)
              for choice in combinations(range(recipients), capacity)]
    states = {0}
    for _ in range(donors):
        states = {state | offer for state in states for offer in offers}
    return ((1 << recipients) - 1) in states


def direct_feasible(n, k, p, q):
    # p = buyers in left part, q = buyers in right part.
    # A buyer can only nominate a nonbuyer in the other part.
    return (covers_by_nominations(p, n-q, k)
            and covers_by_nominations(q, n-p, k))


def formula_spectrum(n, k):
    if k == n:
        return {n}
    s_min = min(2 * ((n + k) // (k+1)),
                2 * ((n - 1 + k) // (k+1)) + 1)
    return {n} | set(range(s_min, 2 * (n-k) + 1))


def verify():
    ncases = 0
    for n in range(2, 9):
        for k in range(1, n+1):
            spectrum = set()
            for p in range(n+1):
                for q in range(n+1):
                    if direct_feasible(n, k, p, q):
                        spectrum.add(p+q)
            expected = formula_spectrum(n, k)
            assert spectrum == expected, (n, k, sorted(spectrum), sorted(expected))
            ncases += 1
    print('PASS: exact nomination subsets agree with cardinality formula for',
          ncases, '(n,k) instances, 2 <= n <= 8.')
    for n in (4, 5, 8):
        print('n =', n, 'capacity n-1 spectrum =',
              sorted(formula_spectrum(n, n-1)))


if __name__ == '__main__':
    verify()
