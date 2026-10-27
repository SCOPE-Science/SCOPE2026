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

# Reproduction and boundaries

Run `python3 check_certificate.py` using Python 3's standard library. Its rational arithmetic regenerates the squared-multinomial three-step moments, calculates the hypothetical dimension-three and dimension-four Schoenberg moments, and asserts the two negative determinant identities and two negative polynomial-square identities. No floating-point rounding, external package, internet connection, or finite-site search enters the certificate.

The mathematical inference from a negative Hankel determinant to failure of radial positive definiteness uses Schoenberg's representation and the elementary nonnegativity of integrals of polynomial squares. Finiteness of moments follows from the analytic positive-definite characteristic function through nonnegative finite differences. The checker certifies the finite arithmetic component; the representation theorem, moment implication, planar positivity, scale invariance, and exclusion of larger dimensions are mathematical proof steps, not code outputs.

The exact moment obstruction does not provide an explicit finite negative Gram matrix, classify all powers, or constitute an independent mathematical audit.
