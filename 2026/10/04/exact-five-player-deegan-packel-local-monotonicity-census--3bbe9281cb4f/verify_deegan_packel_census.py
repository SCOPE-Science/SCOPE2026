#!/usr/bin/env python3
from fractions import Fraction
from itertools import permutations, combinations_with_replacement
import json, sys

N = 5
EXPECTED_SIMPLE = 7579
EXPECTED_COMPLETE_LABELED = 3285
EXPECTED_CLASSES = 117
EXPECTED_VIOL_LABELED = 695
EXPECTED_VIOL_CLASSES = 17
EXPECTED_MIN_MWC = 3
EXPECTED_SPARSE_LABELED = 60
EXPECTED_SPARSE_CLASSES = 1


def monotone_functions(n):
    funcs = [0, 1]
    for k in range(1, n + 1):
        width = 1 << (k - 1)
        nxt = []
        for low in funcs:
            for high in funcs:
                if low & ~high == 0:
                    nxt.append(low | (high << width))
        funcs = nxt
    return funcs


def simple_games(n):
    top = (1 << n) - 1
    return [f for f in monotone_functions(n)
            if (f & 1) == 0 and ((f >> top) & 1) == 1]


def minimal_winning(game, n):
    out = []
    for S in range(1, 1 << n):
        if not ((game >> S) & 1):
            continue
        if all(not ((game >> (S ^ (1 << i))) & 1)
               for i in range(n) if (S >> i) & 1):
            out.append(S)
    return out


def dominates(game, n, i, j):
    # i is at least as desirable as j.
    for S in range(1 << n):
        if (S >> i) & 1 or (S >> j) & 1:
            continue
        if ((game >> (S | (1 << j))) & 1) and not ((game >> (S | (1 << i))) & 1):
            return False
    return True


def complete(game, n):
    return all(dominates(game, n, i, j) or dominates(game, n, j, i)
               for i in range(n) for j in range(i + 1, n))


def dp_raw(game, n):
    score = [Fraction(0) for _ in range(n)]
    for S in minimal_winning(game, n):
        share = Fraction(1, S.bit_count())
        for i in range(n):
            if (S >> i) & 1:
                score[i] += share
    return score


def violation_pairs(game, n):
    score = dp_raw(game, n)
    return [(i, j) for i in range(n) for j in range(n)
            if i != j and dominates(game, n, i, j) and score[i] < score[j]]


def permute_subset(S, p):
    T = 0
    for i, pi in enumerate(p):
        if (S >> i) & 1:
            T |= 1 << pi
    return T


def canonical_mwc(mwc, n):
    best = None
    for p in permutations(range(n)):
        image = tuple(sorted(permute_subset(S, p) for S in mwc))
        if best is None or image < best:
            best = image
    return best


def truth_from_weights(weights, quota):
    game = 0
    for S in range(1 << len(weights)):
        if sum(weights[i] for i in range(len(weights)) if (S >> i) & 1) >= quota:
            game |= 1 << S
    return game


def truth_from_mwc(mwc, n):
    game = 0
    for S in range(1 << n):
        if any((S & M) == M for M in mwc):
            game |= 1 << S
    return game


def coalition(mask, n=N):
    return [i + 1 for i in range(n) if (mask >> i) & 1]


