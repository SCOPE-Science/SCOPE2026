#!/usr/bin/env python3
from itertools import permutations, product
from fractions import Fraction
from collections import Counter
import math

def rsd_counts(profile):
    n=len(profile)
    out=[[0]*n for _ in range(n)]
    for order in permutations(range(n)):
        avail=set(range(n))
        for i in order:
            for o in profile[i]:
                if o in avail:
                    out[i][o]+=1
                    avail.remove(o)
                    break
    return out, math.factorial(n)

def sd_dominates(row_i,row_j,pref):
    s_i=s_j=0
    for o in pref:
        s_i += row_i[o]
        s_j += row_j[o]
        if s_i < s_j:
            return False
    return True

def sd_envy_free(profile):
    counts,d=rsd_counts(profile)
    n=len(profile)
    for i in range(n):
        for j in range(n):
            if not sd_dominates(counts[i],counts[j],profile[i]):
                return False
    return True

def canonical_profile(profile):
    n=len(profile)
    best=None
    for ap in permutations(range(n)):
        # agent relabel: new agent ap[old] gets relabeled preference of old
        for op in permutations(range(n)):
            new=[None]*n
            for old in range(n):
                new[ap[old]]=tuple(op[o] for o in profile[old])
            key=tuple(new)
            if best is None or key<best:
                best=key
    return best

# Exhaustive boundary through n=3.
for n in (1,2):
    prefs=list(permutations(range(n)))
    assert sum(not sd_envy_free(p) for p in product(prefs, repeat=n))==0

n=3
prefs=list(permutations(range(n)))
bad=[]
for p in product(prefs, repeat=n):
    if not sd_envy_free(p): bad.append(p)
assert len(bad)==72
assert all(len(set(p))==3 for p in bad)
all_classes={canonical_profile(p) for p in product(prefs, repeat=n)}
bad_classes={canonical_profile(p) for p in bad}
assert len(all_classes)==10
assert len(bad_classes)==2
# exact orbit sizes under independent S3 x S3 action
for rep in bad_classes:
    orbit={}
    imgs=set()
    for ap in permutations(range(n)):
        for op in permutations(range(n)):
            new=[None]*n
            for old in range(n):
                new[ap[old]]=tuple(op[o] for o in rep[old])
            imgs.add(tuple(new))
    assert len(imgs)==36

# Hosseini-Larson-Cohen/Bogomolnaia-Moulin-type three-agent witness.
a,b,c=0,1,2
w=((a,c,b),(a,b,c),(b,a,c))
counts,d=rsd_counts(w)
expected=[
    [Fraction(1,2),Fraction(0),Fraction(1,2)],
    [Fraction(1,2),Fraction(1,6),Fraction(1,3)],
    [Fraction(0),Fraction(5,6),Fraction(1,6)],
]
assert [[Fraction(x,d) for x in row] for row in counts]==expected
assert not sd_envy_free(w)
# Agent 2 (index1) top-two cumulative probability is 2/3, while row3 gives 5/6.
assert Fraction(counts[1][a]+counts[1][b],d)==Fraction(2,3)
assert Fraction(counts[2][a]+counts[2][b],d)==Fraction(5,6)

# Finite stress-check of the all-n theorem on every two-type multiplicity profile up to n=6,
# with the first type normalized to identity by object relabeling.
checked=0
for n in range(2,7):
    ident=tuple(range(n))
    for second in permutations(range(n)):
        for r in range(1,n):
            p=tuple([ident]*r+[second]*(n-r))
            assert sd_envy_free(p)
            counts,d=rsd_counts(p)
            # Top-k RSD lower bound for every agent.
            for i in range(n):
                cum=0
                for k,o in enumerate(p[i],1):
                    cum += counts[i][o]
                    assert Fraction(cum,d) >= Fraction(k,n)
            checked += 1

print('VERIFY_OK')
print('n3_labeled_profiles', 6**3)
print('n3_sd_envy_free', 144)
print('n3_not_sd_envy_free', 72)
print('n3_total_symmetry_classes', len(all_classes))
print('n3_bad_symmetry_classes', len(bad_classes))
print('n3_bad_orbit_sizes', [36,36])
print('all_n3_failures_use_three_types', True)
print('two_type_profiles_checked_n_le_6', checked)
