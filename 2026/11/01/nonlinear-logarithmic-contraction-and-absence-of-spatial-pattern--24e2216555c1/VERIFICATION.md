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

Reconstructed the estimate for strictly positive continuous data and the extension to nonnegative continuous data. For existence, the map x_i ↦ (b_i+Σ_j h_ij(x_j))/d_i maps the product of the componentwise production-bound intervals to itself, so Brouwer supplies an equilibrium. A zero component there forces every predecessor to be zero and every incoming edge to be activating; strong connectivity then forces the all-zero vector, contradicted by the basal or inhibitory source. In log coordinates the diagonal reaction derivative is −f_i/x_i and the off-diagonal derivative is x_j h′_ij(x_j)/x_i. Both kinetics obey h−s|h′|=h²/a; hence each row margin is −q_i/x_i. Its worst value on the box is exactly −q_i,R/U_i, since the monotone numerator terms have independent input variables and no self-term. Comparison with the equilibrium at the first log-box face gives invariance. For two solutions the log-difference diffusion is the scalar Laplacian plus transport by the sum of the two log-gradients. At a signed spatial maximum, including on the C² Neumann boundary, the gradient vanishes and the Laplacian has the favorable sign. The segment-averaged matrix retains the negative row margin by the triangle inequality. The upper Dini inequality (including tied maximizers) gives the claimed estimate; R=0 follows by uniqueness, and the estimate itself forces uniqueness among positive equilibria. Boundedness and parabolic comparison give global evolution; a basal or inhibitory input supplies a uniform positive forcing on bounded time intervals, and positivity propagates along directed paths by comparison and time integration. Restarting at positive time proves convergence and excludes nonnegative heterogeneous stationary profiles. Independently checked the example: h(2)=1/5 gives 1/50; at s=1/10 the untransformed spectral abscissa is −1/3+2/(1+2s)²=19/18.

## originality

PASS

Pass the spatial, pairwise, explicit-rate theorem under the frozen hypotheses, not the prior well-mixed logarithmic metric or reaction row identity. No equivalent spatial theorem was established in the inspected literature and indexed records.

## value

PASS

This is a global incremental stability and no-pattern theorem for a natural mixed-sign reaction class, not just a local linear-stability calculation. It works for unequal positive diffusivities without a domain-dependent gap, and gives a quantitative, directly computable bound on loss of memory of initial data. The fixed-norm obstruction makes clear why the spatial result is not a routine application of the cited contraction-inheritance theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
