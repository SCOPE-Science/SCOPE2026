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

# Reproducible checks and proof boundaries

Run `python3 verify.py` with Python 3 and the standard library. The expected deterministic output is `VERIFY_OK 2944 normalizations, sample perturbations, and sharpness checks`.

The checker uses facet normal directions to evaluate the minimum zonogon support and vertex norms to evaluate the maximum. It compares the uniform rule for every integer \(2\le N\le30\) to the formula, tests 100 nonuniform positive perturbations at each dimension, evaluates the stated angular-rigidity bound when its hypothesis applies, and checks the tangential sharpness deformation for several \(N\) and perturbation sizes. It does not sample or certify every convex body, every rule, or all integers \(N\). Infinite statements are established only through the analytic proof in RESULT.md. All tests use floating-point arithmetic with explicit comparison tolerances. No independent external validation is claimed.
