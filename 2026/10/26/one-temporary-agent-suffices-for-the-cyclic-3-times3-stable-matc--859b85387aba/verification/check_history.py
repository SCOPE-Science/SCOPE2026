#!/usr/bin/env python3
"""Exact finite verification for a one-temporary-agent stable-marriage history."""
from itertools import product

NONE = -1
M = (0, 1, 2)
W = (3, 4, 5)
A = 6  # one temporary woman
MEN = set(M)
WOMEN = set(W) | {A}
ORIGINAL = set(M) | set(W)

# Each list is best-to-worst and includes NONE at the correct acceptability cutoff.
PREF = {
    0: [3, 4, A, 5, NONE],       # m1: w1 > w2 > a > w3 > unmatched
    1: [4, A, 5, 3, NONE],       # m2: w2 > a > w3 > w1 > unmatched
    2: [5, A, 3, 4, NONE],       # m3: w3 > a > w1 > w2 > unmatched
    3: [1, 2, 0, NONE],          # w1: m2 > m3 > m1 > unmatched
    4: [2, 0, 1, NONE],          # w2: m3 > m1 > m2 > unmatched
    5: [0, 1, 2, NONE],          # w3: m1 > m2 > m3 > unmatched
    6: [0, NONE, 1, 2],          # a accepts only m1
}
RANK = {x: {v: i for i, v in enumerate(lst)} for x, lst in PREF.items()}
SIDE = {x: ('M' if x in MEN else 'W') for x in PREF}

# Restricting each original list to original partners and the unmatched option
# recovers the original market exactly; the temporary insertion changes no
# relative ranking among original partners.
BASE_PREF = {
    0: [3, 4, 5, NONE], 1: [4, 5, 3, NONE], 2: [5, 3, 4, NONE],
    3: [1, 2, 0, NONE], 4: [2, 0, 1, NONE], 5: [0, 1, 2, NONE],
}
for agent, base in BASE_PREF.items():
    original_side = set(W) if agent in MEN else MEN
    projected = [x for x in PREF[agent] if x == NONE or x in original_side]
    assert projected == base, (agent, projected, base)
MU_A = tuple(sorted(((0, 3), (1, 4), (2, 5))))
MU_0 = tuple(sorted(((0, 4), (1, 5), (2, 3))))
MU_B = tuple(sorted(((0, 5), (1, 3), (2, 4))))

def mate(matching, x):
    for m, w in matching:
        if x == m: return w
        if x == w: return m
    return NONE

def prefers(x, y, z):
    return RANK[x][y] < RANK[x][z]

def stable(active, matching):
    for m, w in matching:
        if not prefers(m, w, NONE) or not prefers(w, m, NONE):
            return False
    pm = {x: mate(matching, x) for x in active}
    for m in active & MEN:
        for w in active & WOMEN:
            if pm[m] == w:
                continue
            if prefers(m, w, pm[m]) and prefers(w, m, pm[w]):
                return False
    return True

def all_matchings(active):
    men = sorted(active & MEN)
    women = sorted(active & WOMEN)
    out = []
    def rec(i, used, pairs):
        if i == len(men):
            out.append(tuple(sorted(pairs)))
            return
        m = men[i]
        rec(i + 1, used, pairs)  # unmatched
        for w in women:
            if w not in used:
                rec(i + 1, used | {w}, pairs + [(m, w)])
    rec(0, set(), [])
    return out

def stable_matchings(active):
    return sorted(set(x for x in all_matchings(active) if stable(active, x)))

