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

Run `python3 CHECK.py` using the Python standard library. Its full-structure check enumerates all permutations through order seven at five positive rational inversion parameters and independently evaluates all order-eight permutations at one positive rational parameter. Its window-based check enumerates all standardized orders through length five and evaluates sixteen sample sizes at nine rational parameters. It independently verifies the universal covariance identity as an integer-polynomial identity, since the parameter \(n\) enters both sides affinely; checking two distinct integer values proves that algebraic equality for all values of \(n\). In total there are 285 explicit exact assertions.

The only infinite arguments not delegated to computation are positivity of denominators, Descartes' rule for the coefficient sign variation, the strict root ordering, and a Taylor expansion at the simple limiting root. These arguments appear in RESULT.md. This report does not constitute independent audit.
