#!/usr/bin/env python3
from itertools import combinations

def partitions(n, minimum=1):
    if n == 0:
        yield ()
        return
    for first in range(minimum, n + 1):
        if first == n:
            yield (first,)
        elif first < n:
            for rest in partitions(n - first, first):
                yield (first,) + rest

def excess_max(part):
    return max(part) if part else 0

def excess_square(part):
    return sum(x*x for x in part)

def profile_from_excess(part, k):
    assert len(part) <= k
    return tuple(sorted([1+x for x in part] + [1]*(k-len(part))))

def bp_num(profile):
    return max(profile)

def simpson_num(profile):
    return sum(x*x for x in profile)

def simpson_finite_num(profile):
    return sum(x*(x-1) for x in profile)

# At fixed total N, the population-form and finite-sample Simpson
# concentration statistics have exactly the same ordering.
for k in range(2, 9):
    for N in range(k, k+12):
        profs = []
        def rec(rem, last, arr):
            if len(arr) == k:
                if rem == 0:
                    profs.append(tuple(arr))
                return
            slots = k-len(arr)
            for x in range(last, rem//slots + 1):
                rec(rem-x, x, arr+[x])
        rec(N, 1, [])
        for a,b in combinations(profs,2):
            ds = simpson_num(a)-simpson_num(b)
            df = simpson_finite_num(a)-simpson_finite_num(b)
            assert ds == df

# Complete partition census of excess units.
reversal_counts = {}
reversal_pairs = {}
for r in range(0, 9):
    ps = list(partitions(r))
    rev = []
    for a,b in combinations(ps,2):
        dm = excess_max(a)-excess_max(b)
        dq = excess_square(a)-excess_square(b)
        if dm*dq < 0:
            rev.append((a,b))
    reversal_counts[r] = len(rev)
    reversal_pairs[r] = rev

assert reversal_counts == {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:4}
assert reversal_pairs[8] == [
    ((1,1,1,1,1,3),(2,2,2,2)),
    ((1,1,1,1,4),(2,3,3)),
    ((1,1,1,5),(4,4)),
    ((1,2,5),(4,4)),
]

# The universal witness works for every fixed number k>=3 of species.
for k in range(3, 101):
    A = profile_from_excess((1,2,5), k)
    B = profile_from_excess((4,4), k)
    N = k+8
    assert sum(A) == sum(B) == N
    assert bp_num(A) == 6
    assert bp_num(B) == 5
    assert simpson_num(A) == k+46
    assert simpson_num(B) == k+48
    assert bp_num(A) > bp_num(B)
    assert simpson_num(A) < simpson_num(B)
    assert simpson_finite_num(A) < simpson_finite_num(B)

# Complete first-layer unlabeled counts for each fixed number of species.
expected = {3:1,4:2,5:3}
for k in range(3, 11):
    profs = [profile_from_excess(p,k) for p in partitions(8) if len(p) <= k]
    profs = sorted(set(profs))
    rev = []
    for a,b in combinations(profs,2):
        if (bp_num(a)-bp_num(b))*(simpson_num(a)-simpson_num(b)) < 0:
            rev.append((a,b))
    target = expected.get(k,4)
    assert len(rev) == target, (k, len(rev), rev)

# Two species never reverse, at any integer resolution tested; the symbolic
# proof is that with larger share p>=1/2, both max(p,1-p)=p and
# p^2+(1-p)^2 are strictly increasing in p.
for N in range(2, 501):
    profs = [(a,N-a) for a in range(1, N//2+1)]
    for a,b in combinations(profs,2):
        assert (bp_num(a)-bp_num(b))*(simpson_num(a)-simpson_num(b)) >= 0

# Extremal bound used in the hand proof.
def qmax(r,m):
    q,s = divmod(r,m)
    return q*m*m + s*s
def qmin(r,m):
    return m*m + (r-m)

for r in range(1,8):
    for m1 in range(1,r):
        for m2 in range(m1+1,r+1):
            assert qmax(r,m1) <= qmin(r,m2)

print("VERIFY_OK")
print("strict_reversal_counts_by_excess", reversal_counts)
print("first_layer_pairs", reversal_pairs[8])
print("fixed_k_first_layer_counts", {k:(1 if k==3 else 2 if k==4 else 3 if k==5 else 4) for k in range(3,11)})
print("three_species_witness_A", profile_from_excess((1,2,5),3))
print("three_species_witness_B", profile_from_excess((4,4),3))
print("universal_k_checked_3_to_100")
