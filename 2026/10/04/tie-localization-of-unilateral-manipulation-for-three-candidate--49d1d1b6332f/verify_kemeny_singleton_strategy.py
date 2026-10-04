#!/usr/bin/env python3
from itertools import permutations

R = list(permutations(range(3)))
PAIRS = ((0,1),(1,2),(2,0))

# Pairwise-margin contribution of each strict ballot for (A>B, B>C, C>A).
VEC = []
for ranking in R:
    pos = {x:i for i,x in enumerate(ranking)}
    VEC.append(tuple(1 if pos[x] < pos[y] else -1 for x,y in PAIRS))

def compositions(n, k=6, prefix=()):
    if k == 1:
        yield prefix + (n,)
        return
    for x in range(n + 1):
        yield from compositions(n-x, k-1, prefix + (x,))

def margins(counts):
    u=v=w=0
    for c,z in zip(counts,VEC):
        u += c*z[0]
        v += c*z[1]
        w += c*z[2]
    return u,v,w

def winners_margin(counts):
    """Kemeny winner set from three pairwise margins."""
    u,v,w = margins(counts)
    # For each proposed top candidate, maximize the pairwise-agreement
    # score over the two rankings having that top candidate.
    top_scores = (
        u - w + abs(v),  # A
        v - u + abs(w),  # B
        w - v + abs(u),  # C
    )
    best = max(top_scores)
    return frozenset(i for i,s in enumerate(top_scores) if s == best)

def winners_direct(counts):
    """Independent Kemeny computation by all six rankings and Kendall distance."""
    score = {}
    for social in R:
        spos = {x:i for i,x in enumerate(social)}
        total = 0
        for c,ballot in zip(counts,R):
            if not c:
                continue
            bpos = {x:i for i,x in enumerate(ballot)}
            d = 0
            for x in range(3):
                for y in range(x+1,3):
                    d += ((spos[x] < spos[y]) != (bpos[x] < bpos[y]))
            total += c*d
        score[social] = total
    best = min(score.values())
    opts = [r for r,s in score.items() if s == best]
    return frozenset(r[0] for r in opts)

def cycle_characterization(counts):
    """Check the three-candidate no-tie characterization used in the proof."""
    u,v,w = margins(counts)
    assert all(z != 0 for z in (u,v,w))
    # Tournament is transitive unless u,v,w have one common sign.
    # With our oriented cycle coordinates, u,v,w>0 is A>B>C>A;
    # u,v,w<0 is the reverse cycle.
    W = winners_margin(counts)
    if not (u>0 and v>0 and w>0) and not (u<0 and v<0 and w<0):
        # identify Condorcet winner directly
        beats = [
            (u>0) + ((-w)>0),      # A beats B and C
            ((-u)>0) + (v>0),      # B beats A and C
            (w>0) + ((-v)>0),      # C beats A and B
        ]
        cw = beats.index(2)
        assert W == frozenset({cw})
    elif u>0:
        vals = (u,v,w)
        mn = min(vals)
        expected = frozenset(
            i for i,z in enumerate(vals) if z == mn
        )
        # weakest A>B -> B wins; weakest B>C -> C wins; weakest C>A -> A wins
        expected = frozenset({(i+1)%3 for i in expected})
        assert W == expected
    else:
        # reverse all directions: weakest magnitudes map cyclically the other way
        vals = (-u,-v,-w)
        mn = min(vals)
        expected = set()
        for i,z in enumerate(vals):
            if z != mn:
                continue
            # weak B>A -> A; weak C>B -> B; weak A>C -> C
            expected.add(i)
        assert W == frozenset(expected)

def check_n(n):
    assert n % 2 == 1
    profiles = 0
    singleton_profiles = 0
    unique_to_unique_changes = 0
    profitable_unique_to_unique = 0
    for counts in compositions(n):
        profiles += 1
        W = winners_margin(counts)
        assert W == winners_direct(counts)
        cycle_characterization(counts)
        if len(W) != 1:
            continue
        singleton_profiles += 1
        old = next(iter(W))
        for ti,c in enumerate(counts):
            if c == 0:
                continue
            true = R[ti]
            pos = {x:i for i,x in enumerate(true)}
            for ri in range(6):
                if ri == ti:
                    continue
                cc = list(counts)
                cc[ti] -= 1
                cc[ri] += 1
                W2 = winners_margin(tuple(cc))
                # Cross-check the second implementation on every changed profile
                # for smaller odd electorates and on all singleton endpoints.
                if n <= 11 or len(W2) == 1:
                    assert W2 == winners_direct(tuple(cc))
                if len(W2) == 1:
                    new = next(iter(W2))
                    if new != old:
                        unique_to_unique_changes += 1
                        if pos[new] < pos[old]:
                            profitable_unique_to_unique += 1
    assert profitable_unique_to_unique == 0
    return profiles, singleton_profiles, unique_to_unique_changes

summary = {}
for n in range(1,18,2):
    summary[n] = check_n(n)

# Non-vacuity: unique-to-unique outcome changes do occur; they are simply
# never improvements for the voter whose ballot changes.
assert any(changes > 0 for _,_,changes in summary.values())

# A small tie-touching boundary example, showing why the theorem is not a
# claim of full strategyproofness after arbitrary tie resolution.
# Counts are in lexicographic ranking order
# ABC, ACB, BAC, BCA, CAB, CBA.
P = (0,1,0,1,0,1)
assert winners_margin(P) == frozenset({2})
Q = list(P)
Q[R.index((1,2,0))] -= 1   # BCA voter
Q[R.index((1,0,2))] += 1   # reports BAC
assert winners_margin(tuple(Q)) == frozenset({0,1,2})

print("VERIFY_OK")
for n in sorted(summary):
    print("n", n,
          "anonymous_profiles", summary[n][0],
          "singleton_profiles", summary[n][1],
          "unique_to_unique_outcome_changes", summary[n][2])
print("profitable_unique_to_unique", 0)
print("tie_touching_example", P, "->", tuple(Q))
