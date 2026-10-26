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

# Reproducible checks and limits

Execute `python3 verify.py` (Python standard library only) and compare its complete output to `certificate.json`. The verifier uses exact rational arithmetic and asserts strict inequalities for the initial peak and the two internal peaks of the explicit three-species distribution. It verifies finite instances only; the general theorem is justified by the analytic exponential-polynomial zero bound and the separate asymptotic construction in `RESULT.md`. No independent third-party audit is asserted.
