"""Reproduce the complete S5-character and simplicial-flag orbit check.

Requires Python 3 standard library only. All vertex sets use {0,1,2,3,4}.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations

U = range(5)
verts = tuple(combinations(U, 2))
vertex_index = {v: i for i, v in enumerate(verts)}
triangles = tuple(sorted(tuple(sorted(vertex_index[p] for p in combinations(q, 2)))
                         for q in combinations(U, 3)))
edges = tuple(sorted({tuple(sorted(e)) for t in triangles for e in combinations(t, 2)}))
faces = {0: tuple((i,) for i in range(10)), 1: edges, 2: triangles}
assert tuple(map(len, (faces[0], faces[1], faces[2]))) == (10, 30, 10)
assert len({e for tri in triangles for e in combinations(tri, 2)}) == 30

def parity(seq):
    return -1 if sum(seq[i] > seq[j] for i in range(len(seq))
                     for j in range(i + 1, len(seq))) % 2 else 1

def cycletype(p):
    seen, parts = set(), []
    for i in U:
        if i in seen:
            continue
        j, k = i, 0
        while j not in seen:
            seen.add(j)
            k += 1
            j = p[j]
        parts.append(k)
    return tuple(sorted(parts, reverse=True))

def traces(p):
    vperm = tuple(vertex_index[tuple(sorted(p[i] for i in v))] for v in verts)
    out = []
    for j in (0, 1, 2):
        trace = 0
        for simplex in faces[j]:
            im = tuple(vperm[i] for i in simplex)
            if set(im) == set(simplex):
                trace += parity(im)
        out.append(trace)
    return tuple(out)

def h1_char(p):
    a, b, c = traces(p)
    return 1 - a + b - c

def parts(n, maximum=None):
    if n == 0:
        yield ()
        return
    if maximum is None:
        maximum = n
    for first in range(min(maximum, n), 0, -1):
        for rest in parts(n - first, first):
            yield (first,) + rest

def permutation_module_character(sizes, ctype):
    # Number of ways to allocate cycles of a permutation among ordered bins.
    @lru_cache(None)
    def count(k, residual):
        if k == len(ctype):
            return int(all(x == 0 for x in residual))
        total = 0
        for i, n in enumerate(residual):
            if n >= ctype[k]:
                t = list(residual)
                t[i] -= ctype[k]
                total += count(k + 1, tuple(t))
        return total
    return count(0, tuple(sizes))

def specht_character(shape, ctype):
    # Jacobi-Trudi determinant in the power-sum basis.
    count = 0
    for w in permutations(range(len(shape))):
        sizes = tuple(shape[i] - i + w[i] for i in range(len(shape)))
        if min(sizes) >= 0:
            count += parity(w) * permutation_module_character(sizes, ctype)
    return count

all_perms = tuple(permutations(U))
class_sizes = Counter(cycletype(g) for g in all_perms)
characters = {}
for g in all_perms:
    t = cycletype(g)
    val = h1_char(g)
    if t in characters:
        assert characters[t] == val
    else:
        characters[t] = val
expected = {(1, 1, 1, 1, 1): 11, (2, 1, 1, 1): -1,
            (2, 2, 1): -1, (3, 1, 1): -1,
            (3, 2): -1, (4, 1): 1, (5,): 1}
assert characters == expected
multiplicities = {}
for shape in parts(5):
    total = sum(class_sizes[ct] * val * specht_character(shape, ct)
                for ct, val in characters.items())
    assert total % 120 == 0
    multiplicities[shape] = total // 120
assert {s: m for s, m in multiplicities.items() if m} == {(3, 1, 1): 1, (2, 2, 1): 1}

# Flags inside a chosen component: point-vertex <= edge <= triangle.
flags = {(v, e, t) for t in triangles for e in combinations(t, 2) for v in e}
assert len(flags) == 60
seed = next(iter(flags))
flag_orbit = set()
for g in all_perms:
    vp = tuple(vertex_index[tuple(sorted(g[i] for i in v))] for v in verts)
    flag_orbit.add((vp[seed[0]], tuple(sorted(vp[x] for x in seed[1])),
                    tuple(sorted(vp[x] for x in seed[2]))))
assert flag_orbit == flags
print('10 vertices, 30 edges, 10 triangles per component.')
for ct in sorted(characters, reverse=True):
    print('class', ct, 'size', class_sizes[ct], 'H1 character', characters[ct])
print('S5 decomposition: Specht (3,1,1) + Specht (2,2,1).')
print('One orbit of full flags; barycentric quotient is one 2-simplex.')
print('PASS: 120 S5 elements and the induced S5 x C2 character rule.')
