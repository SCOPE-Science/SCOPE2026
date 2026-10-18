"""Reproduce the rank-two signature census for finite nonempty strict posets.

A naturally labelled poset is stored as downset masks D[j] ⊆ {0,...,j-1}.
The inductive generator adjoins a new maximal element above any order ideal.
No external Python packages are required.
"""
from collections import Counter

EXPECTED_MINIMAL = {
    1: 1, 2: 2, 20: 2, 24: 3, 36: 3, 42: 3, 84: 3,
    40: 4, 88: 4, 100: 4, 148: 4, 152: 4, 164: 4, 170: 4,
    104: 5, 168: 5, 212: 5, 216: 5, 228: 5, 232: 6,
}
EXPECTED_COUNTS = (1, 2, 7, 40, 357, 4824)


def order_ideals(D):
    n = len(D)
    for m in range(1 << n):
        if all((not (m >> i & 1)) or (D[i] & m) == D[i] for i in range(n)):
            yield m


def relation(D, i, j):
    if i == j:
        return 0
    if D[j] >> i & 1:
        return 1
    if D[i] >> j & 1:
        return 2
    return 3


def pointed_one_round_types(D):
    n = len(D)
    return frozenset(frozenset(relation(D, i, j) for j in range(n)) for i in range(n))


def signature(D):
    out = 0
    for row in pointed_one_round_types(D):
        # Equality (0) is always present. 1=above, 2=below, 3=incomparable.
        a = (4 if 2 in row else 0) | (2 if 1 in row else 0) | (1 if 3 in row else 0)
        out |= 1 << a
    return out


def two_round_ef_equivalent(A, B):
    # Direct two-round game, starting in either structure. Second-round
    # responses must preserve every atomic relation to the first pebble.
    for X, Y in ((A, B), (B, A)):
        for x in range(len(X)):
            if not any(
                all(any(relation(X, x, xx) == relation(Y, y, yy)
                        for yy in range(len(Y))) for xx in range(len(X)))
                and all(any(relation(X, x, xx) == relation(Y, y, yy)
                            for xx in range(len(X))) for yy in range(len(Y)))
                for y in range(len(Y))
            ):
                return False
    return True


def main():
    parents = {()}
    minima = {}
    for n in range(1, 7):
        current = {D + (ideal,) for D in parents for ideal in order_ideals(D)}
        assert len(current) == EXPECTED_COUNTS[n - 1], (n, len(current))
        for D in current:
            minima.setdefault(signature(D), (n, D))
        parents = current
    found = {mask: n for mask, (n, _) in minima.items()}
    assert found == EXPECTED_MINIMAL, (found, EXPECTED_MINIMAL)
    reps = list(minima.items())
    for i, (mask_a, (_, A)) in enumerate(reps):
        for mask_b, (_, B) in reps[i:]:
            assert two_round_ef_equivalent(A, B) == (mask_a == mask_b)
    assert signature((0, 0, 3, 7, 7, 23)) == 232
    print('PASS: complete witnesses for 20 rank-two poset theories')
    print('Natural-label counts n=1..6:', EXPECTED_COUNTS)
    print('Distinct signatures:', len(minima))
    print('Minimum sizes:', dict(sorted(found.items())))
    print('All representative pairs satisfy the direct two-round EF criterion.')
    print('Unique 6-element minimum signature:', [s for s, n in found.items() if n == 6])


if __name__ == '__main__':
    main()
