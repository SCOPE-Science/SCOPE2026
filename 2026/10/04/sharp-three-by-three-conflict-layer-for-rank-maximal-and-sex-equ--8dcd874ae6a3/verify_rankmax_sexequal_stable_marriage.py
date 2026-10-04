#!/usr/bin/env python3
from itertools import permutations, product
from collections import Counter
from fractions import Fraction

def stable_rankmap(mp, wp):
    n = len(mp)
    mr = [{w:i+1 for i,w in enumerate(pref)} for pref in mp]
    wr = [{m:i+1 for i,m in enumerate(pref)} for pref in wp]
    out = []
    for M in permutations(range(n)):
        inv = [0]*n
        for m,w in enumerate(M):
            inv[w] = m
        ok = True
        for m in range(n):
            for w in range(n):
                if M[m] == w:
                    continue
                if mr[m][w] < mr[m][M[m]] and wr[w][m] < wr[w][inv[w]]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            men = tuple(mr[m][M[m]] for m in range(n))
            women = tuple(wr[w][inv[w]] for w in range(n))
            out.append((M, men, women))
    return tuple(out)

def stable_listindex(mp, wp):
    n = len(mp)
    out = []
    for M in permutations(range(n)):
        inv = [0]*n
        for m,w in enumerate(M):
            inv[w] = m
        ok = True
        for m in range(n):
            for w in range(n):
                if M[m] == w:
                    continue
                if mp[m].index(w) < mp[m].index(M[m]) and wp[w].index(m) < wp[w].index(inv[w]):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            men = tuple(mp[m].index(M[m])+1 for m in range(n))
            women = tuple(wp[w].index(inv[w])+1 for w in range(n))
            out.append((M, men, women))
    return tuple(out)

def rank_profile(men, women, n):
    ranks = men + women
    return tuple(ranks.count(k) for k in range(1,n+1))

def rankmax_lex(stable, n):
    prof = {M:rank_profile(mr,wr,n) for M,mr,wr in stable}
    best = max(prof.values())
    return {M for M,p in prof.items() if p == best}, prof

def rankmax_steep(stable, n):
    # There are 2n agents. Base 2n+1 makes one extra rank-k assignment
    # dominate every possible contribution from lower ranks.
    B = 2*n + 1
    score = {}
    for M,mr,wr in stable:
        ranks = mr + wr
        score[M] = sum(B**(n-r) for r in ranks)
    best = max(score.values())
    return {M for M,s in score.items() if s == best}

def sexequal_rank_sums(stable):
    val = {M:abs(sum(mr)-sum(wr)) for M,mr,wr in stable}
    best = min(val.values())
    return {M for M,v in val.items() if v == best}, val

def sexequal_preferred_counts(stable, n):
    # For an assigned rank r, exactly r-1 opposite-side agents are preferred.
    # Subtracting the same n from each side's rank sum leaves the absolute
    # difference unchanged, so this is an independent formulation.
    val = {}
    for M,mr,wr in stable:
        men_preferred = sum(r-1 for r in mr)
        women_preferred = sum(r-1 for r in wr)
        val[M] = abs(men_preferred - women_preferred)
    best = min(val.values())
    return {M for M,v in val.items() if v == best}, val

def relation(R,S):
    if R == S:
        return "equal"
    if R < S:
        return "rankmax_subset_sexequal"
    if S < R:
        return "sexequal_subset_rankmax"
    if R & S:
        return "overlap_nonnested"
    return "disjoint"

# n=1
P1 = ((0,),)
A = stable_rankmap(P1,P1)
B = stable_listindex(P1,P1)
assert A == B and len(A) == 1
R1,_ = rankmax_lex(A,1)
S1,_ = sexequal_rank_sums(A)
assert R1 == S1

# n=2 and n=3 complete strict domains.
summary = {}
detail = {}
witness = {}

