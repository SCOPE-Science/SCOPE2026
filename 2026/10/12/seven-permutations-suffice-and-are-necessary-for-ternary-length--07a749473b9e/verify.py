#!/usr/bin/env python3
"""Finite certificate for a permutation covering of ternary even 8-words.

Standard-library only: recomputes all adjacency relations from word
subsequences and all permutations without relying on stored search logs.
"""
from itertools import combinations, permutations, product

N = 4
Q = 3
POS = range(2 * N)
SUBSETS = tuple(combinations(POS, N))
ALL_PERMS = tuple(permutations(range(N)))


def inverse(p):
    return tuple(p.index(i) for i in range(N))


def code(p):
    return ''.join(str(j + 1) for j in p)


def parse_code(s):
    p = tuple(int(ch) - 1 for ch in s)
    assert tuple(sorted(p)) == tuple(range(N))
    return p


def even(w):
    return all(w.count(c) % 2 == 0 for c in range(Q))


def canonical(w):
    seen = {}
    out = []
    for c in w:
        if c not in seen:
            seen[c] = len(seen)
        out.append(seen[c])
    return tuple(out)


def compatible(w, p):
    """Is w a shuffle p-square, allowing either word to be p(image)?"""
    for inds in SUBSETS:
        a = tuple(w[i] for i in inds)
        member = set(inds)
        b = tuple(w[i] for i in POS if i not in member)
        if all(a[j] == b[p[j]] for j in range(N)):
            return True
        if all(b[j] == a[p[j]] for j in range(N)):
            return True
    return False


def orbit_representatives():
    return tuple(sorted({min(p, inverse(p)) for p in ALL_PERMS}))


REPS = orbit_representatives()
assert len(REPS) == 17
UPPER = ('1234', '1342', '2143', '2314', '2431', '3241', '3421')
LOWER = (
    ('00001122', ('1234', '2134')),
    ('00001221', ('1243', '2143')),
    ('00011022', ('1324', '2314')),
    ('00011220', ('1342', '2341')),
    ('00012210', ('1432', '2431')),
    ('01221000', ('3214', '3241')),
    ('01222210', ('3421', '4231', '4321')),
)


def main():
    # All possible even words, including those using 1 or 2 symbols.
    words = tuple(w for w in product(range(Q), repeat=2*N) if even(w))
    assert len(words) == 1641
    canonical_words = tuple(sorted(set(canonical(w) for w in words)))
    assert len(canonical_words) == 274
    assert sum(len(set(w)) == 1 for w in canonical_words) == 1
    assert sum(len(set(w)) == 2 for w in canonical_words) == 63
    assert sum(len(set(w)) == 3 for w in canonical_words) == 210

    # Explicit exhaustive upper certificate on one representative per
    # relabeling orbit, valid for all 1641 labeled words by equivariance.
    chosen = tuple(parse_code(s) for s in UPPER)
    for w in canonical_words:
        assert any(compatible(w, p) for p in chosen), ('uncovered', w)
    # Directly rerun the full labeled census as an independent check of
    # the canonical reduction, using an alternative tabulation order.
    full_covered = sum(any(compatible(w, p) for p in chosen) for w in words)
    assert full_covered == 1641

    # Seven disjoint neighborhood sets force at least seven permutations.
    # There are exactly 17 classes under permutation inversion.
    used = set()
    for spelling, expected in LOWER:
        w = tuple(int(c) for c in spelling)
        assert even(w)
        got = tuple(code(p) for p in REPS if compatible(w, p))
        assert got == expected, ('unexpected neighbor class', spelling, got, expected)
        assert used.isdisjoint(got), ('overlapping neighbor classes', spelling)
        used.update(got)
        # Symmetry premise: replacing a permutation by its inverse never
        # changes compatibility. Check the claim on these hard instances.
        for p in ALL_PERMS:
            assert compatible(w, p) == compatible(w, inverse(p))
    assert len(used) == 15  # seven disjoint groups
    print('VERIFY_OK k=3 n=4 m=7 even_words=1641 canonical=274 inversion_classes=17 lower_witnesses=7')


if __name__ == '__main__':
    main()
