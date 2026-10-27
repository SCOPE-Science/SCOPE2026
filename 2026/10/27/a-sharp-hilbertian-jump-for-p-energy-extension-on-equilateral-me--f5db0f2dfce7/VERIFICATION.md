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

# Reproducible checks

Run `python checker.py` with a standard Python 3 interpreter; no third-party packages or external resources are needed. The script brackets the unique scalar center and uses bisection for numerical comparisons. It tests thousands of sampled data pairs in dimensions \(2,3,4,7\) over exponents on both sides of \(2\), exact attainment for quadratic centers, and asymptotic center-response predictions.

The norm formula and sharpness for every real \(1<p<\infty\) are proved in `RESULT.md`. The numerical checks do not establish infinite-dimensional or global optimality by enumeration; floating-point output cannot certify limits or exact asymptotic coefficients. Independent scientific verification has not been performed.
