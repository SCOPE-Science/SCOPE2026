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

# Reproducibility

The unchanged `checks/verify.py` (Python 3, NumPy and SciPy) implements a finite comparison of the Gauss–Jacobi Beta integral and a hypergeometric root equation, and probes curvature, mode opening and the two endpoint expansions. Its original packaged run reports 48 deterministic assertions. This is finite numerical corroboration only.

The analytical check of the global real zero bound uses exponential test functions and integration by parts with controlled endpoint terms. The nearly uniform endpoint uses a uniform Taylor bound on the lower half of the beta integral and an integrable estimate on the upper half. Neither assertion is inferred from the finite numerical checks.
