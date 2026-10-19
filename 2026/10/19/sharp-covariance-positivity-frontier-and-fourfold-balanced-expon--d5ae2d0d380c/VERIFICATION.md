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

# Reproducible checks

Execute `python3 verify.py` from the extracted file set with Python 3.9 or later. The verifier has no third-party dependencies and uses deterministic constants and a seeded pseudorandom generator. It reports `PASS: 18692 deterministic checks; representative threshold h=0.291803874626216`.

Checks cover integral coefficients, the two-mode PSD determinant, monotone correlation cutoff, strict finite-step Frobenius comparison, fixed-time small-step asymptotics, and five-mode positive-semidefinite Gram forcing. The proof, not the finite verifier, supplies the universal all-dimensional assertions and the strict limiting inequalities. No floating-point result is used as proof of an exact branch or infinite limiting statement.

The claim assumes constant forcing, symmetric negative-definite drift, and exact matrix functions; generalized nonlinear problems and cost-optimal implementations remain unproved. Independent audit: not performed.
