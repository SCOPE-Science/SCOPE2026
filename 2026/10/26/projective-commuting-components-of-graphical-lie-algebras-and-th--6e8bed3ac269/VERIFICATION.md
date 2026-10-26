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

# Direct small-field verification

Execute `python3 verify.py` using Python 3 and its standard library. The script constructs the edge-indexed Lie brackets and evaluates projective commutation directly from \(x_u y_v-x_v y_u\) on every input-graph edge. It computes the observed connected-component partition of each projective commuting graph. Separately, it constructs the predicted complement-block partition by checking connected-dominating supports, and compares the **full sets of projective points in every component**, not merely their sizes. It also checks the exact isolate count and the tree leaf formula.

The executed verifier printed `VERIFY_OK 2950 direct bracket component comparisons`. The cases include all labeled graphs without isolated vertices on \(n=2,3,4,5\) vertices over \(\mathbb F_2\) and \(\mathbb F_3\), every tree on six labeled vertices over \(\mathbb F_2\), and a systematic six-vertex tree sample over \(\mathbb F_3\). These are finite tests, not exhaustive enumeration of all finite graphs and fields. The infinite claims, including arbitrary prime-power fields and the diameter bound, are supported by the mathematical argument in RESULT.md and not inferred from computations. No external audit or independent mathematical validation has been performed.
