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

The theorem is proved symbolically in `RESULT.md` by exact majority-threshold inequalities for a clique with one distinguished bridge vertex and a two-clique case analysis. This proof does not rely on finite-state interpolation.

The standalone verifier `barbell_verify.py` directly constructs adjacency neighbourhood masks, applies the synchronous tie-retaining majority rule to each labelled binary configuration, determines the earliest state satisfying the two-step return condition, and independently checks the theoretical formulas for all \(3\le a,b\le8\).

Reproduction: `python3 barbell_verify.py` (Python 3.9+). The recorded output `barbell_verify.out` ends with `BARBELL_MAJORITY_VERIFY_OK cases=36 labelled_states=254016 nonzero_strata=189`. Checks include equality of four fixed states, nonfixed periodic states, maximum depth, and exact maximum-depth populations in all three parity regimes. The test covers \(254016\) individual labelled configurations on \(36\) graph instances.

Finite tests are not an exhaustive certificate for all graph sizes. No external independent audit, proof-assistant formalization, or verification of every historical paper has been carried out.
