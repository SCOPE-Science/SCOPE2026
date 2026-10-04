#!/usr/bin/env python3
from collections import Counter
from itertools import combinations

N = 17
K = 8
# Binary cyclic [17,8,6] quadratic-residue code.
# g(x)=1+x+x^3+x^6+x^8+x^9; rows are x^j g(x), j=0,...,7.
g_positions = (0,1,3,6,8,9)
rows = []
for j in range(K):
    m = 0
    for e in g_positions:
        m |= 1 << (e+j)
    rows.append(m)

def gf2_rank(vs, nbits):
    a = list(vs)
    r = 0
    for b in range(nbits-1, -1, -1):
        p = next((i for i in range(r, len(a)) if (a[i] >> b) & 1), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        for i in range(len(a)):
            if i != r and ((a[i] >> b) & 1):
                a[i] ^= a[r]
        r += 1
    return r

assert gf2_rank(rows, N) == 8

# Primal minimum distance.
primal = []
for a in range(1 << K):
    w = 0
    for j, row in enumerate(rows):
        if (a >> j) & 1:
            w ^= row
    primal.append(w)
nonzero_weights = [x.bit_count() for x in primal if x]
assert len(set(primal)) == 256
assert min(nonzero_weights) == 6

# Dual code C^perp and its exact low-weight incidence.
dual = []
for x in range(1 << N):
    if all((x & row).bit_count() % 2 == 0 for row in rows):
        dual.append(x)
assert len(dual) == 512
dual_wd = Counter(x.bit_count() for x in dual)
assert min(w for w,c in dual_wd.items() if w and c) == 5
assert dual_wd[5] == 34

w5 = [x for x in dual if x.bit_count() == 5]
pair_incidence = Counter()
for i,j in combinations(range(N), 2):
    c = sum(1 for x in w5 if ((x >> i) & 1) and ((x >> j) & 1))
    pair_incidence[c] += 1
assert max(pair_incidence) == 3
assert pair_incidence == Counter({2:68, 3:68})

# Pure integer lemma used in the proof:
# six positive set sizes with total <=17 and every pair-sum >=5
# must, after sorting, be exactly (2,3,3,3,3,3).
tuples = []
for a1 in range(1,18):
    for a2 in range(a1,18):
        for a3 in range(a2,18):
            for a4 in range(a3,18):
                for a5 in range(a4,18):
                    for a6 in range(a5,18):
                        aa=(a1,a2,a3,a4,a5,a6)
                        if sum(aa) <= 17 and all(aa[i]+aa[j] >= 5 for i,j in combinations(range(6),2)):
                            tuples.append(aa)
assert tuples == [(2,3,3,3,3,3)]

# Why this rules out six disjoint recovery sets in every generator basis:
# if r_1,...,r_6 have the same nonzero syndrome, then r_i+r_j is a
# nonzero dual word. Disjointness makes its weight |r_i|+|r_j|>=5.
# The size lemma forces one size-2 set A and five size-3 sets B_j.
# Each A union B_j is then a distinct dual word of weight 5 containing A,
# requiring five weight-5 dual words through one coordinate pair.
# The exact incidence computation above gives at most three.

print("VERIFY_OK rank=8 primal_d=6 dual_size=512 dual_d=5 dual_w5=34 pair_incidence=2:68,3:68 obstruction=6-recovery")
