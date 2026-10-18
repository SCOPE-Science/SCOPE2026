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

Exact checks were performed using the standalone `check.py` supplied with this finding. It independently forms linearizations as sums of matrix products, uses modular Gaussian elimination for block ranks for exponents 2 through 7 over the prime fields of orders 2, 3, 5, and 7, and directly enumerates all dual coefficients in six finite cases. All assertions passed and the program printed `ALL_EXACT_CHECKS_PASSED`.

The infinite theorem does not follow from these computations; it is supplied by the polynomial-quotient rank proof and nilpotent orbit-size argument. No extension-field brute force or independent mathematical certification was performed.
