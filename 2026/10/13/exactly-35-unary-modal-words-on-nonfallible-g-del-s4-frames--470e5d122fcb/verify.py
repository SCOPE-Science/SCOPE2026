#!/usr/bin/env python3
"""Exact modal-word census and four-world separation certificate."""
from itertools import product
from collections import defaultdict

PURE = ('', 'B', 'D', 'BD', 'DB', 'BDB', 'DBD')
CLASSICAL = PURE + tuple('N' + w for w in PURE)
CANDIDATES = PURE + tuple(a + 'N' + b for a in CLASSICAL for b in PURE)
REPS = ('', 'B', 'D', 'N', 'BD', 'BN', 'DB', 'DN', 'NB', 'NN', 'BDB',
        'BDN', 'BNB', 'DBD', 'DBN', 'NBD', 'NBN', 'NDN', 'NNB',
        'BDBN', 'BNBD', 'DBDN', 'DBNB', 'NBDB', 'NBDN', 'NBNB',
        'NDBN', 'NNBD', 'DBNBD', 'NBDBN', 'NBNBD', 'NDBDN',
        'NDBNB', 'NNBDB', 'NDBNBD')
# Word equations are interpreted on all nonfallible locally linear
# backward-, forward-, downward-confluent S4 birelational models.
AXIOMS = (('BB', 'B'), ('DD', 'D'), ('BDBD', 'BD'), ('DBDB', 'DB'),
          ('NNN', 'N'), ('BN', 'ND'), ('DNB', 'NB'))
# Each bit set in row i denotes an immediate successor of world i.
FRAMES = (
    ((3, 2, 4, 8), (1, 2, 15, 8)),
    ((3, 2, 4, 8), (1, 3, 12, 12)),
)

def elements(mask, n):
    return [i for i in range(n) if mask & (1 << i)]

def preorder(rows):
    n = len(rows)
    return all((rows[i] & (1 << i)) and
               all(not(rows[i] & (1 << j)) or (rows[i] | rows[j]) == rows[i]
                   for j in range(n)) for i in range(n))

def local_linear(p):
    n = len(p)
    return all(not ((p[i] >> j) & 1 and (p[i] >> k) & 1) or
               ((p[j] >> k) & 1) or ((p[k] >> j) & 1)
               for i in range(n) for j in range(n) for k in range(n))

def confluence(p, r):
    n = len(p)
    for w in range(n):
        for v in range(n):
            if r[w] & (1 << v):
                for wp in elements(p[w], n):
                    if not any((r[wp] & (1 << vp)) for vp in elements(p[v], n)):
                        return False  # forward
                for vp in elements(p[v], n):
                    if not any((r[wp] & (1 << vp)) for wp in elements(p[w], n)):
                        return False  # backward
            if p[w] & (1 << v):
                for vp in elements(r[v], n):
                    if not any(p[up] & (1 << vp) for up in elements(r[w], n)):
                        return False  # downward
    return True

def upset(p, s):
    return all(not (s & (1 << i)) or (s & p[i]) == p[i]
               for i in range(len(p)))

def apply(p, r, op, s):
    n = len(p)
    if op == 'N':
        return sum(1 << i for i in range(n)
                   if all(not(s & (1 << v)) for v in elements(p[i], n)))
    if op == 'B':
        return sum(1 << i for i in range(n)
                   if all(s & (1 << u) for v in elements(p[i], n)
                          for u in elements(r[v], n)))
    if op == 'D':
        return sum(1 << i for i in range(n)
                   if all(any(s & (1 << u) for u in elements(r[v], n))
                          for v in elements(p[i], n)))
    raise ValueError(op)

def evaluate(p, r, word, val):
    for op in reversed(word):
        val = apply(p, r, op, val)
    return val

def upper_normal_forms():
    # Each edge is an instance of one of the seven proved operator identities
    # with arbitrary outer and inner contexts. The 105 Pacheco representatives
    # lie in the finite length-10 congruence graph.
    words = [''.join(p) for k in range(11) for p in product('BND', repeat=k)]
    index = {s: i for i, s in enumerate(words)}
    parent = list(range(len(words)))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
    for w, i in index.items():
        for a, b in AXIOMS:
            start = 0
            while True:
                at = w.find(a, start)
                if at < 0:
                    break
                new = w[:at] + b + w[at + len(a):]
                if new in index:
                    union(i, index[new])
                start = at + 1
    roots = {find(index[w]) for w in CANDIDATES}
    assert len(CANDIDATES) == 105 and len(roots) == 35
    assert {find(index[w]) for w in REPS} == roots
    return len(roots)

def lower_witnesses():
    signatures = {w: [] for w in REPS}
    total_upsets = 0
    for p, r in FRAMES:
        assert preorder(p) and preorder(r)
        assert local_linear(p) and confluence(p, r)
        n = len(p)
        vals = [v for v in range(1 << n) if upset(p, v)]
        assert len(vals) == 12
        total_upsets += len(vals)
        for w in REPS:
            signatures[w].extend(evaluate(p, r, w, v) for v in vals)
        # Verify saturation and that finite semantics preserve persistence.
        for v in vals:
            for op in 'BND':
                assert upset(p, apply(p, r, op, v))
    assert len({tuple(v) for v in signatures.values()}) == 35
    assert total_upsets == 24
    return len(signatures), total_upsets

if __name__ == '__main__':
    upper = upper_normal_forms()
    lower, _ = lower_witnesses()
    assert upper == lower == 35
    print('UPPER_NORMAL_FORMS=35')
    print('FINITE_WITNESSES=35')
    print('VERIFY_OK')
