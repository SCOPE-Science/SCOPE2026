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

# Reproduction and verification

The exact finite covariance used as input can be checked with the unchanged `verify.py` (standard Python 3); the script enumerates 16 finite rational models and compares two moment recurrences over 294 further parameter pairs. It conditions on the original root degree. Other conditional-tail tests in the script concern the same tree model but are not needed for the covariance peak.

The all-parameter upper bound, uniform window profile and localization of every maximizer are established by the mathematical proof in `RESULT.md`. The numerical window diagnostics in `verify.py` are illustrations and do not verify a uniform limit or optimization over the continuum.
