#!/usr/bin/env python3
"""Exact verifier for the ternary length-four single-deletion classification."""
from itertools import product, permutations
import json
from pathlib import Path

Q = tuple(range(3))
WORDS = list(product(Q, repeat=4))
INDEX = {w: i for i, w in enumerate(WORDS)}
TRIPLES = list(product(Q, repeat=3))
TINDEX = {w: i for i, w in enumerate(TRIPLES)}

def deletion_mask(w):
    mask = 0
    for i in range(4):
        u = w[:i] + w[i+1:]
        mask |= 1 << TINDEX[u]
    return mask

DMASK = [deletion_mask(w) for w in WORDS]
ADJ = []
for i in range(len(WORDS)):
    m = 0
    for j in range(len(WORDS)):
        if i != j and (DMASK[i] & DMASK[j]) == 0:
            m |= 1 << j
    ADJ.append(m)

# This recursion lists each target-size clique exactly once: after choosing
# vertex v, only currently later candidates compatible with v remain.
def enumerate_target(target):
    solutions = []
    nodes = 0
    def rec(P, chosen):
        nonlocal nodes
        nodes += 1
        need = target - len(chosen)
        if need == 0:
            solutions.append(tuple(chosen))
            return
        if P.bit_count() < need:
            return
        while P:
            if P.bit_count() < need:
                return
            b = P & -P
            v = b.bit_length() - 1
            P ^= b
            rec(P & ADJ[v], chosen + [v])
    rec((1 << len(WORDS)) - 1, [])
    return solutions, nodes

sol11, nodes11 = enumerate_target(11)
sol12, nodes12 = enumerate_target(12)
assert len(sol11) == 6
assert len(sol12) == 0

codes = [frozenset(WORDS[i] for i in s) for s in sol11]
cover_sizes = []
for C in codes:
    assert len(C) == 11
    seen = 0
    for w in C:
        assert seen & DMASK[INDEX[w]] == 0
        seen |= DMASK[INDEX[w]]
    cover_sizes.append(seen.bit_count())
assert set(cover_sizes) == {23}

K = frozenset(
    [(a,a,a,a) for a in Q]
    + [(a,a,b,b) for a in Q for b in Q if a != b]
)
R = frozenset(
    (a,b,c,a) for a,b,c in permutations(Q)
)
assert len(K) == 9 and len(R) == 6
assert all(K <= C and C - K <= R and len(C-K) == 2 for C in codes)

pairs = sorted(
    [tuple(sorted(''.join(map(str,w)) for w in (C-K))) for C in codes]
)
expected_pairs = sorted([
    ('0120','1021'), ('0120','2102'), ('0210','1201'),
    ('0210','2012'), ('1021','2012'), ('1201','2102')
])
assert pairs == expected_pairs

# The six remainder words themselves have compatibility graph C6.
r_words = sorted(R)
r_edges = set()
for i,u in enumerate(r_words):
    for v in r_words[i+1:]:
        if DMASK[INDEX[u]] & DMASK[INDEX[v]] == 0:
            r_edges.add(tuple(sorted((''.join(map(str,u)), ''.join(map(str,v))))))
assert r_edges == set(expected_pairs)
deg = {''.join(map(str,w)): 0 for w in r_words}
for a,b in r_edges:
    deg[a] += 1; deg[b] += 1
assert set(deg.values()) == {2} and len(r_edges) == 6

# Natural channel symmetries: one global alphabet permutation, optionally
# followed by reversal of coordinate order.
def transform(C, p, reverse):
    out = set()
    for w in C:
        u = tuple(p[x] for x in w)
        if reverse:
            u = u[::-1]
        out.add(u)
    return frozenset(out)

group_images = []
rep = codes[0]
for p in permutations(Q):
    for reverse in (False, True):
        group_images.append(transform(rep, p, reverse))
orbit = set(group_images)
assert orbit == set(codes)
stabilizer = sum(1 for C in group_images if C == rep)
assert len(orbit) == 6 and stabilizer == 2

# Cross-check the embedded classification data rather than trusting stdout.
data_path = Path(__file__).with_name('max_codes.json')
data = json.loads(data_path.read_text(encoding='utf-8'))
listed = {frozenset(tuple(map(int,w)) for w in C) for C in data['maximum_codes']}
assert listed == set(codes)
assert data['maximum_size'] == 11
assert data['labeled_maximum_count'] == 6
assert data['orbit_count'] == 1
assert data['orbit_size'] == 6
assert data['stabilizer_order'] == 2

print(
    'VERIFY_OK maximum=11 labeled_maxima=6 orbits=1 orbit_size=6 '
    f'stabilizer=2 nodes11={nodes11} nodes12={nodes12}'
)
