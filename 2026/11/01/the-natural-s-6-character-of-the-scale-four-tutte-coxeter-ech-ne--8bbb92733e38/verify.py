"""Exact finite verification of the natural six-letter action on a graph Cech nerve.

Python 3 standard library only. Constructs the complete complex; no external data.
"""
import collections
import heapq
import itertools
import math


def perfect_matchings(items):
    if not items:
        yield ()
        return
    first, *rest = items
    for other in rest:
        for tail in perfect_matchings([x for x in rest if x != other]):
            yield tuple(sorted(((first, other),) + tail))


def partitions(n, minpart=1):
    if n == 0:
        yield ()
    else:
        for a in range(minpart, n + 1):
            for rest in partitions(n - a, a):
                yield (a,) + rest


def rep_from_parts(parts):
    p = list(range(6))
    offset = 0
    for length in parts:
        for j in range(length):
            p[offset + j] = offset + (j + 1) % length
        offset += length
    return tuple(p)


def permutation_type(p):
    seen = set()
    lengths = []
    for i in range(6):
        if i not in seen:
            x = i
            length = 0
            while x not in seen:
                seen.add(x)
                length += 1
                x = p[x]
            lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def action_cycles(p):
    seen = set()
    result = []
    for i in range(len(p)):
        if i not in seen:
            cycle = []
            j = i
            while j not in seen:
                seen.add(j)
                cycle.append(j)
                j = p[j]
            assert j == i
            result.append(cycle)
    return result


def perm_parity(images):
    return (-1) ** sum(images[i] > images[j]
                       for i in range(len(images))
                       for j in range(i + 1, len(images)))


def gf2_rank(rows):
    basis = {}
    for word in rows:
        while word:
            j = word.bit_length() - 1
            if j not in basis:
                basis[j] = word
                break
            word ^= basis[j]
    return len(basis)


DUADS = tuple(itertools.combinations(range(6), 2))
SYNTHEMES = tuple(sorted(set(perfect_matchings(list(range(6))))))
assert len(DUADS) == len(SYNTHEMES) == 15
DIDX = {d: i for i, d in enumerate(DUADS)}
SIDX = {s: j + 15 for j, s in enumerate(SYNTHEMES)}
ADJ = [set() for _ in range(30)]
for d, i in DIDX.items():
    for s, j in SIDX.items():
        if d in s:
            ADJ[i].add(j)
            ADJ[j].add(i)
assert all(len(x) == 3 for x in ADJ)
assert sum(map(len, ADJ)) == 90
BALLS = []
for i in range(30):
    distances = [-1] * 30
    distances[i] = 0
    queue = collections.deque([i])
    while queue:
        x = queue.popleft()
        for y in ADJ[x]:
            if distances[y] == -1:
                distances[y] = distances[x] + 1
                queue.append(y)
    assert max(distances) == 4
    mask = sum(1 << j for j, r in enumerate(distances) if r <= 2)
    assert mask.bit_count() == 10
    BALLS.append(mask)

# Even-scale graph Cech lemma: every face is a subset of one closed two-ball.
FACES = set()
for mask in BALLS:
    sub = mask
    while sub:
        FACES.add(sub)
        sub = (sub - 1) & mask
assert len(FACES) == 27535
FVEC = tuple(sum(f.bit_count() == k for f in FACES) for k in range(1, 11))
assert FVEC == (30, 435, 2620, 5625, 7290, 6255, 3600, 1350, 300, 30)
assert sum((-1)**i * v for i, v in enumerate(FVEC)) == 145

# Elementary collapses: a free codimension-one face and unique maximal coface.
UP = {f: set() for f in FACES}
for f in FACES:
    bits = f
    while bits:
        bit = bits & -bits
        bits -= bit
        subface = f ^ bit
        if subface:
            UP[subface].add(f)
