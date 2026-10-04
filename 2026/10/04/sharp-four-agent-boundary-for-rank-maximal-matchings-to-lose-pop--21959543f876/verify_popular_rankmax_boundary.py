#!/usr/bin/env python3
from itertools import permutations, product
from collections import Counter
import hashlib

def rank_maps(profile):
    n = len(profile)
    out = []
    for pref in profile:
        r = [0] * n
        for k, obj in enumerate(pref):
            r[obj] = k
        out.append(r)
    return out

def popular_direct(profile):
    n = len(profile)
    ranks = rank_maps(profile)
    matchings = list(permutations(range(n)))
    pop = set()
    for M in matchings:
        ok = True
        for N in matchings:
            if M == N:
                continue
            score = 0
            for i in range(n):
                if ranks[i][N[i]] < ranks[i][M[i]]:
                    score += 1
                elif ranks[i][N[i]] > ranks[i][M[i]]:
                    score -= 1
            if score > 0:
                ok = False
                break
        if ok:
            pop.add(tuple(M))
    return pop

def popular_characterization(profile):
    # Abraham-Irving-Kavitha-Mehlhorn characterization specialized to
    # balanced complete strict lists. Any popular matching must be perfect:
    # otherwise adding an unmatched acceptable agent-post edge improves one
    # applicant and harms nobody.
    n = len(profile)
    matchings = list(permutations(range(n)))
    first = [pref[0] for pref in profile]
    fposts = set(first)
    second = []
    for pref in profile:
        s = None
        for obj in pref:
            if obj not in fposts:
                s = obj
                break
        second.append(s)  # None represents the private last-resort edge.
    out = set()
    for M in matchings:
        # Every f-post must be matched to an applicant who ranks it first;
        # and every applicant must receive f(a) or s(a).
        good = True
        for p in fposts:
            i = M.index(p)
            if first[i] != p:
                good = False
                break
        if not good:
            continue
        for i, p in enumerate(M):
            if p != first[i] and p != second[i]:
                good = False
                break
        if good:
            out.add(tuple(M))
    return out

def rankmax_signature(profile):
    n = len(profile)
    ranks = rank_maps(profile)
    matchings = list(permutations(range(n)))
    sig = {}
    for M in matchings:
        counts = [0] * n
        for i, obj in enumerate(M):
            counts[ranks[i][obj]] += 1
        sig[tuple(M)] = tuple(counts)
    best = max(sig.values())
    return {M for M, s in sig.items() if s == best}, best

def rankmax_steep(profile):
    # Independent exact encoding of lexicographic signature:
    # base B=n+1 makes one additional rank-k assignment outweigh all
    # possible lower-rank contributions.
    n = len(profile)
    ranks = rank_maps(profile)
    B = n + 1
    matchings = list(permutations(range(n)))
    score = {}
    for M in matchings:
        v = 0
        for i, obj in enumerate(M):
            v += B ** (n - 1 - ranks[i][obj])
        score[tuple(M)] = v
    best = max(score.values())
    return {M for M, v in score.items() if v == best}

def relation(R, P):
    if not P:
        return "no_popular"
    if R == P:
        return "equal"
    if R < P:
        return "rankmax_subset_popular"
    if P < R:
        return "popular_subset_rankmax"
    if R & P:
        return "overlap_nonnested"
    return "disjoint"

def exhaustive(n):
    orders = list(permutations(range(n)))
    hist = Counter()
    detail = Counter()
    digest = hashlib.sha256()
    nop_identical = 0
    for profile in product(orders, repeat=n):
        P1 = popular_direct(profile)
        P2 = popular_characterization(profile)
        assert P1 == P2
        R1, sig = rankmax_signature(profile)
        R2 = rankmax_steep(profile)
        assert R1 == R2
        rel = relation(R1, P1)
        hist[rel] += 1
        detail[(len(R1), len(P1), rel)] += 1
        if rel == "no_popular" and len(set(profile)) == 1:
            nop_identical += 1
        digest.update(repr((profile, tuple(sorted(R1)), tuple(sorted(P1)), sig, rel)).encode())
        digest.update(b"\n")
    return hist, detail, nop_identical, digest.hexdigest()

r2 = exhaustive(2)
assert r2[0] == Counter({"equal": 4})
assert r2[1] == Counter({(2,2,"equal"):2, (1,1,"equal"):2})

r3 = exhaustive(3)
assert r3[0] == Counter({
    "equal": 138,
    "rankmax_subset_popular": 72,
    "no_popular": 6,
})
assert r3[1] == Counter({
    (2,2,"equal"): 90,
    (1,1,"equal"): 48,
    (1,2,"rankmax_subset_popular"): 72,
    (6,0,"no_popular"): 6,
})
assert r3[2] == 6

# Sharp four-agent witness: popular matchings exist, but not every
# rank-maximal matching is popular.
W = (
    (3,1,0,2),
    (3,1,0,2),
    (2,3,1,0),
    (3,2,0,1),
)
P1 = popular_direct(W)
P2 = popular_characterization(W)
assert P1 == P2
R1, sig = rankmax_signature(W)
R2 = rankmax_steep(W)
assert R1 == R2
assert sig == (2,1,1,0)
assert P1 == {(3,1,2,0), (1,3,2,0)}
assert R1 == {
    (0,1,2,3),
    (3,1,2,0),
    (1,0,2,3),
    (1,3,2,0),
}
assert P1 < R1

print("VERIFY_OK")
print("n2_relation_hist", dict(r2[0]))
print("n3_relation_hist", dict(r3[0]))
print("n3_detail", {str(k): v for k,v in sorted(r3[1].items(), key=str)})
print("n3_no_popular_identical_profiles", r3[2])
print("n3_digest", r3[3])
print("n4_witness_rankmax", sorted(R1))
print("n4_witness_popular", sorted(P1))
print("n4_witness_signature", sig)
