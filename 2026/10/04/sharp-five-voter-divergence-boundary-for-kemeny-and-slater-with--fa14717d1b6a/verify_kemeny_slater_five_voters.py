#!/usr/bin/env python3
from itertools import permutations, product
from collections import Counter
from math import factorial
from fractions import Fraction

CANDS = (0,1,2)
ORDERS = list(permutations(CANDS))
OID = {o:i for i,o in enumerate(ORDERS)}
CPERMS = list(permutations(CANDS))

def positions(order):
    return {c:i for i,c in enumerate(order)}

def pairwise_support(profile):
    pos = [positions(v) for v in profile]
    s = {}
    for a in CANDS:
        for b in CANDS:
            if a != b:
                s[(a,b)] = sum(1 for p in pos if p[a] < p[b])
    return s

def kemeny_direct(profile):
    s = pairwise_support(profile)
    scores = {}
    for R in ORDERS:
        pos = positions(R)
        scores[R] = sum(s[(a,b)] for a in CANDS for b in CANDS if a < b and pos[a] < pos[b]) \
                  + sum(s[(b,a)] for a in CANDS for b in CANDS if a < b and pos[b] < pos[a])
    best = max(scores.values())
    return {R for R,v in scores.items() if v == best}

def kemeny_margin(profile):
    # Independent implementation: minimize total majority-margin weight of reversed majority edges.
    n = len(profile)
    assert n % 2 == 1
    s = pairwise_support(profile)
    maj = {}
    for a in CANDS:
        for b in CANDS:
            if a < b:
                d = s[(a,b)] - s[(b,a)]
                if d > 0: maj[(a,b)] = d
                else: maj[(b,a)] = -d
    costs = {}
    for R in ORDERS:
        pos = positions(R)
        costs[R] = sum(w for (a,b),w in maj.items() if pos[a] > pos[b])
    best = min(costs.values())
    return {R for R,v in costs.items() if v == best}

def slater_direct(profile):
    n = len(profile)
    assert n % 2 == 1
    s = pairwise_support(profile)
    maj = set()
    for a in CANDS:
        for b in CANDS:
            if a < b:
                if s[(a,b)] > s[(b,a)]: maj.add((a,b))
                else: maj.add((b,a))
    costs = {}
    for R in ORDERS:
        pos = positions(R)
        costs[R] = sum(1 for (a,b) in maj if pos[a] > pos[b])
    best = min(costs.values())
    return {R for R,v in costs.items() if v == best}

def slater_cycle_formula(profile):
    # Independent three-candidate formula.
    n = len(profile)
    assert n % 2 == 1
    s = pairwise_support(profile)
    edges = []
    for a in CANDS:
        for b in CANDS:
            if a < b:
                if s[(a,b)] > s[(b,a)]: edges.append((a,b))
                else: edges.append((b,a))
    # Transitive tournament: the unique topological order.
    for R in ORDERS:
        pos = positions(R)
        if all(pos[a] < pos[b] for a,b in edges):
            return {R}
    # Three-cycle: exactly the three rankings that reverse one majority edge.
    out=set()
    for R in ORDERS:
        pos=positions(R)
        if sum(pos[a] > pos[b] for a,b in edges) == 1:
            out.add(R)
    return out

def winners(rankings):
    return {R[0] for R in rankings}

def margins_on_cycle(profile):
    s = pairwise_support(profile)
    directed=[]
    for a in CANDS:
        for b in CANDS:
            if a < b:
                d=s[(a,b)]-s[(b,a)]
                directed.append((a,b,d) if d>0 else (b,a,-d))
    # Return sorted magnitudes if cyclic, else None.
    for R in ORDERS:
        pos=positions(R)
        if all(pos[a] < pos[b] for a,b,_ in directed):
            return None
    return tuple(sorted(w for _,_,w in directed))

def counts_from_profile(profile):
    c=[0]*6
    for v in profile: c[OID[v]] += 1
    return tuple(c)

def profile_from_counts(c):
    out=[]
    for o,k in zip(ORDERS,c): out.extend([o]*k)
    return tuple(out)

def compositions(total,k,prefix=()):
    if k==1:
        yield prefix+(total,)
        return
    for x in range(total+1):
        yield from compositions(total-x,k-1,prefix+(x,))

def relabel_counts(c,p):
    out=[0]*6
    for o,k in zip(ORDERS,c):
        ro=tuple(p[x] for x in o)
        out[OID[ro]] += k
    return tuple(out)

def canon_counts(c):
    return min(relabel_counts(c,p) for p in CPERMS)

def multinomial(c):
    x=factorial(sum(c))
    for k in c: x//=factorial(k)
    return x

# Full labeled replay for 1,3,5 voters.
summary={}
div5=[]
for n in (1,3,5):
    h=Counter()
    mt=Counter()
    for P in product(ORDERS, repeat=n):
        K1=kemeny_direct(P); K2=kemeny_margin(P)
        S1=slater_direct(P); S2=slater_cycle_formula(P)
        assert K1==K2
        assert S1==S2
        KW,SW=winners(K1),winners(S1)
        h[(len(KW),len(SW),KW==SW)] += 1
        if KW != SW:
            mt[margins_on_cycle(P)] += 1
            if n==5: div5.append(P)
    summary[n]=(h,mt)

assert summary[1][0] == Counter({(1,1,True):6})
assert summary[3][0] == Counter({(1,1,True):204,(3,3,True):12})
assert summary[5][0] == Counter({
    (1,1,True):7236,
    (3,3,True):360,
    (2,3,False):180,
})
assert summary[5][1] == Counter({(1,1,3):180})
assert len(div5)==180
assert Fraction(180,6**5) == Fraction(5,216)

# Independent anonymous-profile replay for n=5.
anon_div=[]
weighted=0
for c in compositions(5,6):
    P=profile_from_counts(c)
    K=kemeny_direct(P)
    S=slater_direct(P)
    if winners(K) != winners(S):
        anon_div.append(c)
        weighted += multinomial(c)

assert len(anon_div)==6
assert weighted==180
orbits=Counter(canon_counts(c) for c in anon_div)
assert len(orbits)==1
canonical=next(iter(orbits))
assert orbits[canonical]==6
assert canonical == (0,1,2,0,0,2)
assert all(multinomial(c)==30 for c in anon_div)

# Human-readable witness: 2 ABC, 2 BCA, 1 CAB.
ABC=(0,1,2); BCA=(1,2,0); CAB=(2,0,1)
W=(ABC,ABC,BCA,BCA,CAB)
K=kemeny_direct(W); S=slater_direct(W)
assert K=={ABC,BCA}
assert S=={ABC,BCA,CAB}
assert margins_on_cycle(W)==(1,1,3)

print("VERIFY_OK")
print("n1",dict(summary[1][0]))
print("n3",dict(summary[3][0]))
print("n5",dict(summary[5][0]))
print("n5_divergent",len(div5),"prob","5/216")
print("n5_divergent_margin_multiset",(1,1,3))
print("anonymous_divergent_profiles",len(anon_div))
print("candidate_relabel_orbits",dict(orbits))
print("canonical_counts_in_order_list",canonical)
print("order_list",ORDERS)
print("witness_kemeny_rankings",sorted(K))
print("witness_slater_rankings",sorted(S))
