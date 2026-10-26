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

# Reproducibility

Run `python3 verify.py` with Python 3 standard library. The verifier enumerates all monotone regressive transformations on orders one through ten and independently checks root-block decomposition, canonical breadth-first tree numbering, the Dyck-height statistic, rational-series coefficients for every feasible exponent, Catalan totals, low-depth Fibonacci/power formulas, and the unique longest-depth map. It prints `VERIFY_OK_CATALAN_POWER_STABILIZATION` on success.

The general all-order theorem is proved in RESULT.md. Neither finite test results nor self-review constitute independent certification. Broader historical priority cannot be proved by negative search results.
