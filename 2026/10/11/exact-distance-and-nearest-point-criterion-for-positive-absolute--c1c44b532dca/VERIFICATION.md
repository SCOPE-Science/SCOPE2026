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

# Reproducibility and verification notes

The finding is an analytic spectral theorem and requires no finite computational certificate. The full domain, normalization and source of the imported positive absolute norm-attainment criterion are specified in RESULT.md.

Checks carried out: (1) verify the Calkin norm formula for a positive self-adjoint element and the unique minimizer of the two-endpoint Chebyshev problem; (2) verify that the part of the spectrum below the essential minimum by a fixed positive gap has finite-rank projection; (3) verify compactness of the positive part above the essential spectral maximum by continuous functional calculus; (4) verify that the spectral clipping is positive and has finite-rank negative part about the essential midpoint; (5) verify the strict-expectation contradiction against an infinite-dimensional lower spectral subspace; and (6) separately check the zero-width and zero-bottom cases.

Illustrative diagonal models with essential spectrum \(\{1,2\}\) show both outcomes: infinitely many coefficients below \(1\) obstruct a minimizer, whereas all coefficients at least \(1\) admit spectral clipping. Finite-prefix numerical calculations are consistent with the explicit formulas, but they do not certify an infinite-dimensional result.

The quoted characterization is due to the primary literature; the new approximation theorem has undergone same-model review only. Independent audit was not performed.
