"""Standalone exhaustive checks of the binary linear diameter-three anticode census.

Uses closure of finite vector subspaces rather than the proof's column-geometric classification.
Python 3 standard library only.
"""
from collections import Counter
from math import comb

EXPECTED = {
    (0, 0): 1,
    (1, 1): 1,
    (1, 2): 1,
    (1, 3): 1,
    (2, 2): 1,
    (2, 3): 4,
    (2, 4): 6,
    (3, 3): 1,
    (3, 4): 4,
}


def all_subspaces(n):
    """Each finite linear space is grown by one independent vector at a time."""
    current = {frozenset((0,))}
    every = set(current)
    for _ in range(n):
        following = set()
        for space in current:
            for v in range(1, 1 << n):
                if v not in space:
                    enlarged = frozenset(space | {v ^ w for w in space})
                    if enlarged not in every:
                        following.add(enlarged)
        every.update(following)
        current = following
    return every


def coefficient(n, s):
    return comb(n, s) if 0 <= s <= n else 0


def predicted(n, k=None):
    if k is None:
        return 1+n+2*coefficient(n,2)+6*coefficient(n,3)+10*coefficient(n,4)
    if k == 0:
        return 1
    if k == 1:
        return n + coefficient(n,2) + coefficient(n,3)
    if k == 2:
        return coefficient(n,2) + 4*coefficient(n,3) + 6*coefficient(n,4)
    if k == 3:
        return coefficient(n,3) + 4*coefficient(n,4)
    return 0


def main():
    for n in range(8):
        all_spaces = all_subspaces(n)
        counter = Counter()
        for space in all_spaces:
            if max(w.bit_count() for w in space) > 3:
                continue
            k = len(space).bit_length()-1
            support = 0
            for w in space:
                support |= w
            counter[(k, support.bit_count())] += 1
        for k in range(4):
            total = sum(v for (dim, _), v in counter.items() if dim == k)
            assert total == predicted(n, k), (n, k, total, predicted(n,k))
        assert sum(counter.values()) == predicted(n), (n, sum(counter.values()), predicted(n))
        for (k,s),count in counter.items():
            assert count == EXPECTED.get((k,s), 0) * coefficient(n,s), (n,k,s,count)
        print(f"AMBIENT_N={n} SUBSPACES={len(all_spaces)} VALID={sum(counter.values())}")
        if n == 7:
            print("DIM_SUPPORT_COUNTS", sorted(counter.items()))
    print("VERIFY_OK: all binary subspaces n<=7 exhaustively checked")


if __name__ == '__main__':
    main()
