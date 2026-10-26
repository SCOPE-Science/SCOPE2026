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

# Verification and limits

The companion executable `verify.py` can be run from the same directory using `python verify.py` with NumPy installed. It tests the exact rational SPD projected-system identities, independent direct Galerkin and least-squares solves across Krylov steps and sketch sizes, and the normalization and selected moments of the underlying multivariate Student density.

The infinite-order claims and the exact hyperplane-tail constant require the density, cofactor, transversal integral, and norm-comparison proofs in `RESULT.md`. The finite checks are not certificates of population moments, numerical software stability or mathematical novelty. No independent scientific audit has been performed.