PRIORITY = [(f.bit_count(), f) for f in FACES if len(UP[f]) == 1]
heapq.heapify(PRIORITY)
PAIRS = 0
while PRIORITY:
    _, f = heapq.heappop(PRIORITY)
    if f not in UP or len(UP[f]) != 1:
        continue
    coface = next(iter(UP[f]))
    if UP[coface]:
        continue
    for cell in (f, coface):
        bits = cell
        while bits:
            bit = bits & -bits
            bits -= bit
            subface = cell ^ bit
            if subface and subface in UP:
                UP[subface].discard(cell)
                if len(UP[subface]) == 1:
                    heapq.heappush(PRIORITY, (subface.bit_count(), subface))
        del UP[cell]
    PAIRS += 1
CORE = UP
assert PAIRS == 13495
assert len(CORE) == 545
assert collections.Counter(f.bit_count() for f in CORE) == {1: 30, 2: 200, 3: 315}

# All triangles are genuine two-cells of the collapsed simplicial complex.
EDGES = sorted(f for f in CORE if f.bit_count() == 2)
EDGE_ID = {e: i for i, e in enumerate(EDGES)}
TRIANGLES = [f for f in CORE if f.bit_count() == 3]
triangle_boundaries = []
for t in TRIANGLES:
    word = 0
    bits = t
    while bits:
        bit = bits & -bits
        bits -= bit
        edge = t ^ bit
        assert edge in EDGE_ID
        word ^= 1 << EDGE_ID[edge]
    triangle_boundaries.append(word)
R2 = gf2_rank(triangle_boundaries)
# Independently certify connectedness of the actual remaining 1-skeleton.
remaining_neighbors = [set() for _ in range(30)]
for e in EDGES:
    vs = [i for i in range(30) if (e >> i) & 1]
    a, b = vs
    remaining_neighbors[a].add(b)
    remaining_neighbors[b].add(a)
seen = {0}
queue = collections.deque([0])
while queue:
    i = queue.popleft()
    for j in remaining_neighbors[i]:
        if j not in seen:
            seen.add(j)
            queue.append(j)
assert len(seen) == 30
R1 = len(seen) - 1
assert R2 == 171 == len(EDGES) - R1
# Thus rational reduced homology is concentrated in degree 2, rank 144.
assert len(TRIANGLES) - R2 == 144


def action_on_30(p):
    values = []
    for d in DUADS:
        values.append(DIDX[tuple(sorted(p[x] for x in d))])
    for s in SYNTHEMES:
        t = tuple(sorted(tuple(sorted((p[a], p[b]))) for a, b in s))
        values.append(SIDX[t])
    return tuple(values)


def euler_trace_via_cycles(p):
    cycles = action_cycles(action_on_30(p))
    cyclemasks = [sum(1 << v for v in c) for c in cycles]
    admissible = {0}
    for ball in BALLS:
        eligible = [i for i, mask in enumerate(cyclemasks)
                    if mask & ball == mask]
        # Use unique subsets of complete vertex orbits; include the empty set.
        for choice in range(1, 1 << len(eligible)):
            small = sum(1 << eligible[j] for j in range(len(eligible))
                        if choice >> j & 1)
            admissible.add(small)
    # Reduced Euler/Lefschetz trace in degree two.
    return -sum((-1)**m.bit_count() for m in admissible)


def euler_trace_via_signed_faces(p):
    action = action_on_30(p)
    lef = 0
    for face in FACES:
        inds = [j for j in range(30) if face >> j & 1]
        images = [action[j] for j in inds]
        if sum(1 << j for j in images) != face:
            continue
        lef += (-1)**(len(inds) - 1) * perm_parity(images)
    return lef - 1  # H0 contributes trace 1.


def class_size(part):
    counts = collections.Counter(part)
    denom = math.prod(length**multiplicity * math.factorial(multiplicity)
                      for length, multiplicity in counts.items())
    return math.factorial(6) // denom


PARTS = sorted((tuple(sorted(p, reverse=True)) for p in partitions(6)),
               key=lambda z: (-len(z), z))
CHAR = {}
for mu in PARTS:
    rep = rep_from_parts(mu)
    x = euler_trace_via_cycles(rep)
    assert euler_trace_via_signed_faces(rep) == x
    CHAR[mu] = x
