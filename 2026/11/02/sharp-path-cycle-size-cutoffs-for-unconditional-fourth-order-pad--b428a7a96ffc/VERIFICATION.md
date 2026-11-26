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

# Reproducibility and boundaries

Run `python3 verify.py`. With exact rational arithmetic the script checks the homogeneous path pseudoinverse coefficient at orders 2 through 10. It compares selected two- and three-vertex end-step matrices with the small-order formulas, including time zero, and tests the negative entry for orders 4 through 10 at a large positive step. The run printed `PASS: 9 path coefficients, 10 small-path kernels, 7 large-step witnesses`. These spot checks corroborate but do not replace the analytic proof for all orders and real steps in `RESULT.md`.
