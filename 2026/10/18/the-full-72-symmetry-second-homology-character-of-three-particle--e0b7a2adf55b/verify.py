#!/usr/bin/env python3
"""Self-contained exact cubical and character checks for three points on K(3,3)."""
import itertools
from collections import defaultdict
from fractions import Fraction

P = list(itertools.permutations(range(3)))
ORIGINAL_EDGES = [(i, 3 + j) for i in range(3) for j in range(3)]
V = list(range(15))
E = []
for k, (a, b) in enumerate(ORIGINAL_EDGES):
    E.extend(((a, 6 + k), (6 + k, b)))
EDGE_INDEX = {frozenset(e): k for k, e in enumerate(E)}
C = []
for d in range(4):
    cells = []
    for es in itertools.combinations(range(18), d):
        ends = set(v for e in es for v in E[e])
        if len(ends) != 2 * d:
            continue
        for vs in itertools.combinations(sorted(set(V) - ends), 3 - d):
            cells.append((es, vs))
    C.append(cells)
assert [len(c) for c in C] == [455, 1404, 1386, 432]
INDEX = [{cell: i for i, cell in enumerate(cs)} for cs in C]
B = [None]
for d in range(1, 4):
    cols = []
    for es, vs in C[d]:
        col = {}
        for j, e in enumerate(es):
            for k, endpoint in enumerate(E[e]):
                k0 = INDEX[d - 1][(es[:j] + es[j + 1:], tuple(sorted(vs + (endpoint,))))]
                col[k0] = col.get(k0, 0) + (-1 if (j + k) % 2 == 0 else 1)
        assert all(col.values())
        cols.append(col)
    B.append(cols)
for d in (2, 3):
    for col in B[d]:
        total = defaultdict(int)
        for row, a in col.items():
            for lower, b in B[d - 1][row].items():
                total[lower] += a * b
        assert not any(total.values())

def rank_mod2(columns):
    basis = {}
    for col in columns:
        v = sum(1 << i for i, coeff in col.items() if coeff & 1)
        while v:
            pivot = v.bit_length() - 1
            if pivot not in basis:
                basis[pivot] = v
                break
            v ^= basis[pivot]
    return len(basis)

def rank_mod3(columns):
    basis = {}
    for col in columns:
        v = {i: a % 3 for i, a in col.items() if a % 3}
        while v:
            pivot = min(v)
            if pivot not in basis:
                inv = pow(v[pivot], -1, 3)
                basis[pivot] = {i: (a * inv) % 3 for i, a in v.items()}
                break
            factor = v[pivot]
            for i, a in basis[pivot].items():
                new = (v.get(i, 0) - factor * a) % 3
                if new: v[i] = new
                elif i in v: del v[i]
    return len(basis)

r1, r2, r3 = rank_mod2(B[1]), rank_mod3(B[2]), rank_mod2(B[3])
assert (r1, r2, r3) == (454, 946, 432)
# Connectedness makes rank(d1)=454 over Q.  The four graph cycles
# (L0,R0,Li,Rj,L0), for 1<=i,j<=2, can be traversed with two
# particles parked at the two original vertices outside the square.
# Their images under the forgetful total-motion map to H1(K3,3;Q)
# form a basis (one unique non-tree edge (Li,Rj) per cycle).
# Hence b1>=4.  On the other hand mod 3 rank(d2)>=946, so
# b1<=1404-454-946=4.  Thus b1=4 and rank_Q(d2)=946.
assert len(C[1]) - r1 - r2 == 4
assert len(C[2]) - r2 - r3 == 8

def sign(p):
    return (-1) ** sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))

def std(p): return sum(p[i] == i for i in range(3)) - 1

def compose(p, q): return tuple(p[q[i]] for i in range(3))

def vertex_map(p, q, sw):
    if sw: m = [3 + p[i] for i in range(3)] + [q[j] for j in range(3)]
    else: m = [p[i] for i in range(3)] + [3 + q[j] for j in range(3)]
    for a, b in ORIGINAL_EDGES:
        x, y = m[a], m[b]
        l, r = (x, y) if x < 3 else (y, x)
        m.append(6 + ORIGINAL_EDGES.index((l, r)))
    return m

