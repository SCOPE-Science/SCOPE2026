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

The executable `check_meanders.py` enumerates all pairs of noncrossing perfect matchings on up to fourteen labelled boundary points. It computes exact fractions for the displayed means, mixed moments, factorial moments, negative signs and conditional binomial counts for every realized value of the short-loop count and total four-vertex component count. The finite range is \(2\le n\le7\), comprising 203454 pairs, and is not an unrestricted mathematical proof.

The symbolic covariance formulas are obtained from Catalan ratios by direct simplification. The asymptotic covariance matrix uses exact rational expansions. The independent bivariate Gaussian claim additionally relies on Janson–Thévenin's established marginal short-loop central limit theorem and the proved independent-orientation symmetry. The general full shape-vector central limit theorem is not established here.

Run with `python check_meanders.py` in a directory containing that file. No external packages are required. Independent audit has not been performed.
