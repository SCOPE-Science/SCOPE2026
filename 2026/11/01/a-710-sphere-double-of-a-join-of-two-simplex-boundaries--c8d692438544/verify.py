#!/usr/bin/env python3
"""Exact independent checks for D(partial Delta^3 * partial Delta^4).
Only Python standard library; execute python3 verify.py in this directory.
"""
from itertools import combinations, permutations
from collections import Counter, defaultdict, deque
from functools import lru_cache
from fractions import Fraction
import math
import csv
from pathlib import Path

A = tuple(range(4))
B = tuple(range(4, 9))
EDGES = tuple(combinations(range(9), 2))
EDGE_INDEX = {e: i for i, e in enumerate(EDGES)}


def permitted(edge_indices):
    used = set()
    for ei in edge_indices:
        e = EDGES[ei]
        if used.intersection(e):
            return False
        used.update(e)
    return not (set(A).issubset(used) or set(B).issubset(used))


def enumerate_faces():
    # Enumerator I: depth-first edge extension, checking endpoints directly.
    levels = [[], [], []]
    def extend(prefix, used, next_e):
        if prefix:
            levels[len(prefix) - 1].append(prefix)
        if len(prefix) == 3:
            return
        for j in range(next_e, len(EDGES)):
            e = EDGES[j]
            if e[0] in used or e[1] in used:
                continue
            updated = used | set(e)
            if set(A).issubset(updated) or set(B).issubset(updated):
                continue
            extend(prefix + (j,), updated, j + 1)
    extend((), set(), 0)
    return [sorted(layer) for layer in levels]


def independent_counts():
    # Enumerator II: iterate unordered edge families rather than recursive growth.
    counts = []
    for k in (1, 2, 3, 4):
        counts.append(sum(permitted(s) for s in combinations(range(36), k)))
    return tuple(counts)



def check_mod_two_boundary(levels):
    # Independent chain-matrix computation, not used to infer the integral homotopy.
    def rank(columns):
        pivots = {}
        for v in columns:
            while v:
                lead = v.bit_length() - 1
                if lead in pivots:
                    v ^= pivots[lead]
                else:
                    pivots[lead] = v
                    break
        return len(pivots)
    idx0 = {x: i for i, x in enumerate(levels[0])}
    idx1 = {x: i for i, x in enumerate(levels[1])}
    rank_d1 = rank(sum(1 << idx0[(v,)] for v in e) for e in levels[1])
    rank_d2 = rank(sum(1 << idx1[s[:j]+s[j+1:]] for j in range(3)) for s in levels[2])
    assert (rank_d1, rank_d2) == (35, 340)
    assert len(levels[1]) - rank_d1 - rank_d2 == 0
    assert len(levels[2]) - rank_d2 == 710
    return rank_d1, rank_d2


def build_morse(levels):
    allfaces = tuple(s for layer in levels for s in layer)
    face_id = {s: i for i, s in enumerate(allfaces)}
    remaining = set(range(len(allfaces)))
    matching = set()
    for vertex in range(36):
        for s in allfaces:
            if vertex in s:
                continue
            lo = face_id[s]
            if lo not in remaining:
                continue
            hi = face_id.get(tuple(sorted(s + (vertex,))))
            if hi is not None and hi in remaining:
                matching.add((lo, hi))
                remaining.remove(lo)
                remaining.remove(hi)
    assert 2 * len(matching) + len(remaining) == len(allfaces)
    dims = Counter(len(allfaces[i]) - 1 for i in remaining)
    assert dims == Counter({0: 1, 2: 710}), (dims, len(matching))
    graph = [[] for _ in allfaces]
    indeg = [0] * len(allfaces)
    incidences = 0
    for hi, s in enumerate(allfaces):
        for k in range(len(s)):
            lowface = s[:k] + s[k+1:]
            if not lowface:
                continue
            lo = face_id[lowface]
            u, v = (lo, hi) if (lo, hi) in matching else (hi, lo)
            graph[u].append(v)
            indeg[v] += 1
            incidences += 1
    assert incidences == 3900, incidences
    queue = deque(i for i, d in enumerate(indeg) if d == 0)
    visited = 0
    while queue:
        u = queue.popleft()
        visited += 1
        for v in graph[u]:
            indeg[v] -= 1
            if not indeg[v]:
                queue.append(v)
    assert visited == len(allfaces), (visited, len(allfaces))
    return allfaces, matching, dims, incidences


def cycle_type(perm):
    remaining = set(range(len(perm)))
    cycle_lengths = []
    while remaining:
        a = min(remaining)
        t = a
        c = 0
        while t in remaining:
            remaining.remove(t)
            c += 1
            t = perm[t]
        cycle_lengths.append(c)
    return tuple(sorted(cycle_lengths, reverse=True))


def sign_of_permutation_on_orbit(mapped):
    parity = sum(mapped[i] > mapped[j] for i in range(len(mapped))
                 for j in range(i + 1, len(mapped))) % 2
    return -1 if parity else 1