def fracstr(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def enumerate_weighted_classes(max_weight=5):
    reps = {}
    n = N
    for asc in combinations_with_replacement(range(max_weight + 1), n):
        weights = tuple(reversed(asc))
        if weights[0] == 0:
            continue
        total = sum(weights)
        for quota in range(1, total + 1):
            game = truth_from_weights(weights, quota)
            if (game & 1) or not ((game >> ((1 << n) - 1)) & 1):
                continue
            key = canonical_mwc(minimal_winning(game, n), n)
            if key not in reps:
                reps[key] = (quota, weights, game)
    return reps


def build_census():
    games = simple_games(N)
    assert len(games) == EXPECTED_SIMPLE
    complete_games = [g for g in games if complete(g, N)]
    assert len(complete_games) == EXPECTED_COMPLETE_LABELED

    class_rep = {}
    for g in complete_games:
        key = canonical_mwc(minimal_winning(g, N), N)
        class_rep.setdefault(key, g)
    assert len(class_rep) == EXPECTED_CLASSES

    # Independent weighted-representation route: enumerate all nonincreasing
    # integer weight vectors with entries 0..5 and all quotas. Every complete
    # class found above receives an explicit representation this way.
    weighted = enumerate_weighted_classes(5)
    assert set(class_rep) == set(weighted), (len(class_rep), len(weighted), len(set(class_rep) - set(weighted)))

    viol_games = [g for g in complete_games if violation_pairs(g, N)]
    assert len(viol_games) == EXPECTED_VIOL_LABELED
    viol_keys = sorted({canonical_mwc(minimal_winning(g, N), N) for g in viol_games})
    assert len(viol_keys) == EXPECTED_VIOL_CLASSES

    min_mwc = min(len(minimal_winning(g, N)) for g in viol_games)
    assert min_mwc == EXPECTED_MIN_MWC
    sparse = [g for g in viol_games if len(minimal_winning(g, N)) == min_mwc]
    assert len(sparse) == EXPECTED_SPARSE_LABELED
    sparse_keys = {canonical_mwc(minimal_winning(g, N), N) for g in sparse}
    assert len(sparse_keys) == EXPECTED_SPARSE_CLASSES

    rows = []
    for key in viol_keys:
        q, w, wg = weighted[key]
        score = dp_raw(wg, N)
        pairs = violation_pairs(wg, N)
        rows.append({
            "canonical_minimal_winning_coalitions": [coalition(S) for S in key],
            "minimal_winning_count": len(key),
            "integer_weighted_representation": {"quota": q, "weights": list(w)},
            "deegan_packel_normalized": [fracstr(x / len(key)) for x in score],
            "violating_dominance_pairs": [[i + 1, j + 1] for i, j in pairs],
        })

    # Explicit unique sparsest representative.
    witness_mwc = [3, 13, 21]  # {1,2}, {1,3,4}, {1,3,5}
    witness = truth_from_mwc(witness_mwc, N)
    assert witness == truth_from_weights((5, 3, 2, 1, 1), 8)
    assert complete(witness, N)
    assert dominates(witness, N, 1, 2) and not dominates(witness, N, 2, 1)
    raw = dp_raw(witness, N)
    assert raw == [Fraction(7, 6), Fraction(1, 2), Fraction(2, 3), Fraction(1, 3), Fraction(1, 3)]
    norm = [x / 3 for x in raw]
    assert norm == [Fraction(7, 18), Fraction(1, 6), Fraction(2, 9), Fraction(1, 9), Fraction(1, 9)]
    assert norm[1] < norm[2]
    assert canonical_mwc(witness_mwc, N) in sparse_keys

    return {
        "schema_version": 1,
        "domain": "five-player weighted simple voting games up to player relabeling",
        "simple_games_labeled": len(games),
        "complete_games_labeled": len(complete_games),
        "weighted_isomorphism_classes": len(class_rep),
        "deegan_packel_local_monotonicity_violating_labeled_games": len(viol_games),
        "deegan_packel_local_monotonicity_violating_isomorphism_classes": len(viol_keys),
        "minimum_minimal_winning_coalitions_among_violations": min_mwc,
        "sparsest_violating_labeled_games": len(sparse),
        "sparsest_violating_isomorphism_classes": len(sparse_keys),
        "unique_sparsest_representative": {
            "weighted_representation": {"quota": 8, "weights": [5, 3, 2, 1, 1]},
            "minimal_winning_coalitions": [[1, 2], [1, 3, 4], [1, 3, 5]],
            "deegan_packel_raw": [fracstr(x) for x in raw],
            "deegan_packel_normalized": [fracstr(x) for x in norm],
            "strict_dominance_witness": {
                "more_desirable_player": 2,
                "less_desirable_player": 3,
                "coalition_showing_strictness": [1]
            }
        },
        "violating_classes": rows,
    }


def main():
    census = build_census()
    if len(sys.argv) == 2:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            archived = json.load(f)
        assert archived == census
    print("VERIFY_OK")
    print("simple_games_labeled=7579")
    print("complete_games_labeled=3285")
    print("weighted_isomorphism_classes=117")
    print("violating_labeled_games=695")
    print("violating_isomorphism_classes=17")
    print("minimum_mwc_count=3")
    print("sparsest_labeled_games=60")
    print("sparsest_isomorphism_classes=1")
    print("witness=[8;5,3,2,1,1]")
    print("witness_DP_normalized=7/18,1/6,2/9,1/9,1/9")

if __name__ == "__main__":
    main()
