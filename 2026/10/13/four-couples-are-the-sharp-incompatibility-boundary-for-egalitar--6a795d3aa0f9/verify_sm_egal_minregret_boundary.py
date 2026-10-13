#!/usr/bin/env python3
from itertools import permutations, product
from collections import Counter

def rank_maps(profile,n):
    men=profile[:n]; women=profile[n:]
    mr=[{w:i+1 for i,w in enumerate(p)} for p in men]
    wr=[{m:i+1 for i,m in enumerate(p)} for p in women]
    return mr,wr

def stable_rankmap(profile,n,matching):
    mr,wr=rank_maps(profile,n)
    inv=[0]*n
    for m,w in enumerate(matching):
        inv[w]=m
    for m in range(n):
        current=matching[m]
        for w in range(n):
            if w==current:
                continue
            if mr[m][w] < mr[m][current] and wr[w][m] < wr[w][inv[w]]:
                return False
    return True

def stable_direct(profile,n,matching):
    men=profile[:n]; women=profile[n:]
    inv=[0]*n
    for m,w in enumerate(matching):
        inv[w]=m
    for m in range(n):
        current=matching[m]
        for w in men[m]:
            if w==current:
                break
            curm=inv[w]
            if women[w].index(m) < women[w].index(curm):
                return False
    return True

def objective_rankmap(profile,n,matching):
    mr,wr=rank_maps(profile,n)
    inv=[0]*n
    for m,w in enumerate(matching):
        inv[w]=m
    ranks=[mr[m][matching[m]] for m in range(n)] + [wr[w][inv[w]] for w in range(n)]
    return sum(ranks),max(ranks),tuple(ranks)

def objective_direct(profile,n,matching):
    men=profile[:n]; women=profile[n:]
    inv=[0]*n
    for m,w in enumerate(matching):
        inv[w]=m
    ranks=[men[m].index(matching[m])+1 for m in range(n)]
    ranks += [women[w].index(inv[w])+1 for w in range(n)]
    return sum(ranks),max(ranks),tuple(ranks)

def stable_data(profile,n):
    out=[]
    for M in permutations(range(n)):
        a=stable_rankmap(profile,n,M)
        b=stable_direct(profile,n,M)
        assert a==b
        if a:
            x=objective_rankmap(profile,n,M)
            y=objective_direct(profile,n,M)
            assert x==y
            out.append((M,)+x)
    assert out
    return out

def relation(st):
    em=min(x[1] for x in st)
    gm=min(x[2] for x in st)
    E={x[0] for x in st if x[1]==em}
    G={x[0] for x in st if x[2]==gm}
    if E==G: t="equal"
    elif E < G: t="EsubsetG"
    elif G < E: t="GsubsetE"
    elif E.isdisjoint(G): t="disjoint"
    else: t="overlap"
    return t,E,G,em,gm

def all_profiles(n):
    P=list(permutations(range(n)))
    for idxs in product(range(len(P)), repeat=2*n):
        yield tuple(P[i] for i in idxs)

expected_profile_counts={1:1,2:16,3:46656}
expected_stable_count_dist={
    1:Counter({1:1}),
    2:Counter({1:14,2:2}),
    3:Counter({1:34080,2:11484,3:1092}),
}
expected_rel={
    1:Counter({"equal":1}),
    2:Counter({"equal":16}),
    3:Counter({"equal":40056,"EsubsetG":5400,"GsubsetE":1200}),
}
for n in (1,2,3):
    pc=0
    sc=Counter()
    rc=Counter()
    for prof in all_profiles(n):
        pc+=1
        st=stable_data(prof,n)
        sc[len(st)]+=1
        t,E,G,em,gm=relation(st)
        rc[t]+=1
        assert E & G
    assert pc==expected_profile_counts[n], (n,pc)
    assert sc==expected_stable_count_dist[n], (n,sc)
    assert rc==expected_rel[n], (n,rc)

W=(
    (0,1,2,3),
    (1,3,2,0),
    (1,0,3,2),
    (2,3,0,1),
    (1,3,2,0),
    (0,1,3,2),
    (2,3,0,1),
    (2,3,1,0),
)
st=stable_data(W,4)
assert len(st)==2
t,E,G,em,gm=relation(st)
assert t=="disjoint"
ME=(1,0,3,2)
MG=(1,3,0,2)
assert E=={ME}
assert G=={MG}
d={x[0]:x for x in st}
assert d[ME][1:]==(15,4,(2,4,3,1,1,1,2,1))
assert d[MG][1:]==(16,3,(2,2,2,1,3,1,2,3))

print("VERIFY_OK")
print("profile_counts", expected_profile_counts)
print("stable_count_distribution", {n:dict(expected_stable_count_dist[n]) for n in expected_stable_count_dist})
print("optimum_set_relations", {n:dict(expected_rel[n]) for n in expected_rel})
print("three_couple_disagreements", 6600, "fraction", "275/1944")
print("four_couple_witness_stable_matchings")
for x in st:
    print(x)
