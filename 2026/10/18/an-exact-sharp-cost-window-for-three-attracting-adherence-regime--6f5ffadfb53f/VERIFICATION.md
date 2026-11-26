---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The accompanying `verify.py` checks exact polynomial identities, selected rational endpoint values, and positivity of rational Bernstein coefficients on the closed interval that contains every upper endemic root in the cost window. Its auxiliary radical comparisons use floating-point square roots. The analytic argument in `RESULT.md` establishes the all-parameter ceiling and the exact cost thresholds.
