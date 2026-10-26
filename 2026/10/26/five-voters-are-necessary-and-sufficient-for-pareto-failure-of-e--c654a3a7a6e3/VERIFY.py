"""Exact finite check of the first Pareto-inefficient two-seat local PAV profile.

Run using Python 3: python VERIFY.py. No packages required.
The proof of the universal lower bound is in RESULT.md, not inferred from sampling.
"""
from itertools import combinations_with_replacement
from collections import Counter

W = (0, 1)
O = (2, 3)
H2 = (0, 2, 3)  # Twice the harmonic satisfaction of 0, 1, 2 approvals.

def utility(ballot, committee):
    return sum(bool(ballot & (1 << j)) for j in committee)

def score2(ballot, committee):
    return H2[utility(ballot, committee)]

# A Pareto-dominating comparator must weakly improve EVERY ballot.
TYPES = tuple(t for t in range(16) if utility(t, O) >= utility(t, W))
STRICT = tuple(t for t in TYPES if utility(t, O) > utility(t, W))
SWAPS = tuple(tuple(sorted((set(W) - {w}) | {o})) for w in W for o in O)
DELTA = {t: tuple(score2(t, s) - score2(t, W) for s in SWAPS) for t in TYPES}

def profile_valid(p):
    return (any(t in STRICT for t in p)
            and all(sum(DELTA[t][j] for t in p) <= 0 for j in range(4)))

# Exhaustively enumerate MULTISETS, not arbitrary selected examples.
COUNTS = {}
PROFILES5 = []
for n in range(1, 6):
    count = 0
    for p in combinations_with_replacement(TYPES, n):
        if profile_valid(p):
            count += 1
            if n == 5:
                PROFILES5.append(p)
    COUNTS[n] = count
assert COUNTS == {1: 0, 2: 0, 3: 0, 4: 0, 5: 2}, COUNTS

cross = [((1 << w) | (1 << o)) for w in W for o in O]
expected = {
    tuple(sorted(cross + [(1 << w) | (1 << O[0]) | (1 << O[1])]))
    for w in W
}
assert set(PROFILES5) == expected
for p in PROFILES5:
    assert sum(score2(t, W) for t in p) == 10
    assert sum(score2(t, O) for t in p) == 11
    assert sorted(sum(DELTA[t][j] for t in p) for j in range(4)) == [-1, -1, 0, 0]
    assert Counter((utility(t, W), utility(t, O)) for t in p) == {(1, 1): 4, (1, 2): 1}

# Verify the exact swap-sum contributions underlying the general proof.
expected_sums = {(0, 0): 0, (0, 1): 4, (0, 2): 8,
                 (1, 1): -1, (1, 2): 2, (2, 2): 0}
for t in TYPES:
    kind = utility(t, W), utility(t, O)
    assert sum(DELTA[t]) == expected_sums[kind], (t, kind)

print('PASS: exhaustive 4-candidate Pareto-compatible multiset census')
print('Counts for voter numbers 1..5:', COUNTS)
print('Exactly two labeled 5-voter profiles, one orbit under swapping selected candidates.')
print('Witness: PAV(W)=5, PAV(O)=11/2; four swap gains are -1/2,-1/2,0,0.')
print('Note: the general candidate-count theorem follows from the analytic proof.')
