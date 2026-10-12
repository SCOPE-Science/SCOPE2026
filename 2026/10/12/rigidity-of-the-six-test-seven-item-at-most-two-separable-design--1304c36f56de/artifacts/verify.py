from itertools import permutations
from hashlib import sha256

N = 6
COLS = list(range(1, 1 << N))

def enumerate_target(k, collect=True):
    solutions = []
    nodes = 0
    def rec(chosen, used_outputs, start):
        nonlocal nodes
        nodes += 1
        need = k - len(chosen)
        if len(COLS) - start < need:
            return
        if need == 0:
            solutions.append(tuple(chosen) if collect else 1)
            return
        max_index = len(COLS) - need
        for index in range(start, max_index + 1):
            x = COLS[index]
            if x in used_outputs:
                continue
            new_outputs = {x}
            ok = True
            for c in chosen:
                y = x | c
                if y in used_outputs or y in new_outputs:
                    ok = False
                    break
                new_outputs.add(y)
            if not ok:
                continue
            rec(chosen + [x], used_outputs | new_outputs, index + 1)
    rec([], set(), 0)
    return solutions, nodes

def direct_check(family):
    outputs = list(family)
    for i in range(len(family)):
        for j in range(i + 1, len(family)):
            outputs.append(family[i] | family[j])
    return len(outputs) == len(set(outputs)) == len(family) + len(family) * (len(family) - 1) // 2

def permute_mask(x, p):
    y = 0
    for i in range(N):
        if (x >> i) & 1:
            y |= 1 << p[i]
    return y

def bitstring(x):
    return format(x, '06b')

maxima, nodes7 = enumerate_target(7, True)
target8, nodes8 = enumerate_target(8, False)
assert len(maxima) == 30
assert len(target8) == 0
assert all(direct_check(f) for f in maxima)

maximum_set = set(maxima)
representative = min(maxima)
orbit = set()
for p in permutations(range(N)):
    orbit.add(tuple(sorted(permute_mask(x, p) for x in representative)))
assert orbit == maximum_set
assert len(orbit) == 30
stabilizer = 720 // len(orbit)
assert stabilizer == 24

for family in maxima:
    weights = sorted(x.bit_count() for x in family)
    assert weights == [2, 2, 2, 3, 3, 3, 3]
    pairs = [x for x in family if x.bit_count() == 2]
    triples = [x for x in family if x.bit_count() == 3]
    assert len(pairs) == 3 and len(triples) == 4
    assert all((pairs[i] & pairs[j]) == 0 for i in range(3) for j in range(i + 1, 3))
    assert (pairs[0] | pairs[1] | pairs[2]) == (1 << N) - 1
    for t in triples:
        assert all((t & p).bit_count() == 1 for p in pairs)
    base = triples[0]
    parity = []
    for t in triples:
        flips = sum((t & p) != (base & p) for p in pairs)
        parity.append(flips % 2)
    assert len(set(parity)) == 1

    extended = [x | (1 << N) for x in pairs] + triples
    pair_counts = {}
    for block in extended:
        points = [i for i in range(N + 1) if (block >> i) & 1]
        assert len(points) == 3
        for a in range(3):
            for b in range(a + 1, 3):
                key = tuple(sorted((points[a], points[b])))
                pair_counts[key] = pair_counts.get(key, 0) + 1
    assert len(pair_counts) == 21 and set(pair_counts.values()) == {1}

census_bytes = '\n'.join(','.join(bitstring(x) for x in f) for f in sorted(maxima)).encode('ascii')
canonical = ';'.join(bitstring(x) for x in representative)
print(
    'VERIFY_OK',
    f'nodes7={nodes7}',
    f'nodes8={nodes8}',
    'maximum=7',
    'labeled_row_families=30',
    'fully_labeled_matrices=151200',
    'row_group=720',
    'orbits=1',
    'orbit_size=30',
    'stabilizer=24',
    'weights=2x3,3x4',
    f'canonical={canonical}',
    f'census_sha256={sha256(census_bytes).hexdigest()}'
)
