#!/usr/bin/env python3
from itertools import permutations, product
from collections import Counter, defaultdict

def perfect_matchings(n):
    def rec(rem):
        if not rem:
            yield ()
            return
        a=min(rem)
        for b in sorted(rem):
            if b==a:
                continue
            for tail in rec(rem-{a,b}):
                yield tuple(sorted(((min(a,b),max(a,b)),)+tail))
    return tuple(sorted(set(rec(set(range(n))))))

def stable_rankmap(profile, matchings):
    n=len(profile)
    rank=[{x:i+1 for i,x in enumerate(pref)} for pref in profile]
    out=[]
    for M in matchings:
        p={}
        for a,b in M:
            p[a]=b; p[b]=a
        ok=True
        for a in range(n):
            for b in range(a+1,n):
                if p[a]==b:
                    continue
                if rank[a][b] < rank[a][p[a]] and rank[b][a] < rank[b][p[b]]:
                    ok=False
                    break
            if not ok:
                break
        if ok:
            rv=tuple(rank[i][p[i]] for i in range(n))
            out.append((M,rv))
    return tuple(out)

def stable_listindex(profile, matchings):
    n=len(profile)
    out=[]
    for M in matchings:
        p={}
        for a,b in M:
            p[a]=b; p[b]=a
        ok=True
        for a in range(n):
            for b in range(a+1,n):
                if p[a]==b:
                    continue
                if profile[a].index(b) < profile[a].index(p[a]) and profile[b].index(a) < profile[b].index(p[b]):
                    ok=False
                    break
            if not ok:
                break
        if ok:
            rv=tuple(profile[i].index(p[i])+1 for i in range(n))
            out.append((M,rv))
    return tuple(out)

def signature(rv, maxrank):
    return tuple(rv.count(k) for k in range(1,maxrank+1))

def rankmax_signature(stable, maxrank):
    sig={M:signature(rv,maxrank) for M,rv in stable}
    best=max(sig.values())
    return {M for M,s in sig.items() if s==best}, sig

def rankmax_steep(stable, maxrank):
    # Independent exact scalar encoding of lexicographic signature.
    # With four agents, base 5 guarantees one extra rank-k assignment
    # outweighs every possible lower-rank contribution.
    B=5
    score={}
    for M,rv in stable:
        v=sum(B**(maxrank-r) for r in rv)
        score[M]=v
    best=max(score.values())
    return {M for M,v in score.items() if v==best}

def minreg_direct(stable):
    vals={M:max(rv) for M,rv in stable}
    best=min(vals.values())
    return {M for M,v in vals.items() if v==best}, vals

def minreg_threshold(stable):
    # Independent threshold formulation.
    for r in range(1,4):
        good={M for M,rv in stable if all(x<=r for x in rv)}
        if good:
            return good,r
    raise AssertionError

def relation(R,M):
    # R = rank-maximal set, M = minimum-regret set
    if not R and not M:
        return "none"
    if R==M:
        return "equal"
    if R < M:
        return "rankmax_subset_minreg"
    if M < R:
        return "minreg_subset_rankmax"
    if R & M:
        return "overlap_nonnested"
    return "disjoint"

def relabel_profile(profile,p):
    n=len(profile)
    q=[None]*n
    for i in range(n):
        q[p[i]]=tuple(p[j] for j in profile[i])
    return tuple(q)

def canonical(profile):
    n=len(profile)
    return min(relabel_profile(profile,p) for p in permutations(range(n)))

# n=2: one complete strict profile.
M2=perfect_matchings(2)
P2=((1,),(0,))
S2a=stable_rankmap(P2,M2)
S2b=stable_listindex(P2,M2)
assert S2a==S2b and len(S2a)==1
R2,_=rankmax_signature(S2a,1)
MR2,_=minreg_direct(S2a)
assert R2==MR2

# n=4 complete strict domain.
n=4
matchings=perfect_matchings(n)
assert len(matchings)==3
orders=[list(permutations([j for j in range(n) if j!=i])) for i in range(n)]

hist=Counter()
stable_hist=Counter()
orbit_buckets=defaultdict(list)
witness=None
for profile in product(*orders):
    A=stable_rankmap(profile,matchings)
    B=stable_listindex(profile,matchings)
    assert A==B
    stable_hist[len(A)] += 1
    if not A:
        hist["none"] += 1
        continue

    R1,sigs=rankmax_signature(A,3)
    R2=rankmax_steep(A,3)
    assert R1==R2

    MR1,regs=minreg_direct(A)
    MR2,threshold=minreg_threshold(A)
    assert MR1==MR2
    assert threshold==min(regs.values())

    rel=relation(R1,MR1)
    hist[rel]+=1
    if rel!="equal":
        orbit_buckets[(rel,canonical(profile))].append(profile)

    # Check rank sums too, for the disjoint witness.
    if rel=="disjoint" and witness is None:
        witness=(profile,A,R1,MR1,sigs,regs)

assert stable_hist==Counter({1:1098,2:150,0:48})
assert hist==Counter({
    "equal":1176,
    "rankmax_subset_minreg":48,
    "disjoint":24,
    "none":48,
})
assert hist["minreg_subset_rankmax"]==0
assert hist["overlap_nonnested"]==0

# The 72 solvable disagreements split into exactly three full S4 orbits.
orbit_sizes=Counter()
canon_details=[]
for (rel,c),profiles in orbit_buckets.items():
    orbit_sizes[(rel,len(profiles))]+=1
    canon_details.append((rel,c,len(profiles)))
assert orbit_sizes==Counter({
    ("rankmax_subset_minreg",24):2,
    ("disjoint",24):1,
})

# Canonical disjoint orbit and its exact objective values.
disjoint_canons=[c for rel,c,size in canon_details if rel=="disjoint"]
assert len(disjoint_canons)==1
C=disjoint_canons[0]
assert C == (
    (1,2,3),
    (2,3,0),
    (0,3,1),
    (2,1,0),
)
SC=stable_rankmap(C,matchings)
RC,sigs=rankmax_signature(SC,3)
MRC,regs=minreg_direct(SC)
assert SC==(
    (((0,1),(2,3)),(1,3,2,1)),
    (((0,2),(1,3)),(2,2,1,2)),
)
assert RC=={((0,1),(2,3))}
assert MRC=={((0,2),(1,3))}
assert sigs[((0,1),(2,3))]==(2,1,1)
assert sigs[((0,2),(1,3))]==(1,3,0)
assert regs[((0,1),(2,3))]==3
assert regs[((0,2),(1,3))]==2
assert sum((1,3,2,1))==sum((2,2,1,2))==7

print("VERIFY_OK")
print("n2_relation","equal")
print("n4_profiles",6**4)
print("stable_count_hist",dict(stable_hist))
print("relation_hist",dict(hist))
print("solvable_profiles",1248)
print("disjoint_unconditional","24/1296 = 1/54")
print("disjoint_conditional_solvable","24/1248 = 1/52")
print("disagreement_orbits",sorted((rel,size) for rel,c,size in canon_details))
print("canonical_disjoint_profile",C)
print("canonical_stable",SC)
print("canonical_signatures",sigs)
print("canonical_regrets",regs)
