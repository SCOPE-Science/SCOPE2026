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

Run `python checks/verify.py` with Python 3, NumPy, and SciPy. The self-contained code checks the independently normalized Gauss–Jacobi Beta integral against a hypergeometric root equation, probes the two sides of the shape transition, verifies the critical quartic sign and peak-splitting coefficient, and checks numerical approximations for both endpoint asymptotics. Its execution on the packaged code gave 48 passing deterministic assertions. Numerical verification does not prove the global zero count or uniform asymptotic errors.

The analytic proof of uniqueness uses strict total positivity of the Gaussian kernel, and the two endpoint limits use separate asymptotic analyses. Earlier literature gives the exact convolution and implicit shape-transition equation; neither is independently rederived as a novel claim. No independent external audit was performed.
