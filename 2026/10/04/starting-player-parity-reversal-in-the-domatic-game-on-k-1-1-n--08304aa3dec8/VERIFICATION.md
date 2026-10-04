---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The proof is analytic. Its critical checks are:

1. In a completed two-coloring of \(K_{1,1,n}\), a color class that misses both universal vertices dominates only when it contains every vertex of the independent part. Exhausting terminal colorings in the bundled checker confirms this characterization for \(2\le n\le7\).
2. The four parity/starting-player strategies in `RESULT.md` are finite pairing strategies and do not depend on the computational range.
3. Hartnell--Rall's published even-minimum-degree bound gives \(\operatorname{dom}_g,\operatorname{dom}^\prime_g\le2\) when \(\delta=2\). The proof does not infer this infinite upper bound from finite experiments.
4. `verify.py` independently constructs the adjacency relation, computes domination directly, solves the alternating game by exact minimax, and checks the ordinary three-class domatic partition for every \(2\le n\le7\).

Reproduction command:

`python3 verify.py`

Expected output is recorded verbatim in `verification_output.txt`.

The finite replay is not an exhaustive proof for arbitrary \(n\); it is a stress test of the terminal characterization and strategy outcomes. No independent audit has been performed.