assert CHAR[(1, 1, 1, 1, 1, 1)] == 144
assert CHAR[(5, 1)] == -1
assert all(x == 0 for mu, x in CHAR.items()
           if mu not in ((1, 1, 1, 1, 1, 1), (5, 1)))
COUNTS = collections.Counter()
for p in itertools.permutations(range(6)):
    mu = permutation_type(p)
    COUNTS[mu] += 1
    action = action_on_30(p)
    for center, ball in enumerate(BALLS):
        moved = sum(1 << action[j] for j in range(30) if ball >> j & 1)
        assert moved == BALLS[action[center]]
    assert euler_trace_via_cycles(p) == CHAR[mu]
assert sum(COUNTS.values()) == 720
assert all(COUNTS[mu] == class_size(mu) for mu in PARTS)
assert sum(class_size(mu) * CHAR[mu] for mu in PARTS) == 0
assert sum(class_size(mu) * CHAR[mu] *
           (-1)**(6-len(mu)) for mu in PARTS) == 0

# Independently reconstruct the full rational S6 character table using the
# Jacobi-Trudi alternant of multiset/permutation (Young tabloid) characters.
from functools import lru_cache
@lru_cache(None)
def tabloid_character(mu, row_sizes):
    if min(row_sizes) < 0 or sum(row_sizes) != sum(mu):
        return 0
    dp = {row_sizes: 1}
    for cycle_length in mu:
        next_dp = {}
        for remains, coefficient in dp.items():
            for i in range(len(remains)):
                if remains[i] >= cycle_length:
                    new = tuple(remains[j] - (cycle_length if i == j else 0)
                                for j in range(len(remains)))
                    next_dp[new] = next_dp.get(new, 0) + coefficient
        dp = next_dp
    return dp.get((0,) * len(row_sizes), 0)


def specht_char(lam, mu):
    total = 0
    for perm in itertools.permutations(range(len(lam))):
        sizes = tuple(lam[i] - i + perm[i] for i in range(len(lam)))
        if min(sizes) < 0:
            continue
        total += perm_parity(perm) * tabloid_character(mu, sizes)
    return total

SPECHT = {(lam, mu): specht_char(lam, mu)
          for lam in PARTS for mu in PARTS}
for lam in PARTS:
    for lam2 in PARTS:
        orth = sum(class_size(mu) * SPECHT[lam, mu] * SPECHT[lam2, mu]
                   for mu in PARTS)
        assert orth == (720 if lam == lam2 else 0)
MULTS = {}
for lam in PARTS:
    numerator = sum(class_size(mu) * CHAR[mu] * SPECHT[lam, mu]
                    for mu in PARTS)
    assert numerator % 720 == 0
    MULTS[lam] = numerator // 720
    assert MULTS[lam] >= 0
assert sum(MULTS[l] * SPECHT[l, (1,) * 6] for l in PARTS) == 144
assert MULTS[(6,)] == MULTS[(1,) * 6] == 0

print('VERIFY_OK')
print('graph: 30 vertices 45 edges; closed two-balls: 30 facets of size 10')
print('full Cech f-vector:', FVEC)
print('elementary-collapse pairs:', PAIRS,
      'remaining face vector:', (30, 200, 315))
print('F2 boundary ranks of 2-complex:', R1, R2)
print('rational reduced homology: H2 dimension 144, all other degrees zero')
print('S6 conjugacy character (cycle type, class size, H2 trace):')
for mu in PARTS:
    print(mu, class_size(mu), CHAR[mu])
print('S6 irreducible Specht multiplicities (nonzero):')
for lam in PARTS:
    if MULTS[lam]:
        print(lam, MULTS[lam], 'dimension', SPECHT[lam, (1,) * 6])
print('invariant dimension under S6 = 0; under A6 = 0')
print('C5 induction: identity 144, five-cycles -1, others 0')
print('720 actions and 11 independent signed-simplex Lefschetz checks passed')
