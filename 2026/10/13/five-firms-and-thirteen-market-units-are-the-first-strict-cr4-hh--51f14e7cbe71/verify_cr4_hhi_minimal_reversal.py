#!/usr/bin/env python3
from itertools import combinations

EXPECTED_PARTITION_COUNTS = {5:1,6:1,7:2,8:3,9:5,10:7,11:10,12:13,13:18}
EXPECTED_REVERSALS = {5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:2}
EXPECTED_PAIRS = {
    tuple(sorted(((5,2,2,2,2),(4,3,3,2,1)), reverse=True)),
    tuple(sorted(((5,2,2,2,2),(3,3,3,3,1)), reverse=True)),
}

def recursive_partitions(total, k, cap=None, prefix=()):
    if cap is None:
        cap = total
    if k == 1:
        if 1 <= total <= cap:
            yield prefix + (total,)
        return
    for x in range(min(cap, total-(k-1)), 0, -1):
        yield from recursive_partitions(total-x, k-1, x, prefix+(x,))

def composition_partitions(total, k):
    out = set()
    def rec(rem, slots, prefix):
        if slots == 1:
            if rem >= 1:
                out.add(tuple(sorted(prefix+(rem,), reverse=True)))
            return
        for x in range(1, rem-(slots-1)+1):
            rec(rem-x, slots-1, prefix+(x,))
    rec(total, k, ())
    return out

def hhi_num(p):
    return sum(x*x for x in p)

def cr4_num(p):
    # With five firms and total S, CR4 = (S-min(p))/S.
    return sum(p)-p[-1]

def strict_reversal(a,b):
    dc = (cr4_num(a)>cr4_num(b)) - (cr4_num(a)<cr4_num(b))
    dh = (hhi_num(a)>hhi_num(b)) - (hhi_num(a)<hhi_num(b))
    return dc*dh < 0

tables = {}
for S in range(5,14):
    p1 = set(recursive_partitions(S,5))
    p2 = composition_partitions(S,5)
    assert p1 == p2
    assert len(p1) == EXPECTED_PARTITION_COUNTS[S]
    rev = set()
    for a,b in combinations(sorted(p1, reverse=True),2):
        if strict_reversal(a,b):
            rev.add(tuple(sorted((a,b), reverse=True)))
    assert len(rev) == EXPECTED_REVERSALS[S]
    tables[S] = rev

assert tables[13] == EXPECTED_PAIRS

A=(5,2,2,2,2)
B=(4,3,3,2,1)
C=(3,3,3,3,1)
assert sum(A)==sum(B)==sum(C)==13
assert cr4_num(A)==11 and cr4_num(B)==12 and cr4_num(C)==12
assert hhi_num(A)==41 and hhi_num(B)==39 and hhi_num(C)==37

# Extremal lower-bound check used in the proof.
# For S<=12, a reversal must compare min=2 to min=1:
# max HHI at min>=2 versus min HHI at min=1.
def max_hhi_min_ge_2(S):
    vals=[hhi_num(p) for p in recursive_partitions(S,5) if p[-1]>=2]
    return max(vals) if vals else None

def min_hhi_min_eq_1(S):
    vals=[hhi_num(p) for p in recursive_partitions(S,5) if p[-1]==1]
    return min(vals) if vals else None

for S in range(10,13):
    assert max_hhi_min_ge_2(S) <= min_hhi_min_eq_1(S)
assert max_hhi_min_ge_2(13) == 41
assert min_hhi_min_eq_1(13) == 37

# Two infinite reversal families extending the two boundary pairs.
for x in range(5,501):
    A=(x,2,2,2,2)
    B=(x-1,3,3,2,1)
    C=(x-2,3,3,3,1)
    assert sum(A)==sum(B)==sum(C)==x+8
    assert cr4_num(B)>cr4_num(A) and hhi_num(A)>hhi_num(B)
    assert cr4_num(C)>cr4_num(A) and hhi_num(A)>hhi_num(C)
    assert hhi_num(A)-hhi_num(B) == 2*x-8
    assert hhi_num(A)-hhi_num(C) == 4*x-16

print("VERIFY_OK")
print("partition_counts", EXPECTED_PARTITION_COUNTS)
print("reversal_counts", EXPECTED_REVERSALS)
print("boundary_pairs", sorted(EXPECTED_PAIRS))
print("boundary_CR4_numerators", cr4_num((5,2,2,2,2)), cr4_num((4,3,3,2,1)), cr4_num((3,3,3,3,1)))
print("boundary_HHI_numerators", 41,39,37)
print("families_checked_x_5_to_500")
