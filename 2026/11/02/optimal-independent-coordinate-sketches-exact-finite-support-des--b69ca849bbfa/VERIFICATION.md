---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

# Verification

The analytic proof establishes the sharp ratio on the infinite spectrum. The unchanged `coupon_checker.py` in the original package supplies standard-library diagnostics: finite coupon-space enumeration, stationarity and normalization, the two-draw case, and finite-budget approaches to the predicted ratio. The original record reports 90 check families; these are finite corroboration, not an asymptotic proof. The finite-support allocation is a known weighted-cache rule, and is used as a proof ingredient. Full-support sketch laws are isotropic in the scalar-product sense, even though the squared sketch norm has infinite expectation.
