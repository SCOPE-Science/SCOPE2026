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

The proof relies on direct, invertible symmetric congruences of \(I-T_h^\mathsf{T}T_h\) and \(A^{-1}-T_h^\mathsf{T}A^{-1}T_h\), followed by a rank-two eigenvalue calculation and an SPD comparison. These establish the quantified results in every finite dimension and at all positive step sizes, including the exact boundary.

Run `python3 checker.py` to reproduce 1,792 two-dimensional exact-rational matrix tests. Each test independently checks the Euclidean congruence identity, the inverse-generator-weighted congruence identity, the semidefinite sign correspondence and the rank-one closed-form threshold away from roundoff-ambiguous boundary comparisons. Two rational witnesses at the transition and beyond it are computed exactly; no external library or data file is required.

Numerical enumeration does not prove spectral statements in arbitrary dimension. The proof supplies the required strictly positive operator inequalities and handles the eigenvector-aligned and one-dimensional cases. This package does not constitute an independent review, mechanized infinite proof or external certification. The method's full-order accuracy, nonlinear behavior and varying-step product bounds are not established.
