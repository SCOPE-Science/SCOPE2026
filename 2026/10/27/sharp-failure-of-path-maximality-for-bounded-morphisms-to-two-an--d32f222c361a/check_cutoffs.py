"""Check the first path-maximality cutoffs by exhaustive direct enumeration."""
from itertools import product


def shapes(n):
    out = {}
    for parents in product(*(range(i) for i in range(1, n))):
        children = [[] for _ in range(n)]
        for i, p in enumerate(parents, 1):
            children[p].append(i)
        enc = [None] * n
        for i in reversed(range(n)):
            enc[i] = '(' + ''.join(sorted(enc[c] for c in children[i])) + ')'
        out.setdefault(enc[0], parents)
    return out


def count_maps(n, parents, q):
    desc = [1 << i for i in range(n)]
    for i in reversed(range(1, n)):
        desc[parents[i-1]] |= desc[i]
    total = 0
    for values in product(range(q), repeat=n):
        labels = [0] * q
        for i, v in enumerate(values):
            labels[v] |= 1 << i
        if all(not any(d & labels[a] for a in range(v))
               and all(d & labels[a] for a in range(v, q))
               for d, v in zip(desc, values)):
            total += 1
    return total


def path(n):
    return '(' * n + ')' * n


data = []
for n in range(1, 8):
    reps = shapes(n)
    row = []
    for q in (2, 3):
        scores = {s: count_maps(n, p, q) for s, p in reps.items()}
        m = max(scores.values())
        row.append((m, [s for s, count in scores.items() if count == m]))
    data.append((row[0][0], row[1][0]))
    if n == 6:
        assert row[0] == (7, ['(' + ''.join(sorted((path(2), path(3)))) + ')'])
    if n == 7:
        assert row[1] == (25, ['(' + path(3)*2 + ')'])
    print(n, len(reps), row)
assert data == [(1,1),(2,2),(3,4),(4,7),(5,11),(7,16),(10,25)]
