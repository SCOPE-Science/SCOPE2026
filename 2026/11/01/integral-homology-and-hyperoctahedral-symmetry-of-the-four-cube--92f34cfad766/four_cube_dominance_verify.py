"""Exact simplicial, Morse and symmetry checks for the four-cube dominance complex.

Only Python's standard library is required. Execute with Python 3.10 or later.
All masks, chain coefficients, ranks and group actions are computed exactly.
"""
from collections import Counter, defaultdict, deque
from itertools import permutations

D = 4
N = 1 << D
ALL = (1 << N) - 1
BALLS = tuple(sum(1 << w for w in range(N) if (v ^ w).bit_count() <= 1)
              for v in range(N))


def face_by_forbidden_balls(m):
    return all((m & b) != b for b in BALLS)


def face_by_complement_domination(m):
    remaining = ALL ^ m
    for v in range(N):
        if not any(((remaining >> w) & 1) and (v == w or (v ^ w).bit_count() == 1)
                   for w in range(N)):
            return False
    return True


faces = set()
for m in range(1 << N):
    a = face_by_forbidden_balls(m)
    b = face_by_complement_domination(m)
    assert a == b, (m, a, b)
    if m and a:
        faces.add(m)

assert len(faces) == 45706
fv = Counter(m.bit_count() - 1 for m in faces)
assert [fv[k] for k in range(12)] == [16, 120, 560, 1820, 4352, 7832,
                                         10560, 10310, 6800, 2736, 560, 40]

# Repeated vertex-toggle partial matchings, followed by a *complete* direct
# directed-Hasse acyclicity check: no unverified matching lemma is assumed.
remaining = set(faces)
matched_hi_to_lo = {}
for v in range(N):
    bv = 1 << v
    batch = [(m, m | bv) for m in remaining if not (m & bv) and (m | bv) in remaining]
    for lo, hi in batch:
        matched_hi_to_lo[hi] = lo
        remaining.remove(lo)
        remaining.remove(hi)

critical = Counter(m.bit_count() - 1 for m in remaining)
assert len(matched_hi_to_lo) == 22847
assert critical == {0: 1, 7: 10, 9: 1}

indegree = {m: 0 for m in faces}
outgoing = defaultdict(list)
incidences = 0
for hi in faces:
    mm = hi
    while mm:
        bv = mm & -mm
        mm -= bv
        lo = hi ^ bv
        if lo not in faces:
            continue
        if matched_hi_to_lo.get(hi) == lo:
            outgoing[lo].append(hi)
            indegree[hi] += 1
        else:
            outgoing[hi].append(lo)
            indegree[lo] += 1
        incidences += 1
