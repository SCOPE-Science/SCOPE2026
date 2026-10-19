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

# Verification

The checker uses only the Python standard library, including `fractions.Fraction`, and operates on the twelve antipodal representatives. Its exact quadratic-field arithmetic verifies the Legendre identity at degree nine and both left-nullspace constraints on all twelve rows. Exact modular row reduction in each of two prime fields gives the asserted ranks for degrees 0 through 119, inclusive. No floating-point rank decision is used.

The proof beyond degree 119 is analytic: the Legendre Bernstein bound from NIST DLMF 18.14.7 and the vertex angle bound ensure strict row diagonal dominance. The public proof states the normalization and all boundary conditions. An executable finite certificate does not by itself prove the infinite tail.

No independent audit, external certification, or experimental claim of uniqueness in the literature has been performed.
