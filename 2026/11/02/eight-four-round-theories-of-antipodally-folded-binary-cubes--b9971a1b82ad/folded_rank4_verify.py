#!/usr/bin/env python3
"""Exact four-round first-order types of antipodally folded binary cubes.

The only graph language is equality and an undirected adjacency predicate.
Run with Python 3.9 or newer; no third-party modules are used.
"""
from functools import lru_cache
from itertools import product


def atomic_from_column_counts(counts):
    """Complete 4-tuple atomic diagram, with the first representative zero.

    Pattern p in [0,7] stores bits for the other three representatives.
    Two folded vertices agree iff their vector difference has Hamming
    weight 0 or n, and are adjacent iff it has weight 1 or n-1.
    """
    n = sum(counts)
    answer = shift = 0
    for i in range(4):
        for j in range(i + 1, 4):
            mismatch = sum(
                count for p, count in enumerate(counts)
                if ((p >> (i - 1)) & 1 if i else 0)
                != ((p >> (j - 1)) & 1 if j else 0)
            )
            symbol = (1 if mismatch in (0, n)
                      else 2 if mismatch in (1, n - 1) else 0)
            answer |= symbol << shift
            shift += 2
    return answer


def extend_counts(counts):
    """Enumerate all choices of a new vector by splitting each pattern."""
    for split in product(*(range(c + 1) for c in counts)):
        yield tuple(c - x for c, x in zip(counts, split)) + split


@lru_cache(maxsize=None)
def triple_type(counts):
    return frozenset(atomic_from_column_counts(child)
                     for child in extend_counts(counts))


@lru_cache(maxsize=None)
def pair_type(counts):
    return frozenset(triple_type(child) for child in extend_counts(counts))


def root_type(n):
    # The automorphism group acts transitively on the vertex set.
    return frozenset(pair_type((n - a, a)) for a in range(n + 1))


def direct_atomic(n, vertices):
    """Atomic diagram computed from actual graph vertices, not patterns."""
    width = n - 1
    answer = shift = 0
    for i in range(4):
        for j in range(i + 1, 4):
            dist = (vertices[i] ^ vertices[j]).bit_count()
            symbol = (1 if dist == 0 else
                      2 if dist == 1 or dist == width else 0)
            answer |= symbol << shift
            shift += 2
    return answer


def direct_root_type(n):
    vertices = range(1 << (n - 1))

    @lru_cache(maxsize=None)
    def t3(a, b):
        return frozenset(direct_atomic(n, (0, a, b, c)) for c in vertices)

    @lru_cache(maxsize=None)
    def t2(a):
        return frozenset(t3(a, b) for b in vertices)

    return frozenset(t2(a) for a in vertices)


def main():
    first = {}
    representatives = []
    for n in range(2, 17):
        t = root_type(n)
        representative = next((k for k in representatives if first[k] == t), None)
        if representative is None:
            representative = n
            first[n] = t
            representatives.append(n)
        print(f'ORBIT n={n} representative={representative} '
              f'root_extension_types={len(t)}', flush=True)

    assert representatives == [2, 3, 4, 5, 6, 7, 8, 10]
    assert all(root_type(n) == root_type(10) for n in range(10, 17))
    assert root_type(8) == root_type(9)
    for n in range(2, 8):
        assert direct_root_type(n) == root_type(n)
        print(f'DIRECT_ORBIT_AGREEMENT_OK n={n} vertices={1 << (n - 1)}',
              flush=True)
    print('EIGHT_CLASSES_AND_FINITE_BOUNDARY_OK')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
