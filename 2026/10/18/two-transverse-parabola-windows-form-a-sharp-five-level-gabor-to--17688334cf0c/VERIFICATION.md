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

# Verification and reproducibility

The all-odd-prime-power theorem follows from the Weyl-character orthogonality and finite-field argument in `RESULT.md`. In particular, each translated parabola intersects the original in either zero or one point for a nonzero shift and in all \(q\) points for the zero shift; quadratic character sums have exact magnitude \(\sqrt q\) when their quadratic coefficient is nonzero. These establish the complete normal spectrum for every field in scope.

Run `python checks/verify_two_parabola_gabor.py` from the package root with Python 3 and NumPy. The program independently enumerates ambiguity coefficients for \(q=3,5,7,9\), including a genuine extension field of order nine, and compares their integer-rounded spectra to the formulas. For \(q=3,5\), the separate direct projector-lift matrix calculation has eigenvalues within \(10^{-7}\) of the theoretical spectrum. The exact finite results and floating-point output are preserved at `checks/verification_output.txt`.

Finite enumerations are sanity checks and are not a proof for all odd fields. Nothing here constitutes an external or independent audit, and no full classification of alternative designs or optimal conditioning under a different sparsity constraint is claimed.
