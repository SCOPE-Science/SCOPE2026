"""Finite exact-arithmetic checks of contiguous-block Sylvester-Hadamard sketches.

The assertions test sample Gram entries and the combinatorial classification.
They are not a replacement for the all-dimension character-orthogonality proof.
"""
from itertools import combinations, product
from math import comb


def parity(value):
    return value.bit_count() & 1


def verify():
    checked = 0
    count_checks = 0
    for d in (3, 4):
        n = 1 << d
        for s in range(1, d):
            tau = 1 << s
            kmax = n // tau
            # Count coordinate subspaces with distinct residue classes.
            for m in range(1, min(n, tau + 1) + 1):
                total = sum(len({a % tau for a in indices}) == m
                            for indices in combinations(range(n), m))
                assert total == comb(tau, m) * kmax**m if m <= tau else total == 0
                count_checks += 1
            for q in range(1, 4):
                for a, b in combinations(range(n), 2):
                    delta = a ^ b
                    for sign in (-1, 1):
                        for seq in product(range(kmax), repeat=q):
                            # Direct unnormalized Walsh-character Gram numerator.
                            numerator = sum(
                                (-1 if parity((block*tau + u) & delta) else 1)
                                for block in seq for u in range(tau)
                            ) * sign
                            # Closed formula from dyadic residue grouping.
                            if delta & (tau - 1):
                                expected = 0
                            else:
                                expected = tau * sign * sum(
                                    -1 if parity(block & (delta >> s)) else 1
                                    for block in seq
                                )
                            assert numerator == expected
                            assert abs(numerator) <= q*tau
                            checked += 1
                # Two columns in the same low-bit class: exact rank-loss count.
                losses = sum(
                    abs(sum(-1 if parity(block & 1) else 1 for block in seq)) == q
                    for seq in product(range(kmax), repeat=q)
                )
                assert losses * 2**(q-1) == kmax**q
    return checked, count_checks


if __name__ == '__main__':
    checked, count_checks = verify()
    print(f'Passed {checked} exact Gram checks and {count_checks} exact subset-count checks.')
