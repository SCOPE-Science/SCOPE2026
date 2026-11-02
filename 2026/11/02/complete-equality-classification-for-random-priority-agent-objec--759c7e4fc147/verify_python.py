"""Independent exact enumeration reduced only by object-label symmetry.

Each of the 24 rankings of three objects and the outside option appears once
per agent. Fixing the first agent's order of the three objects to a,b,c is a
sixfold quotient with no stabilizers. The insertion point of the outside
option remains free (four possibilities). Thus exactly 4*24**3 profiles are
examined here, independently of the full C++ enumeration.
"""
from itertools import permutations, product
from collections import Counter

OUT = 3
objects = (0, 1, 2)
ALL_RANKINGS = tuple(permutations((0, 1, 2, OUT)))
PRIORITIES = tuple(permutations(range(4)))
FIRST = tuple(tuple((0, 1, 2)[:j] + (OUT,) + (0, 1, 2)[j:]) for j in range(4))

# A direct, separately written simulator: each priority maintains a list of
# still available objects; another agent may stay unmatched when OUT appears.
def waste_numerator(profile):
    none_counts = [0, 0, 0, 0]
    free_counts = [0, 0, 0]
    for priority in PRIORITIES:
        available = [0, 1, 2]
        for i in priority:
            chosen = next((x for x in profile[i] if x == OUT or x in available), OUT)
            if chosen == OUT:
                none_counts[i] += 1
            else:
                available.remove(chosen)
        for obj in available:
            free_counts[obj] += 1
    attainable = []
    for i, row in enumerate(profile):
        for obj in row[:row.index(OUT)]:
            attainable.append((min(none_counts[i], free_counts[obj]), i, obj))
    best = max((t[0] for t in attainable), default=0)
    witnesses = [(i, obj) for z, i, obj in attainable if z == best and z > 0]
    return best, witnesses, tuple(none_counts), tuple(free_counts)

hist = Counter()
extremal_count = 0
witness_multiplicities = Counter()
for profile in product(FIRST, ALL_RANKINGS, ALL_RANKINGS, ALL_RANKINGS):
    score, witnesses, _, _ = waste_numerator(profile)
    hist[score] += 1
    if score == 4:
        extremal_count += 1
        witness_multiplicities[len(witnesses)] += 1

assert sum(hist.values()) == 4 * 24**3 == 55296
assert [hist[x] for x in range(5)] == [52944, 288, 840, 1152, 72]
assert all(hist[x] == 0 for x in range(5, 25))
assert extremal_count == 72
assert witness_multiplicities == {1: 72}

# Independently verify the six claimed canonical orbit representatives and
# their common unmatched marginal vector, without depending on the C++ code.
patterns = (
    ((0, 1, OUT, 2), (0, 1, OUT, 2), (0, 2, OUT, 1), (1, 0, 2, OUT)),
    ((0, 1, OUT, 2), (0, 1, OUT, 2), (0, 2, OUT, 1), (1, 2, OUT, 0)),
    ((0, 1, OUT, 2), (0, 1, OUT, 2), (0, 2, OUT, 1), (1, 2, 0, OUT)),
    ((0, 1, OUT, 2), (0, 1, OUT, 2), (0, 2, 1, OUT), (1, 0, 2, OUT)),
    ((0, 1, OUT, 2), (0, 1, OUT, 2), (0, 2, 1, OUT), (1, 2, OUT, 0)),
    ((0, 1, OUT, 2), (0, 1, OUT, 2), (0, 2, 1, OUT), (1, 2, 0, OUT)),
)
# The six normal forms also induce identical *individual* allocations at
# each priority, not just the same unassignment marginals.
def outcome_by_priority(profile, priority):
    left = set(objects)
    outcome = [OUT] * 4
    for i in priority:
        for x in profile[i]:
            if x == OUT: break
            if x in left:
                outcome[i] = x
                left.remove(x)
                break
    return tuple(outcome)

reference = tuple(outcome_by_priority(patterns[0], o) for o in PRIORITIES)
for profile in patterns:
    score, witnesses, u, v = waste_numerator(profile)
    assert (score, witnesses, u, v) == (4, [(3, 2)], (11, 11, 2, 4), (0, 0, 4))
    assert tuple(outcome_by_priority(profile, o) for o in PRIORITIES) == reference
print('VERIFY_PY_OK canonical_profiles=55296 times_six=331776',
      'histogram=', dict(sorted(hist.items())), 'unique_extremal_witnesses=', extremal_count)