def equivariant_character(levels):
    table = {}
    class_sizes = Counter()
    for p in permutations(range(4)):
        for q in permutations(range(5)):
            perm = p + tuple(4 + x for x in q)
            eimage = [EDGE_INDEX[tuple(sorted((perm[a], perm[b])))]
                      for a, b in EDGES]
            t = []
            for layer in levels:
                c = 0
                for face in layer:
                    images = tuple(eimage[ei] for ei in face)
                    if set(images) == set(face):
                        c += sign_of_permutation_on_orbit(images)
                t.append(c)
            char = t[0] - t[1] + t[2] - 1
            typ = (cycle_type(p), cycle_type(q))
            if typ in table:
                assert table[typ] == char
            else:
                table[typ] = char
            class_sizes[typ] += 1
    assert len(table) == 35
    assert sum(class_sizes.values()) == math.factorial(4) * math.factorial(5)
    assert table[((1, 1, 1, 1), (1, 1, 1, 1, 1))] == 710
    assert sum(table[typ] * class_sizes[typ] for typ in table) == 0
    return table, class_sizes


def partitions(n, top=None):
    if n == 0:
        yield ()
        return
    if top is None:
        top = n
    for x in range(min(n, top), 0, -1):
        for nu in partitions(n - x, x):
            yield (x,) + nu


@lru_cache(None)
def symmetric_character(lam, cyc):
    # Murnaghan--Nakayama, with all removable connected rim hooks enumerated.
    if not cyc:
        return int(not lam)
    length = cyc[0]
    left = sum(lam) - length
    if left < 0:
        return 0
    ans = 0
    for nu in partitions(left):
        if len(nu) > len(lam) or any(x > y for x,y in zip(nu,lam)):
            continue
        cells = {(i,j) for i in range(len(lam)) for j in
                 range(nu[i] if i < len(nu) else 0, lam[i])}
        if len(cells) != length:
            continue
        if any((i+1,j) in cells and (i,j+1) in cells and
               (i+1,j+1) in cells for i,j in cells):
            continue
        work = [next(iter(cells))]
        connected = set(work)
        while work:
            i,j = work.pop()
            for xy in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if xy in cells and xy not in connected:
                    connected.add(xy)
                    work.append(xy)
        if len(connected) != len(cells):
            continue
        height = len({i for i,j in cells}) - 1
        ans += (-1)**height * symmetric_character(nu, cyc[1:])
    return ans


def z(mu):
    return math.prod(k**v * math.factorial(v) for k,v in Counter(mu).items())


def irreducible_decomposition(table):
    out = {}
    p4, p5 = list(partitions(4)), list(partitions(5))
    # First check character orthogonality with exact rational arithmetic.
    for p in (p4, p5):
        for lam in p:
            for nu in p:
                pairing = sum(Fraction(symmetric_character(lam,t)*
                                       symmetric_character(nu,t), z(t)) for t in p)
                assert pairing == int(lam == nu), (lam, nu, pairing)
    for lam in p4:
        for nu in p5:
            multiplicity = sum(Fraction(table[(u,v)] *
                symmetric_character(lam,u) * symmetric_character(nu,v),
                z(u)*z(v)) for u in p4 for v in p5)
            assert multiplicity.denominator == 1 and multiplicity >= 0
            out[(lam,nu)] = int(multiplicity)
    assert out[((4,), (5,))] == 0
    assert sum(v*symmetric_character(lam,(1,)*4)*
               symmetric_character(nu,(1,)*5) for (lam,nu),v in out.items()) == 710
    assert sum(1 for v in out.values() if v) == 22
    return out


def write_tables(table, sizes, decomp):
    directory = Path(__file__).resolve().parent
    with (directory/'character_table.csv').open('w',newline='',encoding='utf-8') as f:
        writer=csv.writer(f)
        writer.writerow(['cycle_type_A','cycle_type_B','class_size','trace_H2'])
        for a,b in sorted(table):
            writer.writerow(['.'.join(map(str,a)),'.'.join(map(str,b)),sizes[(a,b)],table[(a,b)]])
    with (directory/'irreducible_multiplicities.csv').open('w',newline='',encoding='utf-8') as f:
        writer=csv.writer(f)
        writer.writerow(['partition_A','partition_B','multiplicity','dimension'])
        for (a,b),v in sorted(decomp.items()):
            writer.writerow(['.'.join(map(str,a)),'.'.join(map(str,b)),v,
                v*symmetric_character(a,(1,)*4)*symmetric_character(b,(1,)*5)])


def main():
    levels = enumerate_faces()
    assert tuple(map(len, levels)) == (36, 375, 1050)
    assert independent_counts() == (36, 375, 1050, 0)
    ranks = check_mod_two_boundary(levels)
    allfaces, matching, critical, incidences = build_morse(levels)
    table, sizes = equivariant_character(levels)
    modules = irreducible_decomposition(table)
    write_tables(table, sizes, modules)
    print('FACES_OK', tuple(map(len,levels)), 'independently enumerated')
    print('BOUNDARY_MOD2_OK', 'ranks', ranks, 'bettis', (0,0,710))
    print('MORSE_OK', 'cells',len(allfaces),'pairs',len(matching),
          'critical',dict(critical),'incidences',incidences,'DAG')
    print('CHARACTER_OK',len(table),'classes',sum(sizes.values()),
          'group elements','invariants',0)
    print('DECOMPOSITION_OK',sum(v>0 for v in modules.values()),
          'irreducible constituents', 'dimension',710)
    print('ALL_VERIFY_OK')

if __name__ == '__main__':
    main()
