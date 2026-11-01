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

# Verification record

The proof in `RESULT.md` is the basis for the universal result. The key nonstandard calculation is the exact boundary identity \(\overline{\phi}Q^2=\kappa^{-1}QP^{\#}\), and the critical domain condition is \(\phi(\kappa^{-1}QP^{\#})=\kappa^{-1}PP^{\#}\), both polynomials. With the norm formula and adjointness this yields the entrywise Toeplitz formula for arbitrary indices before finite truncation. The last-row count follows directly from the degree of \(Q^2\).

Run the standalone Python standard-library script `python CHECK.py` from the package directory. Six exact Gaussian-integer examples cover a repeated boundary pole, two opposite poles, two distinct nonreal-complex coefficients, mixed multiplicities and a fourth-order pole. The script verifies \(Q^{\#}=\kappa Q\), computes coefficients by the exact rational-function recurrence, and compares 726 transformed Gram entries against the explicit Toeplitz symbol. In the displayed bounded examples, ordinary floating-point complex arithmetic represents all intermediate Gaussian integers exactly; a failed equality raises an assertion. This is a supplementary finite check only, not an exhaustion of all coefficients or degrees.

All normalization assumptions, matrix orientation, degree ranges, and the possible \(P=0\) case are specified in `RESULT.md`. No independent mathematical audit has been performed.
