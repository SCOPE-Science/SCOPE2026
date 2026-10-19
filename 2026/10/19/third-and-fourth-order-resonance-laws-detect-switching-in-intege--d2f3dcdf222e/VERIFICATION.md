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

The standalone check `python3 checks/verify_moments.py` evaluates exact Fourier coefficients and rational moments; it does not use numerical integration or floating-point quadrature. In the recorded run it passed 2,297 exact formula comparisons and 66 complete small-length inverse-spectrum comparisons. The script covers all binary switching words of length at most ten and 250 sampled schedules with integer multipliers drawn from six values. The full quantified theorem is established by the signed-frequency case analysis and binary-run construction in `RESULT.md`; finite comparisons alone are not an infinite proof. The actual embedded checker is self-contained (Python standard library). Independent mathematical audit has not been performed.
