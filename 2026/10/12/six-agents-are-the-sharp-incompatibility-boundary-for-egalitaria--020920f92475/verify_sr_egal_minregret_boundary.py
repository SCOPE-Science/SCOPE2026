#!/usr/bin/env python3
from itertools import permutations, product
from collections import Counter
from fractions import Fraction

def perfect_matchings(n):
    def rec(remaining):
        if not remaining:
            yield ()
            return
        a = remaining[0]
        for idx in range(1, len(remaining)):
            b = remaining[idx]
            rest = remaining[1:idx] + remaining[idx+1:]
            for tail in rec(rest):
                yield ((a,b),) + tail
    yield from rec(tuple(range(n)))

def partner_tuple(n, matching):
    p = [-1]*n
    for a,b in matching:
        p[a]=b; p[b]=a
    return tuple(p)

def rank_maps(prefs):
    return tuple({x:i+1 for i,x in enumerate(pref)} for pref in prefs)

def stable_rankmap(prefs, matching):
    n=len(prefs); p=partner_tuple(n, matching); r=rank_maps(prefs)
    for a in range(n):
        for b in range(a+1,n):
            if p[a]==b:
                continue
            if r[a][b] < r[a][p[a]] and r[b][a] < r[b][p[b]]:
                return False
    return True

def stable_listindex(prefs, matching):
    n=len(prefs); p=partner_tuple(n, matching)
    for a in range(n):
        for b in range(a+1,n):
            if p[a]==b:
                continue
            if prefs[a].index(b) < prefs[a].index(p[a]) and prefs[b].index(a) < prefs[b].index(p[b]):
                return False
    return True

def objectives_rankmap(prefs, matching):
    p=partner_tuple(len(prefs),matching); r=rank_maps(prefs)
    vals=tuple(r[i][p[i]] for i in range(len(prefs)))
    return sum(vals), max(vals), vals

def objectives_listindex(prefs, matching):
    p=partner_tuple(len(prefs),matching)
    vals=tuple(prefs[i].index(p[i])+1 for i in range(len(prefs)))
    return sum(vals), max(vals), vals

def stable_set(prefs):
    n=len(prefs)
    out=[]
    for M in perfect_matchings(n):
        a=stable_rankmap(prefs,M)
        b=stable_listindex(prefs,M)
        assert a==b
        if a:
            x=objectives_rankmap(prefs,M)
            y=objectives_listindex(prefs,M)
            assert x==y
            out.append((tuple(sorted(tuple(sorted(e)) for e in M)),x))
    return tuple(sorted(out))

def opt_sets(prefs):
    st=stable_set(prefs)
    if not st:
        return st,set(),set()
    min_sum=min(x[1][0] for x in st)
    min_reg=min(x[1][1] for x in st)
    E={x[0] for x in st if x[1][0]==min_sum}
    G={x[0] for x in st if x[1][1]==min_reg}
    return st,E,G

def relation(E,G):
    if E==G: return "equal"
    if E < G: return "egalitarian_subset_minregret"
    if G < E: return "minregret_subset_egalitarian"
    if E & G: return "overlap_nonnested"
    return "disjoint"

def relabel_profile(prefs, sigma):
    n=len(prefs)
    out=[None]*n
    for old in range(n):
        out[sigma[old]]=tuple(sigma[x] for x in prefs[old])
    return tuple(out)

def profile_code(prefs):
    n=len(prefs)
    code=[]
    for i,p in enumerate(prefs):
        orders=tuple(permutations(tuple(j for j in range(n) if j!=i)))
        idx={q:k for k,q in enumerate(orders)}
        code.append(idx[p])
    return tuple(code)

def canonical_profile(prefs):
    n=len(prefs)
    return min(profile_code(relabel_profile(prefs,s)) for s in permutations(range(n)))

# Two-agent base case.
p2=((1,),(0,))
st,E,G=opt_sets(p2)
assert len(st)==1 and E==G

# Complete strict four-agent domain.
n=4
orders_by_agent=[]
for i in range(n):
    others=tuple(j for j in range(n) if j!=i)
    orders_by_agent.append(tuple(permutations(others)))

stable_hist=Counter()
rel_hist=Counter()
disagree_canon=Counter()
canon_relation={}
witnesses={}
total=0

for prefs in product(*orders_by_agent):
    prefs=tuple(prefs)
    total += 1
    st,E,G=opt_sets(prefs)
    stable_hist[len(st)] += 1
    if not st:
        continue
    rel=relation(E,G)
    rel_hist[rel] += 1
    if rel!="equal":
        c=canonical_profile(prefs)
        disagree_canon[c] += 1
        canon_relation.setdefault(c,rel)
        assert canon_relation[c]==rel
        witnesses.setdefault(c,(prefs,st,E,G))

assert total == 6**4 == 1296
assert stable_hist == Counter({1:1098,2:150,0:48})
assert rel_hist == Counter({
    "equal":1176,
    "egalitarian_subset_minregret":48,
    "minregret_subset_egalitarian":24,
})
assert len(disagree_canon)==3
assert Counter(disagree_canon.values()) == Counter({24:3})
assert Counter(canon_relation.values()) == Counter({
    "egalitarian_subset_minregret":2,
    "minregret_subset_egalitarian":1,
})

# Record exact canonical representatives and their objective structures.
canon_summary = {}
for c,(prefs,st,E,G) in witnesses.items():
    got=tuple(sorted((x[1][0],x[1][1]) for x in st))
    canon_summary[c]=(canon_relation[c],got,prefs,st)

# Explicit six-agent disjoint witness.
prefs6 = (
    (5,4,3,1,2),
    (5,2,3,0,4),
    (4,0,1,5,3),
    (1,4,0,5,2),
    (0,1,3,2,5),
    (2,0,4,3,1),
)
st6,E6,G6=opt_sets(prefs6)
assert len(st6)==2
M_reg = ((0,5),(1,2),(3,4))
M_egal = ((0,5),(1,3),(2,4))
M_reg=tuple(sorted(tuple(sorted(e)) for e in M_reg))
M_egal=tuple(sorted(tuple(sorted(e)) for e in M_egal))
byM={M:obj for M,obj in st6}
assert set(byM)=={M_reg,M_egal}
assert byM[M_reg][:2] == (13,3)
assert byM[M_egal][:2] == (12,4)
assert E6 == {M_egal}
assert G6 == {M_reg}
assert not (E6 & G6)
assert relation(E6,G6) == "disjoint"

# There are no other feasible even agent counts strictly between four and six.
print("VERIFY_OK")
print("n2_stable_relation equal")
print("n4_total_profiles", total)
print("n4_stable_count_hist", dict(sorted(stable_hist.items())))
print("n4_solvable_profiles", total-stable_hist[0])
print("n4_relation_hist", dict(rel_hist))
print("n4_disagreement_profiles", sum(v for k,v in rel_hist.items() if k!="equal"))
print("n4_disagreement_orbits", len(disagree_canon))
print("n4_orbit_sizes", sorted(disagree_canon.values()))
print("n4_relation_orbits", dict(Counter(canon_relation.values())))
print("n4_canonical_orbits")
for c in sorted(canon_summary):
    rel,got,prefs,st=canon_summary[c]
    print(c, rel, "prefs", prefs, "stable", st)
print("n6_stable_matchings", st6)
print("n6_egalitarian", sorted(E6))
print("n6_minimum_regret", sorted(G6))
print("n6_relation disjoint")
