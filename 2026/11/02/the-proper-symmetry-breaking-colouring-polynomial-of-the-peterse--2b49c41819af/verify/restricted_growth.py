"""Independent restricted-growth and labelled-colouring certificate for Petersen symmetry breaking."""
from itertools import combinations, permutations
from collections import Counter

v = tuple(combinations(range(5), 2))
adjacency = [[int(set(v[i]).isdisjoint(v[j])) for j in range(10)] for i in range(10)]
assert sum(sum(row) for row in adjacency) == 30
permute = [tuple(v.index(tuple(sorted((p[a],p[b])))) for a,b in v)
           for p in permutations(range(5))]
assert len(set(permute)) == 120

hist = Counter()
word = [0] * 10

def rg(i, used):
    if i == 10:
        fixing = sum(all(word[j] == word[p[j]] for j in range(10)) for p in permute)
        hist[used, fixing] += 1
        return
    for label in range(used + 1):
        if any(adjacency[i][j] and word[j] == label for j in range(i)):
            continue
        word[i] = label
        rg(i + 1, max(used, label + 1))

rg(1, 1)
expected_hist = {
(3,6):20,(4,1):160,(4,2):350,(4,6):10,(5,1):1844,(5,2):400,
(6,1):2745,(6,2):120,(7,1):1425,(7,2):10,(8,1):315,(9,1):30,(10,1):1}
assert dict(hist) == expected_hist

# Independently scan all proper maps to a named palette of four colours,
# without canonicalizing colour classes.
assigned = [-1] * 10
palette_counts = Counter()

def labels(i):
    if i == 10:
        fixing = sum(all(assigned[j] == assigned[p[j]] for j in range(10)) for p in permute)
        palette_counts[fixing] += 1
        return
    for label in range(4):
        if any(adjacency[i][j] and assigned[j] == label for j in range(i)):
            continue
        assigned[i] = label
        labels(i + 1)

labels(0)
assert dict(palette_counts) == {1:3840,2:8400,6:720}
assert sum(palette_counts.values()) == 12960

# An independent identity check: all proper-colouring partition counts
# reconstruct the established Petersen chromatic polynomial.
proper = [sum(n for (k,s),n in hist.items() if k == j) for j in range(11)]
distinguished = [hist[j,1] for j in range(11)]
def coefficient_array(seq):
    poly = [0]*11
    falling = [1]
    for k, count in enumerate(seq):
        for deg, a in enumerate(falling):
            poly[deg] += count*a
        # multiply by (q-k)
        out=[0]*(len(falling)+1)
        for deg,a in enumerate(falling):
            out[deg] -= k*a
            out[deg+1] += a
        falling = out
    return poly
chrom = [0,-704,2606,-4305,4275,-2861,1353,-455,105,-15,1]
break_poly = [0,-984,3466,-5405,5065,-3211,1443,-465,105,-15,1]
assert coefficient_array(proper) == chrom
assert coefficient_array(distinguished) == break_poly

# The ten symbol transpositions are exactly the nonidentity permutations
# with seven orbits on Petersen vertices. All others have at most six.
cycle_orbits = Counter()
for p in permute:
    seen = set()
    cycles = 0
    for i in range(10):
        if i not in seen:
            cycles += 1
            j = i
            while j not in seen:
                seen.add(j)
                j = p[j]
    cycle_orbits[cycles] += 1
assert dict(cycle_orbits) == {10:1,7:10,6:15,4:20,3:50,2:24}
print('RG_VERIFIER_PASS: 7430 partitions; independent named-palette scan', dict(palette_counts))
print('EXACT_CHROMATIC_AND_DISTINGUISHING_POLYNOMIALS_PASS')
print('SYMMETRY_ORBIT_CYCLES_PASS',dict(cycle_orbits))
