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

The proof is analytical and unrestricted in complex coefficients. Finite testing is corroborative only. The supplied `checker.py` recomputes coefficient convolutions, checks the exact shell fourth-power expression, the center–shell polynomial, the six-corner tensor estimate, random complex-coefficient inequalities, a two-angle family of equality vectors, and normalized finite-torus moments at orders 5, 6 and 7.

Run with `python checker.py` using the Python standard library. The deterministic run records 3,589 passed assertions and reports the positive cubic root and exact-rational-envelope value numerically. No computer calculation proves the all-coefficient inequality; that follows from the displayed convolution identities, Cauchy bounds, singular-value estimate, and one-variable derivative sign. Independent mathematical audit has not occurred. No finite-grid assertion is made for orders below five.
