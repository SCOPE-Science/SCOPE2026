#!/usr/bin/env python3
from itertools import combinations
from fractions import Fraction

EXPECTED_PARTITION_COUNTS = {2:2, 3:3, 4:5, 5:7, 6:11, 7:15}
EXPECTED_REVERSALS = {2:0, 3:0, 4:0, 5:0, 6:0, 7:2}
EXPECTED_ORDER_MISMATCHES = {2:0, 3:0, 4:0, 5:0, 6:2, 7:4}

def recursive_partitions(n, cap=None):
    if cap is None:
        cap = n
    if n == 0:
        yield ()
        return
    for first in range(min(cap, n), 0, -1):
        for rest in recursive_partitions(n-first, first):
            yield (first,) + rest

def composition_partitions(n):
    # Independent construction: every composition corresponds to a subset
    # of the n-1 gaps between n unit objects; sort its parts to forget labels.
    out = set()
    for cuts_mask in range(1 << (n-1)):
        parts = []
        run = 1
        for gap in range(n-1):
            if (cuts_mask >> gap) & 1:
                parts.append(run)
                run = 1
            else:
                run += 1
        parts.append(run)
        out.add(tuple(sorted(parts, reverse=True)))
    return out

def shannon_product(part):
    # For fixed total N:
    # H(part) = log N - (1/N) log(prod_j n_j^{n_j}).
    # Thus a smaller integer product means larger Shannon diversity.
    p = 1
    for x in part:
        p *= x ** x
    return p

def simpson_collision_sum(part):
    # Tothmeresz's finite-sample Simpson diversity is
    # D = 1 - sum n_j(n_j-1)/(N(N-1)).
    # For fixed N, smaller collision sum means larger D.
    return sum(x*(x-1) for x in part)

def simpson_diversity(part):
    n = sum(part)
    return Fraction(n*(n-1)-simpson_collision_sum(part), n*(n-1))

all_reversals = {}
for n in range(2, 8):
    rparts = set(recursive_partitions(n))
    cparts = composition_partitions(n)
    assert rparts == cparts
    assert len(rparts) == EXPECTED_PARTITION_COUNTS[n]

    rev = []
    mismatch = []
    parts = sorted(rparts, reverse=True)
    for a,b in combinations(parts, 2):
        pa,pb = shannon_product(a), shannon_product(b)
        qa,qb = simpson_collision_sum(a), simpson_collision_sum(b)
        sh = (pb > pa) - (pb < pa)  # sign of H(a)-H(b)
        sd = (qb > qa) - (qb < qa)  # sign of D(a)-D(b)
        if sh != sd:
            mismatch.append((a,b,sh,sd))
        if sh*sd < 0:
            rev.append((a,b))
    all_reversals[n] = rev
    assert len(rev) == EXPECTED_REVERSALS[n]
    assert len(mismatch) == EXPECTED_ORDER_MISMATCHES[n]

expected7 = {
    ((5,1,1),(4,3)),
    ((4,1,1,1),(3,2,2)),
}
observed7 = {tuple(sorted((a,b), reverse=True)) for a,b in all_reversals[7]}
canonical_expected7 = {tuple(sorted(pair, reverse=True)) for pair in expected7}
assert observed7 == canonical_expected7

# Exact witness inequalities.
A=(5,1,1); B=(4,3)
C=(4,1,1,1); D=(3,2,2)

assert shannon_product(A) == 5**5 == 3125
assert shannon_product(B) == 4**4 * 3**3 == 6912
assert shannon_product(A) < shannon_product(B)
assert simpson_diversity(A) == Fraction(11,21)
assert simpson_diversity(B) == Fraction(4,7)
assert simpson_diversity(A) < simpson_diversity(B)

assert shannon_product(C) == 4**4 == 256
assert shannon_product(D) == 3**3 * 2**4 == 432
assert shannon_product(C) < shannon_product(D)
assert simpson_diversity(C) == Fraction(5,7)
assert simpson_diversity(D) == Fraction(16,21)
assert simpson_diversity(C) < simpson_diversity(D)

# Population Gini-Simpson, 1-sum p_i^2, has the same ordering at fixed N.
def gini_simpson(part):
    n=sum(part)
    return Fraction(n*n-sum(x*x for x in part), n*n)

for n in range(2,8):
    parts=list(recursive_partitions(n))
    for a,b in combinations(parts,2):
        s1=simpson_diversity(a)-simpson_diversity(b)
        s2=gini_simpson(a)-gini_simpson(b)
        assert (s1 > 0) == (s2 > 0)
        assert (s1 < 0) == (s2 < 0)

print("VERIFY_OK")
print("partition_counts", EXPECTED_PARTITION_COUNTS)
print("order_mismatch_counts", EXPECTED_ORDER_MISMATCHES)
print("reversal_counts", EXPECTED_REVERSALS)
print("first_reversal_pairs", sorted(observed7))
print("n6_tie_split_pairs", [((4,1,1),(3,3)), ((3,1,1,1),(2,2,2))])
print("A_B_products", shannon_product(A), shannon_product(B))
print("A_B_Simpson", simpson_diversity(A), simpson_diversity(B))
print("C_D_products", shannon_product(C), shannon_product(D))
print("C_D_Simpson", simpson_diversity(C), simpson_diversity(D))
