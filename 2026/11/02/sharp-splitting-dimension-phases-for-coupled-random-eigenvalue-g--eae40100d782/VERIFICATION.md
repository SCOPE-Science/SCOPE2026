---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Rationalization gives Δₕ=h g(R/h), g(t)=c/t+O(t⁻³) for t≥1, and Δₕ/h²≤c/R. Below the moment threshold use domination by (c/R)ᵖ; above it change variables X=hy and use the integrable rescaled kernel. At p=d, the integral for h≤R≤δ has main term cᵈ h²ᵈ times the angular-density integral against dR/R. The O((h/R)²) relative kernel error, the inner ball and the exterior each contribute O(h²ᵈ) at fixed δ; continuity at zero controls the coefficient without requiring a density derivative. The stated means, variances and fourth-moment constants follow: for d≤4 the centering terms are lower order (at d=4 they are O(h⁸) versus h⁸ log(1/h)); in d≥5 use L⁴ convergence. The sample-variance identity follows from the pair kernel (Yᵢ−Yⱼ)²/2: disjoint pairs have zero covariance and overlapping pairs have covariance (μ₄−σ⁴)/4. For bounded N, κ≥1 implies a strictly positive lower bound 2/[N(N−1)]; this verifies necessity in the finite-kurtosis regime. The positive Clifford branch exists because an orthogonal Clifford generator exchanges the signs. Statistical independence of coordinates is not needed; the joint density hypothesis permits dependence. The frozen script's advertised characteristic-polynomial tests compare algebraically identical expressions, not independently computed determinants. They are unnecessary to the verified analytic calculation. No supplied code was executed. Independent bounded-interval quadrature (/workspace/review-checks/frozen_constants.py) gave J₂,₁≈0.290374807140502, J₄,₁≈0.0357744018751969 and coefficient 0.424281907450405; this checks constants, not the limiting theorem.

## originality

PASS

The closest indexed record overlaps exactly on the one-dimensional coupled variance, and on uncoupled moments at θ=0 in an extension of the frozen domain. The supported distinction is the joint positive-θ, multidimensional classification, including the centered fourth moment and sharp relative-MSE budgets. Standard radial asymptotics and the unbiased sample-variance identity are not claimed as new. No inspected statement establishes the full classification.

## value

PASS

An almost quartic absolute variance decay in d=2 coexists with the most severe relative variance-estimation budget of the listed dimensions. The exact phase classification reveals why looking at absolute variance is insufficient and supplies necessary and sufficient sample sizes for this common coupling. The contrast with the deterministic trace-square difference is useful when choosing spectral observables. The result is model-specific, not a general sample complexity or MLMC cost theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
