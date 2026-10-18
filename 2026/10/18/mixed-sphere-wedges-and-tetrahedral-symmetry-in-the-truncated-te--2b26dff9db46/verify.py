"""Exact finite chain and symmetry verification for a higher-independence complex.

Python 3 standard library only. All integer chain calculations are exact.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import permutations
import json

V = [(u, v) for u in range(4) for v in range(4) if v != u]
ID = {v: i for i, v in enumerate(V)}
EDGES = [(i, j) for i, (a, b) in enumerate(V)
         for j, (c, d) in enumerate(V) if i < j and
         (a == c or (a == d and b == c))]
N = len(V)
ADJ = [0] * N
for i, j in EDGES:
    ADJ[i] |= 1 << j
    ADJ[j] |= 1 << i
FACES = {s for s in range(1, 1 << N)
         if all(not (s & (1 << v)) or (ADJ[v] & s).bit_count() <= 1
                for v in range(N))}
ORDER = (1, 7, 10, 0, 6, 11, 4, 5, 2, 8, 9, 3)


def boundaries(s):
    b = [v for v in range(N) if s & (1 << v)]
    return [(s ^ (1 << v), -1 if k & 1 else 1)
            for k, v in enumerate(b) if s ^ (1 << v)]


def add(target, key, value):
    target[key] += value
    if target[key] == 0:
        del target[key]


remaining = set(FACES)
pairs = []
for v in ORDER:
    for s in sorted(remaining):
        if s & (1 << v):
            continue
        t = s | (1 << v)
        if t in remaining:
            pairs.append((s, t))
            remaining.remove(s)
            remaining.remove(t)
CRITICAL = remaining
LOW = dict(pairs)
UP = {t: s for s, t in pairs}

# Independently verify that the directed matching graph is acyclic.
deg = {s: 0 for s in FACES}
out = {s: [] for s in FACES}
covers = 0
for s in FACES:
    for t, _ in boundaries(s):
        covers += 1
        if LOW.get(t) == s:
            a, b = s, t
        else:
            a, b = t, s
        out[a].append(b)
        deg[b] += 1
q = deque(s for s in FACES if deg[s] == 0)
visited = 0
while q:
    s = q.popleft()
    visited += 1
    for t in out[s]:
        deg[t] -= 1
        if deg[t] == 0:
            q.append(t)
assert visited == len(FACES)
assert not (set(LOW) & set(UP))
assert len(pairs) * 2 + len(CRITICAL) == len(FACES)

# Integral algebraic-Morse projection: recursively eliminate lower matched cells.
@lru_cache(None)
def proj(s):
    if s in CRITICAL:
        return {s: 1}
    if s in UP:
        return {}
    t = LOW[s]
    eps = dict(boundaries(t))[s]
    ans = defaultdict(int)
    for u, sg in boundaries(t):
        if u != s:
            for c, a in proj(u).items():
                add(ans, c, -eps * sg * a)
    return dict(ans)


@lru_cache(None)
def lift_homotopy(s):
    if s not in LOW:
        return {}
    t = LOW[s]
    eps = dict(boundaries(t))[s]
    ans = defaultdict(int)
    add(ans, t, eps)
    for u, sg in boundaries(t):
        if u != s:
            for z, a in lift_homotopy(u).items():
                add(ans, z, -eps * sg * a)
    return dict(ans)


def chain_boundary(chain):
    out = defaultdict(int)
    for s, a in chain.items():
        for u, sg in boundaries(s):
            add(out, u, a * sg)
    return dict(out)


def project_chain(chain):
    out = defaultdict(int)
    for s, a in chain.items():
        for u, b in proj(s).items():
            add(out, u, a * b)
    return dict(out)


def lift(s):
    out = defaultdict(int, {s: 1})
    for f, sg in boundaries(s):
        for t, a in lift_homotopy(f).items():
            add(out, t, -sg * a)
    return dict(out)


crit = {dim: sorted(s for s in CRITICAL if s.bit_count() == dim + 1)
        for dim in (0, 3, 4)}
assert {d: len(xs) for d, xs in crit.items()} == {0: 1, 3: 3, 4: 3}
assert len(CRITICAL) == 7
morse_boundary = {}
cycles = {}
for dim in (3, 4):
    for s in crit[dim]:
        morse_boundary[s] = project_chain(dict(boundaries(s)))
        assert morse_boundary[s] == {}
        cycles[s] = lift(s)
        assert chain_boundary(cycles[s]) == {}
        assert project_chain(cycles[s]) == {s: 1}


def permute_simplex(s, p):
    vertex_images = [ID[(p[u], p[v])] for k, (u, v) in enumerate(V)
                     if s & (1 << k)]
    sign = (-1) ** sum(vertex_images[i] > vertex_images[j]
                       for i in range(len(vertex_images))
                       for j in range(i + 1, len(vertex_images)))
    return sum(1 << i for i in vertex_images), sign


def mat_mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


PERMS = list(permutations(range(4)))
reps = {3: {}, 4: {}}
chars = {3: {}, 4: {}}
lefschetz_tests = 0
for p in PERMS:
    for dim in (3, 4):
        base = crit[dim]
        M = [[0] * len(base) for _ in base]
        for j, s in enumerate(base):
            transformed = defaultdict(int)
            for t, coeff in cycles[s].items():
                image, sign = permute_simplex(t, p)
                add(transformed, image, sign * coeff)
            projected = project_chain(transformed)
            for i, z in enumerate(base):
                M[i][j] = projected.get(z, 0)
        reps[dim][p] = M
        chars[dim][p] = sum(M[i][i] for i in range(len(M)))
    # Check a separate signed simplicial Lefschetz trace at chain level.
    L = 0
    for s in FACES:
        t, sign = permute_simplex(s, p)
        if s == t:
            L += (-1) ** (s.bit_count() - 1) * sign
    assert L == 1 - chars[3][p] + chars[4][p]
    lefschetz_tests += 1
for p in PERMS:
    for q in PERMS:
        composite = tuple(p[q[i]] for i in range(4))
        for dim in (3, 4):
            assert mat_mul(reps[dim][p], reps[dim][q]) == reps[dim][composite]


def partition(p):
    remaining = set(range(4))
    lengths = []
    while remaining:
        x = min(remaining)
        y = x
        count = 0
        while y in remaining:
            remaining.remove(y)
            count += 1
            y = p[y]
        lengths.append(count)
    return tuple(sorted(lengths, reverse=True))


character_table = {}
for p in PERMS:
    typ = str(partition(p))
    val = [chars[3][p], chars[4][p]]
    if typ in character_table:
        assert character_table[typ] == val
    else:
        character_table[typ] = val
assert character_table == {
    '(1, 1, 1, 1)': [3, 3],
    '(2, 1, 1)': [-1, -1],
    '(2, 2)': [3, -1],
    '(3, 1)': [0, 0],
    '(4,)': [-1, 1],
}

# Independent mod-two ranks of the original simplicial boundary operators.
by_dimension = {k: sorted(s for s in FACES if s.bit_count() - 1 == k)
                for k in range(6)}
ranks = {}
for k in range(1, 6):
    basis = {s: i for i, s in enumerate(by_dimension[k - 1])}
    pivots = {}
    for s in by_dimension[k]:
        column = 0
        for t, _ in boundaries(s):
            column ^= 1 << basis[t]
        while column:
            j = column.bit_length() - 1
            if j in pivots:
                column ^= pivots[j]
            else:
                pivots[j] = column
                break
    ranks[k] = len(pivots)
ranks[0] = 0
ranks[6] = 0
bettis = {k: len(by_dimension[k]) - ranks[k] - ranks[k + 1]
          for k in by_dimension}
assert bettis == {0: 1, 1: 0, 2: 0, 3: 3, 4: 3, 5: 0}
assert len(V) == 12 and len(EDGES) == 18

result = {
    'graph_vertices': len(V), 'graph_edges': len(EDGES),
    'simplices_nonempty': len(FACES),
    'simplicial_fvector': [len(by_dimension[d]) for d in range(6)],
    'matching_pairs': len(pairs),
    'hasse_cover_relations': covers,
    'acyclic_toposort_nodes': visited,
    'critical_cells': {str(k): len(v) for k, v in crit.items()},
    'critical_cell_masks': {str(k): [format(s, '03x') for s in v]
                            for k, v in crit.items()},
    'exact_morse_differential': 'zero in all degrees',
    'cycle_lift_term_counts': {str(k): [len(cycles[s]) for s in crit[k]]
                               for k in (3, 4)},
    'mod2_boundary_ranks': {str(k): ranks[k] for k in range(1, 6)},
    'mod2_betti_numbers': {str(k): bettis[k] for k in bettis},
    's4_character_3_4_by_cycle_type': dict(sorted(character_table.items())),
    'lefschetz_checks': lefschetz_tests,
    'representation_composition_checks': len(PERMS) ** 2 * 2,
    'all_assertions_passed': True,
}
print(json.dumps(result, sort_keys=True, indent=2))
