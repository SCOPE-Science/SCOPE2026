#!/usr/bin/env python3
"""Exact certificate for the Fano-incidence graph's 2-independence complex.

Only Python's standard library is required. All simplicial chains and graph
permutations are constructed from the displayed incidence rule.
"""
from collections import Counter, defaultdict, deque
from itertools import product


def main():
    vec = sorted(t for t in product((0, 1), repeat=3) if any(t))
    assert len(vec) == 7
    vidx = {v: i for i, v in enumerate(vec)}
    incidence = lambda a, b: sum(x*y for x, y in zip(a, b)) % 2 == 0
    adj = [0] * 14
    edge_count = 0
    for i, v in enumerate(vec):
        for j, w in enumerate(vec):
            if incidence(v, w):
                adj[i] |= 1 << (j + 7)
                adj[j + 7] |= 1 << i
                edge_count += 1
    assert edge_count == 21
    assert all(m.bit_count() == 3 for m in adj)
    assert all((adj[i] & ((1 << 7) - 1)) == 0 for i in range(7))
    faces = set()
    by_dim = defaultdict(list)
    for mask in range(1, 1 << 14):
        if all((adj[i] & mask).bit_count() <= 1 for i in range(14) if (mask >> i) & 1):
            faces.add(mask)
            by_dim[mask.bit_count()-1].append(mask)
    f_vector = tuple(len(by_dim[i]) for i in range(7))
    assert len(faces) == 2256
    assert f_vector == (14, 91, 322, 651, 728, 392, 58), f_vector
    assert sum((-1)**i * n for i, n in enumerate(f_vector)) == -12

    unmatched = set(faces)
    pairs = []
    for vertex in range(14):
        vbit = 1 << vertex
        chosen = [(a, a | vbit) for a in sorted(unmatched)
                  if not (a & vbit) and (a | vbit) in unmatched]
        for lower, upper in chosen:
            assert lower in unmatched and upper in unmatched
            assert upper.bit_count() == lower.bit_count() + 1
            unmatched.remove(lower)
            unmatched.remove(upper)
            pairs.append((lower, upper))
    critical = sorted((m.bit_count()-1, m) for m in unmatched)
    assert len(pairs) == 1121
    assert critical == [(0, 1)] + [(5, x) for x in
        (1008, 3300, 5460, 6712, 8064, 9826, 10600,
         12160, 12504, 14208, 15232, 15744, 16000)], critical
    matched = set(pairs)
    indeg = {f: 0 for f in faces}
    outgoing = {f: [] for f in faces}
    incidences = 0
    for upper in faces:
        bits = upper
        while bits:
            bit = bits & -bits
            bits ^= bit
            lower = upper ^ bit
            if lower == 0:
                continue
            tail, head = (lower, upper) if (lower, upper) in matched else (upper, lower)
            outgoing[tail].append(head)
            indeg[head] += 1
            incidences += 1
    assert incidences == 10150, incidences
    queue = deque(f for f in faces if indeg[f] == 0)
    seen = 0
    while queue:
        f = queue.popleft()
        seen += 1
        for target in outgoing[f]:
            indeg[target] -= 1
            if indeg[target] == 0:
                queue.append(target)
    assert seen == len(faces), (seen, len(faces))

    # Independent check of all mod-two simplicial boundary ranks.
    def gf2rank(cols):
        pivots = {}
        for c in cols:
            while c:
                p = c.bit_length()-1
                if p in pivots:
                    c ^= pivots[p]
                else:
                    pivots[p] = c
                    break
        return len(pivots)

    ranks = {0: 0}
    for d in range(1, 7):
        low_index = {f: i for i, f in enumerate(by_dim[d-1])}
        cols = []
        for face in by_dim[d]:
            col = 0
            remaining = face
            while remaining:
                bit = remaining & -remaining
                remaining ^= bit
                col ^= 1 << low_index[face ^ bit]
            cols.append(col)
        ranks[d] = gf2rank(cols)
    assert tuple(ranks[d] for d in range(1, 7)) == (13, 78, 244, 407, 321, 58)
    mod2_betti = tuple(len(by_dim[d])-ranks[d]-ranks.get(d+1, 0) for d in range(7))
    assert mod2_betti == (1, 0, 0, 0, 0, 13, 0), mod2_betti

    # Enumerate the point-line preserving incidence automorphisms by GL(3,2).
    perms = []
    for code in range(1 << 9):
        rows = [tuple((code >> (3*i+j)) & 1 for j in range(3)) for i in range(3)]
        images = [tuple(sum(rows[i][j]*v[j] for j in range(3)) % 2 for i in range(3)) for v in vec]
        if len(set(images)) != 7:
            continue
        pmap = tuple(vidx[y] for y in images)
        lmap = []
        for line in vec:
            image_points = frozenset(pmap[i] for i, point in enumerate(vec) if incidence(point, line))
            target = next(j for j, cand in enumerate(vec)
                          if frozenset(i for i, point in enumerate(vec) if incidence(point, cand)) == image_points)
            lmap.append(target + 7)
        perm = pmap + tuple(lmap)
        assert all((bool((adj[i] >> j) & 1) == bool((adj[perm[i]] >> perm[j]) & 1))
                   for i in range(14) for j in range(14))
        perms.append(perm)
    assert len(perms) == 168
    assert len(set(perms)) == 168
    duality = tuple(i + 7 if i < 7 else i - 7 for i in range(14))
    dual_perms = [tuple(duality[p[i]] for i in range(14)) for p in perms]
    assert len(set(perms + dual_perms)) == 336
    assert all(bool((adj[i] >> j) & 1) == bool((adj[duality[i]] >> duality[j]) & 1)
               for i in range(14) for j in range(14))

    def signed_lefschetz_trace(perm):
        # The reduced Lefschetz number is -tr on degree-five homology.
        # A fixed nonempty face with c vertex-permutation orbits contributes
        # (-1)^(c+1) to the unreduced chain-level Lefschetz number.
        L = 0
        for f in faces:
            image = 0
            active = f
            while active:
                bit = active & -active
                active ^= bit
                image |= 1 << perm[bit.bit_length()-1]
            if image != f:
                continue
            cycles = 0
            active = f
            while active:
                pos = (active & -active).bit_length()-1
                v = pos
                while (active >> v) & 1:
                    active ^= 1 << v
                    v = perm[v]
                cycles += 1
            L += 1 if cycles % 2 == 1 else -1
        return 1-L

    def signed_trace_by_oriented_faces(perm):
        """Independent parity formula using image-order inversions, not orbits."""
        L = 0
        for f in faces:
            verts = [i for i in range(14) if (f >> i) & 1]
            transformed = [perm[i] for i in verts]
            if set(transformed) != set(verts):
                continue
            inversions = sum(transformed[i] > transformed[j]
                             for i in range(len(transformed))
                             for j in range(i + 1, len(transformed)))
            L += (-1 if (len(verts)-1+inversions) & 1 else 1)
        return 1-L

    def ord_perm(perm):
        current = tuple(range(14))
        for k in range(1, 100):
            current = tuple(perm[v] for v in current)
            if current == tuple(range(14)):
                return k
        raise AssertionError('No finite order <=99')

    class_counts = {'preserving': defaultdict(Counter), 'duality': defaultdict(Counter)}
    for p in perms:
        val = signed_lefschetz_trace(p)
        assert val == signed_trace_by_oriented_faces(p)
        pts_fixed = sum(p[i] == i for i in range(7))
        assert val == 1 + 2*(pts_fixed - 1), (p, val, pts_fixed)
        class_counts['preserving'][ord_perm(p)][val] += 1
    for p in dual_perms:
        assert signed_lefschetz_trace(p) == signed_trace_by_oriented_faces(p)
        assert signed_lefschetz_trace(p) == -1
        class_counts['duality'][ord_perm(p)][-1] += 1
    assert dict(class_counts['preserving']) == {
        1: Counter({13: 1}), 2: Counter({5: 21}),
        3: Counter({1: 56}), 4: Counter({1: 42}),
        7: Counter({-1: 48})}
    assert dict(class_counts['duality']) == {
        2: Counter({-1: 28}), 6: Counter({-1: 56}), 8: Counter({-1: 84})}
    assert sum(k*v for k, v in class_counts['preserving'][1].items()) == 13
    assert (13 + 21*5 + 56 + 42 - 48) // 168 == 1
    assert 13 + 21*5 + 56 + 42 - 48 - 168 == 0
    print('F_VECTOR', f_vector)
    print('FACES', len(faces), 'MATCHED_PAIRS', len(pairs), 'INCIDENCES', incidences)
    print('CRITICAL', critical)
    print('BOUNDARY_RANK_MOD2', tuple(ranks[d] for d in range(1, 7)))
    print('BETTI_MOD2', mod2_betti)
    print('GL_CHARACTER_BY_ORDER', {k: dict(v) for k, v in sorted(class_counts['preserving'].items())})
    print('DUALITY_COSET_CHARACTER_BY_ORDER', {k: dict(v) for k, v in sorted(class_counts['duality'].items())})
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