def proposal_chain(active, matching, proposer):
    """Return the stable matching after a single entrant/abandoned partner proposes."""
    pairs = list(matching)
    rejected = {x: set() for x in active}
    p = proposer
    steps = []
    while True:
        assert mate(tuple(pairs), p) == NONE, (p, pairs)
        choices = [x for x in PREF[p]
                   if x != NONE and x in active and SIDE[x] != SIDE[p]
                   and x not in rejected[p] and prefers(p, x, NONE)]
        accepted = False
        for x in choices:
            old = mate(tuple(pairs), x)
            if prefers(x, p, old):
                if old != NONE:
                    pairs = [(m, w) for m, w in pairs
                             if not ((m == old and w == x) or (m == x and w == old))]
                pairs.append((p, x) if SIDE[p] == 'M' else (x, p))
                steps.append((p, x, 'accept', old))
                if old == NONE:
                    return tuple(sorted(pairs)), steps
                p = old
                accepted = True
                break
            rejected[p].add(x)
            steps.append((p, x, 'reject', old))
        if not accepted:
            return tuple(sorted(pairs)), steps

def enter(active, matching, x):
    new_active = active | {x}
    new_matching, steps = proposal_chain(new_active, matching, x)
    assert stable(new_active, new_matching), ('unstable after entry', x, new_matching)
    return new_active, new_matching, steps

def exit_agent(active, matching, x):
    new_active = active - {x}
    old = mate(matching, x)
    restricted = tuple((m, w) for m, w in matching if m != x and w != x)
    if old != NONE:
        new_matching, steps = proposal_chain(new_active, restricted, old)
    else:
        new_matching, steps = restricted, []
    assert stable(new_active, new_matching), ('unstable after exit', x, new_matching)
    return new_active, new_matching, steps

# Exact stable-set and predecessor obstruction checks for the original 3x3 market.
full = set(ORIGINAL)
assert set(stable_matchings(full)) == {MU_A, MU_0, MU_B}
# Correct the explicit tuples in a normalized form for all six codimension-one markets.
expected_missing = {
    0: tuple(sorted(((1, 4), (2, 5)))),
    1: tuple(sorted(((2, 5), (0, 3)))),
    2: tuple(sorted(((0, 3), (1, 4)))),
    3: tuple(sorted(((0, 5), (2, 4)))),
    4: tuple(sorted(((1, 3), (0, 5)))),
    5: tuple(sorted(((2, 4), (1, 3)))),
}
for missing in sorted(ORIGINAL):
    active = full - {missing}
    sms = stable_matchings(active)
    assert len(sms) == 1, (missing, sms)
    assert sms[0] == expected_missing[missing], (missing, sms[0], expected_missing[missing])
    reached, _ = proposal_chain(full, sms[0], missing)
    expected = MU_A if missing in MEN else MU_B
    assert reached == expected, (missing, reached, expected)

# Explicit eight-event history, with the final temporary entrant's proposal chain shown.
active = set()
matching = tuple()
for x in (0, 1, 2, 3, 4, 5):
    active, matching, _ = enter(active, matching, x)
assert matching == MU_B
active, matching, steps = enter(active, matching, A)
assert matching == MU_0 and A not in {v for pair in matching for v in pair}
# The last entrant's chain must include the expected rejection/acceptance sequence.
# Proposal events: a->m1 accepted; w3->m1 rejected, w3->m2 accepted;
# w1->m2 rejected, w1->m3 accepted; w2->m3 rejected, w2->m1 accepted;
# a->m1 rejected.
expected_steps = [
    (6, 0, 'accept', 5),
    (5, 0, 'reject', 6),
    (5, 1, 'accept', 3),
    (3, 1, 'reject', 5),
    (3, 2, 'accept', 4),
    (4, 2, 'reject', 3),
    (4, 0, 'accept', 6),
    (6, 0, 'reject', 4),
]
assert steps == expected_steps, steps
assert stable(active, matching)
active, matching, steps = exit_agent(active, matching, A)
assert matching == MU_0 and active == full and not steps
assert stable(active, matching)
print('PASS: exactly three stable matchings; all six five-agent submarkets have unique stable matchings; every terminal-agent final-entry transition misses the middle matching; one temporary woman realizes it; the minimum temporary-agent count is exactly 1.')
print('Temporary-entry proposal chain:', ' -> '.join(f'{p}:{x}:{act}' for p,x,act,_ in expected_steps))
