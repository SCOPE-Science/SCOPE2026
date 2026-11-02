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

# Reproduction and limits

Execute `python verification/check_coefficients.py` with SymPy installed. It tests the exact positive-coefficient logarithmic residual, negative-coefficient slow-branch residual, coefficient relations, and zero-coefficient conserved energy; the observed output was `CHECK_OK: exact identity, logarithmic coefficient, damped slow branch`.

Optionally execute `python verification/numerical_probe.py` with SciPy installed. It integrates the orbital equation at position \(x=40\) from common \(x_0=1\) and initial speeds \(1\) and \(2\) for coefficients \(b=1,0,-1\); the observed output ended in `NUMERICAL_PROBE_OK`. Numerical values are diagnostic, not interval enclosures or certificates of the infinite-domain claims.

The all-parameter proof uses the exact orbital equation, forward-invariant positivity, barriers, integrable errors and the reciprocal-velocity time identity as stated in RESULT.md. The mathematics has not been independently audited, and no machine formalization is claimed.
