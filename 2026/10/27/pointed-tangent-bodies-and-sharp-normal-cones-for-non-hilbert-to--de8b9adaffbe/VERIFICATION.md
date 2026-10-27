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

The self-contained `verification.py` uses only the Python standard library. Run `python verification.py` to reproduce 203 finite numerical checks: source ellipse reparameterization, critical supporting-normal cones over nine exponents, numerical approximation of limiting support, convergence from both sides of the Hilbert exponent, and the critical vertical-half-width root.

All universal, infinite-dimensional, and asymptotic conclusions follow from the explicit analytical proof in `RESULT.md` and the prior essential-range identity cited there. Numerical sampling cannot establish uniqueness for all parameters or the quadratic Hausdorff bound. No independent scientific audit or external verification has been performed.
