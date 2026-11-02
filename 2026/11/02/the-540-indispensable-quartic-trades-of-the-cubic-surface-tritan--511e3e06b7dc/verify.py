"""Exact independent fiber census for the toric algebra of cubic-surface tritangents.
Requires only the Python 3 standard library; no external data."""
from collections import defaultdict, Counter
from itertools import combinations, combinations_with_replacement

# On the blowup of P2 in six points, index exceptional, two-point and
# five-point-conic (-1)-curves in this specified order.
names = ([('E', i) for i in range(6)]
         + [('L', i, j) for i, j in combinations(range(6), 2)]
         + [('Q', i) for i in range(6)])
index = {a: i for i, a in enumerate(names)}
assert len(names) == 27

def divisor(name):
    kind, *inds = name
    d = [0] * 7
    if kind == 'E':
        d[1 + inds[0]] = 1
    elif kind == 'L':
        d[0] = 1
        for i in inds:
            d[1 + i] = -1
    else:
        d[0] = 2
        for i in range(6):
            if i != inds[0]:
                d[1 + i] = -1
    return tuple(d)

classes = [divisor(name) for name in names]
T = []
for i in range(6):
    for j in range(6):
        if i != j:
            T.append(tuple(sorted((index['E', i],
                                   index['L', min(i, j), max(i, j)],
                                   index['Q', j]))))
for i, j in combinations(range(6), 2):
    rem = [v for v in range(6) if v not in (i, j)]
    for k, ell in combinations(rem, 2):
        rest = [v for v in rem if v not in (k, ell)]
        t = tuple(sorted((index['L', i, j], index['L', k, ell],
                          index['L', rest[0], rest[1]])))
        if t not in T:
            T.append(t)
assert len(T) == len(set(T)) == 45
anticanonical = (3, -1, -1, -1, -1, -1, -1)
for t in T:
    assert tuple(sum(classes[j][m] for j in t) for m in range(7)) == anticanonical

# Fibers are the exact 27-component exponent vectors of the line monomials.
def signature(monomial):
    vec = [0] * 27
    for t in monomial:
        for i in T[t]:
            vec[i] += 1
    return tuple(vec)

def fibers(degree):
    result = defaultdict(list)
    for mono in combinations_with_replacement(range(45), degree):
        result[signature(mono)].append(mono)
    return result

f2 = fibers(2)
assert len(f2) == 1035 and all(len(v) == 1 for v in f2.values())
f3 = fibers(3)
assert Counter(map(len, f3.values())) == {1: 15975, 2: 120}
rels3 = [tuple(v) for v in f3.values() if len(v) == 2]
assert len(rels3) == 120
f4 = fibers(4)
assert Counter(map(len, f4.values())) == {1: 182700, 2: 5940}
quartic = [tuple(v) for v in f4.values() if len(v) == 2]
primitive = [pair for pair in quartic if not set(pair[0]) & set(pair[1])]
nonprimitive = [pair for pair in quartic if set(pair[0]) & set(pair[1])]
assert len(primitive) == 540 and len(nonprimitive) == 5400
assert all(len(set(a)) == len(set(b)) == 4 for a, b in primitive)
assert all(len(set(a) & set(b)) == 1 for a, b in nonprimitive)
# Every nonprimitive relation comes from exactly one cubic relation times a variable.
lifts = set()
for a, b in rels3:
    for t in range(45):
        aa = tuple(sorted(a + (t,)))
        bb = tuple(sorted(b + (t,)))
        lifts.add(tuple(sorted((aa, bb))))
assert len(lifts) == 5400
assert lifts == {tuple(sorted(pair)) for pair in nonprimitive}

# Weyl group W(E6) simple reflections on Pic(S) classes.
root = [(1, -1, -1, -1, 0, 0, 0)]
for i in range(5):
    v = [0] * 7
    v[i + 1] = 1
    v[i + 2] = -1
    root.append(tuple(v))
class_index = {c: i for i, c in enumerate(classes)}
t_index = {t: i for i, t in enumerate(T)}
actions = []
for alpha in root:
    by_line = []
    for c in classes:
        product = c[0] * alpha[0] - sum(c[i] * alpha[i] for i in range(1, 7))
        reflected = tuple(c[i] + product * alpha[i] for i in range(7))
        by_line.append(class_index[reflected])
    image = tuple(t_index[tuple(sorted(by_line[i] for i in t))] for t in T)
    assert sorted(image) == list(range(45))
    actions.append(image)

primitive_pairs = {tuple(sorted(pair)) for pair in primitive}
seed = min(primitive_pairs)
seen = {seed}
queue = [seed]
for pair in queue:
    for action in actions:
        new = tuple(sorted(tuple(sorted(action[i] for i in side)) for side in pair))
        assert new in primitive_pairs
        if new not in seen:
            seen.add(new)
            queue.append(new)
assert len(seen) == 540 == len(primitive_pairs)

print('TRITANGENTS_OK: 27 (-1)-curves, 45 triples with anticanonical class')
print('CUBIC_OK: 120 two-monomial fibers, no degree-two relations')
print('QUARTIC_OK: 182700 singleton, 5940 doubleton fibers; 540 indispensable quartics')
print('LIFTS_OK: other 5400 quartic pairs are exactly cubic times variable')
print('WEYL_OK: all 540 indispensable quartics form one W(E6) orbit')
print('EXAMPLE_TUPLES:', seed)
