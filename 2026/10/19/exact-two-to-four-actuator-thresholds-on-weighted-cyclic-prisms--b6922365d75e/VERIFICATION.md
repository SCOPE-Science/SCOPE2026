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

# Exact verification

The complete analytical verification is in `RESULT.md`: the spectrum of the tensor-sum Laplacian, a complete classification of eigenvalue collisions, a PBH multiplicity lower bound, and exact nonvanishing evaluation minors for the given actuator placements. The special even-cycle single-to-single collision uses the explicit determinant \(\sigma-(-1)^d\).

The standalone `verify.py` runs 18 full-size, exact-rational Kalman-rank checks on prisms with \(n=3,4,5,6\), plus an exact algebraic check of the double-to-double resonance at \(n=5\). It requires Python 3 and SymPy. Execute `python verify.py`. Its finite checks are not substituted for proof of the all-order and all-weight theorem. The source dates and literature comparisons support a self-review; independent scientific auditing remains unperformed.
