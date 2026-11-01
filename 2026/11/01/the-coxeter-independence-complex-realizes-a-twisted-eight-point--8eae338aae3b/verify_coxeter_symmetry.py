#!/usr/bin/env python3
"""Exact finite verification of the Coxeter independence-complex symmetry theorem.

Pure Python 3; no external packages or downloaded data are required.
The graph is constructed from non-collinear triples of the Fano plane.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations, permutations

N = 28
P = range(1, 8)
LINES = {frozenset((a, b, a ^ b)) for a in P for b in P if a < b}
assert len(LINES) == 7
VERTICES = tuple(c for c in combinations(P, 3) if frozenset(c) not in LINES)
assert len(VERTICES) == 28
EDGE = tuple(
    sum(1 << j for j, v in enumerate(VERTICES) if j != i and not set(u).intersection(v))
    for i, u in enumerate(VERTICES)
)
assert sum(a.bit_count() for a in EDGE) == 84
assert all(a.bit_count() == 3 for a in EDGE)


def all_independent_faces():
    faces = [0]
    for v in range(N):
        bit = 1 << v
        faces.extend([s | bit for s in faces if not (s & EDGE[v])])
    assert len(faces) == 196009
    counts = Counter(s.bit_count() for s in faces)
    assert tuple(counts[i] for i in range(13)) == (
        1, 28, 336, 2268, 9506, 25788, 45836,
        52928, 38556, 16660, 3752, 336, 14,
    )
    return faces


def check_morse(faces):
    # An independently chosen alternating-parity pivot sequence.
    order = list(range(0, N, 2)) + list(range(1, N, 2))
    unpaired = set(faces)
    mate = {}
    for v in order:
        bit = 1 << v
        lows = [s for s in unpaired if not (s & bit) and (s | bit) in unpaired]
        for s in lows:
            t = s | bit
            unpaired.remove(s)
            unpaired.remove(t)
            mate[s] = t
            mate[t] = s
    assert len(unpaired) == 7
    assert {s.bit_count() for s in unpaired} == {7}
    assert len(mate) == 196002
    first = mate.pop(0)
    mate.pop(first)
    assert first.bit_count() == 1
    f_nonempty = [s for s in faces if s]
    # Full finite proof of acyclicity, not merely a face-rank heuristic.
    indegree = {s: 0 for s in f_nonempty}
    edge_count = 0
    for s in f_nonempty:
        x = s
        while x:
            bit = x & -x
            x ^= bit
            t = s ^ bit
            if not t:
                continue
            if mate.get(t) == s:
                indegree[t] += 1
            else:
                indegree[s] += 1
            edge_count += 1
    assert edge_count == 1319724
    queue = deque(s for s in f_nonempty if indegree[s] == 0)
    visited = traversed = 0
    while queue:
        s = queue.popleft()
        visited += 1
        lower = mate.get(s)
        if lower is not None and lower.bit_count() == s.bit_count() - 1:
            indegree[lower] -= 1
            traversed += 1
            if indegree[lower] == 0:
                queue.append(lower)
        allowed = (1 << N) - 1
        x = s
        while x:
            bit = x & -x
            x ^= bit
            allowed &= ~(bit | EDGE[bit.bit_length() - 1])
        while allowed:
            bit = allowed & -allowed
            allowed ^= bit
            upper = s | bit
            if mate.get(s) == upper:
                continue
            indegree[upper] -= 1
            traversed += 1
            if indegree[upper] == 0:
                queue.append(upper)
    assert visited == 196008 and traversed == edge_count
    crit = Counter(s.bit_count() - 1 for s in f_nonempty if s not in mate)
    assert crit == {0: 1, 6: 7}
    print('EXACT_MORSE_OK', visited, traversed, len(mate) // 2, dict(crit))


def all_automorphisms():
    # Full backtracking enumeration, using every adjacency and nonadjacency.
    neighbors = [tuple(j for j in range(N) if EDGE[i] >> j & 1) for i in range(N)]
    autos = []
    universe = tuple(range(N))

    def search(mp, used):
        if len(mp) == N:
            autos.append(tuple(mp[i] for i in universe))
            return
        assigned = tuple(mp.items())
        best = None
        best_candidates = None
        for u in universe:
            if u in mp:
                continue
            candidates = [v for v in universe if not ((used >> v) & 1)
                          and all(bool(EDGE[u] >> x & 1) == bool(EDGE[v] >> y & 1)
                                  for x, y in assigned)]
            if not candidates:
                return
            if best_candidates is None or len(candidates) < len(best_candidates):
                best, best_candidates = u, candidates
                if len(candidates) == 1:
                    break
        for v in best_candidates:
            mp[best] = v
            search(mp, used | (1 << v))
            del mp[best]

    for target in universe:
        for neighbors_image in permutations(neighbors[target]):
            mapping = {0: target}
            mapping.update(zip(neighbors[0], neighbors_image))
            search(mapping, sum(1 << x for x in mapping.values()))
    assert len(autos) == 336 and len(set(autos)) == 336
    assert all(all((EDGE[i] >> j & 1) ==
                       (EDGE[p[i]] >> p[j] & 1)
                       for i in universe for j in universe) for p in autos)
    print('FULL_AUTOMORPHISM_GROUP_OK', len(autos))
    return autos


def mul(a, b):
    return tuple(a[b[i]] for i in range(N))


def inverse(a):
    inv = [None] * N
    for i, x in enumerate(a):
        inv[x] = i
    return tuple(inv)


def perm_cycles(p):
    seen = set()
    cycles = []
    for i in range(len(p)):
        if i in seen:
            continue
        orb = []
        j = i
        while j not in seen:
            seen.add(j)
            orb.append(j)
            j = p[j]
        cycles.append(tuple(orb))
    return cycles


def parity(p):
    return (-1) ** (len(p) - len(perm_cycles(p)))


def perm_order(p):
    from math import lcm
    z = 1
    for c in perm_cycles(p):
        z = lcm(z, len(c))
    return z


def homology_trace(p):
    # Reduced Lefschetz trace from all invariant oriented faces, compressed
    # to an independent-set polynomial on admissible vertex orbits.
    allowed = []
    for orbit in perm_cycles(p):
        mask = sum(1 << v for v in orbit)
        if not any(EDGE[v] & mask for v in orbit):
            allowed.append(mask)
    m = len(allowed)
    conflicts = [0] * m
    for i, mask in enumerate(allowed):
        edges = 0
        x = mask
        while x:
            bit = x & -x
            x ^= bit
            edges |= EDGE[bit.bit_length()-1]
        for j, other in enumerate(allowed):
            if i != j and edges & other:
                conflicts[i] |= 1 << j

    @lru_cache(None)
    def polynomial_at_minus_one(mask):
        if mask == 0:
            return 1
        bit = mask & -mask
        i = bit.bit_length()-1
        return (polynomial_at_minus_one(mask ^ bit)
                - polynomial_at_minus_one(mask & ~(bit | conflicts[i])))
    return -polynomial_at_minus_one((1 << m) - 1)


def directly_signed_trace(p, faces):
    # Independent full face-level orientation computation for class representatives.
    total = -1  # The reduced degree-minus-one chain of the empty face.
    imagebits = [1 << p[i] for i in range(N)]
    for s in faces:
        if not s:
            continue
        x = s
        target = 0
        while x:
            bit = x & -x
            x ^= bit
            target |= imagebits[bit.bit_length()-1]
        if target != s:
            continue
        selected = [i for i in range(N) if s >> i & 1]
        ranks = {v: j for j, v in enumerate(selected)}
        # Selected images form the same set. Count inversions of image word.
        values = [ranks[p[i]] for i in selected]
        inversions = sum(values[i] > values[j] for i in range(len(values))
                         for j in range(i+1, len(values)))
        total += (-1) ** (len(selected)-1+inversions)
    return total


def verify_characters(faces, autos):
    idp = tuple(range(N))
    order7 = [g for g in autos if perm_order(g) == 7]
    sylow_sets = set()
    for g in order7:
        powers = set()
        x = idp
        for _ in range(7):
            powers.add(x)
            x = mul(g, x)
        assert x == idp and len(powers) == 7
        sylow_sets.add(frozenset(powers))
    assert len(sylow_sets) == 8
    sylows = sorted(sylow_sets, key=lambda h: sorted(autos.index(v) for v in h))
    index = {s: i for i, s in enumerate(sylows)}
    tally = Counter()
    traces = []
    representatives = {}
    for g in autos:
        gi = inverse(g)
        on_sylows = tuple(index[frozenset(mul(mul(g, x), gi) for x in h)]
                          for h in sylows)
        eps = parity(on_sylows)
        fixed = sum(i == on_sylows[i] for i in range(8))
        derived = eps*(fixed-1)
        actual = homology_trace(g)
        assert actual == derived, (actual,derived)
        key = (perm_order(g),eps,fixed,actual)
        tally[key] += 1
        traces.append(actual)
        representatives.setdefault(key,g)
    expected = {
        (1, 1, 8, 7):1, (2, 1, 0, -1):21,
        (2, -1, 2, -1):28, (3, 1, 2, 1):56,
        (4, 1, 0, -1):42, (6, -1, 2, -1):56,
        (7, 1, 1, 0):48, (8, -1, 0, 1):84,
    }
    assert tally == expected, (tally,expected)
    for key,g in representatives.items():
        direct = directly_signed_trace(g, faces)
        assert direct == key[-1],(key,direct)
    assert sum(traces) == 0
    assert sum(key[-1]*count for key,count in tally.items() if key[1]==1) == 0
    assert (7+sum(homology_trace(g) for g in order7[:6])) == 7
    assert sum(x*x for x in traces) == 336
    print('JOINT_CHARACTER_OK',len(autos),'sylow7_subgroups',len(sylows),
          'direct_face_representatives',len(representatives))
    print('GROUP_CLASS_TABLE: order epsilon fixed_count trace count')
    for key, count in sorted(tally.items()):
        print(*key, count)
    print('IRREDUCIBLE_INNER_PRODUCT',sum(x*x for x in traces),'/',len(traces))
    print('RATIONAL_QUOTIENT_RANKS full=0 normal_168=0 order_7=1')


def main():
    faces = all_independent_faces()
    check_morse(faces)
    automorphisms = all_automorphisms()
    verify_characters(faces, automorphisms)
    print('COXETER_SYMMETRY_VERIFY_OK')


if __name__ == '__main__':
    main()
