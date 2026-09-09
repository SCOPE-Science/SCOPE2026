#!/usr/bin/env python3
"""Independent verifier for the primitive 3-set census (max<=10, heaps 0..500).

Recomputes every Grundy table from the subtraction-set rules alone (mex DP),
then checks each claimed row (S, N0, p, M, h, nP):
  (C1) closing window: G[n]==G[n+p] for all n in [N0, 500-p], with N0+p+max(S)-1<=500
  (C2) period leastness: for every 1<=q<p, some n in [N0,500-q] has G[n]!=G[n+q]
  (C3) preperiod leastness: if N0>=1 then G[N0-1]!=G[N0-1+p]
  (C4) maximal witness: max(G[0..500])==M with least witness index h
  (C5) cold count: |{n<=500 : G[n]==0}| == nP
C1 plus the closing-window lemma (proved in DRAFT.md) promotes the finite
check to true infinite eventual periodicity; C2/C3 promote to globally least
(N0, p) by the tail-rigidity argument (proved in DRAFT.md).
Usage: python3 verify.py [census.json]
"""
import json
import sys

NMAX = 500


def grundy(S, nmax):
    G = [0] * (nmax + 1)
    for n in range(1, nmax + 1):
        seen = set()
        for s in S:
            if n >= s:
                seen.add(G[n - s])
        g = 0
        while g in seen:
            g += 1
        G[n] = g
    return G


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "census.json"
    with open(path) as f:
        data = json.load(f)
    assert data["NMAX"] == NMAX, "window mismatch"
    rows = data["rows"]
    assert len(rows) == 109, f"expected 109 rows, got {len(rows)}"
    seen_sets = set()
    for r in rows:
        S = r["S"]
        assert len(S) == 3 and S == sorted(S) and max(S) <= 10, f"bad set {S}"
        import math
        assert math.gcd(math.gcd(S[0], S[1]), S[2]) == 1, f"non-primitive {S}"
        seen_sets.add(tuple(S))
        m = max(S)
        N0, p, M, h, nP = r["N0"], r["p"], r["M"], r["h"], r["nP"]
        G = grundy(S, NMAX)
        assert N0 + p + m - 1 <= NMAX, f"{S}: cutoff exceeds window"
        for n in range(N0, NMAX - p + 1):  # C1
            assert G[n] == G[n + p], f"{S}: C1 fails at n={n}"
        for q in range(1, p):  # C2
            assert any(G[n] != G[n + q] for n in range(N0, NMAX - q + 1)), \
                f"{S}: C2 fails for q={q}"
        if N0 >= 1:  # C3
            assert G[N0 - 1] != G[N0 - 1 + p], f"{S}: C3 fails"
        assert max(G) == M and G.index(M) == h, f"{S}: C4 fails"  # C4
        assert sum(1 for g in G if g == 0) == nP, f"{S}: C5 fails"  # C5
    # census completeness: all C(10,3) primitive triples present
    import itertools
    import math
    full = {s for s in itertools.combinations(range(1, 11), 3)
            if math.gcd(math.gcd(s[0], s[1]), s[2]) == 1}
    assert seen_sets == full, "census family incomplete"
    pure = sum(1 for r in rows if r["N0"] == 0)
    print(f"VERIFY_OK: 109/109 rows, checks C1-C5 pass; "
          f"pure N0=0: {pure}, max N0: {max(r['N0'] for r in rows)}, "
          f"max period: {max(r['p'] for r in rows)}, "
          f"max M: {max(r['M'] for r in rows)}")


if __name__ == "__main__":
    main()
