#!/usr/bin/env python3
"""Exact finite certificate for two open graph-neighborhood complexes.

Run with Python 3.10+ and the standard library only. All masks, incidences,
matchings, orientations and ranks are constructed afresh by this program.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from math import gcd

N = 16
SHRIKHANDE_STEPS = {(1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)}
# Each permutation uses the index 4*i+j of (i,j) in (Z/4Z)^2.
FACET_CENTER_MAP = (0, 8, 2, 10, 7, 3, 5, 1, 14, 6, 12, 4, 9, 13, 11, 15)
VERTEX_MAP = (11, 1, 9, 3, 2, 4, 0, 6, 5, 15, 7, 13, 12, 10, 14, 8)


def adjacency(kind):
    out = []
    for a in range(N):
        i, j = divmod(a, 4)
        mask = 0
        for b in range(N):
            k, l = divmod(b, 4)
            if kind == 'Shrikhande':
                adjacent = ((k-i) % 4, (l-j) % 4) in SHRIKHANDE_STEPS
            else:
                adjacent = a != b and (i == k or j == l)
            if adjacent:
                mask |= 1 << b
        out.append(mask)
    for a in range(N):
        assert not (out[a] & (1 << a))
        assert out[a].bit_count() == 6
        for b in range(N):
            assert bool(out[a] & (1 << b)) == bool(out[b] & (1 << a))
            if a != b:
                assert (out[a] & out[b]).bit_count() == 2
    return tuple(out)


def map_mask(m, perm):
    result = 0
    while m:
        bit = m & -m
        result |= 1 << perm[bit.bit_length()-1]
        m ^= bit
    return result


def faces_from_facets(neighbors):
    f = {0}
    for nm in neighbors:
        verts = [i for i in range(N) if nm >> i & 1]
        assert len(verts) == 6
        for x in range(1 << 6):
            mask = 0
            for j, v in enumerate(verts):
                if x >> j & 1:
                    mask |= 1 << v
            f.add(mask)
    # Independent exhaustive membership check against every vertex subset.
    check = {m for m in range(1 << N) if any(m & ~nm == 0 for nm in neighbors)}
    assert f == check
    assert all((m ^ (m & -m)) in f for m in f if m)
    return f


def matching(faces):
    remaining = set(faces)
    pairs = []
    for vertex in range(N):
        bit = 1 << vertex
        for f in sorted(remaining, key=lambda x: (x.bit_count(), x)):
            if f in remaining and not f & bit and (f | bit) in remaining:
                pairs.append((f, f | bit))
                remaining.remove(f)
                remaining.remove(f | bit)
    assert pairs[0] == (0, 1)
    # The augmented pair is only an enumeration convenience; keep its
    # singleton as the unique critical 0-cell in the ordinary CW model.
    pairs = pairs[1:]
    critical = remaining | {1}
    nonempty = faces - {0}
    assert len(critical) + 2 * len(pairs) == len(nonempty)
    return nonempty, critical, pairs


def incidence(upper, lower):
    bit = upper ^ lower
    assert bit.bit_count() == 1 and (upper & lower) == lower
    return -1 if (lower & (bit - 1)).bit_count() % 2 else 1


def acyclic(nonempty, pairs):
    matched = set(pairs)
    directed = {f: [] for f in nonempty}
    degree = {f: 0 for f in nonempty}
    incidence_count = 0
    for top in nonempty:
        m = top
        while m:
            bit = m & -m
            bottom = top ^ bit
            m ^= bit
            if bottom == 0:
                continue
            incidence_count += 1
            if (bottom, top) in matched:
                frm, to = bottom, top
            else:
                frm, to = top, bottom
            directed[frm].append(to)
            degree[to] += 1
    q = deque(f for f, d in degree.items() if d == 0)
    removed = 0
    while q:
        f = q.popleft()
        removed += 1
        for to in directed[f]:
            degree[to] -= 1
            if degree[to] == 0:
                q.append(to)
    assert removed == len(nonempty)
    return incidence_count


def morse_boundaries(critical, pairs):
    low_to_high = {a: b for a, b in pairs}
    high_to_low = {b: a for a, b in pairs}
    assert len(low_to_high) == len(high_to_low) == len(pairs)

    @lru_cache(None)
    def projected(face):
        if face in critical:
            return {face: 1}
        if face in high_to_low:
            return {}
        assert face in low_to_high
        high = low_to_high[face]
        unit = incidence(high, face)  # ±1
        result = defaultdict(int)
        bits = high
        while bits:
            bit = bits & -bits
            bits ^= bit
            other = high ^ bit
            if other == face:
                continue
            for c, z in projected(other).items():
                result[c] -= unit * incidence(high, other) * z
        return {c: z for c, z in result.items() if z}

    rows = {}
    for face in critical:
        if face.bit_count() <= 1:
            continue
        result = defaultdict(int)
        bits = face
        while bits:
            bit = bits & -bits
            bits ^= bit
            lower = face ^ bit
            for c, z in projected(lower).items():
                result[c] += incidence(face, lower) * z
        rows[face] = {c: z for c, z in result.items() if z}
    return rows


def mod_rank(nonempty, dimension, prime):
    upper = sorted(f for f in nonempty if f.bit_count() == dimension + 1)
    pivots = {}
    for top in upper:
        col = {}
        bits = top
        while bits:
            bit = bits & -bits
            bits ^= bit
            low = top ^ bit
            if low:
                col[low] = incidence(top, low) % prime
        while col:
            row = min(col)
            if row not in pivots:
                inv = pow(col[row], -1, prime)
                pivots[row] = {k: (v*inv) % prime for k, v in col.items()}
                break
            k = col[row]
            for j, v in pivots[row].items():
                new = (col.get(j, 0) - k*v) % prime
                if new:
                    col[j] = new
                else:
                    col.pop(j, None)
    return len(pivots)


def betti(nonempty, prime):
    dims = Counter(f.bit_count()-1 for f in nonempty)
    maxdim = max(dims)
    ranks = {d: mod_rank(nonempty, d, prime) for d in range(1, maxdim+1)}
    return tuple(dims[d] - ranks.get(d, 0) - ranks.get(d+1, 0) for d in range(maxdim+1))


def main():
    graphs = {kind: adjacency(kind) for kind in ('Shrikhande','Rook')}
    assert set(FACET_CENTER_MAP) == set(VERTEX_MAP) == set(range(N))
    for c in range(N):
        assert map_mask(graphs['Shrikhande'][c], VERTEX_MAP) == graphs['Rook'][FACET_CENTER_MAP[c]]
    print('BIPARTITE_INCIDENCE_ISOMORPHISM_OK')
    for name, neighbors in graphs.items():
        faces = faces_from_facets(neighbors)
        assert len(faces) == 809
        fvector = tuple(Counter(m.bit_count()-1 for m in faces)[d] for d in range(6))
        assert fvector == (16, 120, 320, 240, 96, 16)
        nonempty, critical, pairs = matching(faces)
        crit = Counter(m.bit_count()-1 for m in critical)
        assert crit == {0: 1, 1: 1, 2: 56}
        assert len(pairs) == 375
        incidences = acyclic(nonempty, pairs)
        boundaries = morse_boundaries(critical, pairs)
        critical_edge, = (c for c in critical if c.bit_count() == 2)
        critical_vertex, = (c for c in critical if c.bit_count() == 1)
        assert boundaries[critical_edge] == {}
        vals = [boundaries[c].get(critical_edge, 0) for c in sorted(critical) if c.bit_count() == 3]
        assert all(boundaries[c] == ({critical_edge: v} if v else {}) for c, v in zip(sorted(c for c in critical if c.bit_count() == 3), vals))
        assert {abs(x) for x in vals} == {0, 2}
        g = 0
        for x in vals:
            g = gcd(g, abs(x))
        assert g == 2
        b2 = betti(nonempty, 2)
        b3 = betti(nonempty, 3)
        assert b2 == (1, 1, 56, 0, 0, 0)
        assert b3 == (1, 0, 55, 0, 0, 0)
        print(f'{name}: faces=808 fvector={fvector} pairs=375 critical=(1,1,56) incidences={incidences}')
        print(f'{name}: critical_edge_mask={critical_edge} boundary_coefficients={dict(sorted(Counter(vals).items()))} gcd=2')
        print(f'{name}: betti_mod_2={b2} betti_mod_3={b3}')
    print('OPEN_NEIGHBORHOOD_RP2_PLUS_55_S2_OK')


if __name__ == '__main__':
    main()