assert incidences == 329552
q = deque(m for m, d in indegree.items() if d == 0)
removed = 0
while q:
    u = q.popleft()
    removed += 1
    for v in outgoing[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            q.append(v)
assert removed == len(faces)
del outgoing, indegree

# Independent simplicial boundary ranks over GF(2), in every dimension.
by_dim = defaultdict(list)
for m in faces:
    by_dim[m.bit_count() - 1].append(m)
ranks = {}
for d in range(1, 12):
    row_index = {m: i for i, m in enumerate(by_dim[d - 1])}
    pivots = {}
    for m in by_dim[d]:
        col = 0
        mm = m
        while mm:
            bv = mm & -mm
            mm -= bv
            col ^= 1 << row_index[m ^ bv]
        while col:
            k = col.bit_length() - 1
            if k in pivots:
                col ^= pivots[k]
            else:
                pivots[k] = col
                break
    ranks[d] = len(pivots)
assert [ranks[d] for d in range(1, 12)] == [15, 105, 455, 1365, 2987,
                                             4845, 5715, 4585, 2215, 520, 40]
betti = {d: len(by_dim[d]) - ranks.get(d, 0) - ranks.get(d + 1, 0)
         for d in range(12)}
betti[0] -= 1  # reduced H_0
assert betti == {d: (10 if d == 7 else 1 if d == 9 else 0) for d in range(12)}


def boundary(mask):
    """Signed oriented simplex boundary, with vertex order 0,...,15."""
    bits = [v for v in range(N) if mask & (1 << v)]
    return [(mask ^ (1 << v), -1 if i & 1 else 1)
            for i, v in enumerate(bits)]


def upward_pairs_of_lower_size(lower_size):
    """DAG of alternating paths between lower cells matched upward.

    Returns the lower-to-upper map and an elimination order. Distinct
    incidences along a matched upper simplex are used to construct the DAG.
    """
    up = {lo: hi for hi, lo in matched_hi_to_lo.items()
          if lo.bit_count() == lower_size}
    next_lows = {lo: [] for lo in up}
    indeg = {lo: 0 for lo in up}
    for lo, hi in up.items():
        for other, _ in boundary(hi):
            if other != lo and other in up:
                next_lows[lo].append(other)
                indeg[other] += 1
    queue = deque(lo for lo in up if indeg[lo] == 0)
    order = []
    while queue:
        lo = queue.popleft()
        order.append(lo)
        for other in next_lows[lo]:
            indeg[other] -= 1
            if indeg[other] == 0:
                queue.append(other)
    assert len(order) == len(up)
    return up, order


critical_9 = next(m for m in remaining if m.bit_count() == 10)
up8, order8 = upward_pairs_of_lower_size(9)
assert len(up8) == 2215
z = {critical_9: 1}
bdz = defaultdict(int)
for f, s in boundary(critical_9):
    bdz[f] += s
for lo in order8:
    c = bdz.get(lo, 0)
    if c:
        hi = up8[lo]
        sigma = dict(boundary(hi))[lo]
        delta = -c * sigma
        z[hi] = z.get(hi, 0) + delta
        for f, s in boundary(hi):
            bdz[f] += delta * s
            if not bdz[f]:
                del bdz[f]
assert not bdz
assert len(z) == 448 and set(z.values()) <= {-1, 1}

up9, order9 = upward_pairs_of_lower_size(10)
assert len(up9) == 520


def homology_coordinate(cycle):
    """Project a nine-cycle modulo 10-boundaries to its Morse critical 9-cell."""
    c = dict(cycle)
    for lo in order9:
        coef = c.get(lo, 0)
        if coef:
            hi = up9[lo]
            sigma = dict(boundary(hi))[lo]
            delta = -coef * sigma
            for face, sgn in boundary(hi):
                c[face] = c.get(face, 0) + delta * sgn
                if c[face] == 0:
                    del c[face]
    return c.get(critical_9, 0)


assert homology_coordinate(z) == 1


def vertex_map(p, t):
    return [sum(((v >> i) & 1) << p[i] for i in range(D)) ^ t
            for v in range(N)]


def orientation_sign(m, mapp):
    image = [mapp[v] for v in range(N) if m & (1 << v)]
    inversions = sum(image[i] > image[j] for i in range(len(image))
                     for j in range(i + 1, len(image)))
    return -1 if inversions & 1 else 1


def image_chain(chain, mapp):
    out = {}
    for m, c in chain.items():
        image = sum(1 << mapp[v] for v in range(N) if m & (1 << v))
        out[image] = c * orientation_sign(m, mapp)
    return out


def orbits(mapp):
    seen, orbs = set(), []
    for v in range(N):
        if v in seen:
            continue
        bits = 0
        w = v
        while w not in seen:
            seen.add(w)
            bits |= 1 << w
            w = mapp[w]
        orbs.append(bits)
    return orbs


def alternating_fixed_face_sum(mapp):
    """Signed fixed-simplex enumeration, including the empty simplex."""
    orb = orbits(mapp)
    total = 0
    for sub in range(1 << len(orb)):
        face = 0
        for i, bits in enumerate(orb):
            if sub & (1 << i):
                face |= bits
        if face_by_forbidden_balls(face):
            total += -1 if sub.bit_count() & 1 else 1
    return total


character7 = {}
character9 = {}
for p in permutations(range(D)):
    permutation_sign = (-1) ** sum(p[i] > p[j] for i in range(D)
                                  for j in range(i + 1, D))
    for t in range(1 << D):
        g = vertex_map(p, t)
        chi9 = homology_coordinate(image_chain(z, g))
        assert chi9 == permutation_sign
        chi7 = alternating_fixed_face_sum(g) - chi9
        character7[(p, t)] = chi7
        character9[(p, t)] = chi9

assert len(character7) == 384
assert character7[(tuple(range(D)), 0)] == 10
assert character9[(tuple(range(D)), 0)] == 1
assert sum(character7.values()) == 768
assert sum(character9.values()) == 0
assert Counter(character7.values()) == {0: 116, 2: 177, 4: 68, 6: 22, 10: 1}

print('DOMINANCE_Q4_INTEGRAL_AND_SYMMETRY_VERIFIED')
print('vertices', N, 'edges', N * D // 2)
print('nonempty_faces', len(faces), 'face_vector', [fv[k] for k in range(12)])
print('morse_pairs', len(matched_hi_to_lo), 'hasse_incidences', incidences)
print('acyclic_vertices', removed, 'critical', sorted(critical.items()))
print('mod2_boundary_ranks', [ranks[d] for d in range(1, 12)])
print('reduced_mod2_betti', [betti[d] for d in range(12)])
print('degree_9_integral_cycle_support', len(z), 'coefficient_set', sorted(set(z.values())))
print('automorphisms', len(character7), 'degree_9_sign_checks', len(character9))
print('degree_7_character_histogram', sorted(Counter(character7.values()).items()))
print('rational_quotient_betti_7_9', sum(character7.values()) // 384,
      sum(character9.values()) // 384)
