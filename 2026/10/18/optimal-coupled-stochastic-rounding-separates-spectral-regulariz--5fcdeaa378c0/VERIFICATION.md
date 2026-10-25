---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Bernoulli four-state joint mass is (1−p−q+τ,q−τ,p−τ,τ) for τ in exact Frechet interval. The population Gram has diagonals u²+h1²p(1−p), v²+h2²q(1−q) and affine cross term uv+h1h2(τ−pq). IID rows and strong law give n^-1 A_n^T A_n→G(τ) a.s.; ordered eigenvalue continuity then gives limiting least singular squared. Fixed-diagonal 2×2 smallest eigenvalue decreases strictly with absolute cross term, hence unique clipped projection τ_spec. Covariance matrix PSD implies |cov12|<=s1s2 and 2Σ0−Σ(τ) PSD, so G(τ) <= 2G(pq) in Loewner order. Midpoint symmetrical L,h>0 gives λmin=h²(1/2−τ), optimum τ=0, ratio exactly 2. Distinct row *rays* have masses (2τ,1/2−τ,1/2−τ); all rows on one ray iff rank<2, yielding exact (2τ)^n+2(1/2−τ)^n for n≥1. Convexity for n≥2 gives unique τ_rank=1/6 and min 3^(1−n), not the spectral optimum. Independently checked 15,000 admissible random parameter samples for τ and spectral inequality plus rational finite-n exact cases; tested limits do not replace strong-law proof.

## originality

PASS

Best-of-knowledge source/statement comparison, not mere keyword or parameter match: Different algebraic framework: allow Bernoulli dependence *within* row while maintaining independent rows. There is no direct equivalence to independent entrywise random matrices; this contrast is explicitly central. The existing broad independent-noise spectral bounds are not statements encompassing dependent-coordinate noise. General 2×2 covariance min-eigen formulas overlap as tools, not the paired optimizations. Classical covariance eigenvalue monotonicity and convexity provide an elementary proof, but this conflict for unbiased rounding with fixed marginals and all row counts is not an implication of the compared independent-entry literature.

## value

PASS

Stochastic rounding is a credible numerical regularization mechanism, but its usual independent-error model hides a design degree of freedom: coupling coordinate decisions while preserving unbiased marginals. The exact spectral optimizer and sharp gain quantify the advantage, while the opposing *unique* finite-sample rank optimizer shows two reasonable rank-recovery objectives cannot be conflated, with a concrete exact floating-point instance. This is a motivated operational boundary/counterexample, not a trivial new parameter name.

The dated certificate retains the supplied scientific assessment, sources and limitations.
