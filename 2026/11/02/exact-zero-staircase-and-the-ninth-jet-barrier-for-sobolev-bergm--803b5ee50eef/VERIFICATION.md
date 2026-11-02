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

# Verification evidence and limits

The analytic proof verifies the monomial normalization, scalar-zero reduction, root simplicity, boundary phase, inward crossing sign, exact threshold ordering, and high-order missing-root count. In particular, the finite root count is not inferred from a numerical table.

A standalone Python/NumPy reproduction script, `checks.py`, was run from the accompanying package. It printed `VERIFY_OK 1130 finite assertions`. The finite assertions compare the independent numerical polynomial roots against the closed crossing-count formula over multiple penalties and jet orders, and check low-degree endpoint formulas.

The script requires Python 3.10+ and NumPy and can be run with `python checks.py`. Its finite checks are auxiliary rather than evidence of arbitrary-parameter or asymptotic certification. No independent external mathematical audit has been conducted.
