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

# Verification scope

Run `python verify.py` using standard Python 3. The checker performs exhaustive finite-word enumeration for small alphabets and window lengths, exact rational first and second factorial moment comparisons, reversible detailed-balance checks for the proposed stationary generator, finite-size mean/covariance asymptotic consistency tests, and independent numerical quadratures of the Laplace identity. Its recorded run produced `186 deterministic finite-identity and consistency assertions passed`.

It does **not** certify functional convergence, uniform clock coupling, first-passage continuity, or originality. Those conclusions require the arguments and explicit limitations in RESULT.md. No independent audit has been performed.
