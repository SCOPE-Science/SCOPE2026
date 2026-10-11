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

# Reproducible verification

Run `python3 verify.py` with Python 3.10 or later and no external dependencies. The script checks the integral coefficients for \(d=3,4,5,6,7\) by independent Simpson quadrature, the normalized beta evaluation, and the exact rational strict-gap certificate. It also evaluates the axial \(d=3\) case independently. Inspect the script as part of the proof trace.

The infinite-family result rests on the exact algebraic integration and the affine Jacobian argument in `RESULT.md`, not on finite tests. No claim is made about which direction globally maximizes the functional. Numerical quadrature cannot certify absence of earlier equivalent literature. Independent audit: not performed.
