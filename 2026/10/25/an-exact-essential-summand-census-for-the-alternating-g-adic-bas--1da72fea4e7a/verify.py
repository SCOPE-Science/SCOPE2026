#!/usr/bin/env python3
"""Finite independent exact enumeration of an essential-summand fiber."""

def fiber(g, k):
    bound = g ** (2 * k)
    admissible = []
    for number in range(1, bound):
        digit_positions = set()
        q, r = number, 0
        while q:
            if q % g:
                digit_positions.add(r % 2)
            q //= g
            r += 1
        if len(digit_positions) == 1:
            admissible.append(number)
    representations = {}
    for idx, a in enumerate(admissible):
        for b in admissible[idx:]:
            n = a + b
            if n >= bound:
                break
            representations.setdefault(n, []).append((a, b))
    observed = {n for n, pairs in representations.items()
                if any(1 in pair for pair in pairs)
                and all(1 in pair for pair in pairs)}
    explicit = {2, 3}
    explicit.update(1 + g ** (2 * j) for j in range(1, k))
    for encoding in range(g ** k):
        digits, q = [], encoding
        for _ in range(k):
            digits.append(q % g)
            q //= g
        if max(digits) >= 2:
            explicit.add(1 + sum(d * g ** (2 * i + 1)
                                 for i, d in enumerate(digits)))
    assert observed == explicit, (g, k, sorted(observed ^ explicit)[:10])
    assert len(observed) == g ** k - 2 ** k + k + 1
    return len(observed)

if __name__ == '__main__':
    for base in (3, 4, 5):
        for blocks in (1, 2, 3):
            print(base, blocks, fiber(base, blocks))
    for blocks in (1, 2):
        print(6, blocks, fiber(6, blocks))
    print('VERIFY_OK')
