"""Independent three-round Spoiler--Duplicator minimax validation.

Checks that profiles grouped together admit a winning Duplicator strategy,
while all 21 class representatives are pairwise separable by Spoiler.
"""
import csv
from functools import lru_cache
from pathlib import Path
from itertools import product

P = [p for p in product(range(4), repeat=3) if any(p)]


def carrier(p):
    labels = []
    label = 0
    for size, multiplicity in enumerate(p, 1):
        for _ in range(multiplicity):
            labels += [label] * size
            label += 1
    return tuple(labels)

C = {p:carrier(p) for p in P}


@lru_cache(None)
def duplicator(a, b, ta=(), tb=(), left=3):
    A, B = C[a], C[b]
    for i in range(len(ta)):
        for j in range(i):
            if (ta[i] == ta[j]) != (tb[i] == tb[j]):
                return False
            if (A[ta[i]] == A[ta[j]]) != (B[tb[i]] == B[tb[j]]):
                return False
    if left == 0:
        return True
    for x in range(len(A)):
        if not any(duplicator(a, b, ta+(x,), tb+(y,), left-1)
                   for y in range(len(B))):
            return False
    for y in range(len(B)):
        if not any(duplicator(a, b, ta+(x,), tb+(y,), left-1)
                   for x in range(len(A))):
            return False
    return True

with (Path(__file__).parent / 'rank3_classes.csv').open(newline='',encoding='utf-8') as f:
    rows = list(csv.DictReader(f))
assert len(rows) == 63
classmap = {}
for row in rows:
    p = tuple(int(row[key]) for key in ('n1','n2','n3plus'))
    rep = tuple(int(x) for x in row['representative'].split('.'))
    classmap.setdefault(int(row['type']), (rep, []))[1].append(p)
reps = []
for index in sorted(classmap):
    representative, members = classmap[index]
    assert representative in members
    for p in members:
        assert duplicator(p, representative), ('false identification',p,representative)
    reps.append(representative)
assert len(reps) == 21 and len(set(reps)) == 21
for i, a in enumerate(reps):
    for b in reps[:i]:
        assert not duplicator(a,b), ('false separation',a,b)
print('PASS: 63 exact membership checks and 210 pairwise separation checks')