for n in (2,3):
    orders = tuple(permutations(range(n)))
    relhist = Counter()
    stablehist = Counter()
    detailed = Counter()

    for mp in product(orders, repeat=n):
        for wp in product(orders, repeat=n):
            A = stable_rankmap(mp,wp)
            B = stable_listindex(mp,wp)
            assert A == B

            stablehist[len(A)] += 1

            Rlex, prof = rankmax_lex(A,n)
            Rsteep = rankmax_steep(A,n)
            assert Rlex == Rsteep

            Ssum, sex1 = sexequal_rank_sums(A)
            Spref, sex2 = sexequal_preferred_counts(A,n)
            assert Ssum == Spref
            assert sex1 == sex2

            rel = relation(Rlex,Ssum)
            relhist[rel] += 1
            detailed[(rel,len(A),len(Rlex),len(Ssum))] += 1
            witness.setdefault((n,rel),(mp,wp,A,Rlex,Ssum,prof,sex1))

    summary[n] = (relhist,stablehist)
    detail[n] = detailed

assert summary[2][0] == Counter({"equal":16})
assert summary[2][1] == Counter({1:14,2:2})

assert summary[3][1] == Counter({1:34080,2:11484,3:1092})
assert summary[3][0] == Counter({
    "equal":39084,
    "disjoint":6204,
    "sexequal_subset_rankmax":864,
    "rankmax_subset_sexequal":504,
})
assert detail[3] == Counter({
    ("equal",1,1,1):34080,
    ("equal",2,1,1):3552,
    ("equal",2,2,2):1452,
    ("rankmax_subset_sexequal",2,1,2):504,
    ("sexequal_subset_rankmax",2,2,1):864,
    ("disjoint",2,1,1):5112,
    ("disjoint",3,1,1):792,
    ("disjoint",3,1,2):72,
    ("disjoint",3,2,1):228,
})
assert detail[3][("overlap_nonnested",2,1,1)] == 0

# Canonical first disjoint witness encountered.
mp,wp,A,R,S,prof,sex = witness[(3,"disjoint")]
assert mp == ((0,1,2),(0,1,2),(0,2,1))
assert wp == ((0,1,2),(0,2,1),(1,0,2))
assert A == (
    ((0,1,2),(1,2,2),(1,3,3)),
    ((0,2,1),(1,3,3),(1,2,1)),
)
assert R == {(0,2,1)}
assert S == {(0,1,2)}
assert prof[(0,1,2)] == (2,2,2)
assert prof[(0,2,1)] == (3,1,2)
assert sex[(0,1,2)] == 2
assert sex[(0,2,1)] == 3

total = 6**6
assert total == 46656
disagree = total - summary[3][0]["equal"]
assert disagree == 7572
assert Fraction(disagree,total) == Fraction(631,3888)
assert Fraction(summary[3][0]["disjoint"],total) == Fraction(517,3888)
assert Fraction(summary[3][0]["sexequal_subset_rankmax"],total) == Fraction(1,54)
assert Fraction(summary[3][0]["rankmax_subset_sexequal"],total) == Fraction(7,648)

print("VERIFY_OK")
print("n1_relation equal")
print("n2_relation_hist",dict(summary[2][0]))
print("n2_stable_count_hist",dict(summary[2][1]))
print("n3_relation_hist",dict(summary[3][0]))
print("n3_stable_count_hist",dict(summary[3][1]))
print("n3_detailed",dict(detail[3]))
print("n3_disagreement",disagree,"of",total,"=", "631/3888")
print("n3_disjoint",6204,"of",total,"=", "517/3888")
print("n3_sexequal_subset_rankmax",864,"of",total,"=", "1/54")
print("n3_rankmax_subset_sexequal",504,"of",total,"=", "7/648")
print("witness_men",mp)
print("witness_women",wp)
print("witness_stable",A)
print("witness_rankmax",sorted(R))
print("witness_sexequal",sorted(S))
print("witness_profiles",prof)
print("witness_sexequal_scores",sex)
