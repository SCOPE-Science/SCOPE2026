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

# Reproducible verification

Run `python3 check_star_quiver.py` using a Python standard-library interpreter. The implementation independently enumerates all reduced-row-echelon-form central subspaces over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\) and directly tests inclusion of the selected arrow-image spans. It checks 96 configurations and 1,440 support sets against the Gaussian formula, reconstructs rank functions from nonempty thresholds, and inverts the coarse rank-profile transform. A separate \(\mathbb F_5\) comparison checks identical profiles for parameters \(2\) and \(3\) and exhaustively searches potential central invertible matrices with leaf rescalings for an isomorphism (none exists). It prints `ALL_STAR_QUIVER_CHECKS_PASSED` on success.

These computations test only prime fields of the listed orders and modest vector-space dimensions. The all-field scheme classification, finite-prime-power count formula, and general brick family rely on the given mathematical proof, not an exhaustive computation. No independent audit has been performed.
