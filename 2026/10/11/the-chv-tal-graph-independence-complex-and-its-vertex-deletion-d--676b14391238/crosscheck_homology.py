"""Independent full boundary-rank check over F_2 for Chvatal deletion/link cases.

Run: python3 crosscheck_homology.py. Uses only the standard library.
This homology check corroborates, but does not replace, the Morse homotopy proof.
"""
from itertools import combinations
from collections import Counter

ADJACENCY = (
    (1, 4, 6, 9),
    (0, 2, 5, 7),
    (1, 3, 6, 8),
    (2, 4, 7, 9),
    (0, 3, 5, 8),
    (1, 4, 10, 11),
    (0, 2, 10, 11),
    (1, 3, 8, 11),
    (2, 4, 7, 10),
    (0, 3, 10, 11),
    (5, 6, 8, 9),
    (5, 6, 7, 9),
)
V = tuple(range(12))
assert all(len(x) == 4 for x in ADJACENCY)
assert all((a in ADJACENCY[b]) == (b in ADJACENCY[a]) for a in V for b in V)

def faces(excluded):
    allowed = sorted(set(V) - set(excluded))
    by_degree = {}
    for r in range(1, len(allowed) + 1):
        good = []
        for subset in combinations(allowed, r):
            if all(b not in ADJACENCY[a] for a, b in combinations(subset, 2)):
                good.append(subset)
        if good:
            by_degree[r - 1] = good
    return by_degree

def binary_rank(columns):
    pivots = {}
    for value in columns:
        x = value
        while x:
            b = x.bit_length() - 1
            if b not in pivots:
                pivots[b] = x
                break
            x ^= pivots[b]
    return len(pivots)

def betti(f):
    ranks = {0: 1} if f else {0: 0}
    for d in range(1, max(f) + 1):
        index = {x: i for i, x in enumerate(f[d - 1])}
        columns = []
        for face in f[d]:
            mask = 0
            for j in range(len(face)):
                mask ^= 1 << index[face[:j] + face[j+1:]]
            columns.append(mask)
        ranks[d] = binary_rank(columns)
    out = {}
    for d, cells in f.items():
        rank_in = ranks.get(d, 0)
        rank_next = ranks.get(d+1, 0)
        value = len(cells) - rank_in - rank_next
        assert value >= 0
        if value:
            out[d] = value
    return out

A = {0, 1, 4, 5}
full = faces(())
assert {d: len(v) for d, v in full.items()} == {0: 12, 1: 42, 2: 52, 3: 20}
assert betti(full) == {2: 1}
for v in V:
    deleted = faces((v,))
    linked = faces(set(ADJACENCY[v]) | {v})
    expect_delete = {} if v in A else {2: 1}
    expect_link = {1: 1} if v in A else {}
    assert betti(deleted) == expect_delete, (v, betti(deleted))
    assert betti(linked) == expect_link, (v, betti(linked))
    assert sum(len(xs) for xs in deleted.values()) == (99 if v in A else 98)
    assert sum(len(xs) for xs in linked.values()) == (26 if v in A else 27)
print('CHVATAL_MOD2_CROSSCHECK_OK',
      'full_beta2=1',
      'four_deletions_acyclic',
      'eight_deletions_beta2=1',
      'four_links_beta1=1',
      'eight_links_acyclic')
