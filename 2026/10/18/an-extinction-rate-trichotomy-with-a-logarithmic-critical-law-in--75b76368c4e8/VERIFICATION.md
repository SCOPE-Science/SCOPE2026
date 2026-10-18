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

Reproduce exact identities by running `python verify.py` with SymPy installed. The program checks the exact reduced ratio field, its zero-density expansion, subcritical asymptotic coefficients, critical limiting coefficient, and the existence/stability of the example's positive equilibria. It evaluates the ratio-field sign for rational sample states; no floating calculation or finite-time output is used to infer the infinite-time theorem. The analytic proof and sector trapping in `RESULT.md` establish the latter. No external independent verification has been performed.
