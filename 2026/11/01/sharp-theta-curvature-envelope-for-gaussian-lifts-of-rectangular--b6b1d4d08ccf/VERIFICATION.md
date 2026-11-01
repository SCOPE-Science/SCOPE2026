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
# Verification and scope

The mathematical assertions are proved in RESULT.md, including exact normalization, derivative signs across the entire positive parameter line, and equality classification. The necessary non-elementary shift-covariance inequality is an explicitly cited and inspected mathematical lemma; its proof uses the Gaussian parallelogram identity and Cauchy–Schwarz on parity classes. The Poisson summation identity is classical.

The standalone checker evaluates rapidly convergent theta sums with `mpmath`, finds the root, checks finite samples against the derivative and curvature formulas, and checks sufficient scalar inequalities. Numerical sampling cannot prove global uniqueness or coverage. The analytic estimates in the main proof do so.

The approximate decimal values are reproducibility aids, not independently certified interval bounds. Neither a stronger statement for arbitrary densities nor independent external validation is claimed.
