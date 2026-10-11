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

# Verification

Run `python3 verify_gap3_roots.py` with standard Python 3. The script reconstructs the diagonal numerator via source equations (3.21) and compares the exact coefficient formulas for 61 integers in each of the two coprime progressions. It computes and compares the exact discriminant factorization and the cubic values at the endpoints with integer/rational arithmetic. It reports 610 successful exact checks.

The checker is finite and cannot certify a theorem quantified over all integers. The analytic proof consists of the exact interval sums, positivity of every coefficient in the two factored discriminants, the root-location argument and the locally uniform rescaling. The asymptotic constant is obtained from the derivative of the inverse map, not numerical extrapolation. The full two-variable Bergman-kernel zero set is outside the scope.
