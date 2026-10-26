"""Exact FO quantifier-rank-three census for finite equivalence relations.

The input profiles exhaust class multiplicities 0,1,2,>=3 in each of
three class-size categories 1,2,>=3. The quotient by this profile reduction
is established mathematically, not inferred from these calculations.
"""
from functools import lru_cache
from itertools import product
from pathlib import Path
import csv

P = [p for p in product(range(4), repeat=3) if any(p)]


def carrier(p):
    labels = []
    c = 0
    for sz, count in enumerate(p, 1):
        for _ in range(count):
            labels.extend([c] * sz)
            c += 1
    return tuple(labels)


C = {p: carrier(p) for p in P}


@lru_cache(None)
def tp(p, a, r):
    c = C[p]
    atoms = tuple((int(a[i] == a[j]), int(c[a[i]] == c[a[j]]))
                  for i in range(len(a)) for j in range(i))
    if r == 0:
        return (0, atoms)
    return (r, atoms, frozenset(tp(p, a + (v,), r - 1)
                                for v in range(len(c))))


groups = {}
for p in P:
    groups.setdefault(tp(p, (), 3), []).append(p)

size = lambda p: sum(i * p[i - 1] for i in (1, 2, 3))
classes = sorted(groups.values(), key=lambda g: (min(size(p) for p in g),
                                                  min(g, key=lambda p:(size(p),p))))
assert len(P) == 63
assert len(classes) == 21
assert max(min(size(p) for p in g) for g in classes) == 9
rows = []
for index, group in enumerate(classes, 1):
    rep = min(group, key=lambda p: (size(p), p))
    for p in group:
        rows.append((p, index, rep, size(rep)))
rows.sort()
with (Path(__file__).parent / 'rank3_classes.csv').open(newline='', encoding='utf-8') as f:
    actual = list(csv.DictReader(f))
expected = [{'n1':str(p[0]),'n2':str(p[1]),'n3plus':str(p[2]),
             'type':str(i),'representative':'.'.join(map(str,rep)),
             'representative_order':str(n)} for p,i,rep,n in rows]
assert actual == expected, 'The 63-profile classification table differs.'
print('PASS: 63 profiles, 21 rank-three types, sharp representative ceiling 9')
print('Representative orders:', sorted(set(n for _,_,_,n in rows)))
