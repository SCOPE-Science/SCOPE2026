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

Root the gaps at a sampled point, not at a fixed angular origin: conditional on that sample the other rotated locations are iid uniform, giving the Dirichlet law and beta marginals. The perimeter does not depend on which sample is the root. The Klein model gives the cyclic edges, and the hyperbolic cosine rule gives the chord as 2 arsinh(Sₙ sin(πx)), including x>1/2. This yields the exact mean. Cubic bounds give E[1−Wₙ]=O((1+Sₙ²)/n²) in the small regime, and Jensen gives the deterministic upper bound arsinh(πqₙ)/(πqₙ) in the large regime. For finite positive qₙ→s, replacing sin(πx) by πx costs O_P(n⁻²) by the Dirichlet third moment. The normalized-exponential representation and expansion at the sample mean 1 give the influence function in (6): averaging the derivative replaces it by −b(πqₙ) with fluctuation O_P(n⁻¹/²), and the quadratic remainder is O_P(n⁻¹). Uniform moments give the triangular-array CLT; nonaffinity of arsinh gives positive variance. This centers at F(qₙ) without a rate assumption. Exponential moments give the small-s expansion, and strict decrease follows from arsinh(t)/t. For the large-s bound, the proof shorthand for h(t)=arsinh(t)−log(2t) is not a uniform bound near t=1; the precise bounds O(1+|log t|) on (0,1] and O(t⁻²) on [1,∞) make h integrable and give E[h(zZ)]=O(1/z), proving the stated remainder. The fixed-radius cubic coefficient is −π³S(1+S²)/6, with remainder controlled by the fifth gap moment. verify.py was inspected, not executed; its diagnostics do not prove the limit laws.

## originality

PASS

The critical CLT mechanism, including the covariance correction and flexibility to use n-dependent scores, is already covered by a stronger circular-spacings theorem. Credit the supported distinct geometric contribution: the explicit perimeter-fraction crossover with sharp profile expansions in both extreme-radius directions, joined to the exact mean and the critical fluctuation formula for this growing-radius polygon model. No separate novelty is claimed for the spacings CLT or for the normalization correction. The strongest exact-model catalogue match concerns area, not perimeter; the older perimeter comparisons use different sampling or are deterministic.

## value

PASS

For growing circles the number of sampled points alone does not determine accurate perimeter approximation. The result identifies an exact nontrivial fraction at the logarithmic radius threshold and gives leading errors on both sides of the profile, alongside its critical variance and the rate-sensitive centering. These determine what aspect of perimeter is resolved at each scale; the contribution is the geometric transition, not a new generic CLT.

The dated certificate retains the supplied scientific assessment, sources and limitations.