def traces(p, q, sw):
    vm = vertex_map(p, q, sw)
    em = []
    orient = []
    for a, b in E:
        mapped = (vm[a], vm[b])
        j = EDGE_INDEX[frozenset(mapped)]
        em.append(j)
        orient.append(1 if E[j] == mapped else -1)
    cell_traces = []
    for d in range(4):
        total = 0
        for es, vs in C[d]:
            mapped_es = [em[e] for e in es]
            if tuple(sorted(mapped_es)) != es or tuple(sorted(vm[v] for v in vs)) != vs:
                continue
            total += sign(mapped_es) * __import__('math').prod(orient[e] for e in es)
        cell_traces.append(total)
    lefschetz = sum((-1) ** i * x for i, x in enumerate(cell_traces))
    fixed_v = sum(vm[x] == x for x in range(6))
    fixed_signed_e = sum((1 if not sw else -1) for a, b in ORIGINAL_EDGES if {vm[a], vm[b]} == {a, b})
    h1 = fixed_signed_e - fixed_v + 1
    return cell_traces, lefschetz, h1, lefschetz - 1 + h1

def typ(p):
    visited = set()
    types = []
    for start in range(3):
        if start in visited: continue
        j = start; n = 0
        while j not in visited:
            visited.add(j); n += 1; j = p[j]
        types.append(n)
    return tuple(sorted(types))

classes = defaultdict(list)
inner = defaultdict(int)
for p, q, sw in itertools.product(P, P, (0, 1)):
    c, L, h1, h2 = traces(p, q, sw)
    predicted = -std(compose(p, q)) if sw else std(p) * std(q) + sign(p) * std(q) + std(p) * sign(q)
    assert h2 == predicted, (p, q, sw, h2, predicted)
    if sw: key = ('swap', typ(compose(p, q)))
    else: key = ('preserve', tuple(sorted((typ(p), typ(q)))))
    classes[key].append(h2)
    for a in ('T', 'S', 'V'):
        f = {'T': lambda _: 1, 'S': sign, 'V': std}[a]
        for eps in (1, -1):
            irr = eps * f(compose(p, q)) if sw else f(p) * f(q)
            inner[(a, eps)] += irr * h2
    for a, b in (('T', 'S'), ('T', 'V'), ('S', 'V')):
        funcs = {'T': lambda _: 1, 'S': sign, 'V': std}
        f, h = funcs[a], funcs[b]
        irr = 0 if sw else f(p) * h(q) + h(p) * f(q)
        inner[(a, b)] += irr * h2
assert len(classes) == 9
expected = {
    ('preserve', ((1, 1, 1), (1, 1, 1))): (1, 8),
    ('preserve', ((1, 1, 1), (1, 2))): (6, -2),
    ('preserve', ((1, 1, 1), (3,))): (4, -1),
    ('preserve', ((1, 2), (1, 2))): (9, 0),
    ('preserve', ((1, 2), (3,))): (12, 1),
    ('preserve', ((3,), (3,))): (4, -1),
    ('swap', (1, 1, 1)): (6, -2),
    ('swap', (1, 2)): (18, 0),
    ('swap', (3,)): (12, 1),
}
assert {k: (len(v), v[0]) for k, v in classes.items()} == expected
assert all(len(set(v)) == 1 for v in classes.values())
mult = {k: Fraction(n, 72) for k, n in inner.items()}
assert mult[('V', -1)] == 1 and mult[('S', 'V')] == 1
assert all(v == 0 for k, v in mult.items() if k not in (('V', -1), ('S', 'V')))
print('PASS: cells', [len(c) for c in C], 'boundary square zero; modular ranks', (r1, r2, r3))
print('PASS: rational Betti vector (1,4,8,0); all 72 signed cellular traces')
print('PASS: nine classes', sorted(expected.items(), key=str))
print('PASS: 2 irreducible Q representations of dimension 4, each once; no invariant class')
