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

# Reproducibility
Run `python verify_degree_one_motifs.py` using standard Python. The test builds all fixed-edge labeled graphs for selected orders and all injective motif maps independently, then compares exact integer-derived rational covariances with the theorem. The recorded execution passed 72 exhaustive graph checks and 2,896 rational sign-monotonicity-grid cases. In `G(12,10)`, the separately computed path and star ratios were 41664/49555 and 11284/9911.

## Interpretation and limits
The proof is analytic and covers the theorem's full parameter range; the verifier checks only the cases explicitly enumerated in its source. An exact finite computation is not independent mathematical certification or a proof by exhaustive enumeration of infinite parameters. Historical priority also remains subject to further source access and independent examination.
