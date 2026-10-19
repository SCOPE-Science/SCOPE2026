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

Execute `python checker.py` with Python, NumPy, and SciPy installed. The program evaluates independent one-trial resolvent integrals, renewal probabilities, mean exit time, both analytically equivalent dispersion formulas, homogeneous and clustered asymptotes, and phase boundary inequalities. Observed output: `PASS 2177 numerical/quadrature/phase assertions`, with golden-ratio threshold approximately `4.245100247620143` for the dimensionless product and approximately `18.0208761123446` for its square. These checks are finite tests and do not constitute an exhaustive proof; the exact convexity and endpoint argument is in RESULT.md. Independent audit: not performed.
