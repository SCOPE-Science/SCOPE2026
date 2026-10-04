#!/usr/bin/env python3
from itertools import permutations, product
from collections import Counter
from fractions import Fraction
import hashlib

def stable_rankmap(men, women):
    n = len(men)
    mr = [{x:i+1 for i,x in enumerate(p)} for p in men]
    wr = [{x:i+1 for i,x in enumerate(p)} for p in women]
    out = []
    for M in permutations(range(n)):
        inv = [None]*n
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
            mc = sum(mr[m][M[m]] for m in range(n))
            wc = sum(wr[w][inv[w]] for w in range(n))
            out.append((tuple(M), mc+wc, abs(mc-wc), mc, wc))
    return tuple(out)

def stable_direct(men, women):
    n = len(men)
    out = []
    for M in permutations(range(n)):
        inv = [None]*n
        for m,w in enumerate(M):
            inv[w] = m
        ok = True
        for m in range(n):
            mw = M[m]
            for w in range(n):
                if w == mw:
                    continue
                if men[m].index(w) < men[m].index(mw):
                    incumbent = inv[w]
                    if women[w].index(m) < women[w].index(incumbent):
                        ok = False
                        break
            if not ok:
                break
        if ok:
            mr = [men[m].index(M[m])+1 for m in range(n)]
            wr = [women[w].index(inv[w])+1 for w in range(n)]
            mc = sum(mr)
            wc = sum(wr)
            out.append((tuple(M), mc+wc, abs(mc-wc), mc, wc))
    return tuple(out)

def relation(st):
    e = min(x[1] for x in st)
    s = min(x[2] for x in st)
    E = {x[0] for x in st if x[1] == e}
    S = {x[0] for x in st if x[2] == s}
    if E == S:
        r = "equal"
    elif E < S:
        r = "egalitarian_subset_sexequal"
    elif S < E:
        r = "sexequal_subset_egalitarian"
    elif E & S:
        r = "overlap_nonnested"
    else:
        r = "disjoint"
    return e,s,E,S,r

def exhaustive(n):
    orders = list(permutations(range(n)))
    relhist = Counter()
    stablehist = Counter()
    detail = Counter()
    lines = []
    first_disjoint = None
    for prof in product(orders, repeat=2*n):
        men = prof[:n]
        women = prof[n:]
        a = stable_rankmap(men,women)
        b = stable_direct(men,women)
        assert a == b and a
        e,s,E,S,r = relation(a)
        relhist[r] += 1
        stablehist[len(a)] += 1
        detail[(len(a),r,len(E),len(S))] += 1
        if r == "disjoint" and first_disjoint is None:
            first_disjoint = (prof,a,E,S)
        lines.append(repr((prof,a,e,s,tuple(sorted(E)),tuple(sorted(S)),r)))
    return relhist,stablehist,detail,first_disjoint,hashlib.sha256(
        "\n".join(lines).encode("utf-8")
    ).hexdigest()

r2 = exhaustive(2)
assert r2[0] == Counter({"equal":16})
assert r2[1] == Counter({1:14,2:2})

r3 = exhaustive(3)
assert r3[0] == Counter({
    "equal":40056,
    "sexequal_subset_egalitarian":3720,
    "egalitarian_subset_sexequal":360,
    "disjoint":2520,
})
assert r3[0]["overlap_nonnested"] == 0
assert r3[1] == Counter({1:34080,2:11484,3:1092})

# Check a compact explicit 3x3 witness with two stable matchings and disjoint optima.
MEN = (
    (0,1,2),
    (0,1,2),
    (0,2,1),
)
WOMEN = (
    (0,1,2),
    (0,2,1),
    (1,0,2),
)
w = stable_rankmap(MEN,WOMEN)
assert w == stable_direct(MEN,WOMEN)
assert w == (
    ((0,1,2),12,2,5,7),
    ((0,2,1),11,3,7,4),
)
e,s,E,S,r = relation(w)
assert e == 11 and s == 2
assert E == {(0,2,1)}
assert S == {(0,1,2)}
assert r == "disjoint"

N = 6**6
probs = {k: Fraction(v,N) for k,v in r3[0].items()}

print("VERIFY_OK")
print("n2_relation_hist", dict(r2[0]))
print("n3_profiles", N)
print("n3_relation_hist", dict(r3[0]))
print("n3_probabilities", {k:str(v) for k,v in probs.items()})
print("n3_stable_count_hist", dict(r3[1]))
print("n3_detail", {str(k):v for k,v in sorted(r3[2].items())})
print("witness_stable_matchings", w)
print("n3_digest", r3[4])
