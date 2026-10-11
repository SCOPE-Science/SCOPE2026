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

## Mathematical verification
The exact Cayley identity, coefficient bounds of the Schur transform, and global cubic minimization appear in `RESULT.md`. The endpoint and interior critical-angle evaluations are exhaustive because the cubic derivative has at most two critical points. For each branch, substituting the formula for \(B(a)\) into the quadratic boundary inequality gives zero; the boundary defect decreases for larger nonnegative \(|b|\). The concavity check is an explicit second derivative, including the downward derivative jump at the branch point.

Run `python3 check_region.py` for finite-parameter algebra and boundary sanity checks. These checks supplement, not replace, the proof over all parameters. No automated external independent audit has occurred. Originality comparisons cannot preclude unindexed equivalent publications. No claim is made for complex coefficients or longer Laurent series.
