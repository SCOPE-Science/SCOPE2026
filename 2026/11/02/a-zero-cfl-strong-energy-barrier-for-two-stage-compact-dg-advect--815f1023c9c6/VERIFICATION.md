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

Run the standalone `verify.py` using Python 3 with SymPy installed. The verifier reconstructs a two-cell periodic DG operator from the coefficient weak form rather than assuming the two-dimensional alternating update. It checks all entries of the resulting compact-stage map, the exact \(-4\nu^4\) determinant, the generalized trace/product, the rational positive-energy-growth witness, and the exact maximal squared-energy formula. It also checks finitely many positive Courant values, independently from the identity proof.

The proof in `RESULT.md` establishes the quantifier **for every \(\nu>0\)** via a symbolic polynomial identity and indefinite symmetric matrix, not extrapolation from finite tests. The closed-form maximum refers only to the alternating invariant subspace; no maximization over all mesh modes was performed. No finite-precision or corrected-method guarantee is inferred. Source-access limitations and historical-priority risks are stated in `REVIEW.md`.

Independent audit has not been performed.
