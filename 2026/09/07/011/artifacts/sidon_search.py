"""Sidon census in Z_60 — primary exhaustive search (difference-occupancy pruning).
Frozen definitions:
  n=60, Sidon primary = all k(k+1)/2 sums a+b mod 60 (a<=b) distinct.
  Cross-check = all k(k-1) ordered differences a-b (a!=b) nonzero+distinct (Lemma 1: equivalent).
  Search: fix 0, increasing order, deterministic (seed 0, no RNG).
  Node = accepted partial Sidon set visited (incl. root {0}).
  Attempt = candidate v trial.
  Pruning: reject v if any new difference (v-a),(a-v) is 0, equals occupied, equals another new diff (incl. d1==d2 i.e. distance 30), else accept.
  Soundness: superset of non-Sidon is non-Sidon, so pruning complete.
  Canonical: trans-canonical = lex-min sorted tuple among translates containing 0 (= min over all 60);
             dihedral-canonical = min(trans-canonical(A), trans-canonical(-A)).
Stdlib only. Usage: python3 sidon_search.py [--out DIR]
Writes: k8_exhaustion.json, sidon7_translation_reps.json, sidon7_dihedral_reps.json, witness.json
"""
import sys, time, json, hashlib, os, argparse

N = 60
SEED = 0
ORDER = "increasing"

def trans_canonical(S):
    best = None
    for a in S:
        T = tuple(sorted(((x - a) % N for x in S)))
        if best is None or T < best:
            best = T
    return best

def dihedral_canonical(S):
    c1 = trans_canonical(S)
    neg = tuple(sorted(((-x) % N for x in S)))
    c2 = trans_canonical(neg)
    return c1 if c1 < c2 else c2

def sums_of(S):
    return sorted({(a + b) % N for i, a in enumerate(S) for b in list(S)[i:]})

def diffs_of(S):
    return {(a - b) % N for a in S for b in S if a != b}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.dirname(os.path.abspath(__file__)))
    args = ap.parse_args()
    out = args.out
    os.makedirs(out, exist_ok=True)
    sys.setrecursionlimit(10000)
    visited = 0
    attempts = 0
    from collections import Counter
    bydepth = Counter()
    solutions7 = []
    solutions8 = []
    t0 = time.perf_counter()
    # iterative recursion with explicit diff set
    def dfs(current, D):
        nonlocal visited, attempts
        visited += 1
        bydepth[len(current)] += 1
        d = len(current)
        if d == 8:
            solutions8.append(tuple(current))
            return
        if d == 7:
            solutions7.append(tuple(current))
        start = current[-1] + 1
        for v in range(start, N):
            attempts += 1
            ok = True
            seen = set()
            adds = []
            for a in current:
                d1 = (v - a) % N
                d2 = (a - v) % N
                if d1 == 0 or d2 == 0 or d1 == d2:
                    ok = False; break
                if d1 in D or d2 in D:
                    ok = False; break
                if d1 in seen or d2 in seen:
                    ok = False; break
                seen.add(d1); seen.add(d2)
                adds.append(d1); adds.append(d2)
            if not ok:
                continue
            for x in adds: D.add(x)
            current.append(v)
            dfs(current, D)
            current.pop()
            for x in adds: D.remove(x)
    dfs([0], set())
    t1 = time.perf_counter()
    elapsed = t1 - t0
    # canonical reduction
    trans_map = {}
    for S in solutions7:
        c = trans_canonical(S)
        trans_map.setdefault(c, []).append(S)
    trans_reps = sorted(trans_map.keys())
    dih_map = {}
    for c in trans_reps:
        d = dihedral_canonical(c)
        dih_map.setdefault(d, []).append(c)
    dih_reps = sorted(dih_map.keys())
    # witness
    W = (0,1,3,7,12,20,38)
    wsums = sums_of(W)
    wdiffs = sorted(diffs_of(W))
    # checksums
    h_dih = hashlib.sha256(json.dumps(dih_reps).encode()).hexdigest()
    h_trans = hashlib.sha256(json.dumps(trans_reps).encode()).hexdigest()
    exh = {
        "n": N, "seed": SEED, "order": ORDER,
        "definition": "sums-distinct primary (k(k+1)/2 sums a+b,a<=b mod 60 distinct); differences cross-check",
        "canonical": "lex-min translate containing 0; dihedral = min(canonical(A),canonical(-A))",
        "visited_nodes": visited,
        "candidate_attempts": attempts,
        "depth_distribution": {str(k): bydepth[k] for k in sorted(bydepth)},
        "num_rooted_7": len(solutions7),
        "num_8": len(solutions8),
        "num_translation_classes": len(trans_reps),
        "num_dihedral_classes": len(dih_reps),
        "elapsed_sec": elapsed,
        "sha256_dihedral_reps": h_dih,
        "sha256_translation_reps": h_trans,
        "witness": list(W),
        "witness_sums": wsums,
        "witness_num_sums": len(wsums),
        "witness_num_diffs": len(wdiffs),
    }
    with open(os.path.join(out, "k8_exhaustion.json"), "w") as f:
        json.dump(exh, f, indent=2, sort_keys=True)
    with open(os.path.join(out, "sidon7_dihedral_reps.json"), "w") as f:
        json.dump({"n": N, "count": len(dih_reps), "sha256": h_dih, "reps": [list(r) for r in dih_reps]}, f, indent=1, sort_keys=True)
    with open(os.path.join(out, "sidon7_translation_reps.json"), "w") as f:
        json.dump({"n": N, "count": len(trans_reps), "sha256": h_trans, "reps": [list(r) for r in trans_reps]}, f, indent=1, sort_keys=True)
    with open(os.path.join(out, "witness.json"), "w") as f:
        json.dump({"witness": list(W), "sums": wsums, "diffs": wdiffs, "num_sums": len(wsums), "num_diffs": len(wdiffs)}, f, indent=2, sort_keys=True)
    print(json.dumps(exh, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
