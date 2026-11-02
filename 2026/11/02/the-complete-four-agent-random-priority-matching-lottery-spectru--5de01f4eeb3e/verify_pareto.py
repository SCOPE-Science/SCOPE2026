#!/usr/bin/env python3
"""Independent Pareto-frontier cross-check for four-agent RSD support.

Checks all 13,824 canonical strict profiles (all 24 object relabelings
are equivalent) and all 24 possible perfect matchings per profile.
A candidate is Pareto efficient iff no alternative matching is weakly
better for everybody and strictly better for at least one agent.
"""
from itertools import permutations, product
from collections import Counter

PERMS = tuple(permutations(range(4)))

def rsd_support(profile):
    s=set()
    for priority in PERMS:
        match=[-1]*4
        mask=0
        for i in priority:
            for o in profile[i]:
                if not ((mask >> o) & 1):
                    match[i]=o
                    mask |= 1 << o
                    break
        s.add(tuple(match))
    return s

def pareto_support(profile):
    rank = [{o:j for j,o in enumerate(p)} for p in profile]
    scores = [tuple(rank[i][m[i]] for i in range(4)) for m in PERMS]
    accepted = set()
    for idx, s in enumerate(scores):
        dominated = False
        for t in scores:
            if all(t[i]<=s[i] for i in range(4)) and any(t[i]<s[i] for i in range(4)):
                dominated = True
                break
        if not dominated:accepted.add(PERMS[idx])
    return accepted

if __name__ == '__main__':
    profilecount=0
    histogram=Counter()
    for rest in product(PERMS,repeat=3):
        profile = (PERMS[0],) + rest
        a=rsd_support(profile)
        b=pareto_support(profile)
        assert a==b, (profile,a,b)
        profilecount+=1
        histogram[len(a)]+=24
    assert profilecount==24**3
    assert sum(histogram.values())==24**4
    assert len(histogram)==16
    print(f'VERIFY_OK pareto_frontier_matches_rsd_support canonical_profiles={profilecount} labeled_profiles={sum(histogram.values())}')
