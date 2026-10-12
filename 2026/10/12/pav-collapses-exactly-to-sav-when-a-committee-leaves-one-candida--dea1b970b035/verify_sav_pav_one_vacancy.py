#!/usr/bin/env python3
from itertools import combinations, product
from fractions import Fraction


def harmonic(r):
    return sum((Fraction(1,j) for j in range(1,r+1)), Fraction(0))


def sav_ballot(ballot, committee):
    return Fraction(len(ballot & committee), len(ballot))


def pav_ballot(ballot, committee):
    return harmonic(len(ballot & committee))


def score(rule, profile, committee):
    return sum((rule(A,committee) for A in profile), Fraction(0))


def winners(rule, profile, candidates):
    committees=[frozenset(set(candidates)-{c}) for c in candidates]
    vals=[score(rule,profile,W) for W in committees]
    mx=max(vals)
    return {committees[i] for i,v in enumerate(vals) if v==mx}, vals

# Termwise identity check for all nonempty ballots through eight candidates.
for m in range(2,9):
    C=frozenset(range(m))
    ballots=[]
    for r in range(1,m+1):
        ballots.extend(frozenset(x) for x in combinations(C,r))
    for A in ballots:
        h=harmonic(len(A))
        for c in C:
            W=C-{c}
            penalty=Fraction(1,len(A)) if c in A else Fraction(0)
            assert sav_ballot(A,W) == 1-penalty
            assert pav_ballot(A,W) == h-penalty

# Independent profile-level exhaustive replay for every profile with up to four
# candidates and up to four voters. Empty ballots are excluded by definition.
checked_profiles=0
for m in range(2,5):
    C=frozenset(range(m))
    ballots=[frozenset(i for i in C if mask & (1<<i)) for mask in range(1,1<<m)]
    for n in range(1,5):
        for profile in product(ballots, repeat=n):
            ws,sv=winners(sav_ballot,profile,C)
            wp,pv=winners(pav_ballot,profile,C)
            assert ws==wp
            # Score vectors differ by a committee-independent constant.
            diffs={pv[i]-sv[i] for i in range(m)}
            assert len(diffs)==1
            # Both choose exactly the omitted candidates with minimum normalized support.
            support=[]
            for c in C:
                support.append(sum((Fraction(1,len(A)) for A in profile if c in A), Fraction(0)))
            mn=min(support)
            omitted={c for c,x in enumerate(support) if x==mn}
            expected={frozenset(set(C)-{c}) for c in omitted}
            assert ws==expected
            checked_profiles += 1

print('VERIFY_OK')
print('checked_termwise_candidates_through', 8)
print('checked_profiles', checked_profiles)
