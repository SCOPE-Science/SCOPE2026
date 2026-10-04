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

The proof was checked statement-by-statement against the exact domain: a trivariate positive-definite Gaussian correlation matrix with one zero off-diagonal and two strictly negative off-diagonals, exact one-sided uniform transforms, and positive simplex weights.

Critical checks:

- The one-coordinate reciprocal tails are exact, so their sum is exactly \(1/t\).
- The zero-correlated Gaussian pair is genuinely independent, giving the exact two-Pareto convolution and coefficient \(2w_1w_2\).
- For each negative pair, the simultaneous-extreme exponent is strictly greater than two. The remaining edge core is controlled by Gaussian conditional tails and an integrable Mills-ratio envelope, giving \(O(t^{-2})\).
- In the all-lower trivariate corner, the correlation matrix is Stieltjes; its inverse is entrywise nonnegative, so the Gaussian copula density is bounded there. The three-face product-corner integral is therefore \(O(t^{-2})\).
- If one reciprocal score is bounded, the three-face finite difference can be nonzero only in fixed-width singleton or pair-sum shells, each of probability \(O(t^{-2})\).
- The quantile and independence-threshold size formulas were re-derived by substitution from the tail expansions.

The bundled checker verifies the exact Boolean Möbius identity, the coefficient subtraction, and a representative positive-definite correlation matrix. It does not certify the asymptotic theorem and no simulation is used as proof.
