---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-02.md",
      "INDEPENDENT_AUDIT_2026-10-02.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

The primary paper's exact mean-intensity formula (3.4)–(3.7) has the claimed first mark-dependent coefficient d(v_d γ)^(2/d), multiplying (log ρ^d)^(d−2)/d and the difference E M²−s². Its Corollary 3.3 gives s_{d,ρ}/log ρ^d→1 for every correct shift; for s=A−y/t the first term differs from its endpoint by −2Ay+o(1), while every i≥2 term has variation O((log ρ^d)^(−2(i−1)/d)) on bounded y. The endpoint-tail hypothesis therefore yields the Gamma(β,rate 2A) law by a direct Laplace–Stieltjes calculation. Lemma 3.4's Taylor error is uniform over all mark sets D, including the shrinking endpoint windows; Proposition 3.10's Palm/stabilization bound uses the same exceedance event and a general measurable mark coordinate, so it applies after deterministic rescaling. Together they establish product-intensity Poisson convergence on bounded score/endpoint windows, and the source's unique-maximum mapping then gives the stated independent U,Y,G limit. Equation (1.7) contains +log γ, whereas v1 Example 3.11 (3.23),(3.24) omit it; substitution gives the submitted corrected forms and the omitted versions indeed normalize to γ rather than 1. The archived numerical check tends accordingly toward 0.4 versus 1 for γ=0.4, and the Beta endpoint quadrature approaches Gamma(1.5,3.4); these calculations support rather than replace the analytic proof.

## originality

PASS

The primary 2026 Poisson–Laguerre paper states only unscaled δ_A mark convergence in d≥3 and no Gamma endpoint rescaling. Its d=3 equation (1.7) provides a general exact shift, but it neither states the β-dependent endpoint asymptotic nor the product marked-process refinement. Older exponential-family work establishes the scalar Gamma tilting principle, and that portion is openly disclaimed; it does not apply the principle to the nontrivial Poisson–Laguerre extreme-cell point process or establish independence from the Gumbel score. The missing +log γ is explicitly a version-specific correction, not an original general probability law.

## value

PASS

The prior theorem collapses extreme-cell marks to the deterministic endpoint and hides their fluctuation size. This result gives a non-degenerate universal law, dimensional localization scale, spatial/score independence, and the maximum-cell mark distribution; those are meaningful quantities for extreme stochastic geometry, not an arbitrary parameter slice. The d=3 β-dependent shift and exact normalization correction make the process result usable for a natural endpoint-tail family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
