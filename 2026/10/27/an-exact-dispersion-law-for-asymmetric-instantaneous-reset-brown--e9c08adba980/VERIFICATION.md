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

# Reproduction and limits

Run `python3 check.py` with Python 3 and no third-party dependencies. The checker evaluates the scaled logarithmic derivative without overflowing at large resetting rates and brackets a zero at eight representative asymmetries. It checks both sides of the critical point, the numerical ordering of those eight roots, and several scaled near-endpoint roots. These are numerical diagnostics, not a proof of global optimality, monotonicity, or asymptotic scaling. The analytic proof is in `RESULT.md`.
