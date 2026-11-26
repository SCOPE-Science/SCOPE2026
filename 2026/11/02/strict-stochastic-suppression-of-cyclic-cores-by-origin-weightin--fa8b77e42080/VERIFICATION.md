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

# Finite verification and mathematical limits

The unchanged `verify.py` enumerates all functions for sizes 2 through 7, computes origins and cyclic vertices directly, and compares exact rational cyclic tails to the uniform law and tilted mixture. It checks strict comparisons for the indicated weight pairs in the script. Its checks of conditional origin-count laws and uniform covariance, including the floating-point asymptotic diagnostic, concern auxiliary facts outside the narrowed finding.

The all-size, all-weight strict result is established by the prescribed-origin mixture and the likelihood-ratio comparison in `RESULT.md`, not by the finite checks.
