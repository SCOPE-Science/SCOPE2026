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

Execute `python verify.py` (standard Python only). The checker reconstructs each section vertex from opposite-signed endpoint heights and evaluates its Euclidean squared norm; it never treats experimental frequencies as proof. The exact checks cover the planar endpoint and mid-cdf and the analytic cutoff parameter, while seeded Gaussian orientation samples test the full planar distribution at four interior points and the three-dimensional first-order asymptotic at two small thresholds. Tolerances are specified in the code and reflect finite sample sizes. The all-dimensional claim rests on the self-contained argument in RESULT.md, including the \(O_d(arepsilon^2)\) overlap estimate. Independent validation has not been performed.
