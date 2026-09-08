"""Independent verifier: replays N=13 census from output/artifacts/census.json alone (stdlib only)."""
import itertools, json
pts=tuple(range(6))
triples=[tuple(sorted(t)) for t in itertools.combinations(pts,3)]
T={tuple(sorted([x+1 for x in t])):t for t in triples}
rows=json.load(open("output/artifacts/census.json"))
perms=list(itertools.permutations(pts))
def apply(fam,p): return frozenset(tuple(sorted(p[x] for x in t)) for t in fam)
def canon(fam): return min(tuple(sorted(apply(fam,p))) for p in perms)
base=[0,1,2,3,4,5]
circles=set()
for p in perms:
    o=tuple(p[i] for i in base)
    circles.add(frozenset(frozenset([o[i],o[(i+1)%6],o[(i+2)%6]]) for i in range(6)))
assert len(circles)==60, len(circles)
seen=set(); total=0
for i,r in enumerate(rows):
    fam=frozenset(T[tuple(t)] for t in r["rep"])
    assert len(fam)==10, i
    L=list(fam)
    for a in range(10):
        for b in range(a+1,10):
            assert set(L[a])&set(L[b]), (i,"not intersecting")
            assert not (set(L[a])|set(L[b])==set(pts) and not set(L[a])&set(L[b])), i
    for t in fam:
        assert tuple(sorted(set(pts)-set(t))) not in fam, (i,"both complements")
    c=canon(fam)
    assert tuple(tuple(t) for t in c)==tuple(tuple(x-1 for x in t) for t in r["canon"]), (i,"canon mismatch")
    assert c not in seen, (i,"duplicate type")
    seen.add(c)
    s=sum(1 for p in perms if apply(fam,p)==fam)
    assert s==r["stab"], (i,s,r["stab"])
    assert 720//s==r["orbit_size"], i
    total+=r["orbit_size"]
    assert max(sum(1 for a in C if a in set(map(frozenset,fam))) for C in circles)<=3, (i,"katona")
assert len(rows)==13 and total==1024, (len(rows),total)
print("VERIFY_OK: 13 types, 1024 labeled families, all certificates replay")
