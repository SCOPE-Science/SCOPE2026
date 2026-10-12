from itertools import permutations
import json

V = (0, 1)
TYPES = tuple((v, mask) for v in V for mask in range(4))


def bits(mask):
    return tuple(q for q in V if mask & (1 << q))


def support_closure(S):
    S = set(S)
    C = {s for s in S if s[1] == 0}
    stages = {s: 0 for s in C}
    stage = 0
    while True:
        add = []
        for s in sorted(S - C):
            _, T = s
            ok = True
            for q in bits(T):
                if not any(t[0] == q and (t[1] & ~T) == 0 for t in C):
                    ok = False
                    break
            if ok:
                add.append(s)
        if not add:
            return C, stages
        stage += 1
        for s in add:
            C.add(s)
            stages[s] = stage


def permutation_test(S):
    S = tuple(S)
    if not S:
        return True
    for order in permutations(S):
        earlier = set()
        good = True
        for s in order:
            _, T = s
            for q in bits(T):
                if not any(t[0] == q and (t[1] & ~T) == 0 for t in earlier):
                    good = False
                    break
            if not good:
                break
            earlier.add(s)
        if good:
            return True
    return False


def build_and_check(S, stages):
    S = tuple(sorted(S))
    n = len(S)
    index = {s: i for i, s in enumerate(S)}
    edges = [[False] * (n + 1) for _ in range(n + 1)]
    root = n

    for s in S:
        i = index[s]
        _, T = s
        for q in bits(T):
            candidates = [
                t for t in S
                if t[0] == q and (t[1] & ~T) == 0 and stages[t] < stages[s]
            ]
            if not candidates:
                return False
            t = min(candidates, key=lambda x: (stages[x], x))
            edges[i][index[t]] = True

    for s in S:
        edges[root][index[s]] = True

    # Transitive closure.
    for k in range(n + 1):
        for i in range(n + 1):
            if edges[i][k]:
                for j in range(n + 1):
                    if edges[k][j]:
                        edges[i][j] = True

    if any(edges[i][i] for i in range(n + 1)):
        return False
    for i in range(n + 1):
        for j in range(n + 1):
            if edges[i][j]:
                for k in range(n + 1):
                    if edges[j][k] and not edges[i][k]:
                        return False

    for s in S:
        i = index[s]
        observed = 0
        for j, t in enumerate(S):
            if edges[i][j]:
                observed |= 1 << t[0]
        if observed != s[1]:
            return False

    observed_spectrum = {S[j] for j in range(n) if edges[root][j]}
    return observed_spectrum == set(S)


accepted = []
size_distribution = {k: 0 for k in range(9)}
perm_mismatches = 0
construction_failures = 0

for mask in range(1 << len(TYPES)):
    S = tuple(TYPES[i] for i in range(len(TYPES)) if mask & (1 << i))
    closure, stages = support_closure(S)
    via_closure = closure == set(S)
    via_permutation = permutation_test(S)
    if via_closure != via_permutation:
        perm_mismatches += 1
    if via_closure:
        accepted.append(S)
        size_distribution[len(S)] += 1
        if not build_and_check(S, stages):
            construction_failures += 1

result = {
    "accepted_spectra": len(accepted),
    "construction_failures": construction_failures,
    "depth2_pointed_types": 2 * len(accepted),
    "equivalence_classes": "2^170",
    "permutation_mismatches": perm_mismatches,
    "size_distribution": {str(k): size_distribution[k] for k in range(9)},
    "total_candidate_spectra": 1 << len(TYPES),
}

assert result == {
    "accepted_spectra": 85,
    "construction_failures": 0,
    "depth2_pointed_types": 170,
    "equivalence_classes": "2^170",
    "permutation_mismatches": 0,
    "size_distribution": {"0": 1, "1": 2, "2": 5, "3": 12, "4": 21, "5": 22, "6": 15, "7": 6, "8": 1},
    "total_candidate_spectra": 256,
}
print(json.dumps(result, sort_keys=True, separators=(",", ":")))
