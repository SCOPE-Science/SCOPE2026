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

# Reproducibility of the mathematical finding

The endpoint matrix is computed independently in `verify.py` as a finite Taylor sum of matrix powers using Python `fractions.Fraction`. It is then compared exactly with the derived transient and absorbing formulas. The script checks orders 2 through 10, transient-state counts 1 through 8, and six rational step sizes; it also tests the closed staircase boundaries in orders 3 through 10. The script uses no downloaded datasets and only the Python standard library. The run printed `VERIFY_OK` and reported 10400 counted checks.

The proof, rather than these finite tests, establishes the sign pattern for all orders and dimensions, uniqueness of the odd-degree roots, sharpness for all \(h>H_{p,d}\), the dimension staircase, and the two fixed-dimensional asymptotic constants. There is no assertion of infinite exhaustive computation or external validation.
