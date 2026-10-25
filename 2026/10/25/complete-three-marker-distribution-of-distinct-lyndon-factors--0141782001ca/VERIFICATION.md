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

# Mathematical verification

From the directory containing these files run `python3 checker.py` with Python 3. The script uses only standard-library packages. It independently enumerates Lyndon contiguous factors by the rotation definition for 1,365 words with 0–11 zeros; expands the bivariate generating function via independent truncated formal-series arithmetic through 25 zeros and compares every coefficient to an explicit 23,751-word fixed-content enumeration; and re-evaluates the limiting Dirichlet-sector first and second moments using exact fractions. Passing finite tests is not an infinite proof. All-length correctness follows from the gap-classification and geometric-series argument in `RESULT.md`. Convergence in distribution and the moments follow from weak-composition-to-simplex convergence and a six-sector invertible linear coordinate change. Originality is subject to incomplete historical coverage; no independent mathematical audit has been performed.
