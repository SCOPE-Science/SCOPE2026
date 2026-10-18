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

# Verification and limits
The included `verify.py` was executed in a Python environment with SymPy and returned `ALL_CHECKS_PASS`. It reconstructed the two-by-two Hessian and its determinant over a characteristic-zero polynomial fraction field; all identities have integer coefficients after clearing powers of the invertible parameter and are consequently valid in every odd characteristic. The script also checked the tangent cubic coefficient and the otherwise exceptional characteristic-three cubic expansion directly in the full equation. Direct gradient enumeration was performed for every rational point and every parameter in the prime fields with orders 3, 5, 7, 11, and 29.

The all-prime-power claims are proved algebraically in RESULT.md; sample computations do not establish them by enumeration. No claim is made about singularities defined over extensions of the base field or the complete global singular locus. Independent audit has not been performed.
