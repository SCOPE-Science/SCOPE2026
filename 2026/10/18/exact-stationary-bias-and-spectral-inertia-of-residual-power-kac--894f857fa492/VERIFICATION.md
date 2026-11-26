---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

After projection the row-index transition depends only on the sampled value, and positive degrees plus symmetry give detailed balance. A positive floor gives self-loops; without it the graph is complete multipartite on the distinct-value classes, bipartite exactly for two classes and otherwise with two- and three-step returns. For at least 2r+1 distinct values, the Vandermonde matrix has full column rank. In the coefficient matrix each mirrored exponent pair gives a block of negative determinant, even in the exceptional pair with the floor on its diagonal; the central sign is (-1)^r. Congruence and the diagonal similarity of P to its symmetric form prove the sign and nullity counts. For r=1 the centered degree is m(ε+μ₂+y_i²), giving the displayed mean and excess risk, which is nonnegative with precisely the stated equality case (the least-squares objective differs from squared error by the constant μ₂). On the positive-variance centered sphere the two constraint gradients are independent: each cubic extremizer takes exactly two levels, and its squared standardized skewness is m²/[k(m−k)]−4, maximized at k=1 or m−1. Zero-floor outlier mass follows from equal total degrees on the two parts. The theorem is analytic; inspecting the finite checker was not used as proof of rank, periods, or sharpness.

## originality

PASS

The supported contribution is the sampling-specific combination of exact stationary distortion and the all-even-power sign/rank classification for inconsistent scalar full projections. Do not credit standard detailed balance or the skewness constant as new. The closest catalogue and primary statements inspected do not give the sign transition and the stationary squared-residual comparison for this model.

## value

PASS

The simplest inconsistent full-projection model exposes a concrete design limit: squared residual weighting cannot improve stationary squared error over uniform row selection and can weight one outlier at one-half rather than 1/m. The positive nonstationary modes that appear for fourth but not squared weights show that changing powers also changes relaxation, not merely the magnitude of bias. These exact distinctions are informative without claiming that higher-dimensional or damped methods share them.

The dated certificate retains the supplied scientific assessment, sources and limitations.
