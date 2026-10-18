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

Running `python verify.py` enumerates every recursive parent sequence and every independent retained-edge pattern for tree sizes 2–7, for five rational values of the retention probability, with exact Fraction arithmetic. Each output compares six independent statistics to the closed formulas, including the full mixed covariance and both variances. Additional exact evaluations check the analytic ratio and positivity; numerical asymptotic comparisons test the limiting constant at three interior retention parameters.

The proof does not rely on enumeration. These checks do not establish that no equivalent prior theorem exists and are not an independent mathematical audit. The theorem holds for fixed \(r\in(0,1)\) when stating the asymptotic correlation, and no endpoint-uniform limit is claimed.
