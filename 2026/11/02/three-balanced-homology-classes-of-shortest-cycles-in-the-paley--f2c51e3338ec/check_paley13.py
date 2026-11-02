"""Exact, dependency-free certificate for short cycles in the Paley-13 torus.

All computations are finite and performed in GF(2). No floating point is used.
"""
from itertools import combinations
from collections import Counter

P = 13
R = {pow(a, 2, P) for a in range(1, P)}
V = range(P)
E = tuple((u, v) for u in V for v in range(u + 1, P) if (v - u) % P in R)
I = {e: j for j, e in enumerate(E)}
A = {u: set() for u in V}
for u, v in E:
    A[u].add(v)
    A[v].add(u)
T = tuple(t for t in combinations(V, 3) if all(e in I for e in combinations(t, 2)))
assert R == {1, 3, 4, 9, 10, 12} and (len(E), len(T)) == (39, 26)
assert all(len(A[u]) == 6 for u in V)
assert all(len(A[u] & A[v]) == (2 if v in A[u] else 3)
           for u in V for v in range(u + 1, P))
assert not any(all(tuple(sorted(e)) in I for e in combinations(q, 2))
               for q in combinations(V, 4))
# Every vertex link is a connected six-cycle, not just 2-regular.
for u in V:
    link = {v: A[v] & A[u] for v in A[u]}
    assert all(len(link[v]) == 2 for v in link)
    reached, todo = set(), [next(iter(link))]
    while todo:
        v = todo.pop()
        if v not in reached:
            reached.add(v)
            todo.extend(link[v] - reached)
    assert len(reached) == 6
assert all(sum(u in t for t in T) == 6 for u in V)
assert all(sum(set(e).issubset(t) for t in T) == 2 for e in E)


def edges(c):
    return tuple(tuple(sorted((c[j], c[(j + 1) % len(c)]))) for j in range(len(c)))


def parity(c, cochain):
    return sum(e in cochain for e in edges(c)) % 2


def canon(c):
    c = tuple(c)
    rev = c[::-1]
    return min(tuple(z[k:] + z[:k]) for z in (c, rev) for k in range(len(c)))


def act(c, a, b):
    return canon(tuple((a * u + b) % P for u in c))


def four_cycles():
    out = set()
    for a in V:
        for b in A[a]:
            for c in A[b] - {a}:
                for d in A[c] - {a, b}:
                    if d in A[a] and len({a, b, c, d}) == 4:
                        out.add(canon((a, b, c, d)))
    return out


C = four_cycles()
assert len(C) == 78
# A cochain is closed if its parity on every oriented two-simplex is zero.
co1 = {(2, 3), (2, 12), (3, 6), (6, 7), (7, 10), (7, 11), (8, 11), (11, 12)}
co2 = {(5, 9), (6, 9), (6, 10), (7, 10), (7, 11), (8, 9), (8, 11), (8, 12)}
assert co1 <= set(E) and co2 <= set(E)
assert all(parity(t, co1) == parity(t, co2) == 0 for t in T)
labels = {c: (parity(c, co1), parity(c, co2)) for c in C}
counts = Counter(labels.values())
assert counts == {(0, 0): 39, (1, 0): 13, (0, 1): 13, (1, 1): 13}

# Exact F2-rank of the simplicial 2-boundary, and hence H1 dimension.
def boundary(c):
    return sum(1 << I[e] for e in edges(c))

pivots = {}
for t in T:
    v = boundary(t)
    while v:
        j = v.bit_length() - 1
        if j in pivots:
            v ^= pivots[j]
        else:
            pivots[j] = v
            break
assert len(pivots) == 25
assert len(E) - (len(V) - 1) - len(pivots) == 2
# co1,co2 independent, so they provide a complete H1(F2) coordinate system.
assert labels[canon((0, 1, 2, 3))] == (1, 0)
assert labels[canon((0, 1, 5, 9))] == (0, 1)
assert labels[canon((0, 3, 6, 9))] == (1, 1)
assert labels[canon((0, 1, 4, 3))] == (0, 0)
# Every three-cycle is a two-simplex, so the nonzero minimum length is exactly 4.
tri_cycles = {canon(t) for t in T}
assert len(tri_cycles) == len(T)

n0 = canon((0, 1, 4, 3))
n1 = canon((0, 1, 2, 3))
orb0 = {act(n0, a, b) for a in R for b in V}
orb1 = {act(n1, a, b) for a in R for b in V}
assert len(orb0) == len(orb1) == 39
assert orb0.isdisjoint(orb1) and orb0 | orb1 == C
assert all(labels[c] == (0, 0) for c in orb0)
assert all(labels[c] != (0, 0) for c in orb1)
reps = ((0, 1, 2, 3), (0, 1, 5, 9), (0, 3, 6, 9))
trans_orbits = [{act(tuple(c), 1, b) for b in V} for c in reps]
assert all(len(o) == 13 for o in trans_orbits)
assert len(set.union(*trans_orbits)) == 39
assert set.union(*trans_orbits) == orb1
# 13 has no nontrivial image in GL_2(F2) of order 6;
# therefore translations fix each homology class.
print('PALEY13_FLAG_TORUS_SYSTOLE_EXACT_OK')
print('f=(13,39,26); rank(d2)=25; dim H1(F2)=2')
print('unoriented four_cycles=78; null=39; essential=39')
print('H1 labels (00,10,01,11):', tuple(counts[z] for z in ((0,0),(1,0),(0,1),(1,1))))
print('affine orbit sizes:', len(orb0), len(orb1))
print('essential translation orbit sizes:', tuple(len(o) for o in trans_orbits))
