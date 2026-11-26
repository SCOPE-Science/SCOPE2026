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

Reconstructed the ratio blow-up and the lower-root triangular saddle Jacobian. The invariant graph has derivative z_-/(lambda_u-lambda_z)<0; its physical image has this quadratic coefficient. Locally z-s(u) obeys a scalar multiplicative equation with coefficient bounded below by a positive constant near the saddle, so off-graph points exit on their own side while u decreases. The compact upward extinction strip has u decaying to zero, and points below the lower cutoff go to the prey-only equilibrium. For the noncompact initial-ratio corner, before z hits Z the cap bootstrap bounds u by Z^(-1/c)u_0^(1-1/c)v_0^(1/c), with c>1, so the passage is finite for every point although its time need not be uniformly bounded. This makes the divider valid on one common small square. Integrating under the graph for z_-<=1 (strictly below the upper edge at equality by the negative quadratic term) and above the graph up to the unique crossing for z_->1 gives both claimed corrections and the O(epsilon^2) remainder. Independent root and eigenvalue calculations reproduced (P_0,P_1)=(0.78593652218,0.09564833715) and (0.34535671122,0.09509600864). The packaged finite RK4 examples are illustrative, not proof of the basin split.

## originality

PASS

The normalized dynamics, Lambert roots, Jacobian, and qualitative bistability are prior. The supported distinct claim is the uniform shrinking-square basin-area expansion, including its curvature correction and geometric clipping, not the model, roots, or bare existence of an extinction sector.

## value

PASS

A phase portrait or limiting angular threshold does not quantify extinction under a natural physical-density sampling distribution. The uniform corner control and explicit positive curvature correction give a usable deterministic baseline with sharp dependence on where the separator intersects the square. This is not a demographic extinction probability, a stochastic result or a global large-density basin classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
