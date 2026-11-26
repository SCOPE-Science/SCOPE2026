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

For n>ℓ the Gaussian background block has full column rank almost surely. Rotating its columns conditional on the independent spike row g gives gᵀW⁻¹g=||g||²/V in law, where Gaussian orthogonal residual degrees of freedom are (n−1)−(ℓ−1)=n−ℓ, and the law of V given g is constant. Sherman–Morrison then gives the exact ceiling, for all cn>0. Conditional on the auxiliary sketch the independent start is nondegenerate Gaussian, so its range component is nonzero almost surely; no positive integer power can kill it. In a common-row coupling the strong law applies to the Gram entries and the products of background entries from the two independent sketches. Thus K_n→I+cggᵀ and w_n→cgh almost surely. The top eigengap is c||g||²>0, and the projection coefficient of w_n onto the top eigenvector tends to c||g||h≠0 almost surely. The ratio of off-axis to top coefficients before applying Z_n is bounded by ||b_n||/|α_n| uniformly in q≥1, because (λ_2/λ_1)^(q−1)≤1. Passing through Z_n has bounded distortion under the coupling; its condition number tends to √(1+c||g||²). Both the image top vector's capture and the ceiling tend to c||g||²/(1+c||g||²), proving the uniform result and allowing any adaptive q_n. The unpowered alignment instead depends on the independent h² in the limit. Continuity outside the probability-zero tie yields the gain probabilities, and the beta ratio and ℓ=2 Laplace transform give the stated tail and 1/√2. Compression of A_n A_nᵀ by the orthogonal residual projector sandwiches the spectral norm squared between the compressed spike's norm and that norm plus 1, also if cn≤1. Bounded normalized errors and χ² stochastic domination give the expected risks and strict limiting improvement.

## originality

PASS

The algorithm and the exact projector law are not the distinct contribution. A catalogue result independently covers the usual-spike projector sublaw, and the Wishart derivation is classical even beyond that regime. In the inspected works, no known theorem gives one-step saturation uniformly over all iterations for the independent-start, fixed-auxiliary-width critical model, together with the coupled baseline comparison and its nonzero probability of loss under strictly improved limiting mean risk. This is the supported distinction, not priority for generic sketch-power iteration or Gaussian inverse forms.

## value

PASS

The exact randomized algorithm comparison identifies a natural critical regime where a single iteration attains all asymptotic gains available within the auxiliary range, even under adaptive iteration choices. It also exposes a persistent, quantified chance of individual loss despite a strict expected spectral-risk improvement. This supplies decision-relevant information not contained in the classical projector law or in a generic mean bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
