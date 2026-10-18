"""Exact finite checks for four-step odd-greedy termination of 2/q."""
from fractions import Fraction

FOUR_CLASSES = frozenset((7, 35, 47, 55))


def predicted_length_at_most_four(q):
    assert q >= 3 and q & 1
    if q % 4 == 1 or q % 12 == 3:
        return 2
    if q % 60 in FOUR_CLASSES:
        return 4
    return None  # not finished in four steps


def direct_greedy(q, maximum_steps=4):
    remaining = Fraction(2, q)
    denominators = []
    for _ in range(maximum_steps):
        if not remaining:
            break
        # Smallest odd denominator whose reciprocal is no larger than remaining.
        x = (remaining.denominator + remaining.numerator - 1) // remaining.numerator
        if x % 2 == 0:
            x += 1
        assert Fraction(1, x) <= remaining
        assert x <= 2 or Fraction(1, x - 2) > remaining
        denominators.append(x)
        remaining -= Fraction(1, x)
    assert sum((Fraction(1, x) for x in denominators), Fraction(0)) + remaining == Fraction(2, q)
    return (len(denominators) if remaining == 0 else None), denominators


def main():
    counts = {2: 0, 4: 0, None: 0}
    total = 0
    for q in range(3, 20002, 2):
        pred = predicted_length_at_most_four(q)
        actual, den = direct_greedy(q)
        assert pred == actual, (q, pred, actual, den)
        counts[pred] += 1
        total += 1
    residues = {2: [], 4: [], None: []}
    for q in range(1, 60, 2):
        # q=1 has the same formal residue as all positive q ≡ 1 mod60.
        r = 2 if q % 4 == 1 or q % 12 == 3 else (4 if q in FOUR_CLASSES else None)
        residues[r].append(q)
    assert residues[2] == [1, 3, 5, 9, 13, 15, 17, 21, 25, 27, 29, 33, 37, 39, 41, 45, 49, 51, 53, 57]
    assert residues[4] == [7, 35, 47, 55]
    assert residues[None] == [11, 19, 23, 31, 43, 59]
    print('Direct exact Fraction checks for all odd q in [3, 20001]:', total)
    print('Observed length 2:', counts[2])
    print('Observed length 4:', counts[4])
    print('No termination within four steps:', counts[None])
    print('Residue counts modulo 60 among 30 odd classes: length 2 = 20, length 4 = 4, other = 6')
    print('Examples: q=7 ->', direct_greedy(7), '; q=11 ->', direct_greedy(11))
    print('OK')


if __name__ == '__main__':
    main()
