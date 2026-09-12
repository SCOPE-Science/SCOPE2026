"""Final bounded verification for the TARGET disproof (stdlib only).

Labelled-level (isomorphism-free) certificate:
  L = {C1, C2} union all one-step Pasch switches of C1 and C2 (as labelled
  block sets on Z19). Since J=(pasch,mitre) is an isomorphism invariant,
  |J(N)| <= |J(L)| over the iso-class neighbourhood N. Showing |J(L)| = 5
  refutes the target's >= 10 claim with no isomorphism test anywhere.

Cross-checks (independent code paths):
  - Pasch count: pair-shared-point enumerator (sts19_lib.find_pasches) vs
    6-subset census (a Pasch <=> 6-point subset containing exactly 4 blocks;
    verified each such 6-set is a genuine quadrilateral: 6 points, 4 blocks,
    every point degree 2).
  - Mitre count: root+arms+transversal counter (sts19_lib.count_mitres) vs
    7-subset degree-sequence brute force (5 blocks on 7 points with degrees
    [3,2,2,2,2,2,2]).
Writes ledger_labelled.json.
"""
import itertools
import json
import sys
import time
from collections import Counter

sys.path.insert(0, "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1112/output/artifacts")
from sts19_lib import blocks_from_bases, check_sts, find_pasches, count_mitres, pasch_switch

V = 19
C1 = [[1, 4], [2, 9], [5, 11]]
C2 = [[1, 8], [2, 5], [4, 10]]
OUT = "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1112/output/artifacts/ledger_labelled.json"


def pasch_sixset(bl):
    """Independent Pasch census: 6-sets spanning exactly 4 blocks, each a
    quadrilateral (every point in exactly 2 of the 4 blocks)."""
    blsets = [frozenset(b) for b in bl]
    n = 0
    for six in itertools.combinations(range(V), 6):
        S = frozenset(six)
        inside = [b for b in blsets if b <= S]
        if len(inside) == 4:
            deg = Counter()
            for b in inside:
                for x in b:
                    deg[x] += 1
            assert len(deg) == 6 and sorted(deg.values()) == [2, 2, 2, 2, 2, 2], (six, inside)
            n += 1
    return n


def mitre_bruteforce(bl):
    blsets = [frozenset(b) for b in bl]
    n = 0
    for seven in itertools.combinations(range(V), 7):
        S = frozenset(seven)
        inside = [b for b in blsets if b <= S]
        if len(inside) != 5:
            continue
        deg = Counter()
        for b in inside:
            for x in b:
                deg[x] += 1
        if len(deg) == 7 and sorted(deg.values()) == [2, 2, 2, 2, 2, 2, 3]:
            n += 1
    return n


def main():
    t0 = time.time()
    seeds = {"C1": C1, "C2": C2}
    seed_bl = {}
    for name, fam in seeds.items():
        bl = blocks_from_bases(fam)
        assert check_sts(bl), name
        seed_bl[name] = bl
    # labelled switches per seed
    sw = {}
    for name, bl in seed_bl.items():
        ps = find_pasches(bl)
        sets = set()
        for p in ps:
            nb = pasch_switch(bl, p)
            assert check_sts(nb)
            sets.add(tuple(nb))
        sw[name] = (ps, sets)
        print(f"{name}: {len(ps)} pasches -> {len(sets)} distinct labelled switched sets", flush=True)

    # cross-seed / seed overlap (labelled identity)
    sC1, sC2 = seed_bl["C1"], seed_bl["C2"]
    print("seeds labelled-distinct:", tuple(sC1) != tuple(sC2), flush=True)
    for name, (_, sets) in sw.items():
        print(f"{name} switch == own seed (labelled)?", tuple(seed_bl[name]) in sets, flush=True)
    print("C1-switch == C2-switch overlap (labelled):", len(sw["C1"][1] & sw["C2"][1]), flush=True)
    print("C1-switch == C2 seed?", tuple(sC2) in sw["C1"][1],
          "| C2-switch == C1 seed?", tuple(sC1) in sw["C2"][1], flush=True)

    # J census over every labelled design + independent cross-checks on one
    # representative of each distinct J value (seeds + first switch per J).
    reps = {}  # J -> (label, blocks)
    rows = []
    for name, bl in seed_bl.items():
        p1, m1 = len(find_pasches(bl)), count_mitres(bl)
        reps.setdefault((p1, m1), (f"seed:{name}", bl))
        rows.append({"label": f"seed:{name}", "pasch_fast": p1, "mitre_fast": m1})
    for name, (ps, sets) in sw.items():
        dist = Counter()
        for i, nb in enumerate(sorted(sets)):
            nb = list(nb)
            j = (len(find_pasches(nb)), count_mitres(nb))
            dist[j] += 1
            reps.setdefault(j, (f"sw({name})#{i}", nb))
        print(f"{name} switch J distribution: {sorted((list(k)+[v]) for k, v in dist.items())}", flush=True)
        for j, c in sorted(dist.items()):
            rows.append({"label": f"sw({name})", "J": list(j), "count": c})

    print("distinct J over all labelled designs:", sorted(reps), flush=True)
    assert len(reps) == 5, reps.keys()

    # independent recount of each distinct-J representative
    for j, (label, bl) in sorted(reps.items()):
        p2 = pasch_sixset(bl)
        m2 = mitre_bruteforce(bl)
        ok = (p2 == j[0] and m2 == j[1])
        print(f"J={j} rep {label}: sixset-pasch={p2} brute-mitre={m2} -> {'OK' if ok else 'MISMATCH'}",
              flush=True)
        assert ok, (j, p2, m2)
        rows.append({"rep_label": label, "J": list(j),
                     "pasch_sixset": p2, "mitre_bruteforce": m2, "match": True,
                     "blocks": [list(b) for b in bl]})

    json.dump({"C1": C1, "C2": C2,
               "n_pasch_C1": len(sw["C1"][0]), "n_pasch_C2": len(sw["C2"][0]),
               "n_labelled_sw_C1": len(sw["C1"][1]), "n_labelled_sw_C2": len(sw["C2"][1]),
               "distinct_J": sorted([list(k) for k in reps]),
               "rows": rows,
               "elapsed_s": round(time.time() - t0, 1)},
              open(OUT, "w"))
    print(f"wrote {OUT} elapsed={round(time.time()-t0,1)}s VERIFY_OK", flush=True)


if __name__ == "__main__":
    main()
