"""Independent finite chain-complex calculation for the cuboctahedral graph.
Only Python 3 standard library is needed.
"""
from collections import defaultdict
from itertools import combinations

# Encode each of the 12 cube edges as an unordered pair of 3-bit words.
raw_edges = sorted((a, a ^ (1 << j)) for a in range(8)
                   for j in range(3) if a < (a ^ (1 << j)))
assert len(raw_edges) == 12
# An edge of the cuboctahedron joins two incident cube-edge labels.
poly_edges = sorted((i, j) for i in range(12) for j in range(i + 1, 12)
                    if len(set(raw_edges[i] + raw_edges[j])) == 3)
assert len(poly_edges) == 24

# Unlike the first verifier, enumerate faces by testing each combination
# of graph edges for pairwise vertex-disjointness.
by_dim = {}
for k in range(1, 7):
    by_dim[k - 1] = [face for face in combinations(range(24), k)
                    if len({v for i in face for v in poly_edges[i]}) == 2 * k]
expected = [24, 204, 744, 1116, 528, 32]
assert [len(by_dim[d]) for d in range(6)] == expected

# A column of a mod-2 boundary matrix is represented as a Python integer.
def rank_mod2(columns):
    basis = {}
    for col in columns:
        while col:
            bit = col.bit_length() - 1
            if bit in basis:
                col ^= basis[bit]
            else:
                basis[bit] = col
                break
    return len(basis)

ranks = []
for k in range(1, 6):
    prev = {face: pos for pos, face in enumerate(by_dim[k - 1])}
    cols = []
    for high in by_dim[k]:
        col = 0
        for j in range(k + 1):
            low = high[:j] + high[j + 1:]
            col ^= 1 << prev[low]
        cols.append(col)
    ranks.append(rank_mod2(cols))
assert ranks == [23, 181, 563, 496, 32], ranks
betti = [expected[0] - ranks[0] - 1]
for d in range(1, 5):
    betti.append(expected[d] - ranks[d - 1] - ranks[d])
betti.append(expected[5] - ranks[4])
assert betti == [0, 0, 0, 57, 0, 0], betti
print('VERIFY_OK independent_enumeration=true fvector=' + ','.join(map(str, expected))
      + ' ranks=' + ','.join(map(str, ranks))
      + ' reduced_betti=' + ','.join(map(str, betti)))
