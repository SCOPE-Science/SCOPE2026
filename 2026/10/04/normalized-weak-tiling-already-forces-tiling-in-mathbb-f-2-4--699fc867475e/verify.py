from fractions import Fraction
import itertools

D = 4
N = 1 << D

def points(mask):
    return [x for x in range(N) if (mask >> x) & 1]

def diff_mask(mask):
    xs = points(mask)
    out = 0
    for a in xs:
        for b in xs:
            out |= 1 << (a ^ b)
    return out

def make_generators():
    generators = []
    for kind in range(3):
        perm = []
        for x in range(N):
            bits = [(x >> i) & 1 for i in range(D)]
            if kind == 0:
                bits[0], bits[1] = bits[1], bits[0]
            elif kind == 1:
                bits = bits[1:] + bits[:1]
            else:
                bits[0] ^= bits[1]
            perm.append(sum(bit << i for i, bit in enumerate(bits)))
        generators.append(tuple(perm))
    return tuple(generators)

GENERATORS = make_generators()

def compose(p, q):
    return tuple(p[q[x]] for x in range(N))

def generated_group():
    identity = tuple(range(N))
    seen = {identity}
    stack = [identity]
    while stack:
        g = stack.pop()
        for s in GENERATORS:
            h = compose(s, g)
            if h not in seen:
                seen.add(h)
                stack.append(h)
    return seen

def apply_mask(mask, perm):
    out = 0
    for x in range(N):
        if (mask >> x) & 1:
            out |= 1 << perm[x]
    return out

def orbit_partition():
    seen = set()
    orbits = []
    for mask in range(1, 1 << N):
        if not (mask & 1) or mask in seen:
            continue
        orbit = set()
        stack = [mask]
        seen.add(mask)
        while stack:
            a = stack.pop()
            orbit.add(a)
            for perm in GENERATORS:
                b = apply_mask(a, perm)
                if b not in seen:
                    seen.add(b)
                    stack.append(b)
        orbits.append(tuple(sorted(orbit)))
    assert len(seen) == 1 << (N - 1)
    return orbits

def tiles(mask):
    size = mask.bit_count()
    if N % size:
        return False, None
    complement_size = N // size
    dA = diff_mask(mask)
    for comb in itertools.combinations(range(1, N), complement_size - 1):
        bmask = 1
        for x in comb:
            bmask |= 1 << x
        if (dA & diff_mask(bmask)) == 1:
            return True, bmask
    return False, None

def exact_rank(rows):
    A = [[Fraction(x) for x in row] for row in rows]
    if not A:
        return 0
    m = len(A)
    n = len(A[0])
    r = 0
    for c in range(n):
        pivot = None
        for i in range(r, m):
            if A[i][c]:
                pivot = i
                break
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        pv = A[r][c]
        A[r] = [v / pv for v in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                f = A[i][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r

def weak_system(mask):
    A = points(mask)
    dA = diff_mask(mask)
    M = []
    augmented = []

    row = [0] * N
    row[0] = 1
    M.append(row)
    augmented.append(row + [1])

    for x in range(N):
        row = [0] * N
        for a in A:
            row[x ^ a] += 1
        M.append(row)
        augmented.append(row + [1])

    for z in range(1, N):
        if (dA >> z) & 1:
            row = [0] * N
            row[z] = 1
            M.append(row)
            augmented.append(row + [0])

    return M, augmented

group = generated_group()
assert len(group) == (16 - 1) * (16 - 2) * (16 - 4) * (16 - 8) == 20160

orbits = orbit_partition()
assert len(orbits) == 46

orbit_stats = {}
tile_reps = 0
nontile_reps = 0
normalized_tile_count = 0
rank_gaps = []

for orbit in orbits:
    rep = orbit[0]
    is_tile, witness = tiles(rep)
    k = rep.bit_count()
    orbit_stats.setdefault(k, [0, 0, 0])
    orbit_stats[k][0] += 1
    if is_tile:
        tile_reps += 1
        orbit_stats[k][1] += 1
        normalized_tile_count += len(orbit)
        assert witness is not None
        assert rep.bit_count() * witness.bit_count() == N
        assert (diff_mask(rep) & diff_mask(witness)) == 1
    else:
        nontile_reps += 1
        orbit_stats[k][2] += 1
        M, Aug = weak_system(rep)
        r = exact_rank(M)
        ra = exact_rank(Aug)
        assert ra == r + 1
        rank_gaps.append((rep, r, ra))

assert tile_reps == 9
assert nontile_reps == 37
assert normalized_tile_count == 1867

expected_stats = {
    1: [1, 1, 0],
    2: [1, 1, 0],
    3: [1, 0, 1],
    4: [2, 2, 0],
    5: [3, 0, 3],
    6: [4, 0, 4],
    7: [5, 0, 5],
    8: [6, 4, 2],
    9: [6, 0, 6],
    10: [5, 0, 5],
    11: [4, 0, 4],
    12: [3, 0, 3],
    13: [2, 0, 2],
    14: [1, 0, 1],
    15: [1, 0, 1],
    16: [1, 1, 0],
}
assert orbit_stats == expected_stats

# The exact normalized tile census by size follows from orbit sizes.
tile_counts = {1: 0, 2: 0, 4: 0, 8: 0, 16: 0}
for orbit in orbits:
    rep = orbit[0]
    is_tile, _ = tiles(rep)
    if is_tile:
        tile_counts[rep.bit_count()] += len(orbit)
assert tile_counts == {1: 1, 2: 15, 4: 455, 8: 1395, 16: 1}

print("GL_SIZE=20160")
print("NORMALIZED_SUBSETS=32768")
print("ORBITS=46")
print("TILING_ORBITS=9")
print("NONTILING_ORBITS=37")
print("NORMALIZED_TILES=1867")
print("TILE_COUNTS_BY_SIZE=" + repr(tile_counts))
print("VERIFY_OK")
