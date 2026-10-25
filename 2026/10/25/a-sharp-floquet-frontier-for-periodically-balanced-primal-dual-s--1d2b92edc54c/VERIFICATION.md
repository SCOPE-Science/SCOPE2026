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

# Reproducibility and verification

From the extracted package directory, install dependencies listed in `requirements.txt` and run `python verify.py`. No external data files are used. The verifier operates in exact SymPy integer/rational/algebraic arithmetic rather than estimating eigenvalues from floating-point simulations.

Checks performed: symbolic two-step recurrence characteristic trace/determinant; factorization of all three necessary-and-sufficient Schur margins; stationary-point and minimum calculations for the universal contrast threshold; an exact scalar growing eigenpair with a realizable first step; fourteen independent primal–dual updates matching the eliminated two-step recurrence; and exact rational monodromy characteristic polynomial and excitation minor for the strictly strongly convex–concave example.

The test run returned the literal line `VERIFY_OK: Floquet polynomial, exact Schur margins, dimension-free threshold,` followed by `  bilinear unstable mode, fourteen direct updates, strongly convex rational certificate`.

The analytic proof establishes the infinite-time assertions. The finite direct-iteration checks only verify implementation consistency and do not constitute an independent proof or external validation. No stochastic-block or floating-point-roundoff guarantee is asserted.
