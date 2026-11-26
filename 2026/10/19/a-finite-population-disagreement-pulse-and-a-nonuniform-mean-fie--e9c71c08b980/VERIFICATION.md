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

At total rate N/2 each ordered distinct pair has rate 1/[2(N−1)]. Independently use v=N⁻¹Σx_i² and c=[N(N−1)]⁻¹Σ_{i≠j}x_i x_j. Summing the jump increments yields Lv=μ²/2−μ(2−μ)v/2+μ(1−μ)c and Lc=μ(v−c)/(N−1); in the latter sum the only uncanceled contribution is when the persuader is the other coordinate in the product. I checked the two identities by rational event enumeration on heterogeneous states for N=2,3,5,8 and three μ values. The relation m²=v/N+(N−1)c/N recovers the stated generator, with S=(N−1)(v−c)/N. The centered system has negative trace −μ(2−μ)/2−μ/(N−1), positive determinant μ³/[2(N−1)], and distinct real negative roots. Cayley–Hamilton and S(0)=0, (ES)'(0)=μ²(N−1)/(2N) give the exact pulse. The derivative changes sign once at log(r_f/r_s)/(r_s−r_f); the determinant/fast-root ratio gives −μ²/[(2−μ)N]+O(N⁻²), yielding the stated peak constant, height and population-scale profile. The bounded empirical-mean martingale converges, with limiting second moment one from the centered system; boundedness of each coordinate forces unanimity at the resulting endpoint, and mean zero fixes equal chances. In the symmetric zero-mean mean-field law the learner receives fair signs at rate 1/2, so its second moment tends to μ/(2−μ). The 1-Lipschitz test x²/2 gives a limiting lower bound (1−μ)/(2−μ) against the endpoint mixture. The calculation establishes expectation, not concentration; the original source script was inspected, not executed.

## originality

PASS

Credit the source model and Bernoulli-convolution limit to Cao–Cortez, and qualitative finite-system endpoint agreement to kindness precedents. The supported increment is the exact symmetric finite-N two-mode disagreement trajectory, with the logarithmic peak and N-time decay constants and the explicit one-marginal nonuniformity bound in this normalization. No equivalent or dominating formula was found in the inspected same-model and nearby work.

## value

PASS

The time-dependent exact invariant resolves a real limit-order question in a specific published mean-field model. It determines not just eventual breakdown but the time of maximal disagreement to additive o(1), its height, and the crossover on the population-size time scale. The quantitative separation explains why finite-horizon propagation of chaos cannot be applied uniformly in time to the original rule.

The dated certificate retains the supplied scientific assessment, sources and limitations.
