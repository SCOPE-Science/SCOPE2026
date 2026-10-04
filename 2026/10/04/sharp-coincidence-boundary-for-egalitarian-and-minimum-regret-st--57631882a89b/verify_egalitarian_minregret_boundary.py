#!/usr/bin/env python3
from itertools import permutations, product
from collections import Counter
import hashlib

def ranks(preferences):
    return [{x: i + 1 for i, x in enumerate(pref)} for pref in preferences]

def stable_matchings_rankmap(men, women):
    n = len(men)
    mr = ranks(men)
    wr = ranks(women)
    out = []
    for matching in permutations(range(n)):
        inverse = [None] * n
        for m, w in enumerate(matching):
            inverse[w] = m
        stable = True
        for m in range(n):
            for w in range(n):
                if matching[m] == w:
                    continue
                if mr[m][w] < mr[m][matching[m]] and wr[w][m] < wr[w][inverse[w]]:
                    stable = False
                    break
            if not stable:
                break
        if stable:
            person_ranks = [mr[m][matching[m]] for m in range(n)]
            person_ranks += [wr[w][inverse[w]] for w in range(n)]
            out.append((
                tuple(matching),
                sum(person_ranks),
                max(person_ranks),
                tuple(person_ranks),
            ))
    return tuple(out)

def stable_matchings_direct(men, women):
    n = len(men)
    out = []
    for matching in permutations(range(n)):
        inverse = [None] * n
        for m, w in enumerate(matching):
            inverse[w] = m
        stable = True
        for m in range(n):
            assigned_w = matching[m]
            mpos_assigned = men[m].index(assigned_w)
            for w in range(n):
                if w == assigned_w:
                    continue
                if men[m].index(w) < mpos_assigned:
                    incumbent = inverse[w]
                    if women[w].index(m) < women[w].index(incumbent):
                        stable = False
                        break
            if not stable:
                break
        if stable:
            person_ranks = [men[m].index(matching[m]) + 1 for m in range(n)]
            person_ranks += [women[w].index(inverse[w]) + 1 for w in range(n)]
            out.append((
                tuple(matching),
                sum(person_ranks),
                max(person_ranks),
                tuple(person_ranks),
            ))
    return tuple(out)

def classify_optima(stable):
    min_sum = min(x[1] for x in stable)
    min_regret = min(x[2] for x in stable)
    egalitarian = {x[0] for x in stable if x[1] == min_sum}
    minregret = {x[0] for x in stable if x[2] == min_regret}
    if egalitarian == minregret:
        relation = "equal"
    elif egalitarian < minregret:
        relation = "egalitarian_subset_minregret"
    elif minregret < egalitarian:
        relation = "minregret_subset_egalitarian"
    elif egalitarian & minregret:
        relation = "overlap_nonnested"
    else:
        relation = "disjoint"
    return min_sum, min_regret, egalitarian, minregret, relation

def exhaustive(n):
    orders = list(permutations(range(n)))
    relation_hist = Counter()
    stable_count_hist = Counter()
    overlap_size_hist = Counter()
    total = 0
    digest_lines = []
    for profile in product(orders, repeat=2*n):
        men = profile[:n]
        women = profile[n:]
        a = stable_matchings_rankmap(men, women)
        b = stable_matchings_direct(men, women)
        assert a == b
        assert a
        min_sum, min_regret, E, R, rel = classify_optima(a)
        relation_hist[rel] += 1
        stable_count_hist[len(a)] += 1
        overlap_size_hist[(len(a), len(E), len(R), len(E & R))] += 1
        total += 1
        digest_lines.append(
            repr((profile, a, min_sum, min_regret, tuple(sorted(E)), tuple(sorted(R)), rel))
        )
    digest = hashlib.sha256("\n".join(digest_lines).encode("utf-8")).hexdigest()
    return total, relation_hist, stable_count_hist, overlap_size_hist, digest

# Complete predecessor market.
n2 = exhaustive(2)
assert n2[0] == 16
assert n2[1] == Counter({"equal": 16})

# Complete 3x3 market.
n3 = exhaustive(3)
assert n3[0] == 46656
assert n3[1] == Counter({
    "equal": 40056,
    "egalitarian_subset_minregret": 5400,
    "minregret_subset_egalitarian": 1200,
})
assert "overlap_nonnested" not in n3[1]
assert "disjoint" not in n3[1]

# Independent check of the known stable-count marginal.
assert n3[2] == Counter({1: 34080, 2: 11484, 3: 1092})

# Sharp 4x4 witness. Object labels are A=0, B=1, C=2, D=3.
MEN4 = (
    (1,2,3,0),  # B C D A
    (0,2,1,3),  # A C B D
    (0,3,2,1),  # A D C B
    (0,3,2,1),  # A D C B
)
WOMEN4 = (
    (1,2,0,3),  # m2 m3 m1 m4
    (2,3,0,1),  # m3 m4 m1 m2
    (0,3,2,1),  # m1 m4 m3 m2
    (3,1,2,0),  # m4 m2 m3 m1
)

w1 = stable_matchings_rankmap(MEN4, WOMEN4)
w2 = stable_matchings_direct(MEN4, WOMEN4)
assert w1 == w2
assert w1 == (
    ((1,0,2,3), 15, 3, (1,1,3,2,1,3,3,1)),
    ((2,0,1,3), 13, 4, (2,1,4,2,1,1,1,1)),
)
min_sum, min_regret, E, R, rel = classify_optima(w1)
assert min_sum == 13
assert min_regret == 3
assert E == {(2,0,1,3)}
assert R == {(1,0,2,3)}
assert rel == "disjoint"

print("VERIFY_OK")
print("n2_profiles", n2[0])
print("n2_relation_hist", dict(n2[1]))
print("n3_profiles", n3[0])
print("n3_relation_hist", dict(n3[1]))
print("n3_stable_count_hist", dict(n3[2]))
print("n3_overlap_size_hist", {str(k): v for k, v in sorted(n3[3].items())})
print("n3_digest", n3[4])
print("n4_witness_stable_matchings", w1)
print("n4_witness_relation", rel)
