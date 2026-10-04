from itertools import combinations, permutations, product
from math import prod

# Projective representatives of real flat sign lines in R^5.
V = [(1,) + b for b in product((-1, 1), repeat=4)]
INDEX = {v:i for i,v in enumerate(V)}


def det_bareiss(a):
    a = [list(map(int,row)) for row in a]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    prev = 1
    for k in range(n-1):
        if a[k][k] == 0:
            r = next((r for r in range(k+1,n) if a[r][k] != 0), None)
            if r is None:
                return 0
            a[k], a[r] = a[r], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                a[i][j] = (a[i][j]*pivot - a[i][k]*a[k][j]) // prev
        prev = pivot
        for i in range(k+1,n):
            a[i][k] = 0
        for j in range(k+1,n):
            a[k][j] = 0
    return sign*a[n-1][n-1]


def det_of(indices):
    return det_bareiss([V[i] for i in indices])

# Every five-subset determinant, exactly.
D5 = {J:det_of(J) for J in combinations(range(16),5)}

def full_spark(S):
    return all(D5[J] != 0 for J in combinations(S,5))

# A 7-set would already certify a larger full-spark subset, so ruling out all
# 7-sets proves the upper bound 6 for every subset of the 16 projective lines.
full7 = [S for S in combinations(range(16),7) if full_spark(S)]
assert full7 == []
full6 = [S for S in combinations(range(16),6) if full_spark(S)]
assert len(full6) == 1088

# Explicit lower-bound witness.
W = (0,1,2,4,8,15)
assert full_spark(W)
witness_dets = [D5[J] for J in combinations(W,5)]
assert witness_dets == [16,16,-16,16,-16,-48]

# Signed coordinate permutations, modulo the global sign, acting on projective lines.
def canon(v):
    v = tuple(v)
    if v[0] == -1:
        v = tuple(-x for x in v)
    return v

actions = set()
for p in permutations(range(5)):
    for s_tail in product((-1,1), repeat=4):
        s = (1,) + s_tail  # quotient the global sign
        image = []
        for v in V:
            w = tuple(s[j]*v[p[j]] for j in range(5))
            image.append(INDEX[canon(w)])
        actions.add(tuple(image))
assert len(actions) == 1920

remaining = set(full6)
orbits = []
while remaining:
    S = next(iter(remaining))
    orb = {tuple(sorted(a[i] for i in S)) for a in actions}
    orb &= remaining
    orbits.append((S,len(orb)))
    remaining -= orb
orbit_sizes = sorted(size for _,size in orbits)
assert orbit_sizes == [16,160,192,240,480]
assert sum(orbit_sizes) == 1088

print('VERIFY_OK projective_lines=16 max_full_spark=6 full_spark_6sets=1088 symmetry_group=1920 orbits=5 orbit_sizes=' + ','.join(map(str,orbit_sizes)))
print('WITNESS', W, 'DETS', ','.join(map(str,witness_dets)))
