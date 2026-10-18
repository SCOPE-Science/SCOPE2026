"""Finite checks for a packet-reversal sign-character theorem.

Usage: python check.py
No external dependencies. These are finite checks, not a proof for all n.
"""
from fractions import Fraction
from itertools import product


def packet_permutation(cuts):
    n = len(cuts) + 1
    starts = [0] + [i + 1 for i, bit in enumerate(cuts) if bit]
    stops = starts[1:] + [n]
    order = []
    for a, b in zip(starts, stops):
        order.extend(range(b - 1, a - 1, -1))
    return order, [b - a for a, b in zip(starts, stops)]


def inversion_sign(perm):
    inv = sum(perm[i] > perm[j]
              for i in range(len(perm))
              for j in range(i + 1, len(perm)))
    return -1 if inv % 2 else 1


def direct_sign_mean(n, p):
    q = 1 - p
    total = Fraction(0)
    for cuts in product((0, 1), repeat=n - 1):
        perm, lengths = packet_permutation(cuts)
        s = inversion_sign(perm)
        assert s == (-1) ** sum(k // 2 for k in lengths)
        cut_count = sum(cuts)
        total += s * p ** cut_count * q ** (n - 1 - cut_count)
    return total


def exact_recurrence(n, p):
    q = 1 - p
    if n == 0 or n == 1:
        return Fraction(1)
    a, b = Fraction(1), Fraction(1)
    for _ in range(2, n + 1):
        a, b = b, p * b - q * a
    return b


def run():
    cases = 0
    for p in [Fraction(1, 4), Fraction(1, 2),
              Fraction(3, 4), Fraction(9, 10)]:
        for n in range(1, 13):
            assert direct_sign_mean(n, p) == exact_recurrence(n, p)
            cases += 1
    assert exact_recurrence(2, Fraction(1, 2)) == 0
    assert exact_recurrence(3, Fraction(1, 2)) == -Fraction(1, 2)
    assert exact_recurrence(4, Fraction(3, 4)) == -Fraction(1, 32)
    assert all(exact_recurrence(n, Fraction(9, 10)) > 0
               for n in range(1, 121))
    assert any(exact_recurrence(n, Fraction(3, 4)) < 0
               for n in range(1, 31))
    assert any(exact_recurrence(n, Fraction(3, 4)) > 0
               for n in range(1, 31))
    for p in [Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)]:
        vals = [exact_recurrence(n, p) for n in range(151)]
        assert all(abs(x) <= 1 for x in vals)
        # Sign probabilities of t independent passes are a group character.
        for n in [3, 6, 12]:
            eig = vals[n]
            for t in range(7):
                even_prob = (1 + eig ** t) / 2
                assert Fraction(0) <= even_prob <= Fraction(1)
    print(f"PASS: {cases} exhaustive rational cut-pattern checks, "
          "sign/parity and phase-boundary consistency checks")


if __name__ == '__main__':
    run()
