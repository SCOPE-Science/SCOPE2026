#!/usr/bin/env python3
"""Independent exact-integer checks of the restricted-digit modular count identities."""
from math import gcd

def residue_counts(q, base, digit, length):
    counts = [1] + [0] * (q - 1)
    place = 1
    for _ in range(length):
        nxt = counts[:]
        shift = digit * place % q
        for r, count in enumerate(counts):
            nxt[(r + shift) % q] += count
        counts = nxt
        place = place * base % q
    return counts

def verify_case(q, base, digit, repetitions=4):
    assert q >= 3 and q % 2 == 1 and base >= 3 and 1 <= digit < base
    assert gcd(q, base * digit) == 1
    H = []
    val = 1
    while val not in H:
        H.append(val)
        val = val * base % q
    assert val == 1
    t = len(H)
    if 2 % q in H:
        sign = 1
    elif (-2) % q in H:
        sign = -1
    else:
        raise ValueError('Case outside theorem')
    S = (digit * sum(H)) % q
    assert (pow(2, t, q) == (1 if sign == 1 else (-1)**t % q))
    for length in range(repetitions * t + 1):
        a = residue_counts(q, base, digit, length)
        after = residue_counts(q, base, digit, length + t)
        e = 1 if sign == 1 else (-1) ** t
        assert (2 ** (length + t) - e * 2 ** length) % q == 0
        change = (2 ** (length + t) - e * 2 ** length) // q
        predicted = [change + e * a[(r + (0 if sign == 1 else S)) % q] for r in range(q)]
        assert after == predicted, (q, base, digit, length)
        assert all(v >= 0 for v in predicted)
    return t, sign, S, repetitions * t + 1

def main():
    data = [
        (7, 3, 1), (7, 4, 1), (7, 4, 3),
        (9, 4, 1), (9, 4, 2), (9, 5, 1),
        (11, 3, 1), (11, 3, 2), (15, 8, 1),
        (21, 8, 1), (23, 4, 1), (25, 3, 1),
        (27, 4, 1), (49, 3, 1), (31, 5, 1)
    ]
    checked = 0
    for q, base, digit in data:
        if gcd(q, base * digit) != 1:
            continue
        H = {pow(base, i, q) for i in range(100)}
        if (2 % q) not in H and ((-2) % q) not in H:
            continue
        t, sign, S, steps = verify_case(q, base, digit, 3)
        checked += steps
        print(f'q={q} base={base} digit={digit} t={t} sign={sign:+d} offset={S} verified={steps}')
    # Perfect balancing is a separate exact finite preperiod observation.
    for q, b in [(7, 3), (7, 4), (9, 4)]:
        for length in range(180):
            c = residue_counts(q, b, 1, length)
            assert max(c) - min(c) <= 1, (q, b, length)
    print(f'PASS: {checked} exact signed recurrence comparisons; 540 balanced prefixes')

if __name__ == '__main__':
    main()
